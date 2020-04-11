class BadRequestException(Exception):
    def __init__(self, error="Bad Request"):
        self.error = error
        self.status_code = 400
