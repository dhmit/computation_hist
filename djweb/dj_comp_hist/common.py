import urllib.request, urllib.error
import shutil
import sys
import os
from pathlib import Path, PurePath, PurePosixPath
from django.db import models


DJWEB_PATH = Path(os.path.abspath(os.path.dirname(__file__)))
DATA_BASE_PATH = Path(DJWEB_PATH.parent,"computation_hist","data","processed_pdfs")


def get_file_path(box: int, folder: int, foldername_short:str, file_type:str,
                  doc_id:int = None, page_id:int = None, include_base_path=True, aws_file=False):
    """
    Returns the path to a page, doc, or folder file based on box, folder, name, filetype, docid
    Note: will return a Posix or Windows path depending on the OS. Below, all paths are cast
    to PurePosixPath to make doctests pass on all systems.
    raw_pdf:
    >>> p = get_file_path(1, 8, 'rockefeller', file_type='raw_pdf',
    ... include_base_path=False)
    >>> PurePosixPath(p)
    PurePosixPath('1_8_rockefeller/raw_pdf/1_8_rockefeller_raw.pdf')
    document ocr text file (document txt/pdf returned when a doc_id is included but no page_id)
    >>> p = get_file_path(1, 8, 'rockefeller', file_type='txt', doc_id=4,
    ... include_base_path=False)
    >>> PurePosixPath(p)
    PurePosixPath('1_8_rockefeller/docs/4/1_8_rockefeller_4.txt')
    page png (page path returned when both doc_id and page_id are included
    >>> p = get_file_path(1, 8, 'rockefeller', file_type='txt', doc_id=4, page_id=20,
    ... include_base_path=False)
    >>> PurePosixPath(p)
    PurePosixPath('1_8_rockefeller/docs/4/pages/20/1_8_rockefeller_4_20.txt')
    By default, the path includes the base path of the data directory.
    (No doctest as the result changes from system to system)
    > get_file_path(1, 8, 'rockefeller', file_type='txt', doc_id=4, page_id=20,
    ... include_base_path=True)
    PosixPath('/home/code/computation_hist/computation_hist/data/web_test_set/1_8_rockefeller/docs/4/pages/20/1_8_rockefeller_4_20.txt')
    :param box: int
    :param folder: int
    :param foldername_short: str
    :param doc_type: 'pdf', 'txt', 'png', or 'raw_pdf'
    :param doc_id: int
    :param page_id: int
    :return: Path
    """

    if not file_type in ['pdf', 'txt', 'png', 'raw_pdf']:
        raise ValueError(f'doc_type has to be pdf, txt, png, or raw_pdf but not {file_type}.')

    if file_type == 'raw_pdf' and (doc_id or page_id):
        raise ValueError(f'doc_type raw_pdf returns the path to the un-ocred folder pdf. However, '
                         f'you also passed in a doc or page id. raw ids for pages or docs are not'
                         f'available.')

    if page_id and not doc_id:
        raise ValueError(f'Can only load a page_id if a doc_id was also provided. Doc_id: {doc_id}')

    full_folder_name = f'{box}_{folder}_{foldername_short}'

    if file_type == 'raw_pdf':
        path = Path(full_folder_name, 'raw_pdf', f'{full_folder_name}_raw.pdf')

    elif doc_id and not page_id:
        path = Path(full_folder_name, 'docs', str(doc_id),
                    f'{full_folder_name}_{doc_id}.{file_type}')

    else:
        path = Path(full_folder_name, 'docs', str(doc_id), 'pages', str(page_id),
                    f'{full_folder_name}_{doc_id}_{page_id}.{file_type}')

    if include_base_path:
        path = Path(DATA_BASE_PATH, path)

    if aws_file:
        path = Path("https://s3.amazonaws.com/comp-hist/docs/2_1_digital_comp_to_social_problems" \
                 "/docs/", path)

    return path
