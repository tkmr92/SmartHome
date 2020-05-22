import pymongo


class DatabaseInteraction:
    def __init__(self, database='smarthome-db', host='localhost', port=27017):
        # init variables
        self.client = pymongo.MongoClient(host, port)
        self.database = self.client[database]
        self.collection = None
        self.user = None

    # SETTERS
    def setdatabase(self, dbname):
        self.database = self.client[dbname]

    def setcollection(self, collectionname):
        self.collection = self.database[collectionname]

    def setdocument(self, data):
        self.document = data

    def setuser(self, username):
        self.user = username

    # GETTERS #
    def getuser(self):
        return self.user

    def getdatabase(self):
        return self.database

    def getcollection(self):
        return self.collection

    # Database Manipulation #
    def insertdocument(self):
        self.collection.insert_one(self.document)

    def updatedocument(self, document, update):
        self.collection.find_one_and_update()
