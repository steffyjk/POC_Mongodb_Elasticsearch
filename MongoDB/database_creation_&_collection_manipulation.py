from pymongo import MongoClient

# Establish a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017')

# Create or switch to a database
db = client['series_mongodb']

# # Perform operations on the database
collection = db['series_collection']

collection.insert_one({'name': 'You', 'genre': 'Psychological thriller',
                       'initial_release': 2018, 'total_seasons': 4})


# insert many
collection.insert_many([
    {'name': 'Euphoria', 'genre': 'Drama', 'initial_release': 2019, 'total_seasons': 2},
    {'name': 'Never Have I Ever', 'genre': 'Drama', 'initial_release': 2020, 'total_seasons': 4}, ]
)

# CREATE THE UNIQUE INDEX
collection.create_index('name', unique=True)

# Fetch all documents in the collection
cursor = collection.find()

# Iterate over the documents and print them
for document in cursor:
    print(document)

# Close the database connection
client.close()
