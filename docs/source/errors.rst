============================
PayStackEase Errors Package
============================

Paystack Error Message

-------------------------------------------------------------

.. py:exception:: InvalidRequestMethodError(message: str, error_code: int = None)

    Bases: :py:class:`~paystackease.errors.PayStackError`

    Request Time Error

.. py:exception:: PayStackError(message: str, error_code: int = None)

    Bases: ``Exception``

    PayStack Error

.. py:exception:: SecretKeyError(message: str, error_code: int = None)

    Bases: :py:class:`~paystackease.errors.PayStackError`

    Secret Key Error

.. py:exception:: TypeValueError(message: str, error_code: int = None)

    Bases: :py:class:`~paystackease.errors.PayStackError`

    Type Value Error
