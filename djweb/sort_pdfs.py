import os
from pathlib import Path, PurePath
from django.db import models
from computation_hist.common import make_searchable_pdf
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path


base_path = Path(os.path.abspath(os.path.dirname(__file__)))

# SR: I think it's better to just move sort_pdfs.py to djweb so we don't have to deal with sys path
# insert
#sys.path.insert(0, PurePath.joinpath(base_path.parent, "djweb"))

from dj_comp_hist.models import Person, Document, Box, Folder, Organization, Page
path_to_boxes = Path(base_path.parent,"computation_hist","data","web_test_set")



def create_sub_folders(path_to_boxes=path_to_boxes, foldername_short='rockefeller'):
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
    create_sub_folders()