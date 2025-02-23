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

# Paystack api endpoint
PAYSTACK_API_URL: str = "https://api.paystack.co/"
apple_pay_endpoint: str = "/apple-pay/domain/"
balance_endpoint: str = "/balance/"
bulk_charge_endpoint: str = "/bulkcharge/"
charges_endpoint: str = "/charge/"
customer_endpoint: str = "/customer/"
dvd_endpoint: str = "/dedicated_account/"
dispute_endpoint: str = "/dispute/"
integration_endpoint: str = "/integration/payment_session_timeout/"
misc_bank_endpoint: str = "/bank/"
misc_card_endpoint: str = "/decision/bin/"
misc_country_endpoint: str = "/country/"
misc_state_endpoint: str = "/address_verification/states/"
payment_page_endpoint: str = "/page/"
payment_request_endpoint: str = "/paymentrequest/"
plans_endpoint: str = "/plan/"
product_endpoint: str = "/product/"
refund_endpoint: str = "/refund/"
settlement_endpoint: str = "/settlement/"
subaccount_endpoint: str = "/subaccount/"
subscription_endpoint: str = "/subscription/"
terminal_endpoint: str = "/terminal/"
transaction_split_endpoint: str = "/split/"
transaction_endpoint: str = "/transaction/"
transfer_recipients_endpoint: str = "/transferrecipient/"
transfer_endpoint: str = "/transfer/"



class AccountType(Enum):
    """
    Enumeration for the types of customer accounts.

    Attributes:
        PERSONAL (str): Represents a personal account.
        BUSINESS (str): Represents a business account.
    """

    PERSONAL = "personal"
    BUSINESS = "business"


class Bearer(Enum):
    """
    Enumeration for Bearer types supported by Paystack.

    Attributes:
        ACCOUNT (str): Represents an account bearer.
        SUB_ACCOUNT (str): Represents a sub-account bearer.
    """

    ACCOUNT = "account"
    SUB_ACCOUNT = "subaccount"


class Currency(Enum):
    """
    Enumeration for currencies supported by Paystack.

    Attributes:
        GHS (str): Ghanaian Cedi.
        KES (str): Kenyan Shilling.
        NGN (str): Nigerian Naira.
        USD (str): United States Dollar.
        ZAR (str): South African Rand.
    """

    GHS = "GHS"
    KES = "KES"
    NGN = "NGN"
    USD = "USD"
    ZAR = "ZAR"


class Channels(Enum):
    """
    Enumeration for channels supported by Paystack.

    Attributes:
        BANK (str): Bank channel.
        BANK_TRANSFER (str): Bank transfer channel.
        CARD (str): Card channel.
        ETF (str): Electronic Funds Transfer channel.
        MOBILE_MONEY (str): Mobile money channel.
        QR (str): QR code channel.
        USSD (str): USSD channel.
    """

    BANK = "bank"
    BANK_TRANSFER = "bank_transfer"
    CARD = "card"
    ETF = "etf"
    MOBILE_MONEY = "mobile_money"
    QR = "qr"
    USSD = "ussd"


class DisputeStatus(Enum):
    """
    Enumeration for dispute statuses.

    Attributes:
        MERCHANT_FEEDBACK (str): Awaiting merchant feedback.
        BANK_FEEDBACK (str): Awaiting bank feedback.
        PENDING (str): Dispute is pending.
        RESOLVED (str): Dispute is resolved.
    """

    MERCHANT_FEEDBACK = "awaiting-merchant-feedback"
    BANK_FEEDBACK = "awaiting-bank-feedback"
    PENDING = "pending"
    RESOLVED = "resolved"


class DocumentType(Enum):
    """
    Enumeration for customer’s modes of identity.

    Attributes:
        IDENTITY_NUMBER (str): Identity number.
        PASSPORT_NUMBER (str): Passport number.
        BUSINESS_REG_NUMBER (str): Business registration number.
    """

    IDENTITY_NUMBER = "identityNumber"
    PASSPORT_NUMBER = "passportNumber"
    BUSINESS_REG_NUMBER = "businessRegistrationNumber"


