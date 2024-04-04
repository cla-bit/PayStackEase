""" Paystack Error Message"""

# import requests
# import aiohttp


class PayStackError(Exception):
    """
    Base exception class for Paystack API errors
    """

    def __init__(self, message: str, status_code: int = None) -> None:
        super().__init__(message)
        self.status_code = status_code


# class PayStackRequestError(PayStackError):
#     """
#     Exception raised for errors during requests to Paystack API
#     """
#
#     def __init__(self, message: str, status_code: int = None) -> None:
#         super().__init__(message, status_code)
#
#     @classmethod
#     def from_sync_request_error(cls, error: requests.RequestException):
#         """
#         Creates a PayStackRequestError from a synchronous requests exception.
#         :param error:
#         :return:
#         """
#         status_code = getattr(error.response, "status_code", None)
#         return cls(f"{str(error)}", status_code=status_code)
#
#     @classmethod
#     def from_async_request_error(cls, error: aiohttp.ClientError):
#         """
#         Creates a PayStackRequestError from an asynchronous requests exception.
#         :param error:
#         :return:
#         """
#         status_code = getattr(error.args[0], "status_code", None)
#         return cls(f"{str(error)}", status_code=status_code)


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
