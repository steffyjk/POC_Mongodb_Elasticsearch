from pymongo import MongoClient

# Establish a connection to the MongoDB server
client = MongoClient('mongodb://localhost:27017')
# Get the list of database names
database_names = client.list_database_names()

# Print the database names
for database_name in database_names:
    print(database_name)

# Close the database connection
client.close()
