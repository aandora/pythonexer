class UserDB:
    def __init__(self, conn):
        self.conn = conn

    def getUser(self, username):
        return self.conn.find({'username':username})

    def getUserWithPassword(self, username, password):
        return self.conn.find({'username':username, 'password': password})

    def createUser(self, username, password, email):
        self.conn.insert({'username':username, 'password': password, 'email': email})

    def createUserUsingUser(self, user):
        self.conn.insert({'username':user.username, 'password': user.password, 'email': user.email})