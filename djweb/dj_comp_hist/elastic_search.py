from elasticsearch import Elasticsearch
from IPython import embed


ES_URL = 'https://search-cc-hist-pclno2kchnjcohcayb2n7g3eha.us-west-2.es.amazonaws.com/'


class ESearch():

    def __init__(self, connection_type='local'):

        if connection_type == 'local':
            self.con = Elasticsearch(ES_URL)

        # create index, ignore if it already exists
        self.index_name = 'test'
        self.doc_type = 'cc_doc'
        self.con.indices.create(index=self.index_name, ignore=400)


    def populate_index(self):
        from .models import Document
        from .common import get_file_path

        for document in Document.objects.all():
            try:
                doc = {
                    'foldername_short': document.folder.name,
                    'folder_id': document.folder.number,
                    'box_id': document.folder.box.number,
                    'doc_id': document.doc_id,

                    'title': document.title,
                    'date': document.date,
                    'pages': document.last_page - document.first_page + 1,

                    'author_person': [p.fullname for p in document.author_person.all()],
                    'author_organization': [p.name for p in document.author_organization.all()],
                    'recipient_person': [p.fullname for p in document.recipient_person.all()],
                    'recipient_organization': [p.name for p in
                                               document.recipient_organization.all()],
                    'cced_person': [p.fullname for p in document.cced_person.all()],
                    'cced_organization': [p.name for p in document.cced_organization.all()]
                }

                txt_path = get_file_path(box=doc['box_id'], folder=doc['folder_id'],
                                         foldername_short=doc['foldername_short'], doc_id=doc['doc_id'],
                                         path_type='absolute', file_type='txt')
                try:
                    with open(txt_path, 'r') as f:
                        doc['text'] = f.read()
                except FileNotFoundError:
                    print(f'skipped {document.file_name}')
                    continue

                self.con.index(index=self.index_name, doc_type=self.doc_type, id=document.file_name,
                               body=doc)

                print(f'inserted {document.file_name}.')

            except:
                import traceback
                traceback.print_exc()
                print(f"Uncaught error with {document.file_name}")

                embed()

    def search(self):

        query = {
            'from': 5,
            'size': 20,
            'query': {
                'match': {
                    'text': 'ibm'
                }
            },
            'highlight':{
                'fields': {
                    'text': {}
                }
            }
        }

        results = self.con.search(index=self.index_name, doc_type=self.doc_type, body=query)

        for doc in results['hits']['hits']:
            print("%s) %s" % (doc['_id'], doc['highlight']['text']))

        print(f'No hits: {results["hits"]["total"]}.')

        embed()
#            embed()
