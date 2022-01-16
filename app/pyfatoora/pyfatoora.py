"""
A module to implement ZATCA e-invoice (fatoora)
it will convert seller information to TLV tags,
then to hexadecimal representation finally to base64 encoding.

from base64 encoding result we can render RQ-code

The minimum seller inforamion required are :

- Seller`s name.
- Seller`s tax number.
- Invoice date.
- Invoice total amount.
- Tax amount.

"""
from typing import Optional, Union
from uttlv import TLV
import base64
import qrcode
import datetime
from pydantic import validate_arguments


class PyFatoora:
    """
    This class will help transform given seller information
    to a QR-code image as part of ZATCA requirements for implementation of
    e-invoice (fatoora).
    """

    tags = TLV()

    def __init__(
        self,
        seller_name: Optional[str] = None,
        tax_number: Optional[int] = None,
        invoice_date: Optional[str] = None,
        total_amount: Optional[float] = 0.00,
        tax_amount: Optional[float] = 0.00,
    ):
        self._seller_name = seller_name
        self._tax_number = tax_number
        self._date = invoice_date
        self._total = total_amount
        self._tax_amount = tax_amount

    @property
    def seller_name(self) -> str:
        return self._seller_name

    @seller_name.setter
    @validate_arguments
    def seller_name(self, seller_name: str) -> None:
        self._seller_name = seller_name

    @property
    def tax_number(self) -> int:
        return self._tax_number

    @tax_number.setter
    @validate_arguments
    def tax_nmuber(self, tax_nmuber: int) -> None:
        self._tax_nmuber = tax_nmuber

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    @validate_arguments
    def date(self, date: Optional[Union[str, datetime.datetime]]) -> None:
        self._date = str(date)

    @property
    def total(self) -> float:
        return self._total

    @total.setter
    @validate_arguments
    def total(self, total: float) -> None:
        self._total = total

    @property
    def tax_amount(self) -> float:
        return self._tax_amount

    @tax_amount.setter
    @validate_arguments
    def tax_amount(self, tax_amount: float) -> None:
        self._tax_amount = tax_amount

    def get_info(self) -> dict:

        info: dict = {
            "seller_name": self._seller_name,
            "tax_number": self._tax_number,
            "invoice_date": self._date,
            "total_amount": self._total,
            "tax_amount": self._tax_amount,
        }
        return info

    def tlv_to_base64(self) -> dict:
        """
        convert object tags to byte array then apply base 64 encode on tlv list
        :return: dict: tlv list and base 64 encoded tlv list
        """
        self.tags[0x01] = self._seller_name
        self.tags[0x02] = str(self._tax_number)
        self.tags[0x03] = str(self._date)
        self.tags[0x04] = str(self._total)
        self.tags[0x05] = str(self._tax_amount)

        tlv_as_byte_array = self.tags.to_byte_array()

        tlv_as_base64 = base64.b64encode(tlv_as_byte_array)
        tlv_as_base64 = tlv_as_base64.decode("ascii")

        return tlv_as_base64

    def render_qrcode_image(self) -> qrcode:
        """
        render base64 tlv result to a QR-code image

        :return: None
        """
        base64_tlv = self.tlv_to_base64()
        qr_code_img = qrcode.make(base64_tlv)
        return qr_code_img

    @validate_arguments
    def base64_to_tlv(self, base64_string: str) -> dict:
        """
        decode tlv values to string and return a dict

        :param: base64_string: tlv tags as base64
        :return: dict
        """

        decoded_tlv_data = base64.b64decode(base64_string)

        tags = TLV()
        tags.parse_array(bytes(decoded_tlv_data))

        seller_info = {}
        for tag in tags:
<<<<<<< HEAD
            seller_info[str(tag)] = tags[tag].decode("utf-8")
=======
            seller_info[str(tag)] = str(tags[tag])
>>>>>>> 151fdf101de2b61ad5b954c494c827d64b6097b3
        return seller_info
    """
    need fix :
    @classmethod
    @validate_arguments
    def read_qrcode_image(self, image_url) -> dict:
        extract seller information from qr-code image.
        :param image_url:
            a qr-code image path or url
        :return:
            dictionary contains decoded seller information
        data = decode(Image.open(image_url))
        extracted_info = self.base64_to_tlv(data[0][0])
        return extracted_info"""
