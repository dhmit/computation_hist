import gzip
import os
import pickle
import sys
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


def get_google_sheet(spreadsheet_id, sheet_name, return_type='dataframe'):
    """
    Loads a google sheet by the spreadsheet_id and the sheet name
    It will be primarily used to load the metadata from google sheets

    Note: To run this function, you need to have copied the google_credentials.json from the
    general slack channel into the google_credentials folder. When you run the script for the
    first time, it will create a token.json in the google_credentials folder that is specific to
    you. PLEASE RUN FROM __name__ == '__main__'. RUNNING FROM DOCTEST WILL FAIL THE FIRST TIME.

    Returns either a pandas dataframe...
    >>> df = get_google_sheet('1LU05c0lTSTQ9IY3RS4eDcyvq5HNBMx6mbuMJe6TX-ZA', 'metadata')
    >>> df['author'][0]
    'Corbato, F. J.'

    ... or a list of dicts
    >>> list_of_dicts = get_google_sheet('1LU05c0lTSTQ9IY3RS4eDcyvq5HNBMx6mbuMJe6TX-ZA',
    ...                                  'metadata', return_type='list_of_dicts')
    >>> list_of_dicts[0]['author'], list_of_dicts[0]['title']
    ('Corbato, F. J.', 'Requisition for materials for Audio Monitor of 704 Computer')

    """

    from apiclient.discovery import build
    from httplib2 import Http
    from oauth2client import file, client, tools

    if return_type not in ['dataframe', 'list_of_dicts']:
        raise ValueError('return_type has to be (pandas) "dataframe" or "list_of_dicts" but not '
                         '{return_type}.')

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
    df = df.reset_index()

    if return_type == 'dataframe':
        return df
    elif return_type == 'list_of_dicts':
        return df.to_dict('records')


if __name__ == '__main__':

    df = get_google_sheet('1LU05c0lTSTQ9IY3RS4eDcyvq5HNBMx6mbuMJe6TX-ZA', 'metadata')
    from dh_testers.testRunner import main_test
    main_test(import_plus_relative=True)  # this allows for relative calls in the import.

