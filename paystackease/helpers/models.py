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
from typing import Optional, Union, TypedDict, Dict, List
from pydantic import BaseModel, Field, field_validator

from paystackease.helpers import ExpiryInfo, BankDetails, PWT, MobileMoneyPay, QRPayment, USSDPayment, CustomMetaField


class DomainNameModel(BaseModel):
    domain_name: str = Field(..., alias="domainName", description="Domain name or subdomain name", examples=["example.com"])

    @field_validator("domain_name")
    def validate_domain_name(cls, value):
        if not value or not isinstance(value, str):
            raise ValueError("Domain name can not be empty and it should be a string")
        return value


class ListDomainNamesModel(BaseModel):
    use_cursor: Optional[bool] = Field(default=False, description="use cursor for pagination")
    next_page: Optional[int] = Field(default=None, alias="next", description="next page")
    previous_page: Optional[int] = Field(default=None, alias="previous", description="previous page")

    @field_validator("use_cursor")
    def validate_use_cursor(cls, value):
        if isinstance(value, bool):
            return "True" if value else "False"
        return value


class AuthReferenceObject(BaseModel):
    amount: int = Field(..., description="Amount to charge should be in subunit", examples=[1000, 20000])
    authorization: Optional[str] = Field(default=None, description="Authorization code for the charge", examples=["AUTH_ncx8hews93", "AUTH_ncx8hfaw45"])
    reference: Optional[str] = Field(default=None, description="Unique reference for the charge", examples=["dam1266638dhhe", "dam1290638dhha"])

    @field_validator("amount")
    def validate_amount(cls, value):
        if value < 1:
            raise ValueError("Amount should be a positive integer greater than zero.")
        return value

    @field_validator("authorization")
    def validate_authorization(cls, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Authorization code should be a string or None.")
        return value

    @field_validator("reference")
    def validate_reference(cls, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Reference should be a string or None.")
        return value


class PageModel(BaseModel):
    per_page: Optional[int] = Field(default=50, alias="perPage", description="Number of items per page")
    page: Optional[int] = Field(default=1, description="Page number for pagination")


class DatePageModel(BaseModel):
    from_date: Optional[Union[str, date]] = Field(default=None, alias="from", description="Start date for filtering")
    to_date: Optional[Union[str, date]] = Field(default=None, alias="to", description="End date for filtering")

    @field_validator("from_date", "to_date")
    def validate_dates(cls, value):
        if not isinstance(value, date):
            raise ValueError("Date should be either a string or a date object")
        return value.strftime("%Y-%m-%d")

class VirtualPaymentModel(BaseModel):
    qr: Optional[QRPayment] = Field(default=None, description="", examples=[{'provider': ''}])
    ussd: Optional[USSDPayment] = Field(default=None, description="", examples=[{'provider': ''}])
    mobile_money: Optional[MobileMoneyPay] = Field(default=None, description="", examples=[{'provider': ''}])


class ChargeBankModel(BaseModel):
    bank: Optional[BankDetails] = Field(default=None, description="Bank details", examples=[{'code': 'FBN', 'account_number': '1231241234'}])
    bank_transfer: Optional[Union[ExpiryInfo, Dict[PWT, str]]] = Field(default=None, description="Pay With Transfer (PWT)", examples=[{'account_expires_at': '2023-09-12T13:10:00Z"'}])


class CustomMetaData(BaseModel):
    custom_fields: List[CustomMetaField] = Field(..., description="", examples=[])


class CustomerDetails(BaseModel):
    first_name: Optional[str] = Field(default=None, description="", examples=[])
    last_name: Optional[str] = Field(default=None, description="", examples=[])
    phone: Optional[str] = Field(default=None, description="", examples=[])
    middle_name: Optional[str] = Field(..., description="", examples=[])
