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
    def __init__(self, message: str, error_code: int = None) -> None:
        super(SecretKeyError, self).__init__(message, error_code)


class TypeValueError(PayStackError):
    """
    Type Value Error
    """
    def __init__(self, message: str, error_code: int = None) -> None:
        super(TypeValueError, self).__init__(message, error_code)


class InvalidRequestMethodError(PayStackError):
    """
    Request Time Error
    """
    def __init__(self, message: str, error_code: int = None) -> None:
        super(InvalidRequestMethodError, self).__init__(message, error_code)
