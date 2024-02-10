"""
This module is responsible to validate the tag creator request.
"""

from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def tag_creator_validator(request: any) -> None:
    """
    This method is used to validate the tag creator request
    and raise an exception if the request is invalid.
    """
    tag_creator_schema = Validator(
        {
            "product_code": {
                "type": "string",
                "required": True,
                "regex": "^[0-9]*$",  # only numbers
                "empty": False,
            }
        }
    )
    response = tag_creator_schema.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(tag_creator_schema.errors)
