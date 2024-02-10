"""
This module contains the HttpRequest class, which is used to represent an HTTP request.
"""

from typing import Dict


class HttpRequest:
    """
    This class is used to represent an HTTP request.

    Attributes:
    - method: The HTTP method of the request.
    - path: The path of the request.
    - headers: The headers of the request.
    - body: The body of the request.
    """

    def __init__(
        self,
        method: Dict = None,
        path: Dict = None,
        headers: Dict = None,
        body: Dict = None,
    ) -> None:
        self.method = method
        self.path = path
        self.headers = headers
        self.body = body
