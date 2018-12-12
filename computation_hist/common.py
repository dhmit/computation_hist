import gzip
import os
import pickle
import sys
import pdf2image
import PyPDF2
import pytesseract
from pathlib import Path

import pandas as pd


BASE_PATH = Path(os.path.abspath(os.path.dirname(__file__)))


def store_pickle(obj, filename):
    """
    Store a compressed "pickle" of the object in the "pickle_data" directory
    and return the full path to it.

    The filename should not contain a directory or suffix.

    Example in lieu of Doctest to avoid writing out a file.

        my_object = {'a': 4, 'b': 5, 'c': [1, 2, 3]}
        gender_novels.common.store_pickle(my_object, 'example_pickle')

    :param obj: Any Python object to be pickled
    :param filename: str | Path
    :return: Path
    """
    filename = BASE_PATH / 'data' / 'pickle_data' / (str(filename) + '.pgz')
    with gzip.GzipFile(filename, 'w') as fileout:
        pickle.dump(obj, fileout)
    return filename


def load_pickle(filename):
    """
    Load the pickle stored at filename where filename does not contain a
    directory or suffix.

    Example in lieu of Doctest to avoid writing out a file.

        my_object = gender_novels.common.load_pickle('example_pickle')
        my_object
        {'a': 4, 'b': 5, 'c': [1, 2, 3]}

    :param filename: str | Path
    :return: object
    """
    filename = BASE_PATH / 'data' / 'pickle_data' / (str(filename) + '.pgz')
    with gzip.GzipFile(filename, 'r') as filein:
        obj = pickle.load(filein)
    return obj



def get_metadata_google_sheet(return_type='dataframe'):

    """
    Loads the metadata from google sheets

    Note: To run this function, you need to have copied the google_credentials.json from the
    general slack channel into the google_credentials folder. When you run the script for the
    first time, it will create a token.json in the google_credentials folder that is specific to
    you. PLEASE RUN FROM __name__ == '__main__'. RUNNING FROM DOCTEST WILL FAIL THE FIRST TIME.

    Returns either a pandas dataframe...
    >>> df = get_metadata_google_sheet()
    >>> df['author'][0]
    'Corbato, F. J.'

    ... or a list of dicts
    >>> list_of_dicts = get_metadata_google_sheet(return_type='list_of_dicts')
    >>> list_of_dicts[0]['author'], list_of_dicts[0]['title']
    ('Corbato, F. J.', 'Requisition for materials for Audio Monitor of 704 Computer')

    """

    from apiclient.discovery import build
    from httplib2 import Http
    from oauth2client import file, client, tools

    if return_type not in ['dataframe', 'list_of_dicts']:
        raise ValueError('return_type has to be (pandas) "dataframe" or "list_of_dicts" but not '
                         '{return_type}.')


    spreadsheet_id = '1LU05c0lTSTQ9IY3RS4eDcyvq5HNBMx6mbuMJe6TX-ZA'
    sheet_name = 'metadata'

    credentials_path = Path(Path.home(), 'google_credentials')
    credentials_json_path = Path(credentials_path, 'google_credentials.json')
    token_json_path = Path(credentials_path, 'token.json')

    # Check if credentials file exists (which is used to create the local token.json)
    if not credentials_json_path.is_file():
        raise FileNotFoundError('Could not find google credentials. Please make sure to copy the '
                                'google_credentials.json from the #archivedocs slack channel to '
                                f'{credentials_json_path}')

    # If local credentials have not been created and the script is run from a doctest, raise error.
    # The doctest doesn't allow a user to authenticate via google and get the required token.json
    if not token_json_path.is_file() and hasattr(sys.modules['__main__'], 'DocTestRunner'):
        raise EnvironmentError("Cannot obtain token.json while running in a doctest. "
                               "Please run from __name__=='__main__' and follow the "
                               "automatically generated link to authenticate.")

    # Load credentials and set up Sheets API
    scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    store = file.Storage(token_json_path)
    creds = store.get()
    if not creds or creds.invalid:
        # if run from within doctest, raise an error--
        flow = client.flow_from_clientsecrets(credentials_json_path, scopes)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Download gsheet and turn into dataframe
    gsheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                 range=sheet_name).execute()
    values = gsheet.get('values', [])
    df = pd.DataFrame(values)


    # Turn first row into header
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])

    if return_type == 'dataframe':
        return df
    elif return_type == 'list_of_dicts':
        return df.to_dict('records')


