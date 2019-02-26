import PyPDF2
import pdf2image
import pytesseract
from pathlib import Path
import numpy as np
import cv2
from PIL import Image


def ocr_pdf(input_pdf_path, return_type='text', output_pdf_path=None):
    '''
    OCRs a pdf using Tesseract through the pytesseract module

    This function either returns the text of the pdf as a string (return_type='str') or it
    stores an ocred pdf in the output_pdf_path (return_type='str')

    # return_type='text' returns the text of the pdf
    >>> input_pdf_path = Path('..', 'computation_hist', 'data', 'sample_docs', '3_32_verzuh_1.pdf')
    >>> text = ocr_pdf(input_pdf_path, return_type='text')
    >>> text[31:48]
    'November 21, 1957'

    # return_type='pdf' stores an ocred copy of the pdf
    >>> output_pdf_path = Path('..', 'computation_hist', 'data', 'sample_docs',
    ... '3_32_verzuh_1_ocr.pdf')
    >>> output_pdf_path.exists()    # output_pdf_path shouldn't exist yet
    False
    >>> ocr_pdf(input_pdf_path, return_type='pdf', output_pdf_path=output_pdf_path)
    >>> output_pdf_path.exists()    # after ocring, the output_pdf_path should exist
    True
    >>> output_pdf_path.unlink()


    :param input_pdf_path: str or Path, the filepath to be converted
    :param return_type: str, 'text' or 'pdf'
    :param output_pdf_path:
    :return: str or None
    '''

    # Turn string paths into Path objects if necessary
    if isinstance(input_pdf_path, str):
        input_pdf_path = Path(input_pdf_path)
    if isinstance(output_pdf_path, str):
        output_pdf_path = Path(output_pdf_path)

    # Make sure that the input params are valid
    if return_type not in ['text', 'pdf']:
        raise ValueError(f'return_type has to be "text" (return the ocred text) or "pdf" (store the '
                         f'ocred version of the pdf but not {return_type}.')

    if return_type == 'pdf':
        if output_pdf_path is None:
            raise ValueError('To store the ocred pdf, please pass a location to store it.')
        if not output_pdf_path.parts[-1].endswith('.pdf'):
            raise ValueError('output_pdf path should end in ".pdf"')

    # Converts pdf into a list of PIL files
    skewed = pdf2image.convert_from_path(input_pdf_path, fmt='jpg')

    # Deskews images
    images = fix_pil(skewed)

    # Extracts text and returns string if return_type='str'
    if return_type == 'text':
        text = ''
        for i in range(len(images)):
            text += pytesseract.image_to_string(images[i]) + '\n\n\n'
        return text

    elif return_type == 'pdf':
        output_file_name = output_pdf_path.stem  # pdf name without file extension
        output_pdf_path.parent.mkdir(parents=True, exist_ok=True)

        file_paths = []

        # Converts the PIL files into binaries and saves them in a list, along with the filepaths
        pages = []
        for i in range(len(images)):
            single_page = pytesseract.image_to_pdf_or_hocr(images[i], extension='pdf')
            pages.append(single_page)
            file_paths.append(
                Path(output_pdf_path.parent, output_file_name + '_' + str(i) + '.pdf')
            )

        # Creates dummy pdf documents that will be merged
        for i, page in enumerate(pages):
            with open(file_paths[i], 'wb') as f:
                f.write(page)

        # Merges the pdf files in python
        merger = PyPDF2.PdfFileMerger()
        for path in file_paths:
            merger.append(str(path))

        # Writes the merged file into one document and then deletes dummy files
        merger.write(str(output_pdf_path))
        for path in file_paths:
            path.unlink()


def correct_skew(filepath):
    """
    Reads a saved image with text and rotates the image such that the text is level.

    The image in question will be overridden, use with caution.

    Because this function deals strictly with images, there are no doctests.

    :param filepath: filepath to image to be rotated
    :return: None
    """

    # load the image from disk
    image = cv2.imread(filepath)

    # convert the image to grayscale and flip the foreground
    # and background to ensure foreground is now "white" and
    # the background is "black"

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)

    # threshold the image, setting all foreground pixels to
    # 255 and all background pixels to 0
    thresh = cv2.threshold(gray, 127, 255,
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imwrite(filepath + '_thresh.jpg', thresh)

    # grab the (x, y) coordinates of all pixel values that
    # are greater than zero, then use these coordinates to
    # compute a rotated bounding box that contains all
    # coordinates
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]

    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle
    if angle < -45:
        angle = -(90 + angle)

    # otherwise, just take the inverse of the angle to make
    # it positive
    else:
        angle = -angle

    # if angle == 0, there has been a problem and we should try another method
    if int(angle) == 0.0 or angle == -0.0:
        height, width, channels = image.shape

        boundary = [20, 20, 20]

        # convert all pixels that are almost black to white to imitate page
        for x in range(0, width):
            for y in range(0, height):
                channels_xy = image[y, x]
                if all(channels_xy < boundary):
                    image[y, x] = [255,255,255]

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.bitwise_not(gray)

        # threshold the new image, setting all foreground pixels to
        # 255 and all background pixels to 0
        thresh = cv2.threshold(gray, 127, 255,
                               cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        cv2.imwrite(filepath + '_thresh.jpg', thresh)

        # grab the (x, y) coordinates of all pixel values that
        # are greater than zero, then use these coordinates to
        # compute a rotated bounding box that contains all
        # coordinates
        coords = np.column_stack(np.where(thresh > 0))
        angle = cv2.minAreaRect(coords)[-1]

    print(angle)

    # rotate the image to deskew it
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image,
                             M,
                             (w, h),
                             flags=cv2.INTER_CUBIC,
                             borderMode=cv2.BORDER_REPLICATE
                             )

    # save rotated image
    cv2.imwrite(filepath, rotated)


def fix_pil(doc):
    """
    Takes in a list of PIL files that need to be deskewed and returns the images in PIL format

    Because this function deals strictly with images, there are no doctests.

    :param doc: list of PIL files
    :return: list of PIL files
    """

    # Saves images to disk for reformatting
    filepaths = []
    count = 0
    for image in doc:
        filepaths.append(
            Path('..', 'computation_hist', 'data', 'sample_docs', 'doc_save' + str(count) + '.jpg')
        )
        with open(filepaths[count], 'wb') as pic:
            image.save(pic)
        count += 1

    # Deskew image
    for page in filepaths:
        correct_skew(str(page))

    # Read images for return
    pages = []
    for page in filepaths:
        with open(page, 'rb') as _:
            pages.append(Image.open(page))

    # Delete images from disk
    for path in filepaths:
        path.unlink()

    return pages


if __name__ == '__main__':
    input_pdf_path = Path('..', 'computation_hist', 'data', 'sample_docs',
                                'skew_test_real.pdf')
    output_pdf_path = Path('..', 'computation_hist', 'data', 'sample_docs',
                           'skew_test_out.pdf')
    o = ocr_pdf(input_pdf_path, return_type='pdf', output_pdf_path=output_pdf_path)
