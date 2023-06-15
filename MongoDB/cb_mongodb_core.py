from pymongo import MongoClient


class ClassMongoDB:
    client = None

    def __init__(self):
        # Create mongo client right after object of this class created
        self.connect_mongo_client()

    @classmethod
    def connect_mongo_client(cls):
        # Establish a connection to the MongoDB server
        cls.client = MongoClient('mongodb://localhost:27017')

    def get_database(self, db_name):
        # Select the particular database from MongoDB0
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        # Get particular collection from provided database
        self.collection = self.db[collection_name]

    def create_unique_index(self, field_name):
        # Create index with unique=True provided Field name
        self.collection.create_index(field_name, unique=True)

    def insert_document(self, insertion_data):
        # Insert document one & many both
        if isinstance(insertion_data, dict):
            self.collection.insert_one(insertion_data)
        elif isinstance(insertion_data, list):
            self.collection.insert_many(insertion_data)

    def get_all_documents(self):
        return list(self.collection.find())

    def delete_document_by_filter(self, filter):
        # Delete multiple documents that match the filter
        self.collection.delete_many(filter)

    @classmethod
    def close_connection(cls):
        # close mongo client connection
        cls.client.close()


mongodb_client = ClassMongoDB()
