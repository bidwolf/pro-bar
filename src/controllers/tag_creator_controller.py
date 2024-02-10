"""
This module contains the TagCreatorController class,
which is responsible for handling the tag creation process.
"""

from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler


class TagCreatorController:
    """
    This class is used to handle the tag creation
    business logic.
    """

    def create(self, product_code: str) -> Dict:
        """
        This method creates a barcode from a product code
        and returns a formatted response in a dictionary.
        """
        path_of_barcode = self.__create_barcode(product_code)
        formatted_response = self.__format_response(path_of_barcode)
        return formatted_response

    def __create_barcode(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        path_of_barcode = barcode_handler.create_barcode(product_code)
        return path_of_barcode

    def __format_response(self, path_of_barcode: str) -> Dict:
        return {
            "data": {
                "type": "Barcode Image",
                "count": 1,
                "path": f"{path_of_barcode}.png",
            }
        }
