"""
This is a test for the tag creator controller
"""

from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_controller import TagCreatorController


@patch.object(BarcodeHandler, "create_barcode")
def test_create_controller(mock_create_barcode):
    """
    1. The create method should return a dictionary with the barcode image path
    2. The dictionary should have the type, count and path keys
    3. The type key should have the value "Barcode Image"
    4. The count key should have the value 1
    5. The path key should have the value "temp/image_path.png" when the image_path is "image_path"
    """
    mock_value = "image_path"
    mock_create_barcode.return_value = f"temp/{mock_value}"
    tag_creator_controller = TagCreatorController()
    result = tag_creator_controller.create(mock_value)
    print(result)
    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result.get("data")
    assert "count" in result.get("data")
    assert "path" in result.get("data")
    assert result.get("data").get("type") == "Barcode Image"
    assert result.get("data").get("count") == 1
    assert result.get("data").get("path") == f"temp/{mock_value}.png"