class DVABank(Enum):
    """
    Enumeration for DVA_BANKs supported by Paystack.

    Attributes:
        WEMA_BANK (str): Wema Bank.
        TITAN (str): Titan Paystack.
    """

    WEMA_BANK = "wema-bank"
    TITAN = "titan-paystack"


class EFT(Enum):
    """
    Enumeration for EFTs supported by Paystack.

    Attributes:
        OZOW (str): Ozow.
    """

    OZOW = "ozow"


class EventAction(Enum):
    """
    Enumeration for event actions supported by Paystack.

    Attributes:
        PROCESS (str): Process action.
        VIEW (str): View action.
        PRINT (str): Print action.
    """

    PROCESS = "process"
    VIEW = "view"
    PRINT = "print"


class EventType(Enum):
    """
    Enumeration for event types supported by Paystack.

    Attributes:
        INVOICE (str): Invoice event.
        TRANSACTION (str): Transaction event.
    """

    INVOICE = "invoice"
    TRANSACTION = "transaction"


class GateWay(Enum):
    """
    Enumeration for gateways supported by Paystack.

    Attributes:
        E_MANDATE (str): E-mandate gateway.
        DIGITAL_BANK_MANDATE (str): Digital bank mandate gateway.
    """

    E_MANDATE = "emandate"
    DIGITAL_BANK_MANDATE = "digitalbankmandate"


class Interval(Enum):
    """
    Enumeration for intervals supported by Paystack.

    Attributes:
        DAILY (str): Daily interval.
        WEEKLY (str): Weekly interval.
        MONTHLY (str): Monthly interval.
        QUARTERLY (str): Quarterly interval.
        BIANNUALLY (str): Biannually interval.
        ANNUALLY (str): Annually interval.
    """

    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    BIANNUALLY = "biannually"
    ANNUALLY = "annually"


class MobileMoney(Enum):
    """
    Enumeration for Mobile Money supported by Paystack.
    Only available to businesses in Ghana and Kenya.

    Attributes:
        MTN (str): MTN Mobile Money.
        AIRTEL_TIGO (str): Airtel Tigo Mobile Money.
        VODAFONE (str): Vodafone Mobile Money.
        M_PESA (str): M-Pesa Mobile Money.
    """

    MTN = "mtn"
    AIRTEL_TIGO = "atl"
    VODAFONE = "vod"
    M_PESA = "mpesa"


class PayMentRequestStatus(Enum):
    """
    Enumeration for payment request statuses supported by Paystack.

    Attributes:
        DRAFT (str): Draft status.
        PENDING (str): Pending status.
    """

    DRAFT = "draft"
    PENDING = "pending"


@deprecated("Enum support of this is deprecated. Use 'ExpiryInfo' class as it supports TypedDict type.")
class PWT(Enum):
    """
    Enumeration for PWT supported by Paystack.

    Attributes:
        ACCOUNT_EXPIRES_AT (str): Account expiration time.
    """

    ACCOUNT_EXPIRES_AT = "account_expires_at"


class QRCODE(Enum):
    """
    Enumeration for QR codes supported by Paystack.

    Attributes:
        SCAN_TO_PAY (str): Scan to pay QR code.
        VISA (str): Visa QR code.
    """

    SCAN_TO_PAY = "scan-to-pay"
    VISA = "visa"


class RecipientType(Enum):
    """
    Enumeration for recipient types supported by Paystack.

    Attributes:
        BASE (str): Base recipient.
        GHIPSS (str): GHIPSS recipient.
        MOBILE_MONEY (str): Mobile money recipient.
        NUBAN (str): NUBAN recipient.
    """

    BASE = "base"
    GHIPSS = "ghipss"
    MOBILE_MONEY = "mobile_money"
    NUBAN = "nuban"


class ResendOTP(Enum):
    """
    Enumeration for resend OTP or transfer actions supported by Paystack.

    Attributes:
        RESEND_OTP (str): Resend OTP action.
        TRANSFER (str): Transfer action.
    """

    RESEND_OTP = "resend_otp"
    TRANSFER = "transfer"


