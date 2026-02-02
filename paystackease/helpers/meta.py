"""
Helpers for handling Paystack meta objects.

Use Case / Scenario:
- This helper allows you to safely get pagination and summary info from Paystack API responses.
- Ideal for building dashboards, reports, or any feature that lists transactions, customers, or invoices.

Example:

    from paystackease.helpers.meta import get_meta
    from paystackease import PayStackBase

    # Initialize Paystack client
    paystack = PayStackBase()

    # Fetch a list of transactions
    response = paystack.transactions.list()

    # Use the helper to extract meta safely
    meta = get_meta(response)

    # Display pagination and record info
    print("Current page:", meta.get("page"))
    print("Total pages:", meta.get("pageCount"))
    print("Total records:", meta.get("total"))

Why this is useful:
- Makes building paginated dashboards and reports easier
- Keeps code safe if the meta object is missing
- Provides a single helper for consistent usage across multiple endpoints
"""


from typing import Dict, Any


def get_meta(response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract the meta object from a Paystack API response.

    :param response: Full API response dictionary
    :return: Meta object if present, else empty dict
    """
    if not isinstance(response, dict):
        return {}

    meta = response.get("meta", {})
    if isinstance(meta, dict):
        return meta

    return {}
