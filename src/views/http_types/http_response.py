"""

HTTP Response Types

This module contains the HttpResponse class, which is used to represent an HTTP response.
"""

from typing import Dict


class HttpResponse:
    """
    The HttpResponse class has two attributes: status_code and body:

    - The status_code attribute is an integer representing the HTTP status code
    accordingly to https://developer.mozilla.org/en-US/docs/Web/HTTP/Status.
    - The body attribute is a dictionary representing the response body.

    The HttpResponse class is used to represent an HTTP response.
    """

    def __init__(self, status_code: int, body: Dict) -> None:
        self.status_code = status_code
        self.body = body
