""" Paystack Error Message"""

from typing import Optional, Dict, Union, cast


class PayStackError(Exception):
    """
    Base exception class for Paystack API errors
    """

    def __init__(
            self,
            message: Optional[str] = None,
            headers: Optional[Union[Dict[str, str], None]] = None,
            http_body: Optional[Union[bytes, str, None]] = None,
            status_code: Optional[int] = None,
            error_code: Optional[str] = None,
    ) -> None:

        body: Optional[str] = None
        if http_body and hasattr(http_body, 'decode'):
            try:
                body = cast(bytes, http_body).decode('utf-8')
            except BaseException:
                body = "Unable to decode body as utf-8. Please try again"

        self.message = message
        self.status_code = status_code
        self.headers = headers or {}
        self.http_body = body
        self.error_code = error_code
        self.request_id = self.headers.get("X-Request-ID", None)

        super(PayStackError, self).__init__(self._format_message())

    def __str__(self) -> str:
        """
        Return the error message
        """
        return self._format_message()

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"message='{self.message}', "
                f"status_code={self.status_code}, "
                f"error_code='{self.error_code}', "
                f"headers={self.headers}, "
                f"http_body='{self.http_body}', "
                f"request_id='{self.request_id}')")

    def _format_message(self) -> str:
        """
        Format the error message
        """
        error_msg = f"\nError Message: {self.message}"
        if self.status_code is not None:
            error_msg += f"\nError Status Code: {self.status_code}"
        if self.error_code is not None:
            error_msg += f"\nError Code Message: {self.error_code}"
        if self.headers:
            error_msg += f"\nHeaders Error: {self.headers}"
        if self.request_id:
            return f"\nRequest ID Error: {self.request_id} {self.message}"
        if self.http_body:
            error_msg += f"\nHTTP Body Error: {self.http_body}"
        return error_msg


class APIConnectionError(PayStackError):
    """
    Connection Error
    """

    def __init__(
            self,
            message: str,
            status_code: int = 0,
            error_code: str = "connection_issue, due to slow or not internet connection. "
                              "Check your internet connectivity",
            should_retry: bool = False
    ) -> None:
        super(APIConnectionError, self).__init__(
            message=message, status_code=status_code, error_code=error_code
        )
        self.should_retry: bool = should_retry


class SecretKeyError(PayStackError):
    """
    Secret Key Error
    """
    def __init__(
            self,
            message: str,
            status_code: int = 401,
            error_code: str = "secret_key_error"
    ) -> None:
        super().__init__(
            message=message, status_code=status_code, error_code=error_code
        )


class TypeValueError(PayStackError):
    """
    Type Value Error
    """
    def __init__(
            self,
            message: str,
            status_code: int = 400,
            error_code: str = "type_value_error"
    ) -> None:
        super().__init__(
            message=message, status_code=status_code, error_code=error_code
        )


class InvalidRequestMethodError(PayStackError):
    """
    Request Time Error
    """
    def __init__(
            self,
            message: str,
            status_code: int = 405,
            error_code: str = "invalid_http_request_method"
    ) -> None:
        super().__init__(
            message=message, status_code=status_code, error_code=error_code
        )


class PayStackServerError(PayStackError):
    """
    Server Error
    """
    def __init__(
            self,
            message: str,
            status_code: int,
            error_code: str = "server_error. Contact Paystack Customer Care"
    ) -> None:
        # Check if status code is a server error
        if status_code and 500 <= status_code < 600:
            error_code = "server_error. Contact Paystack Customer Care"
        super().__init__(
            message=message, status_code=status_code, error_code=error_code
        )


class PayStackSignatureVerifyError(PayStackError):
    """
    Signature Verify Error
    """
    def __init__(
            self,
            message: str,
            signature_header,
            status_code: int = 400,
            error_code: str = "signature_verify_error",
            http_body=None
    ):
        super(PayStackSignatureVerifyError, self).__init__(
            message=message,
            status_code=status_code,
            error_code=error_code,
            http_body=http_body
        )
        self.signature_header = signature_header
