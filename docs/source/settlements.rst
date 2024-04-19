===========================================
Settlements Module
===========================================

This wrapper class facilitates synchronous integration with Paystack Settlements API. The Settlements API allows you to gain insights into payouts made by Paystack to your bank account.

-------------

.. py:class:: SettlementClientAPI(secret_key: str = None)

    Paystack Settlement API Reference: `Settlements`_

    .. py:method:: list_settlement_transactions(settlement_id: int, per_page: int | None = 50, page: int | None = 1, from_date: date | None = None, to_date: date | None = None)→ PayStackResponse

        Get the transactions that make up a particular settlement

        :param settlement_id: ID of the settlement
        :type settlement_id: int
        :param per_page: The number of plans per page. (default: 50)
        :type per_page: int, optional
        :param page: The page number. (default: 1)
        :type page: int, optional
        :param from_date:
        :type from_date:
        :param to_date:
        :type to_date:

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: list_settlements(per_page: int | None = 50, page: int | None = 1, status: str | None = None, subaccount: str | None = None, from_date: date | None = None, to_date: date | None = None)→ PayStackResponse

        List all settlements made to your settlement accounts

        :param per_page: The number of plans per page. (default: 50)
        :type per_page: int, optional
        :param page: The page number. (default: 1)
        :type page: int, optional
        :param status: Values can be any of the following: success, processing, pending or failed.
        :param from_date:
        :type from_date:
        :param to_date:
        :type to_date:

        :return: The response from the API
        :rtype: PayStackResponse object


.. _Settlements: https://paystack.com/docs/api/settlement/
