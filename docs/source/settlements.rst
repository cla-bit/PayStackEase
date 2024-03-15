===========================================
Settlements Module
===========================================

.. :py:currentmodule:: paystackease.apis.settlements


Wrapper for Paystack Settlements API. The Settlements API allows you to gain insights into payouts made by Paystack to your bank account.

-----------------------------------------------------------------


.. py:class:: SettlementClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Settlement API Reference: `Settlements`_

    .. py:method:: list_settlement_transactions(settlement_id: int, per_page: int | None = None, page: int | None = None, from_date: date | None = None, to_date: date | None = None)→ dict[source]

        Get the transactions that make up a particular settlement

        :param settlement_id: ID of the settlement
        :type settlement_id: int
        :param per_page: The number of plans per page
        :type per_page: int, optional
        :param page: The page number
        :type page: int, optional
        :param from_date:
        :type from_date:
        :param to_date:
        :type to_date:

        :return: The response from the API
        :rtype: dict

    .. py:method:: list_settlements(per_page: int | None = None, page: int | None = None, status: str | None = None, subaccount: str | None = None, from_date: date | None = None, to_date: date | None = None)→ dict

        List all settlements made to your settlement accounts

        :param per_page: The number of plans per page
        :type per_page: int, optional
        :param page: The page number
        :type page: int, optional
        :param status: Values can be any of the following: success, processing, pending or failed.
        :param from_date:
        :type from_date:
        :param to_date:
        :type to_date:

        :return: The response from the API
        :rtype: dict


.. _Settlements: https://paystack.com/docs/api/settlement/