def make_searchable_pdf(input_path, output_file_name=None):
    """
    This function takes in the file path to a document and return a searchable pdf
    using Tesseract through the pytesseract module

    *WARNING* Once a file is passed through this method while output_file=None, it will be
    overwritten with the Tesseract searchable PDF.

    Example to avoid creating files:

                # External PDF called test.pdf
                make_searchable(path/to/test.pdf, 'output_name')

    :param input_path: the filepath to be converted
    :param output_file_name: the file name that you wish to save the document under (without
    extensions)
    :return: output_file path
    """

    # Keeps track of output filepath, and creates an empty list for creating dummy filepaths
    if isinstance(input_path, str):
        input_path = Path(input_path)
    if output_file_name is None:
        output_file = input_path
        output_file_name = output_file.stem
    else:
        output_file = Path(input_path.parent, output_file_name + '.pdf')

    file_paths = []

    # Converts pdf into a list of PIL files
    image = pdf2image.convert_from_path(input_path, fmt='jpg')

    # Converts the PIL files into binaries and saves them in a list, along with the filepaths
    pages = []
    for i in range(len(image)):
        single_page = pytesseract.image_to_pdf_or_hocr(image[i], extension='pdf')
        pages.append(single_page)
        file_paths.append(Path(output_file.parent, output_file_name + '_' + str(i) + '.pdf'))

    # Creates dummy pdf documents that will be merged
    for i, page in enumerate(pages):
        with open(file_paths[i], 'wb') as f:
            f.write(page)

    # Merges the pdf files in python
    merger = PyPDF2.PdfFileMerger()
    for path in file_paths:
        merger.append(str(path))

    # Writes the merged file into one document and then deletes dummy files
    merger.write(str(output_file))
    for path in file_paths:
        path.unlink()

    return output_file


def make_text(input_path):
    """
    Returns the text received from the OCR of a pdf in a given filepath

    >>> text = make_text('data/sample_docs/3_32_verzuh_1.pdf')
    >>> text.count("Verzuh") == 1
    True

    """

    # Creates input filepath
    if isinstance(input_path, str):
        input_path = Path(input_path)

    # Converts PDF to PIL files
    image = pdf2image.convert_from_path(input_path, fmt='jpg')

    # Extracts text and returns string
    text = ''
    for i in range(len(image)):
        text += pytesseract.image_to_string(image[i]) + '\n\n\n'

    return text


def generate_ocr(input_path, output_file_name=None):
    """
    This method calls both make_readable and make_text to enable generating a searchable pdf and
    text document in one line of code.

    Example to avoid creating files:

                # External PDF called test.pdf
                generate_ocr(path/to/test.pdf, 'output_name')

    :param input_path: filepath to document
    :param output_file_name: file name to save the document as (without extensions)
    :return: dictionary with filepaths for 'pdf_path' and 'text_path' along with 'text'
    """

    # Creates output filepath
    if isinstance(input_path, str):
        input_path = Path(input_path)
    if output_file_name is None:
        output_file = input_path
        output_file_name = output_file.stem
    else:
        output_file = Path(input_path.parent, output_file_name + '.pdf')

    # Creates text file
    with open(Path(output_file.parent, output_file.stem + '.txt'), 'w') as f:
        f.write(make_text(input_path))

    # Returns a dictionary with filepaths and text of new documents
    return {'pdf_path': make_searchable_pdf(input_path, output_file_name),
            'txt_path': output_file,
            'text': make_text(input_path)}


if __name__ == '__main__':

#    df = get_metadata_google_sheet()
#    from dh_testers.testRunner import main_test
#    main_test(import_plus_relative=True)  # this allows for relative calls in the import.
    print(generate_ocr("data/sample_docs/3_32_verzuh_1.pdf", 'test')['text'].count('Verzuh'))

