""" Utility functions for paystackease """

from typing import NamedTuple, Optional, Union, Dict, List, Any


class Response(NamedTuple):
    """
    Paystack API Response from the server after HTTP requests have been made
    """

    status_code: int
    status: str
    message: str
    data: Optional[Union[Dict[str, Any], List[Any]]]
