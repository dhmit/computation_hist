import PyPDF2
import pdf2image
import pytesseract
from pathlib import Path
import numpy as np
import cv2
from PIL import Image
from scipy.ndimage import interpolation as inter


def ocr_pdf(input_pdf_path, return_type='text', output_pdf_path=None):
    """
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
    """

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
    images = fix_pil(skewed, input_pdf_path)

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

    img = Image.open(filepath)

    # convert to binary
    wd, ht = img.size
    pix = np.array(img.convert('1').getdata(), np.uint8)
    bin_img = 1 - (pix.reshape((ht, wd)) / 255.0)

    # evaluates how 'good' the rotation is
    def find_score(arr, test_angle):
        data = inter.rotate(arr, test_angle, reshape=False, order=0)
        hist = np.sum(data, axis=1)
        score = np.sum((hist[1:] - hist[:-1]) ** 2)
        return hist, score

    # Rotates the image through a series of trials, and keeps the best
    delta = 1
    limit = 5
    angles = np.arange(-limit, limit + delta, delta)
    scores = []
    for angle in angles:
        hist, score = find_score(bin_img, angle)
        scores.append(score)

    best_score = max(scores)
    angle = angles[scores.index(best_score)]

    # rotate the image to deskew it
    image = cv2.imread(filepath)
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


def fix_pil(doc, doc_path):
    """
    Takes in a list of PIL files that need to be deskewed and returns the images in PIL format

    Because this function deals strictly with images, there are no doctests.

    :param doc: list of PIL files
    :param doc_path: Path for temporary files to be stored
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
                                '3_32_verzuh_4.pdf')
    output_pdf_path = Path('..', 'computation_hist', 'data', 'sample_docs',
                           'skew_test_out.pdf')
    o = ocr_pdf(input_pdf_path, return_type='pdf', output_pdf_path=output_pdf_path)
