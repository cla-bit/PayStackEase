===========================================
Subscriptions Module
===========================================

.. :py:currentmodule:: paystackease.apis.subscriptions


Wrapper for Paystack Subscriptions API. The Subscriptions API allows you to create and manage recurring payment on your integration.

----------

.. py:class:: SubscriptionClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Subscription API Reference: `Subscriptions`_

    .. py:method:: create_subscription(customer: str, plan_code: str, authorization: str, start_date: date | None = None)→ Response

        Create a subscription

        :param customer: the customer id or email
        :type customer: str
        :param plan_code: the plan code
        :type plan_code: str
        :param authorization: the authorization code
        :type authorization: str
        :param start_date: the start date
        :type start_date: date, optional

        :return: The response from the API
        :rtype: Response object

    .. py:method:: disable_subscription(subscription_code: str, token: str)→ Response

        Disable a subscription

        :param subscription_code: the subscription code
        :type subscription_code: str
        :param token: the token sent to the customer email
        :type token: str

        :return: The response from the API
        :rtype: Response object

    .. py:method:: enable_subscription(subscription_code: str, token: str)→ Response

        Enable a subscription

        :param subscription_code: The subscription code
        :type subscription_code: str
        :param token: The token sent to the customer email
        :type token: str

        :return: The response from the API
        :rtype: Response object

    .. py:method:: fetch_subscription(id_or_code: str)→ Response

        Get details of a subscription

        :param id_or_code: The subscription id or code
        :type id_or_code: str

        :return: The response from the API
        :rtype: Response object

    .. py:method:: generate_update_subscription(subscription_code: str)→ Response

        Generate a link for updating the card on subscription

        :param subscription_code: the subscription code
        :type subscription_code: str

        :return: The response from thw API
        :rtype: Response object

    .. py:method:: list_subscriptions(per_page: int | None = 50, page: int | None = 1, customer: int | None = None, plan_code: int | None = None)→ Response

        List all subscriptions

        :param per_page: The number of subscriptions per page. (default: 50)
        :type per_page: int, optional
        :param page: The page number. (default: 1)
        :type page: int, optional
        :param customer: The customer number
        :type customer: int, optional
        :param plan_code: The plan code
        :type plan_code: int, optional

        :return: The response from the API
        :rtype: Response object

    .. py:method:: send_update_subscription_link(subscription_code: str)→ Response

        Email a customer a link for updating the card on their subscription

        :param subscription_code: The subscription code
        :type subscription_code: str

        :return: The response from the API
        :rtype: Response object


.. _Subscriptions: https://paystack.com/docs/api/subscription/
