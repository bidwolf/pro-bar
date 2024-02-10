"""
This method is used to create a class that represents a tag creator view.
"""

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController


class TagCreatorView:
    """
    responsibility for interact with http request
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        """
        This method is used to validate and create a barcode from a httpRequest.
        """
        tag_creator_controller = TagCreatorController()
        body = http_request.body
        product_code: str = body.get("product_code")
        response = tag_creator_controller.create(product_code)
        return HttpResponse(200, body=response)
