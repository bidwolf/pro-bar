"""
this is the test for the tag_creator_validator
1. missing product_code should raise an unprocessable entity exception
2. product_code being empty, should raise an unprocessable entity exception
4. product_code not containing only numbers should raise an unprocessable entity exception
5. sending an empty request, should raise an unprocessable entity exception
6. sending a request with an unknown field, should raise an unprocessable entity exception
"""

from src.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)
from .tag_creator_validator import tag_creator_validator


class MockRequest:
    """Just mock request class"""

    def __init__(self, json):
        self.json = json


def test_tag_creator_validator_should_not_raises_error():
    """tag_creator_validator should not raise an exception when the request is valid"""
    mock_request_valid = MockRequest(json={"product_code": "123"})
    tag_creator_validator(mock_request_valid)


def test_tag_creator_validator_should_raises_error_when_request_is_missing_product_code():
    """tag_creator_validator should raise an exception when the request is missing product_code"""
    mock_request_missing_product_code = MockRequest(json={})
    try:
        tag_creator_validator(mock_request_missing_product_code)
        assert False
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)


def test_tag_creator_validator_should_raises_error_when_product_code_is_empty():
    """tag_creator_validator should raise an exception when the product_code is empty"""
    mock_request_empty_product_code = MockRequest(json={"product_code": ""})
    try:
        tag_creator_validator(mock_request_empty_product_code)
        assert False
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)


def test_tag_creator_validator_should_raises_error_when_product_code_is_not_only_numbers():
    """tag_creator_validator should raise an exception when the product_code is not only numbers"""
    mock_request_product_code_not_string = MockRequest(
        json={"product_code": "absdkjas123"}
    )
    try:
        tag_creator_validator(mock_request_product_code_not_string)
        assert False
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)


def test_tag_creator_validator_should_raises_error_with_unexpected_param():
    """
    tag_creator_validator should raise an exception when the the request has an unexpected param
    """
    mock_request_product_code_not_string = MockRequest(
        json={"product_code": "123132", "unexpected_param": "unexpected_param_value"}
    )
    try:
        tag_creator_validator(mock_request_product_code_not_string)
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)
