"""
Enums for Currency and Channels with predefined values.
"""

from enum import Enum


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


class PWT(Enum):
    """PWT supported by Paystack."""

    ACCOUNT_EXPIRES_AT = "account_expires_at"


class QRCODE(Enum):
    """QR Codes supported by Paystack."""

    SCAN_TO_PAY = "scan-to-pay"
    VISA = "visa"


class RecipientType(Enum):
    BASE = "base"
    GHIPSS = "ghipss"
    MOBILE_MONEY = "mobile_money"
    NUBAN = "nuban"


class ResendOTP(Enum):
    RESEND_OTP = "resend_otp"
    TRANSFER = "transfer"


class Resolution(Enum):
    MERCHANT = "merchant-accepted"
    DECLINED = "declined"


class RiskAction(Enum):
    """Risk Action supported by Paystack."""

    ALLOW = "allow"
    DEFAULT = "default"
    DENY = "deny"


class SettlementSchedule(Enum):
    """ Schedule"""
    AUTO = "auto"
    WEEKLY = "weekly"
    MANUAL = "manual"
    MONTHLY = "monthly"


class SplitType(Enum):
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
