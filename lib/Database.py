import pymongo


class DatabaseInteraction:
    def __init__(self, host='localhost', port=27017):
        """
        Database interaction module designed to allow the main smarthome to interact with MongoDB.

        :param host: URL where the database server is running. Defaults to the local machine.
        :param port: Port that has been opened to allow access to the database server.
            Defaults to the default MongoDB port.
        """
        # init variables
        self.client = pymongo.MongoClient(host, port)
        self.database = None
        self.collection = None
        self.user = None

    # SETTERS
    def setdatabase(self, dbname):
        """
        Setter to allow you to choose which database you would like to interact with.
        This would be equivalent to a "use dbname" in the MongoDB client.

        :param dbname: string: name of database to interact with.
        :return: Nothing
        """
        self.database = self.client[dbname]

    def setcollection(self, collectionname):
        """
        Setter to allow you to choose which collection you are currently working with.

        :param collectionname: string - Name of the collection you would like to work with
        :return: Nothing
        """
        self.collection = self.database[collectionname]

    def setdocument(self, data):
        """

        :param data:
        :return:
        """
        self.document = data

    def setuser(self, username):
        """

        :param username:
        :return:
        """
        self.user = username

    # GETTERS #
    def getuser(self):
        """

        :return:
        """
        return self.user

    def getdatabase(self):
        """

        :return:
        """
        return self.database

    def getcollection(self):
        """

        :return:
        """
        return self.collection

    def getdocument(self, search):
        """

        :param search:
        :return:
        """
        data = self.collection.find_one(search)
        return data

    # Database Manipulation #
    def insertdocument(self):
        """

        :return:
        """
        self.collection.insert_one(self.document)

    def updatedocument(self, document, update):
        """

        :param document:
        :param update:
        :return:
        """
        self.collection.find_one_and_update()
