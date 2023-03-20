from elasticsearch_dsl.connections import connections
from django_elasticsearch_dsl import Document, Index
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

client = Elasticsearch(['http://elasticsearch:9200'])

my_search = Search(using=client)

from .models import CustomUser

# Create a connection to ElasticSearch
connections.create_connection()

user = Index('users')

user.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@user.doc_type
class UserDocument(Document):
    class Django:
        model = CustomUser
        exclude = 'password'

# define search function
def search(email):
    query = my_search.query("match", email=email)
    response = query.execute()
    return response
