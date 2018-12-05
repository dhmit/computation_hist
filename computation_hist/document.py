from pathlib import Path

from computation_hist.common import BASE_PATH


class Document():
    """
    The document loads and holds the metadata and text fore one archival document
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
        :param load_text: True to load the text, False skips loading the text. Default: True

        Note: You can set the document text by passing a 'text' key
        >>> metadata = {'box': 2, 'foldername_short': 'verzuh', 'doc_id': 1,
        ...             'filename': '2_verzuh_1', 'author': 'Corbato, F. J.', 'title': 'n/a',
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
                    'pdf_path': Path(BASE_PATH, 'data', 'sample_docs', '2_verzuh_1.pdf'),
                    'txt_path': Path(BASE_PATH, 'data', 'sample_docs', '2_verzuh_1.txt'),
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

        # TODO: Check date format (YYYY-MM-DD)

        for key in document_metadata_dict:
            setattr(self, key, document_metadata_dict[key])

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
