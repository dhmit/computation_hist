import os
from pathlib import Path, PurePath
from django.db import models
import sys
base_path = Path(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, PurePath.joinpath(base_path.parent, "djweb"))

from dj_comp_hist import models
from dj_comp_hist.models import Person, Document, Box, Folder, Organization, Page


path_to_boxes = PurePath.joinpath(base_path.parent,"computation_hist","data","web_test_set")


def create_sub_folders(path_to_boxes, foldername_short):
    """
    To run this code :
    sys.path
    sys.path.insert(0, '/Users/ifeademolu-odeneye/Documents/GitHub/computation_hist
    /computation_hist') - replace with your file path
    import sort_pdfs
    sort_pdfs.create_sub_folders(sort_pdfs.path_to_boxes, "rockefeller")

    takes in box, foldername_short and uses django_database to:
    1. sub directory for each document - named doc1, doc2 etc
    2. a sub directory for each page in document- named pg1, pg2 etc
    :return:
    """

    box = str(models.Folder.objects.get(name=foldername_short).box) #not this is a string

    root = PurePath.joinpath(path_to_boxes,  box)
    if not os.path.exists(root):
        Path.mkdir(root)

    root = PurePath.joinpath(root, foldername_short)
    if not os.path.exists(root):
        Path.mkdir(root)

    for doc in models.Folder.objects.get(name=foldername_short).document_set.all():
        Path.mkdir(PurePath.joinpath(root, "doc_" + str(doc.id)))
        for i in range(1,doc.number_of_pages+1):
            Path.mkdir(PurePath.joinpath(root, "doc_" + str(doc.id), "page_"+str(i)))

