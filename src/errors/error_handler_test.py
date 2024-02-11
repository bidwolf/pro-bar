"""
This is a test module for the error handler.
"""

from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .error_handler import handle_errors


def test_handle_regular_errors():
    """
    handle_errors should:
    1. return a HttpResponse instance
    2. return a HttpResponse instance with status 500 when a regular error is raised
    3. return a HttpResponse instance with a body dict when a error is raised
    4. return a HttpResponse with a body with errors array
    5. return in errors array a title with 'Internal Server Error' when a regular error is raised
    6. return in errors array a detail equals raised message error  when a error is raised
    """
    mock_error_message = "some_error"
    try:
        raise Exception(mock_error_message)
    except Exception as exception:
        result = handle_errors(exception)
        assert isinstance(result, HttpResponse)
        assert result.status_code == 500
        assert isinstance(result.body, dict)
        assert "errors" in result.body
        assert isinstance(result.body.get("errors"), list)
        assert len(result.body.get("errors")) == 1
        assert "title" in result.body.get("errors")[0]
        assert "detail" in result.body.get("errors")[0]
        assert result.body.get("errors")[0].get("title") == "Internal Server Error"
        assert result.body.get("errors")[0].get("detail") == mock_error_message


def test_handle_unprocessable_entity_errors():
    """
    when a HttpUnprocessableEntity error occurs, handle_errors should:
    1. return a HttpResponse instance
    2. return a HttpResponse with status 422
    3. return a HttpResponse with a body dict
    4. return a HttpResponse with a body with errors array
    5. return in errors array a title with 'Unprocessable Entity'
    6. return in errors array a detail equals raised message error  when a error is raised
    """
    mock_error_message = "unprocessable_error"
    try:
        raise HttpUnprocessableEntityError(mock_error_message)
    except Exception as exception:
        result = handle_errors(exception)
        assert isinstance(result, HttpResponse)
        assert result.status_code == 422
        assert isinstance(result.body, dict)
        assert "errors" in result.body
        assert isinstance(result.body.get("errors"), list)
        assert len(result.body.get("errors")) == 1
        assert "title" in result.body.get("errors")[0]
        assert "detail" in result.body.get("errors")[0]
        assert result.body.get("errors")[0].get("title") == "Unprocessable Entity"
        assert result.body.get("errors")[0].get("detail") == mock_error_message
