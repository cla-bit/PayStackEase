""" Paystack Error Message"""


class PayStackError(Exception):
    """
    PayStack Error
    """

    def __init__(self, message: str, error_code: int = None) -> None:
        super().__init__(message)
        self.error_code = error_code


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
