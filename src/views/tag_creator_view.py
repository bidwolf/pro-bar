"""
This method is used to create a class that represents a tag creator view.
"""

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    """
    responsibility for interact with http request
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body.get("product_code")
        return HttpResponse(200, {"response": "tag created successfully"})
        # logic of business to create tag
