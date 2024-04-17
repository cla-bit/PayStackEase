""" Utility functions for paystackease """

from typing import NamedTuple, Optional, Union, Dict, List, Any


class PayStackResponse(NamedTuple):
    """
    PaystackEase API Response from the server after HTTP requests have been made
    """

    status_code: int
    status: bool
    message: str
    data: Optional[Union[Dict[str, Any], List[Any]]]

    @property
    def url(self) -> Optional[Union[str, None]]:
        """
        URL of the request
        """
        if self.status_code == 200 and self.data and isinstance(self.data, dict):
            return self.data["authorization_url"]
        return None
