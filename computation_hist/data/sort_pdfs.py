@ -1,7 +1,12 @@
import os
from pathlib import Path, PurePath
from django.db import models
from common import make_searchable_pdf
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path


base_path = Path(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, PurePath.joinpath(base_path.parent, "djweb"))

@ -12,12 +17,14 @@ from dj_comp_hist.models import Person, Document, Box, Folder, Organization, Pag
path_to_boxes = PurePath.joinpath(base_path.parent,"computation_hist","data","web_test_set")



def create_sub_folders(path_to_boxes, foldername_short):
   """
   To run this code :
   sys.path
   sys.path.insert(0, '/Users/ifeademolu-odeneye/Documents/GitHub/computation_hist
   /computation_hist') - replace with your file path
   import dj_comp_hist
   from  dj_comp_hist import models
   import sys
   sys.path.insert(0, '/Users/ifeademolu-odeneye/Documents/GitHub/computation_hist/computation_hist')
   import sort_pdfs
   sort_pdfs.create_sub_folders(sort_pdfs.path_to_boxes, "rockefeller")

@ -27,18 +34,53 @@ def create_sub_folders(path_to_boxes, foldername_short):
   :return:
   """

   box = str(models.Folder.objects.get(name=foldername_short).box) #not this is a string

   box = str(models.Folder.objects.get(name=foldername_short).box) #note this is a string
   root = PurePath.joinpath(path_to_boxes,  box)
   if not os.path.exists(root):
       Path.mkdir(root)
   path_folder_pdf = PurePath.joinpath(root, foldername_short)
   if not os.path.exists(path_folder_pdf):
       Path.mkdir(path_folder_pdf)
   associated_documents = models.Folder.objects.get(name=foldername_short).document_set.all()


   split_folder_to_doc(path_folder_pdf, associated_documents, foldername_short)

   root = PurePath.joinpath(root, foldername_short)
   if not os.path.exists(root):
       Path.mkdir(root)

   for doc in models.Folder.objects.get(name=foldername_short).document_set.all():
       Path.mkdir(PurePath.joinpath(root, "doc_" + str(doc.id)))
       for i in range(1,doc.number_of_pages+1):
           Path.mkdir(PurePath.joinpath(root, "doc_" + str(doc.id), "page_"+str(i)))
def split_doc_to_page(pdf_path, folder_name):
   print("********************")
   print(PurePath.joinpath(pdf_path,"1_08_raw_rockefeller.pdf"))
   # ------------------to be changed next line
   pages = convert_from_path(PurePath.joinpath(pdf_path,"1_08_raw_rockefeller.pdf"))

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