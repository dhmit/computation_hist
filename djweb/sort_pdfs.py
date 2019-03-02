import urllib.request, urllib.error
import shutil
import sys
from IPython import embed
import os
from pathlib import Path, PurePath, PurePosixPath
from django.db import models
from dj_comp_hist.models import Folder
from dj_comp_hist.common import get_file_path, DATA_BASE_PATH
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path

import pytesseract

from ocr import ocr_pdf


def main_function(test_run=True):
    """
    Iterates over all Folder Objects, downloads the folder pdf from aws and stores it in its
    designated directory.
    Split the folder into documents and store those in their respective directory
        within the split_folder_to_doc(...) split each doc into pages and store in directory
    :param test_run: If True then only runs on 2 folders
    :return:
    """
    folder_list = Folder.objects.all()
    #Allows us to test the function
    if test_run:
        folder_list = folder_list[:1]
    for current_folder in folder_list:
        # set values based on folder being processed
        box_id = current_folder.box.number
        folder_id = current_folder.number
        foldername_short = current_folder.name
        # download the folder from aws and store it in the designated directory (creating it if
        # necessary
        folder_pdf_path = download_raw_folder_pdf_from_aws(box_id, folder_id, foldername_short)
        # split the folder into docs and store it in the correct directory
        # within the function doc's are split to pages
        split_folder_to_doc(folder_pdf_path, foldername_short, box_id, folder_id)


def download_raw_folder_pdf_from_aws(box_no:int, folder_no:int, foldername_short:str):
    """
    Downloads a raw (not yet ocred) pdf file from amazon aws and stores it in the proper folder
    relative to DATA_BASE_PATH from dj_comp_hist.common

    :param box_no:
    :param folder_no:
    :param foldername_short:
    :return: the absolute path of the pdf file (including the pdf file itself)
    """
    rel_path = get_file_path(box_no, folder_no, foldername_short, file_type='raw_pdf')
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
    print(abs_path)
    return abs_path


def split_doc_to_page(doc_pdf_path, foldername_short, box_no, folder_no, doc_no):
    """
    split each document into pages and save it's png file and stores it
    root/folder/docs/doc_id:int/pages/page_id:int

    :param doc_pdf_path: path of the pdf itself
    :param foldername_short:
    :param box_no:
    :param folder_no:
    :param doc_no:
    :return:
    """

    pages = convert_from_path(doc_pdf_path)

    for page in range(1, len(pages)+1):
        # find parent directories and make them
        page_png_file_path = get_file_path(box_no, folder_no, foldername_short, file_type='png',
                                 doc_id=doc_no, page_id=page, path_type='absolute')
        page_txt_file_path = get_file_path(box_no, folder_no, foldername_short, file_type='txt',
                                 doc_id=doc_no, page_id=page, path_type='absolute')
        page_png_file_path.parent.mkdir(parents=True, exist_ok=True)
        # create png files
        pages[page-1].save(page_png_file_path, 'PNG')
        # create text file
        with open(page_txt_file_path, 'w') as out:
            text = pytesseract.image_to_string(pages[page - 1])
            out.write(text)


def split_folder_to_doc(folder_pdf_path, foldername_short, box_no, folder_no):
    """
    split the folder into document ocr pdfs and a text file and store it in a file path
    root/folder/docs/doc_id:int/
    split each document into pages and save it's png file and stores it
    root/folder/docs/doc_id:int/pages/page_id:int
    :param folder_pdf_path: absolute path of the raw pdf
    :param foldername_short: foldername_short used to reference model
    :param box_no: used to reference model
    :param folder_no: used to reference model
    :return:
    """
    # get the information of the documents in the folder
    associated_documents = Folder.objects.get(name=foldername_short).document_set.all()
    folder_pdf = PdfFileReader(open(folder_pdf_path, "rb"))
    # iterate over the documents
    for doc in associated_documents:
        # create the path to the place the doc_pdf should be stored
        doc_pdf_file_path = get_file_path(box_no, folder_no, foldername_short, file_type='pdf',
                                          doc_id=doc.doc_id, path_type='absolute')
        # make all the necessary parents directoried of the doc_pdf
        doc_pdf_file_path.parent.mkdir(parents=True, exist_ok=True)
        output = PdfFileWriter()
        # iterate over the pages in the docs page range and save them to doc_pdf_file_path
        for i in range(doc.first_page - 1, doc.last_page):
            output.addPage(folder_pdf.getPage(i))
        with open(doc_pdf_file_path, "wb") as outputStream:
            output.write(outputStream)
        # ocr the new doc pdf
        ocr_pdf(input_pdf_path=doc_pdf_file_path, output_pdf_path=doc_pdf_file_path)
        # ... and create a txt file of the ocr
        doc_txt_file_path = get_file_path(box_no, folder_no, foldername_short, file_type='txt',
                                          doc_id=doc.doc_id, path_type='absolute')
        ocr_text = ocr_pdf(input_pdf_path=doc_pdf_file_path, return_type='text')
        with open(doc_txt_file_path, 'w') as out:
            out.write(ocr_text)
        # split the doc into pages
        split_doc_to_page(doc_pdf_file_path, foldername_short, box_no, folder_no, doc.doc_id)


if __name__ == '__main__':
    download_raw_folder_pdf_from_aws(2, 1, 'digital_comp_to_social_problems')
    pass

