"""
Module: models.py
===================
This module contains Pydantic models for various tasks related to the application.
Each model is designed to validate and serialize data associated with different aspects of the system,
such as user information, configuration settings, data inputs, and responses.

Models in this file use Pydantic's data validation capabilities to ensure proper format, types, and required fields
are maintained for different use cases.
"""


from datetime import date
from typing import Optional, Union, Dict, List
from pydantic import BaseModel, Field, field_validator, model_validator

from paystackease.helpers import (
    ExpiryInfo, BankDetails, PWT, CustomMetaField,
    QRCODE, USSD, MobileMoney
)


class DomainNameModel(BaseModel):
    """
    A Pydantic model representing a domain name.

    Attributes:
    domain_name (str): The domain name or subdomain name.

    Methods:
    validate_domain_name(cls, value): Validates the domain name.

    """
    domain_name: str = Field(..., alias="domainName", description="Domain name or subdomain name", examples=["example.com"])

    @field_validator("domain_name")
    def validate_domain_name(cls, value):
        """
        Validates the domain name.

        Parameters:
        value (str): The domain name to validate.

        Returns:
        str: The validated domain name.

        Raises:
        ValueError: If the domain name is empty or not a string.

        """
        if not value or not isinstance(value, str):
            raise ValueError("Domain name can not be empty and it should be a string")
        return value


class ListDomainNamesModel(BaseModel):
    """
    A Pydantic model representing pagination parameters for listing domain names.

    Attributes:
    use_cursor (Optional[bool]): Flag indicating whether to use cursor-based pagination. Default is False.
    next_page (Optional[int]): The page number for the next set of results. Default is None.
    previous_page (Optional[int]): The page number for the previous set of results. Default is None.

    Methods:
    validate_use_cursor(cls, value): Validates the use_cursor attribute. Converts boolean values to string representation.

    """
    use_cursor: Optional[bool] = Field(default=False, description="use cursor for pagination")
    next_page: Optional[int] = Field(default=None, alias="next", description="next page")
    previous_page: Optional[int] = Field(default=None, alias="previous", description="previous page")

    @field_validator("use_cursor")
    def validate_use_cursor(cls, value):
        """
        Validates the use_cursor attribute. Converts boolean values to string representation.

        Parameters:
        value (bool): The value to validate.

        Returns:
        str: The validated value as a string representation.

        """
        if isinstance(value, bool):
            return "True" if value else "False"
        return value


class AuthReferenceObject(BaseModel):
    """
    A Pydantic model representing the reference object for an authorization or charge.

    Attributes:
    amount (int): The amount to charge in subunit.
    authorization (Optional[str]): The authorization code for the charge.
    reference (Optional[str]): The unique reference for the charge.

    Methods:
    validate_amount(cls, value): Validates the amount attribute.
    validate_authorization(cls, value): Validates the authorization attribute.
    validate_reference(cls, value): Validates the reference attribute.

    """
    amount: int = Field(..., description="Amount to charge should be in subunit", examples=[1000, 20000])
    authorization: Optional[str] = Field(default=None, description="Authorization code for the charge", examples=["AUTH_ncx8hews93", "AUTH_ncx8hfaw45"])
    reference: Optional[str] = Field(default=None, description="Unique reference for the charge", examples=["dam1266638dhhe", "dam1290638dhha"])

    @field_validator("amount")
    def validate_amount(cls, value):
        """
        Validates the amount attribute.

        Parameters:
        value (int): The amount to validate.

        Returns:
        int: The validated amount.

        Raises:
        ValueError: If the amount is not a positive integer greater than zero.

        """
        if value < 1:
            raise ValueError("Amount should be a positive integer greater than zero.")
        return value

    @field_validator("authorization")
    def validate_authorization(cls, value):
        """
        Validates the authorization attribute.

        Parameters:
        value (Optional[str]): The authorization code to validate.

        Returns:
        Optional[str]: The validated authorization code.

        Raises:
        ValueError: If the authorization code is not a string or None.

        """
        if value is not None and not isinstance(value, str):
            raise ValueError("Authorization code should be a string or None.")
        return value

    @field_validator("reference")
    def validate_reference(cls, value):
        """
        Validates the reference attribute.

        Parameters:
        value (Optional[str]): The reference to validate.

        Returns:
        Optional[str]: The validated reference.

        Raises:
        ValueError: If the reference is not a string or None.

        """
        if value is not None and not isinstance(value, str):
            raise ValueError("Reference should be a string or None.")
        return value


