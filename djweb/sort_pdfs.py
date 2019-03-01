import urllib.request, urllib.error
import shutil
import sys
from IPython import embed
import os
from pathlib import Path, PurePath, PurePosixPath
from django.db import models
#from computation_hist.common import make_searchable_pdf
from dj_comp_hist.models import Folder
from dj_comp_hist.common import get_file_path, DATA_BASE_PATH
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path

import pytesseract

from ocr import ocr_pdf


def main_function(test_run=True):
    # ----- go through each folder in the database
        # right now we are setting box,folder,foldername
    folder_list = Folder.objects.all()

    if test_run:
        folder_list = folder_list[:1]

    print(folder_list)

    for current_folder in folder_list:
        box_id = current_folder.box.number
        folder_id = current_folder.number
        foldername_short = current_folder.name
        # place it in the correct folder creating it if neccessary

        folder_pdf_path = download_raw_folder_pdf_from_aws(box_id, folder_id, foldername_short)
        # for each folder - split into documents, for each document - split the document into pages
        #TODO: is this the correct name of the PDF
        split_folder_to_doc(folder_pdf_path, foldername_short, box_id, folder_id)


def download_raw_folder_pdf_from_aws(box:int, folder:int, foldername:str):
    '''
    Downloads a raw (not yet ocred) pdf file from amazon aws and stores it in the proper folder
    relative to DATA_BASE_PATH from dj_comp_hist.common

    :return: Path
    '''
    rel_path = get_file_path(box, folder, foldername, file_type='raw_pdf')
    abs_path = Path(DATA_BASE_PATH, rel_path)
    if abs_path.exists():
        print(f'PDF {rel_path} already downloaded. Skipping download')
        return abs_path
    # SR: I was worried about using str(Path) on Windows systems, hence the awkward "/".join()
    url = f'https://s3.amazonaws.com/comp-hist/docs/{"/".join(rel_path.parts)}'
    try:
        with urllib.request.urlopen(url) as response:
            abs_path.parent.mkdir(parents=True, exist_ok=True)
            with open(abs_path, 'wb') as pdf_file:
                shutil.copyfileobj(response, pdf_file)
    except urllib.error.HTTPError:
        raise(FileNotFoundError(f'{url} is not available from our AWS bucket. For a list of '
                                     f'available files, see aws_available_files.md in the '
                                     f'computation_hist/data directory.'))
    return abs_path


def create_sub_directories(path_to_folder, foldername_short='rockefeller'):
    """
    take in a folder, split into documents, as you split into documents, take the document and
    split into pages
    for each folder - split into documents, for each document - split the document into page

    To run this code :
    sys.path
    import sys
    sys.path.insert(0, '/Users/ifeademolu-odeneye/Documents/GitHub/computation_hist
    /computation_hist') - replace with your file path
    import dj_comp_hist
    from  dj_comp_hist import models
    import sys
    sys.path.insert(0, '/Users/ifeademolu-odeneye/Documents/GitHub/computation_hist
     /computation_hist')
    import sort_pdfs
    sort_pdfs.create_sub_folders(sort_pdfs.path_to_boxes, "rockefeller")

    :return:
    """
    pass


def split_doc_to_page(doc_pdf_path, foldername_short, box_no, folder_no, doc_no):

    """
    Given a path to a document pdf_path, this function extracts all of the pages as png files.

    :param pdf_path:
    :param foldername_short:
    :param box_no:
    :param folder_no:
    :param doc_no:
    :return:
    """

    print(doc_pdf_path)
    pages = convert_from_path(doc_pdf_path)

    for page in range(1, len(pages)+1):
        page_png_file_path = get_file_path(box_no, folder_no, foldername_short, file_type='png',
                                 doc_id=doc_no, page_id=page, path_type='absolute')
        page_txt_file_path = get_file_path(box_no, folder_no, foldername_short, file_type='txt',
                                 doc_id=doc_no, page_id=page, path_type='absolute')
        page_png_file_path.parent.mkdir(parents=True, exist_ok=True)
        pages[page-1].save(page_png_file_path, 'PNG')
        with open(page_txt_file_path, 'w') as out:
            text = pytesseract.image_to_string(pages[page - 1])
            out.write(text)


def split_folder_to_doc(folder_pdf_path, foldername_short, box_id, folder_id):
    """

    :param pdf_path: the path up to the folder containing the pdfs
    :param associated_documents:
    :return:
    """

    associated_documents = Folder.objects.get(name=foldername_short).document_set.all()
    folder_pdf = PdfFileReader(open(folder_pdf_path, "rb"))
    for doc in associated_documents:
        doc_pdf_file_path = get_file_path(box_id, folder_id, foldername_short, file_type='pdf',
                                      doc_id=doc.doc_id, path_type='absolute')
        doc_pdf_file_path.parent.mkdir(parents=True, exist_ok=True)

        output = PdfFileWriter()
        for i in range(doc.first_page - 1, doc.last_page):
            output.addPage(folder_pdf.getPage(i))
        with open(doc_pdf_file_path, "wb") as outputStream:
            output.write(outputStream)

        # ocr the new doc pdf
        ocr_pdf(input_pdf_path=doc_pdf_file_path, output_pdf_path=doc_pdf_file_path)
        # ... and create a txt file of the ocr
        doc_txt_file_path = get_file_path(box_id, folder_id, foldername_short, file_type='txt',
                                      doc_id=doc.doc_id, path_type='absolute')
        ocr_text = ocr_pdf(input_pdf_path=doc_pdf_file_path, return_type='text')
        with open(doc_txt_file_path, 'w') as out:
            out.write(ocr_text)

        split_doc_to_page(doc_pdf_file_path, foldername_short, box_id, folder_id, doc.doc_id)

if __name__ == '__main__':
    download_raw_folder_pdf_from_aws(2, 1, 'digital_comp_to_social_problems')
    pass