===========================================
Data Types
===========================================

The Data Types module defines structured data models used throughout
the PaystackEase library when sending requests to the Paystack API.

These models are implemented using **Pydantic**, which provides automatic
data validation and type checking before data is sent to the API.

Using these models ensures that required fields are provided and that
data types are correct.


Bulk Charge Data Models
-----------------------

These models are used when interacting with the Bulk Charges API.


.. py:class:: BulkChargeItem(authorization: str, amount: int, reference: str)

    Represents a single bulk charge request.

    :param authorization: Authorization code obtained from a successful card transaction.
    :type authorization: str

    :param amount: Amount to charge in the smallest currency unit (e.g. kobo for NGN).
    :type amount: int

    :param reference: A unique reference used to identify the transaction.
    :type reference: str


.. py:class:: BulkChargeListObject(charges: list[BulkChargeItem])

    Container object used when initiating multiple bulk charges.

    :param charges: A list of bulk charge items.
    :type charges: list[BulkChargeItem]
