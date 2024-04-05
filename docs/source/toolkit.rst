=======================
Tool kit module
=======================

This hold Enum classes for PayStackEase with predefined values.

AccountType
---------------

.. py:class:: AccountType

    Bases: Enum

    Customer’s type of Account.

    .. py:attribute:: PERSONAL = 'personal'
    .. py:attribute:: BUSINESS = 'business'

Bearer
-----------------

.. py:class:: Bearer

    Bases: Enum

    Bearer supported by Paystack

    .. py:attribute:: ACCOUNT = 'account'
    .. py:attribute:: SUB_ACCOUNT = 'subaccount'

Channels
---------------

.. py:class:: Channels

    Bases: Enum

    Channels supported by Paystack.

    .. py:attribute:: BANK= 'bank'
    .. py:attribute:: BANK_TRANSFER= 'bank_transfer'
    .. py:attribute:: CARD= 'card'
    .. py:attribute:: ETF= 'etf'
    .. py:attribute:: MOBILE_MONEY= 'mobile_money'
    .. py:attribute:: QR= 'qr'
    .. py:attribute:: USSD= 'ussd'

Currency
------------

.. py:class:: Currency

    Bases: Enum

    Currencies supported by Paystack.

    .. py:attribute:: GHS= 'GHS'
    .. py:attribute:: KES= 'KES'
    .. py:attribute:: NGN= 'NGN'
    .. py:attribute:: USD= 'USD'
    .. py:attribute:: ZAR= 'ZAR'

DisputeStatus
-----------------

.. py:class:: DisputeStatus

    Bases: Enum

    Dispute status.

    .. py:attribute:: MERCHANT_FEEDBACK = "awaiting-merchant-feedback"
    .. py:attribute:: BANK_FEEDBACK = "awaiting-bank-feedback"
    .. py:attribute:: PENDING = "pending"
    .. py:attribute:: RESOLVED = "resolved"

DocumentType
---------------

.. py:class:: DocumentType

    Bases: Enum

    Customer’s mode of identity.

    .. py:attribute:: BUSINESS_REG_NUMBER= 'businessRegistrationNumber'
    .. py:attribute:: IDENTITY_NUMBER= 'identityNumber'
    .. py:attribute:: PASSPORT_NUMBER= 'passportNumber'

DVABank
----------

.. py:class:: DVABank

    Bases: Enum

    DVA_BANK supported by Paystack.

    .. py:attribute:: WEMA_BANK = "wema-bank"
    .. py:attribute:: TITAN = "titan-paystack"

EFT
-----

.. py:class:: EFT

    Bases: Enum

    EFT supported by Paystack.

    .. py:attribute:: OZOW = "ozow"

EventAction
---------------

.. py:class:: EventAction

    Bases: Enum

    Event action supported by Paystack.

    .. py:attribute:: PROCESS = "process"
    .. py:attribute:: VIEW = "view"
    .. py:attribute:: PRINT = "print"


EventType
---------------

.. py:class:: EventType

    Bases: Enum

    Event types supported by Paystack

    .. py:attribute:: INVOICE= 'invoice'
    .. py:attribute:: TRANSACTION= 'transaction'

GateWay
---------

.. py:class:: GateWay

    Bases: Enum

    Gateway supported by Paystack

    .. py:attribute:: E_MANDATE = "emandate"
    .. py:attribute:: DIGITAL_BANK_MANDATE = "digitalbankmandate"


Interval
---------------

.. py:class:: Interval

    Bases: Enum

    Interval supported by Paystack.

    .. py:attribute:: ANNUALLY= 'annually'
    .. py:attribute:: BIANNUALLY= 'biannually'
    .. py:attribute:: DAILY= 'daily'
    .. py:attribute:: MONTHLY= 'monthly'
    .. py:attribute:: QUARTERLY= 'quarterly'
    .. py:attribute:: WEEKLY= 'weekly'

MobileMoney
---------------

.. py:class:: MobileMoney

    Bases: Enum

    Mobile Money supported by Paystack. Only available to businesses in Ghana and Kenya.

    .. py:attribute:: AIRTEL_TIGO= 'atl'
    .. py:attribute:: MTN= 'mtn'
    .. py:attribute:: M_PESA= 'mpesa'
    .. py:attribute:: VODAFONE= 'vod'

PayMentRequestStatus
-----------------------

.. py:class:: PayMentRequestStatus

    Bases: Enum

    Payment request status supported by Paystack

    .. py:attribute:: DRAFT = "draft"
    .. py:attribute:: PENDING = "pending"

PWT
---------------

.. py:class:: PWT

    Bases: Enum

    PWT supported by Paystack.

    .. py:attribute:: ACCOUNT_EXPIRES_AT= 'account_expires_at'

QRCODE
---------------

.. py:class:: QRCODE

    Bases: Enum

    QR Codes supported by Paystack.

    .. py:attribute:: SCAN_TO_PAY= 'scan-to-pay'
    .. py:attribute:: VISA= 'visa'

RecipientType
---------------

.. py:class:: RecipientType

    Bases: Enum

    Recipient Types supported by Paystack.

    .. py:attribute:: BASE= 'base'
    .. py:attribute:: GHIPSS= 'ghipss'
    .. py:attribute:: MOBILE_MONEY= 'mobile_money'
    .. py:attribute:: NUBAN= 'nuban'

ResendOTP
---------------

.. py:class:: ResendOTP

    Bases: Enum

    Resend OTP types supported by Paystack.

    .. py:attribute:: RESEND_OTP= 'resend_otp'
    .. py:attribute:: TRANSFER= 'transfer'

Resolution
---------------

.. py:class:: Resolution

    Bases: Enum

    Resolution types supported by Paystack.

    .. py:attribute:: DECLINED= 'declined'
    .. py:attribute:: MERCHANT= 'merchant-accepted'

RiskAction
---------------

.. py:class:: RiskAction

    Bases: Enum

    Risk Action supported by Paystack.

    .. py:attribute:: ALLOW= 'allow'
    .. py:attribute:: DEFAULT= 'default'
    .. py:attribute:: DENY= 'deny'

SettlementSchedule
--------------------

.. py:class:: SettlementSchedule

    Bases: Enum

    Settlement Schedule supported by Paystack.

    .. py:attribute::AUTO = "auto"
    .. py:attribute::WEEKLY = "weekly"
    .. py:attribute::MANUAL = "manual"
    .. py:attribute::MONTHLY = "monthly"

Status
---------------

.. py:class:: Status

    Bases: Enum

    Status supported by Paystack.

    .. py:attribute:: FAILED= 'failed'
    .. py:attribute:: PENDING= 'pending'
    .. py:attribute:: SUCCESS= 'success'

SplitType
---------------

.. py:class:: SplitType

    Bases: Enum

    Split Types supported by Paystack.

    .. py:attribute:: FLAT= 'flat'
    .. py:attribute:: PERCENTAGE= 'percentage'

TransactionStatus
-------------------

.. py:class:: TransactionStatus

    Bases: Enum

    Transaction Status supported by Paystack.

    .. py:attribute::FAILED = "failed"
    .. py:attribute::SUCCESS = "success"
    .. py:attribute::ABANDONED = "abandoned"

USSD
--------------

.. py:class:: USSD

    Bases: Enum

    USSD supported by Paystack.

    .. py:attribute:: GUARANTY_BANK= '737'
    .. py:attribute:: STERLING_BANK= '822'
    .. py:attribute:: UNITED_BANK_OF_AFRICA= '919'
    .. py:attribute:: ZENITH_BANK= '966'