class PageModel(BaseModel):
    """
    A Pydantic model representing pagination parameters.

    Attributes:
    per_page (Optional[int]): The number of items to display per page. Default is 50.
    page (Optional[int]): The page number for pagination. Default is 1.

    Methods:
    None

    """
    per_page: Optional[int] = Field(default=50, alias="perPage", description="Number of items per page")
    page: Optional[int] = Field(default=1, description="Page number for pagination")


class DatePageModel(BaseModel):
    """
    A Pydantic model representing date range parameters for pagination.

    Attributes:
    from_date (Optional[Union[str, date]]): The start date for filtering. Default is None.
    to_date (Optional[Union[str, date]]): The end date for filtering. Default is None.

    Methods:
    validate_dates(cls, value): Validates the date parameters. Raises ValueError if the date is not a string or a date object.

    """
    from_date: Optional[Union[str, date]] = Field(default=None, alias="from", description="Start date for filtering")
    to_date: Optional[Union[str, date]] = Field(default=None, alias="to", description="End date for filtering")

    @field_validator("from_date", "to_date")
    def validate_dates(cls, value):
        """
        Validates the date parameters.

        Parameters:
        value (Union[str, date]): The date to validate.

        Returns:
        str: The validated date in the format "YYYY-MM-DD".

        Raises:
        ValueError: If the date is not a string or a date object.

        """
        if not isinstance(value, date):
            raise ValueError("Date should be either a string or a date object")
        return value.strftime("%Y-%m-%d")


class QRPayment(BaseModel):
    provider: Union[QRCODE, str]

    @model_validator(mode="before")
    @classmethod
    def convert_enum_string(cls, values):
        if isinstance(values.get("provider"), QRCODE):
            values["provider"] = values["provider"].value
        return values


class USSDPayment(BaseModel):
    type: Union[USSD, str]

    @field_validator("type", mode="before")
    def validate_ussd(cls, value):
        if isinstance(value, USSD):
            return value.value  # convert Enum to string
        return value


class MobileMoneyPay(BaseModel):
    phone: str
    provider: Union[MobileMoney, str]

    @field_validator("provider", mode="before")
    def validate_mobile_money(cls, value):
        if isinstance(value, MobileMoney):
            return value.value  # convert Enum to string
        return value


class VirtualPaymentModel(BaseModel):
    """
    A Pydantic model representing different virtual payment methods.

    Attributes:
    qr (Optional[QRPayment]): QR payment details.
    ussd (Optional[USSDPayment]): USSD payment details.
    mobile_money (Optional[MobileMoneyPay]): Mobile money payment details.
    """

    qr: Optional[QRPayment] = Field(default=None, description="QR Payment Details", examples=[{'provider': QRCODE.SCAN_TO_PAY}, {'provider': QRCODE.VISA}, {'provider': "scan-to-pay"}])
    ussd: Optional[USSDPayment] = Field(default=None, description="", examples=[{'type': USSD.ZENITH_BANK}, {'type': USSD.STERLING_BANK}, {'type': "737"}])
    mobile_money: Optional[MobileMoneyPay] = Field(default=None, description="", examples=[{'phone': '08012345678', "provider": MobileMoney.MTN}, {'phone': '08012345678', "provider": MobileMoney.AIRTEL_TIGO}, {'phone': '08012345678', "provider": "mtn"}])


class ChargeBankModel(BaseModel):
    """
    A Pydantic model representing bank details and Pay With Transfer (PWT) information for a charge.

    Attributes:
    bank (Optional[BankDetails]): Bank details for the charge.
    bank_transfer (Optional[Union[ExpiryInfo, Dict[PWT, str]]]): Pay With Transfer (PWT) information for the charge.
    """

    bank: Optional[BankDetails] = Field(default=None, description="Bank details", examples=[{'code': '057', 'account_number': '1231241234'}])
    bank_transfer: Optional[Union[ExpiryInfo, Dict[PWT, str]]] = Field(default=None, description="Pay With Transfer (PWT)", examples=[{'account_expires_at': '2023-09-12T13:10:00Z"'}])


class CustomMetaData(BaseModel):
    custom_fields: List[CustomMetaField] = Field(default=None, description="Custom Metadata can be passed in here", examples=[])


class MetaDataModel(BaseModel):
    metadata: Dict[str, str] = Field(default=None, description="Metadata of key, value pairs can be passed in here", examples=[])


class CustomerDetails(BaseModel):
    first_name: str = Field(description="Customer first name", examples=["John"])
    last_name: str = Field(description="Customer last name", examples=["Doe Tester"])
    phone: str = Field(description="Customer phone number", examples=["+23490123454678", "090123454678"])
    middle_name: Optional[str] = Field(default=None, description="Customer middle name", examples=["Test"])
