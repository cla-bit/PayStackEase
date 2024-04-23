""" Paystack Error Message"""


class PayStackError(Exception):
    """
    Base exception class for Paystack API errors
    """

    def __init__(self, message: str, status_code: int = None) -> None:
        self.message = message
        self.status_code = status_code
        super(PayStackError, self).__init__(f"\nError Message: {self.message} \nError Status Code: {self.status_code}")


class SecretKeyError(PayStackError):
    """
    Secret Key Error
    """
    def __init__(self, message: str, status_code: int = 401) -> None:
        super().__init__(message, status_code)


class TypeValueError(PayStackError):
    """
    Type Value Error
    """
    def __init__(self, message: str, status_code: int = 400) -> None:
        super().__init__(message, status_code)


class InvalidRequestMethodError(PayStackError):
    """
    Request Time Error
    """
    def __init__(self, message: str, status_code: int = 400) -> None:
        super().__init__(message, status_code)
