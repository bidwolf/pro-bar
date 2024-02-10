"""
This is a class that represents an HttpUnprocessableEntityError.
"""


class HttpUnprocessableEntityError(Exception):
    """
    This class is used to represent an HttpUnprocessableEntityError
    that have the following properties:
    message: str
    status: int
    name: str
    """

    def __init__(self, message: str):
        self.message = message
        self.status_code = 422
        self.name = "Unprocessable Entity"
        super().__init__(self.message)
