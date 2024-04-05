""" Paystack Error Message"""


class PayStackError(Exception):
    """
    Base exception class for Paystack API errors
    """

    def __init__(self, message: str, status_code: int = None) -> None:
        super().__init__(message)
        self.status_code = status_code


class SecretKeyError(PayStackError):
    """
    Secret Key Error
    """


class TypeValueError(PayStackError):
    """
    Type Value Error
    """


class InvalidRequestMethodError(PayStackError):
    """
    Request Time Error
    """
