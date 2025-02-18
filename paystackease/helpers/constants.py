"""
Module: constants.py
=========================

This module defines various constants used throughout the paystackease.
These constants represent keys, patterns, or configuration values that are commonly referenced by other modules to maintain consistency and ease of maintenance.

Usage:
------
This module is intended to store constants that are referenced throughout paystack system.
Instead of hardcoding values directly in multiple places, they are defined here to promote consistency, maintainability, and easier updates.

"""
from warnings import deprecated
from typing import Union, TypedDict
from enum import Enum



IntString = Union[str, int]

PAYSTACK_API_URL: str = "https://api.paystack.co/"

apple_pay_endpoint: str = "/apple-pay/domain/"
bulk_charge_endpoint: str = "/bulkcharge/"
charges_endpoint: str = "/charge/"
customer_endpoint: str = "/customer/"


class AccountType(Enum):
    """Customer’s type of Account."""

    PERSONAL = "personal"
    BUSINESS = "business"


class Bearer(Enum):
    """Bearer supported by Paystack."""

    ACCOUNT = "account"
    SUB_ACCOUNT = "subaccount"


class Currency(Enum):
    """Currencies supported by Paystack."""

    GHS = "GHS"
    KES = "KES"
    NGN = "NGN"
    USD = "USD"
    ZAR = "ZAR"


class Channels(Enum):
    """Channels supported by Paystack."""

    BANK = "bank"
    BANK_TRANSFER = "bank_transfer"
    CARD = "card"
    ETF = "etf"
    MOBILE_MONEY = "mobile_money"
    QR = "qr"
    USSD = "ussd"


class DisputeStatus(Enum):
    """Dispute status."""

    MERCHANT_FEEDBACK = "awaiting-merchant-feedback"
    BANK_FEEDBACK = "awaiting-bank-feedback"
    PENDING = "pending"
    RESOLVED = "resolved"


class DocumentType(Enum):
    """Customer’s mode of identity."""

    IDENTITY_NUMBER = "identityNumber"
    PASSPORT_NUMBER = "passportNumber"
    BUSINESS_REG_NUMBER = "businessRegistrationNumber"


class DVABank(Enum):
    """DVA_BANK supported by Paystack."""

    WEMA_BANK = "wema-bank"
    TITAN = "titan-paystack"


class EFT(Enum):
    """EFT supported by Paystack."""

    OZOW = "ozow"


class EventAction(Enum):
    """Event action supported by Paystack."""

    PROCESS = "process"
    VIEW = "view"
    PRINT = "print"


class EventType(Enum):
    """ Event type supported by Paystack."""

    INVOICE = "invoice"
    TRANSACTION = "transaction"


class GateWay(Enum):
    """ Gateway supported bt Paystack"""

    E_MANDATE = "emandate"
    DIGITAL_BANK_MANDATE = "digitalbankmandate"


class Interval(Enum):
    """Interval supported by Paystack."""

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    BIANNUALLY = "biannually"
    ANNUALLY = "annually"


class MobileMoney(Enum):
    """Mobile Money supported by Paystack.
    Only available to businesses in Ghana and Kenya.
    """

    MTN = "mtn"
    AIRTEL_TIGO = "atl"
    VODAFONE = "vod"
    M_PESA = "mpesa"


class PayMentRequestStatus(Enum):
    """ Payment request status supported by Paystack"""

    DRAFT = "draft"
    PENDING = "pending"


@deprecated("Enum support of this is deprecated. Use 'ExpiryInfo' class as it supports TypedDict type.")
class PWT(Enum):
    """PWT supported by Paystack."""

    ACCOUNT_EXPIRES_AT = "account_expires_at"


class QRCODE(Enum):
    """QR Codes supported by Paystack."""

    SCAN_TO_PAY = "scan-to-pay"
    VISA = "visa"


class RecipientType(Enum):
    """Recipient type supported by Paystack."""

    BASE = "base"
    GHIPSS = "ghipss"
    MOBILE_MONEY = "mobile_money"
    NUBAN = "nuban"


class ResendOTP(Enum):
    """Resend OTP or Transfer supported by Paystack."""

    RESEND_OTP = "resend_otp"
    TRANSFER = "transfer"


class Resolution(Enum):
    """Resolution supported by Paystack."""

    MERCHANT = "merchant-accepted"
    DECLINED = "declined"


class RiskAction(Enum):
    """Risk Action supported by Paystack."""

    ALLOW = "allow"
    DEFAULT = "default"
    DENY = "deny"


class SettlementSchedule(Enum):
    """Settlement Schedule supported by Paystack."""

    AUTO = "auto"
    WEEKLY = "weekly"
    MANUAL = "manual"
    MONTHLY = "monthly"


class SplitType(Enum):
    """Split Type supported by Paystack."""

    PERCENTAGE = "percentage"
    FLAT = "flat"


class STATUS(Enum):
    """Status supported by Paystack."""

    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "pending"
    PROCESSING = "processing"


class TransactionStatus(Enum):
    """Transaction status supported by Paystack."""

    FAILED = "failed"
    SUCCESS = "success"
    ABANDONED = "abandoned"


class USSD(Enum):
    """USSD supported by Paystack."""

    GUARANTY_BANK = "737"
    UNITED_BANK_OF_AFRICA = "919"
    STERLING_BANK = "822"
    ZENITH_BANK = "966"


class ExpiryInfo(TypedDict, total=False):
    account_expires_at: str


class BankDetails(TypedDict):
    code: str
    account_number: str


class CustomMetaField(TypedDict):
    value: str
    display_name: str
    variable_name: str

