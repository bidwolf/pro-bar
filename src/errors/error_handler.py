"""
This module contains the error handler to handle the exceptions.
"""

from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError


def handle_errors(error: Exception) -> HttpResponse:
    """
    This method is used to handle the exceptions.
    """
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{"title": error.name, "detail": str(error)}]},
        )
    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Internal Server Error", "detail": str(error)}]},
    )
