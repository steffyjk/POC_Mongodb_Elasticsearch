from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from document_data import document
es = Elasticsearch(
    hosts=["http://localhost:9200"],

)
index_name = 'job_seeker'

document = document
# Create the index
# try:
#     es.indices.create(index=index_name)
# except Exception as e:
#     print("-->", e)

# ADDING ITEM
# try:
#     res = es.index(index=index_name, body=document)
#     print("--> this is res: ", res)
# except Exception as e:
#     print("There has been error while adding item:", e)

# SEARCHING
# Define the search query (match_all)
# query = {
#     "query": {
#         "match_all": {}
#     }
# }
#
# # # Perform the search query
# res = es.search(index=index_name, body=query)
#
# # Extract the documents from the search results
# documents = [hit['_source'] for hit in res['hits']['hits']]
#
# # Print the documents
# for doc in documents:
#     print(doc)