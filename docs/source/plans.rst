===========================================
Plan Module
===========================================

.. :py:currentmodule:: paystackease.apis.plans


Wrapper for Paystack Plans API The Plans API allows you to create and manage installment payment options on your integration.

You can use the tool kit in the helpers module as reference: :ref:`helpers`

------------------------------------------------------------

.. py:class:: PlanClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Plan API Reference: `Plans`_

    .. py:method:: create_plan(name: str, amount: int, interval: str, currency: str, invoice_limit: int, send_invoices: bool, send_sms: bool, description: str | None = None)→ dict[source]

        Create a plan

        :param name: The name of the plan
        :type name: str
        :param amount: The amount of the plan
        :type amount: int
        :param interval: The interval of the plan. Values: ``Interval.value.value``
        :type interval: str
        :param currency: The currency of the plan
        :type currency: str
        :param invoice_limit: The invoice limit of the plan
        :type invoice_limit: int
        :param send_invoices: Whether or not to send invoices
        :type send_invoices: bool
        :param send_sms: Whether or not to send SMS
        :type send_sms: bool
        :param description: The description of the plan
        :type description: str, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: fetch_plan(id_or_code: str)→ dict

        Fetch a plan

        :param id_or_code: The id or code of the plan
        :type id_or_code: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: list_plans(per_page: int | None = None, page: int | None = None, status: str | None = None, interval: str | None = None, amount: int | None = None)→ dict

        List plans

        :param per_page: The number of plans per page
        :type per_page: int, optional
        :param page: The page number
        :type page: int, optional
        :param status:  Filter list by plans with specified status
        :type status: str, optional
        :param interval: Filter list by plans with specified interval
        :type interval: str, optional
        :param amount: The amount of the plans
        :type amount: int, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: update_plan(id_or_code: str, name: str, amount: int, interval: str, send_invoices: bool, send_sms: bool, currency: str, invoice_limit: int, description: str | None = None)→ dict

        Update a plan

        :param id_or_code: The id or code of the plan
        :type id_or_code: str
        :param name: The name of the plan
        :type name: str
        :param amount: The amount of the plan
        :type amount: int
        :param interval: The interval of the plan. Values: ``Interval.value.value``
        :type interval: str
        :param send_invoices: Whether or not to send invoices
        :type send_invoices: bool
        :param send_sms: Whether or not to send SMS
        :type send_sms: bool
        :param currency: The currency of the plan
        :type currency: str
        :param invoice_limit: The invoice limit of the plan
        :type invoice_limit: int
        :param description: The description of the plan
        :type description: str, optional

        :return: The response from the API
        :rtype: dict


.. _Plans: https://paystack.com/docs/api/plan/
