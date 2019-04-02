import re
from pathlib import Path

import pandas as pd

from common import BASE_PATH


class DocumentCollection():
    """
    The DocumentCollection class holds a collection of documents and can load, as an example,
    the sample documents from one folder.
    For the time being, the purpose of this class is to get the Django group a starting point to
    being work with databases and fulltext search.

    # to load the sample collection, initialize with collection='sample_collection'
    >>> sample_collection = DocumentCollection(collection='sample_collection')
    >>> print(f"Sample collection has {len(sample_collection.documents)} documents.")
    Sample collection has 11 documents.

    # Each document in the collection is a Document type with all the metadata including the full
    # text. See the documentation for the Document class on how to use it.
    >>> first_doc = sample_collection.documents[0]
    >>> first_doc
    Document. Author: Corbato, F. J.. Title: Requisition for materials for Audio Monitor of 704 Computer

    >>> first_doc.text.split()[:10]
    ['/~', 't', 'ht~', 'F.', 'J.', 'Corbato', 'M.', 'November', '21,', '1957']

    """

    def __init__(self, collection='sample_collection'):

        self.documents = []

        if collection not in ['full_collection', 'sample_collection', 'empty']:
            raise ValueError(f'DocumentCollection can only be initialized with collection param '
                             f'set to "full_collection" (loads all documents from the archives), '
                             f'"sample_collection" (loads a collection of 13 sample documents), '
                             f'and "empty" (loads an empty collection). You used collection='
                             f'{collection}.')

        # TODO: Implement loading of the full collection of documents, that is: load the metadata
        # TODO: from the google sheet and import all documents
        if collection == 'full_collection':
            pass

        elif collection == 'sample_collection':
            sample_docs_path = Path(BASE_PATH, 'data', 'sample_docs')
            metadata = pd.read_csv(Path(sample_docs_path, 'verzuh_metadata.csv')).to_dict('records')
            for doc_metadata in metadata:

                doc_metadata['pdf_path'] = Path(sample_docs_path,
                                                f'{doc_metadata["filename"]}.pdf')
                doc_metadata['txt_path'] = Path(sample_docs_path,
                                                f'{doc_metadata["filename"]}.txt')
                doc = Document(doc_metadata)
                self.documents.append(doc)


class Document:
    """
    The Document class loads and holds the metadata and text fore one archival document
    Currently, it is only a stub for further development

    TODO: This may not be needed as a class but might get ported to a Django model.

    You can load a sample document including ocred text with
    >>> sample_doc = Document(load_sample_doc=True)
    >>> sample_doc.author, sample_doc.title
    ('Corbato, F. J.', 'Requisition for materials for Audio Monitor of 704 Computer')

    """

    def __init__(self, document_metadata_dict=None, load_sample_doc=False):
        """
        Loads the metadata for a document

        :param document_metadata_dict: dict or None
        :param load_sample_doc: True to load the sample document. Default: False

        Note: You can set the document text by passing a 'text' key
        >>> metadata = {'box': 2, 'foldername_short': 'verzuh', 'doc_id': 1,
        ...             'filename': '3_32_verzuh_1', 'author': 'Corbato, F. J.', 'title': 'n/a',
        ...             'date': '1957-11-21', 'text': 'Sample text...'}
        >>> doc = Document(metadata)
        >>> doc.text
        'Sample text...'

        You can also load a sample document without passing a document_metadata_dict
        >>> sample_doc = Document(load_sample_doc=True)
        >>> sample_doc.author, sample_doc.title
        ('Corbato, F. J.', 'Requisition for materials for Audio Monitor of 704 Computer')

        The sample_doc includes messy ocr text
        >>> sample_doc.text[8:68].split()
        ['F.', 'J.', 'Corbato', 'M.', 'November', '21,', '1957', 'Verzuh', 'To:', 'Dr.', 'Subject:']

        """

        # If we load the sample doc, set the metadata_dict to the sample_doc
        if load_sample_doc:
            if document_metadata_dict:
                print("WARNING: Loading sample document but also received a "
                      "document_metadata_dict. If you want to load that data, set load_sample_doc "
                      "to False.")
            else:
                document_metadata_dict = {
                    'box': 2, 'foldername_short': 'verzuh', 'doc_id': 1, 'filename': '2_verzuh_1',
                    'foldername_full': 'Verzuh, Dr. Frank M.', 'author': 'Corbato, F. J.',
                    'title': 'Requisition for materials for Audio Monitor of 704 Computer',
                    'date': '1957-11-21', 'type': 'letter', 'recipients': 'Verzuh, F. M.',
                    'notes': 'None',
                    'pdf_path': Path(BASE_PATH, 'data', 'sample_docs', '3_32_verzuh_1.pdf'),
                    'txt_path': Path(BASE_PATH, 'data', 'sample_docs', '3_32_verzuh_1.txt'),
                }

        if not hasattr(document_metadata_dict, 'items'):
            raise ValueError(
                'document_metadata_dict must be a dictionary or support .items()')

        # Check that the essential attributes for the document exists.
        # TODO: Decide which attributes are essential for the document
        for key in ('box', 'foldername_short', 'doc_id', 'filename', 'author', 'title',
                    'date'):
            if key not in document_metadata_dict:
                raise ValueError(f'document_metadata_dict must have an entry for "{key}". Full ',
                                 f'metadata: {document_metadata_dict}')

        for key in document_metadata_dict:
            setattr(self, key, document_metadata_dict[key])

        # check date formatting
        if self.date == 'None':
            self.date = None
        # else:
        #     if not re.match(r'19\d{2}-\d{2}-\d{2}', self.date):
        #         raise ValueError('Invalid date format. Please enter the date in the metadata as '
        #                          f'YYYY-MM-DD. The set date is {self.date}.')

        # Load text if it wasn't passed as a metadata key
        if not hasattr(self, 'text'):
            # Check that the filename looks like a filename (ends in .txt)
            if not self.txt_path.parts[-1].endswith('.txt'):
                raise ValueError(
                    f'The document txt_path({self.txt_path}) should end in .txt . Full '
                    f'metadata: {document_metadata_dict}.')
            try:
                with open(self.txt_path) as f:
                    self.text = f.read()
            except FileNotFoundError:
                err = "Could not find the novel text file "
                err += "at the expected location ({file_path})."
                raise FileNotFoundError(err)

        # split and merge recipients and cced into one list
        if hasattr(self, 'recipients') and self.recipients is not None:
            self.recipients = [recipient.strip() for recipient in self.recipients.split(';')]
            if hasattr(self, 'cced'):
                self.recipients += [recipient.strip() for recipient in self.cced.split(';')]
        else:
            self.recipients = None

    def __repr__(self):
        return f'Document. Author: {self.author}. Title: {self.title}'


if __name__ == '__main__':
    col = DocumentCollection(collection='sample_collection')