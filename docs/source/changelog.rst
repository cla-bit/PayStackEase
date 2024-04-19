-----------
Changelog
-----------

All notable changes to **paystackease** will be documented in this file.

[Version 0.1.0] - 2024-03-05
-------------------------------

**Added:**
================

The apis and async_apis packages were created with the following modules:

1. **Asynchronous and Synchronous class modules**: apple_pay, bulk_charges, charges, customers,
dedicated_virtual_accounts, disputes, integration, miscellaneous, payment_pages,
payment_requests, plans, products, refund, settlements, subaccounts, subscriptions,
terminal,transaction_splits, transactions, transfer_recipients, transfers,
transfers_control, and verification.

The asynchronous and synchronous general modules were created with the following modules:

1. **Asynchronous and Synchronous class modules**: apaystack and paystack.

The errors modules was created with the following modules:

1. **Error class modules**: errors.

**Changed:**
================

The HTTP requests handles Sessions object maintains a pool of persistent connections,
improving performance for subsequent requests to the same server
(Paystack API in this case) by reusing existing connections.
This reduces connection overhead and improves efficiency. The same applies to aiohttp ClientSession object.

**Security:**
================

Improved security to handle sensitive data structures.
This allows for better security when dealing with HTTP requests and responses from different sources.

-----------


[Version 0.1.3] - 2024-03-26
------------------------------

**Added:**
================

1. **Convert to strings method** was added in the asynchronous and synchronous base client classes.
This enables for easy conversion of date, bool, datetime to strings. To be easily handled by Paystack server.
2. **More Enum classes** was added.
3. **datetime** type hint.

**Changed:**
================

The apis and async_apis packages were improved with type hints in the following modules:

1. **Asynchronous and Synchronous class modules**: apple_pay, bulk_charges, charges, customers,
dedicated_virtual_accounts, disputes, integration, miscellaneous, payment_pages,
payment_requests, plans, products, refund, settlements, subaccounts, subscriptions,
terminal,transaction_splits, transactions, transfer_recipients, transfers,
transfers_control, and verification.

**Fixed:**
================

1. **Type Hint** bugs in the BaseClientAPI, AsyncBaseClientAPI classes and in the apis and async_apis packages.
2. **delete request method** bug in the PayStackBaseClientAPI and AsyncPayStackBaseClientAPI classes.

**Security:**
================

Improved security to handle sensitive data structures.
This allows for better security when dealing with HTTP requests and responses from different sources.

---------


[Version 1.0.0] - 2024-04-05
-------------------------------


**Added:**
================

1. **Default values** was added in the asynchronous and synchronous modules:
apple_pay, bulk_charges, charges, customers, dedicated_virtual_accounts, disputes,
integration, miscellaneous, payment_pages, payment_requests, plans, products, refund,
settlements, subaccounts, subscriptions, terminal,transaction_splits, transactions,
transfer_recipients, transfers, transfers_control, and verification.

2. **More Enum classes** was added.

**Changed:**
================

1. **Updated the return type from dict to PayStackResponse object** respectively in the asynchronous and synchronous packages and modules:
apple_pay, bulk_charges, charges, customers, dedicated_virtual_accounts,
disputes, integration, miscellaneous, payment_pages,
payment_requests, plans, products, refund, settlements, subaccounts, subscriptions,
terminal,transaction_splits, transactions, transfer_recipients, transfers,
transfers_control, and verification.

2. **Updated the return type from dict to PayStackResponse object** respectively in the asynchronous and synchronous base client modules.

3. **Updated the data parameter** respectively in the asynchronous and synchronous base client modules
HTTP requests methods to accept dict or list instead of dict.

**Fixed:**
================

1. **Type Hint** bugs in the BaseClientAPI, AsyncBaseClientAPI classes and in the apis and async_apis packages.

**Deprecated:**
==================
1. The objects parameter in the **BulkChargeClientAPI** module now is a required parameter. Deprecated
``Optional[List[Dict[]]] = None``.

**Security:**
================

Improved security to handle sensitive data structures.
This allows for better security when dealing with HTTP requests and responses from different sources.


[Version 2.0.0] - 2024-04-19
-------------------------------

**Changed:**
================

1. **Enhanced Response handling**: The return type for both asynchronous and synchronous calls has been changed from a
generic Response object to a more specific PayStackResponse object. This PayStackResponse object provides richer
information about the API response, including status code, response message, and data.

2. **Flexible data parameter** The data parameter in the base client modules for asynchronous and synchronous calls can now accept either a dictionary or a list.
This allows you to send data in a format that best suits your needs, providing more flexibility for your API requests.

**Fixed:**
================

1. **Type Hint** bugs in the BaseClientAPI, AsyncBaseClientAPI classes and in the apis and async_apis packages.
2. **Enhanced Error Handling**: This version boasts improved error handling by providing informative messages along with status codes for both request and response errors.

**Deprecated:**
==================
1. The objects parameter in the **BulkChargeClientAPI** module now is a required parameter. Deprecated
``Optional[List[Dict[]]] = None``.

2. The ``paystackease.abase``, ``paystackease.base``, ``paystackease.utils``and ``paystackease.errors`` have been deprecated.
Any code that relies on these packages will no longer function.

3. The ``paystackease.apis``and ``paystackease.async_apis``  api packages have been deprecated.
Any code that relies on these packages will no longer function.

**Security:**
================

Improved security to handle sensitive data structures.
This allows for better security when dealing with HTTP requests and responses from different sources.



.. _TestPYPI: https://test.pypi.org/project/paystackease/#files
