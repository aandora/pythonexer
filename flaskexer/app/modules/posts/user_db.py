class UserDB:
    def __init__(self, conn):
        self.conn = conn

    def getUser(self, username):
        return self.conn.find({'u': username})

    def doesUserExist(self, username):
    	cursor = self.conn.find({'u':username});
    	return cursor.count() > 0

    def createUser(self, username, password):
        self.conn.insert({'u':username, 'p':password})