"""
This module contains the error handler to handle the exceptions.
"""

from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    """
    This method is used to handle the exceptions.
    """
    return HttpResponse(
        status_code=500,
        body={"errors": [{"title": "Internal Server Error", "detail": str(error)}]},
    )