class Resolution(Enum):
    """
    Enumeration for resolutions supported by Paystack.

    Attributes:
        MERCHANT (str): Merchant accepted resolution.
        DECLINED (str): Declined resolution.
    """

    MERCHANT = "merchant-accepted"
    DECLINED = "declined"


class RiskAction(Enum):
    """
    Enumeration for risk actions supported by Paystack.

    Attributes:
        ALLOW (str): Allow action.
        DEFAULT (str): Default action.
        DENY (str): Deny action.
    """

    ALLOW = "allow"
    DEFAULT = "default"
    DENY = "deny"


class SettlementSchedule(Enum):
    """
    Enumeration for settlement schedules supported by Paystack.

    Attributes:
        AUTO (str): Automatic settlement.
        WEEKLY (str): Weekly settlement.
        MANUAL (str): Manual settlement.
        MONTHLY (str): Monthly settlement.
    """

    AUTO = "auto"
    WEEKLY = "weekly"
    MANUAL = "manual"
    MONTHLY = "monthly"


class SplitType(Enum):
    """
    Enumeration for split types supported by Paystack.

    Attributes:
        PERCENTAGE (str): Percentage split.
        FLAT (str): Flat split.
    """

    PERCENTAGE = "percentage"
    FLAT = "flat"


class STATUS(Enum):
    """
    Enumeration for statuses supported by Paystack.

    Attributes:
        SUCCESS (str): Indicates a successful status.
        FAILED (str): Indicates a failed status.
        PENDING (str): Indicates a pending status.
        PROCESSING (str): Indicates a processing status.
    """

    SUCCESS = "success"
    FAILED = "failed"
    PENDING = "pending"
    PROCESSING = "processing"


class TransactionStatus(Enum):
    """
    Enumeration for transaction statuses supported by Paystack.

    Attributes:
        FAILED (str): Indicates a failed transaction.
        SUCCESS (str): Indicates a successful transaction.
        ABANDONED (str): Indicates an abandoned transaction.
    """

    FAILED = "failed"
    SUCCESS = "success"
    ABANDONED = "abandoned"


class USSD(Enum):
    """
    Enumeration for USSD codes supported by Paystack.

    Attributes:
        GUARANTY_BANK (str): USSD code for Guaranty Trust Bank.
        UNITED_BANK_OF_AFRICA (str): USSD code for United Bank of Africa.
        STERLING_BANK (str): USSD code for Sterling Bank.
        ZENITH_BANK (str): USSD code for Zenith Bank.
    """

    GUARANTY_BANK = "737"
    UNITED_BANK_OF_AFRICA = "919"
    STERLING_BANK = "822"
    ZENITH_BANK = "966"


class ExpiryInfo(TypedDict, total=False):
    """
    Typed dictionary for expiry information.

    Attributes:
        account_expires_at (str): The expiration time of the account.
    """

    account_expires_at: str


class BankDetails(TypedDict):
    """
    Typed dictionary for bank details.

    Attributes:
        code (str): The bank code.
        account_number (str): The account number.
    """

    code: str
    account_number: str


class CustomMetaField(TypedDict):
    """
    Typed dictionary for custom meta fields.

    Attributes:
        value (str): The value of the meta field.
        display_name (str): The display name of the meta field.
        variable_name (str): The variable name of the meta field.
    """

    value: str
    display_name: str
    variable_name: str


class TransferBatch(TypedDict, total=False):
    """
    Typed dictionary for transfer batch details.

    Attributes:
        type (str): The type of transfer.
        name (str): The name associated with the transfer.
        account_number (str): The account number for the transfer.
        bank_code (str): The bank code for the transfer.
        currency (str): The currency for the transfer.
    """

    # TODO: Add and test these: description, authorization_code & metadata[CustomMetaField type]
    type: str
    name: str
    account_number: str
    bank_code: str
    currency: str
    description: str
    authorization_code: str
    metadata: CustomMetaField
