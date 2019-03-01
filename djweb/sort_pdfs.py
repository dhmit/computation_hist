import urllib.request, urllib.error
import shutil
import sys
import os
from pathlib import Path, PurePath, PurePosixPath
from django.db import models
#from computation_hist.common import make_searchable_pdf
from dj_comp_hist.models import Folder
from dj_comp_hist.common import get_file_path
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path



DJWEB_PATH = Path(os.path.abspath(os.path.dirname(__file__)))
DATA_BASE_PATH = Path(DJWEB_PATH.parent,"computation_hist","data","processed_pdfs")

from IPython import embed; embed()


def main_function(test_run=True):
    # ----- go through each folder in the database
        # right now we are setting box,folder,foldername
    folder_list = Folder.objects.all()

    if test_run:
        folder_list = folder_list[:2]

    for current_folder in folder_list:
        box = current_folder.box
        foldername_short = current_folder.name
        # place it in the correct folder creating it if neccessary
        path_to_folder = download_raw_folder_pdf_from_aws(box, current_folder, foldername_short)
        # for each folder - split into documents, for each document - split the document into pages
        #TODO: is this the correct name of the PDF
        split_folder_to_doc(path_to_folder, path_to_folder, foldername_short)

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


def split_doc_to_page(pdf_path, folder_name):
   print("********************")
   print(PurePath.joinpath(pdf_path,"1_08_raw_rockefeller.pdf"))
   # ------------------to be changed next line
   pages = convert_from_path(Path(pdf_path,"1_08_raw_rockefeller.pdf"))

   for page in range(1, len(pages)+1):
       Path.mkdir(PurePath.joinpath(pdf_path, "page_" + str(page)))

       page_path = PurePath.joinpath(pdf_path, "page_" + str(page), folder_name + '_' + str(page) + '.png')
       pages[page-1].save(page_path, 'PNG')#saves page to the directory


def split_folder_to_doc(pdf_location,pdf_path, foldername_short):
    """

    :param pdf_path: the path up to the folder containing the pdfs
    :param associated_documents:
    :return:
    """

    start_pages = []
    associated_documents = Folder.objects.get(name=foldername_short).document_set.all()
    for single_doc in associated_documents:
        start_pages.append(single_doc.first_page)
        list.sort(start_pages)
    folder_pdf = PdfFileReader(open(pdf_path, "rb"))
    for doc in associated_documents:
        if not os.path.exists(PurePath.joinpath(pdf_location, "doc_" + str(doc.id))):
            Path.mkdir(PurePath.joinpath(pdf_path, "doc_" + str(doc.id)))
        output = PdfFileWriter()
        for i in range(doc.first_page, doc.last_page):
            output.addPage(folder_pdf.getPage(i))
        with open("doc" + str(doc.id) + ".pdf", "wb") as outputStream:
            output.write(outputStream)
        split_doc_to_page(pdf_path, foldername_short)

if __name__ == '__main__':
    download_raw_folder_pdf_from_aws(2, 1, 'digital_comp_to_social_problems')
    pass