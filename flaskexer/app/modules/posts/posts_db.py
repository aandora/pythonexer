class PostDB:
    def __init__(self, conn):
        self.conn = conn

    def getPosts(self, user):
        return self.conn.find({'user': user})

    def createPost(self, user, post):
        self.conn.insert({'user':user, 'post':post})