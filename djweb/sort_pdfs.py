import urllib.request
import shutil
import sys
import os
from pathlib import Path, PurePath, PurePosixPath
from django.db import models
from computation_hist.common import make_searchable_pdf

from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path


DJWEB_PATH = Path(os.path.abspath(os.path.dirname(__file__)))
DATA_BASE_PATH = Path(DJWEB_PATH.parent,"computation_hist","data","processed_pdfs")


def download_raw_folder_pdf_from_aws(box:int, folder:int, foldername:str):
    '''
    Downloads a raw (not yet ocred) pdf file from amazon aws and stores it in the proper folder
    relative to DATA_BASE_PATH

    :return: Path
    '''

    rel_path = get_file_path(box, folder, foldername, file_type='raw_pdf', include_base_path=False)
    abs_path = Path(DATA_BASE_PATH, rel_path)

    # SR: I was worried about using str(Path) on Windows systems, hence the awkward "/".join()
    url = f'https://s3.amazonaws.com/comp-hist/docs/{"/".join(rel_path.parts)}'

    with urllib.request.urlopen(url) as response:
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        with open(abs_path, 'wb') as pdf_file:
            shutil.copyfileobj(response, pdf_file)

    return abs_path


def get_file_path(box: int, folder: int, foldername_short:str, file_type:str,
                  doc_id:int = None, page_id:int = None, include_base_path=True):
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
    :param doc_type: pdf, txt, png, or raw_pdf
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

    return path


def create_sub_folders(path_to_boxes=DATA_BASE_PATH, foldername_short='rockefeller'):


    """
    To run this code :
    sys.path
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


    from dj_comp_hist.models import Person, Document, Box, Folder, Organization, Page

    box = str(Folder.objects.get(name=foldername_short).box) # note this is a string

    # Note: you don't need to use joinpath. You can just join the parts of a path together like
    # this.
    root = Path(path_to_boxes,  box)

    # the command below will create the directory if it doesn't exist as well as any parent folders
    # where necessary.
    root.mkdir(parents=True, exist_ok=True)
    path_folder_pdf = Path(root, foldername_short)
    path_folder_pdf.mkdir(exist_ok=True)
    associated_documents = Folder.objects.get(name=foldername_short).document_set.all()
    split_folder_to_doc(path_folder_pdf, associated_documents, foldername_short)

    for doc in Folder.objects.get(name=foldername_short).document_set.all():
        Path(root, "doc_" + str(doc.id)).mkdir(exist_ok=True)
        for i in range(1,doc.number_of_pages+1):
            Path(root, "doc_" + str(doc.id), "page_"+str(i)).mkdir(exist_ok=True)


def split_doc_to_page(pdf_path, folder_name):
   print("********************")
   print(PurePath.joinpath(pdf_path,"1_08_raw_rockefeller.pdf"))
   # ------------------to be changed next line
   pages = convert_from_path(Path(pdf_path,"1_08_raw_rockefeller.pdf"))

   for page in range(1, len(pages)+1):
       Path.mkdir(PurePath.joinpath(pdf_path, "page_" + str(page)))

       page_path = PurePath.joinpath(pdf_path, "page_" + str(page), folder_name + '_' + str(page) + '.png')
       pages[page-1].save(page_path, 'PNG')#saves page to the directory


def split_folder_to_doc(pdf_path, associated_documents, folder_name):
   """

   :param pdf_path: the path up to the folder containing the pdfs
   :param associated_documents:
   :return:
   """
   #splits the folder pdfs
   start_pages = []
   pdf_location = PurePath.joinpath(pdf_path, "1_08_raw_rockefeller.pdf")
   for single_doc in associated_documents:
       start_pages.append(single_doc.first_page)
       list.sort(start_pages)
   folder_pdf = PdfFileReader(open(pdf_location, "rb"))
   for doc in associated_documents:
       if not os.path.exists(PurePath.joinpath(pdf_path, "doc_" + str(doc.id))):
           Path.mkdir(PurePath.joinpath(pdf_path, "doc_" + str(doc.id)))
       output = PdfFileWriter()
       for i in range(doc.first_page,doc.last_page):
           output.addPage(folder_pdf.getPage(i))
       with open("doc" + str(doc.id) + ".pdf", "wb") as outputStream:
           output.write(outputStream)

       split_doc_to_page(pdf_path, folder_name)

if __name__ == '__main__':
#    create_sub_folders()

    download_raw_folder_pdf_from_aws(2, 1, 'digital_comp_to_social_problems')
    pass