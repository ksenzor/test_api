class PostRequest:

    """ Модель для составления POST/PUT запроса для api posts"""
    def __init__(self, user_id=None, title=None, body=None):
        self.user_id = user_id
        self.title = title
        self.body = body
