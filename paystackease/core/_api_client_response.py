"""  This represents the response from the Paystack API server after making HTTP requests. """

from typing import NamedTuple, Optional, Union, Dict, Any


class PayStackResponse(NamedTuple):
    """
    PaystackEase API Response from the server after HTTP requests have been made
    """

    status_code: int
    status: bool
    message: str
    data: Optional[Union[Dict[str, Any], None]]

    @property
    def checkout_url(self) -> Optional[Union[str, None]]:
        """
        URL of the request
        """
        if self.status_code == 200 and self.data and isinstance(self.data, dict):
            return self.data["authorization_url"]
        return None

    @property
    def charge_url(self) -> Optional[Union[str, None]]:
        """
        URL of the request
        """
        if self.status_code == 200 and self.data and isinstance(self.data, dict):
            return self.data["url"]
        return None
