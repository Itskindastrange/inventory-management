from pymongo import MongoClient
from pymongo.server_api import ServerApi

# URL encode special characters in the password
uri = "mongodb+srv://abdahmd:prvb%24E-M-x3AFxy@stocka-mgm.4wles6c.mongodb.net/?retryWrites=true&w=majority&appName=stocka-mgm"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

if __name__ == "__main__":
# Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print("An error occurred:", e)

