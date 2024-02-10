"""

HTTP Response Types

This module contains the HttpResponse class, which is used to represent an HTTP response.
"""

from typing import Dict


class HttpResponse:

    def __init__(self, status_code: int, body: Dict) -> None:
        self.status_code = status_code
        self.body = body
