import os
from pathlib import Path, PurePosixPath

from dj_config.settings import DATA_DIR

PROCESSED_PDFS_PATH = Path(DATA_DIR, "processed_pdfs")

def get_file_path(box: int, folder: int, foldername_short:str, file_type:str,
                  doc_id:int = None, page_id:int = None, path_type='relative'):
    """
    Returns the path to a page, doc, or folder file based on box, folder, name, filetype, docid
    Note: will return a Posix or Windows path depending on the OS. Below, all paths are cast
    to PurePosixPath to make doctests pass on all systems.

    raw_pdf:
    >>> p = get_file_path(1, 8, 'rockefeller', file_type='raw_pdf')
    >>> PurePosixPath(p)
    PurePosixPath('1_8_rockefeller/raw_pdf/1_8_rockefeller_raw.pdf')

    document ocr text file (document txt/pdf returned when a doc_id is included but no page_id)
    >>> p = get_file_path(1, 8, 'rockefeller', file_type='txt', doc_id=4)
    >>> PurePosixPath(p)
    PurePosixPath('1_8_rockefeller/docs/4/1_8_rockefeller_4.txt')

    >>> p = get_file_path(1, 8, 'rockefeller', file_type='pdf', doc_id=4)
    >>> PurePosixPath(p)
    PurePosixPath('1_8_rockefeller/docs/4/1_8_rockefeller_4.pdf')

    page png (page path returned when both doc_id and page_id are included
    >>> p = get_file_path(1, 8, 'rockefeller', file_type='txt', doc_id=4, page_id=20)
    >>> PurePosixPath(p)
    PurePosixPath('1_8_rockefeller/docs/4/pages/20/1_8_rockefeller_4_20.txt')

    By default, the path returned is relative to the data directory (path_type='relative')
    To generate an absolute path, use path_type='absolute':
    (No doctest as the result changes from system to system)
    > get_file_path(1, 8, 'rockefeller', file_type='txt', doc_id=4, page_id=20, path_type='absolute)
    PosixPath('/home/code/computation_hist/computation_hist/data/web_test_set/1_8_rockefeller/docs/4/pages/20/1_8_rockefeller_4_20.txt')

    To generate an aws path, use path_type='aws'
    >>> get_file_path(1, 8, 'rockefeller', file_type='raw_pdf', path_type='aws')
    PosixPath('https:/s3.amazonaws.com/comp-hist/docs/1_8_rockefeller/raw_pdf/1_8_rockefeller_raw.pdf')

    :param box: int
    :param folder: int
    :param foldername_short: str
    :param doc_type: 'pdf', 'txt', 'png', or 'raw_pdf' raw_pdf is the un-ocred folder-level pdf
    :param doc_id: int
    :param page_id: int
    :param path_type: 'relative', 'absolute', or 'aws'
    :return: Path
    """

    if file_type not in ['pdf', 'txt', 'png', 'raw_pdf']:
        raise ValueError(f'doc_type has to be pdf, txt, png, or raw_pdf but not {file_type}.')

    if path_type not in ['relative', 'absolute', 'aws']:
        raise ValueError(f'path_type has to be relative, absolute, or aws but not {path_type}.')

    if file_type == 'raw_pdf' and (doc_id or page_id):
        raise ValueError(f'doc_type raw_pdf returns the path to the un-ocred folder pdf. However, '
                         f'you also passed in a doc or page id. raw ids for pages or docs are not'
                         f'available.')

    if page_id and not doc_id:
        raise ValueError(f'Can only load a page_id if a doc_id was also provided. Doc_id: {doc_id}')

    full_folder_name = f'{box}_{folder}_{foldername_short}'

    if file_type == 'raw_pdf' :
        path = Path(full_folder_name, 'raw_pdf', f'{full_folder_name}_raw.pdf')

    elif doc_id and not page_id:
        path = Path(full_folder_name, 'docs', str(doc_id),
                    f'{full_folder_name}_{doc_id}.{file_type}')

    else:
        path = Path(full_folder_name, 'docs', str(doc_id), 'pages', str(page_id),
                    f'{full_folder_name}_{doc_id}_{page_id}.{file_type}')

    if path_type == 'relative':
        return path
    elif path_type == 'absolute':
        return Path(PROCESSED_PDFS_PATH, path)
    elif path_type == 'aws':
        return Path("https://s3.amazonaws.com/comp-hist/docs/", path)
    else:
        raise NotImplementedError('Only path_type relative, absolute, and aws are implemented.')


