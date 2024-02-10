"""
This module contains the BarcodeHandler class, which is used to facades the barcode creation process.
"""

import os
from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:
    """
    This class is used to provide the barcode creation process.
    """

    def create_barcode(self, product_code: str) -> str:
        """
        This method is used to create a barcode from a product code.
        """
        barcode = Code128(product_code, writer=ImageWriter())
        if not os.path.exists("temp"):
            os.makedirs("temp")
        path_of_barcode = f"temp/{barcode}"
        barcode.save(path_of_barcode)
        return path_of_barcode
