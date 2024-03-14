paystackease.apis.subscriptions module
--------------------------------------

.. :py:currentmodule:: paystackease.apis.subscriptions


Wrapper for Paystack Subscriptions API. The Subscriptions API allows you to create and manage recurring payment on your integration.

------------------------------------------------------------

.. py:class:: SubscriptionClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Subscription API Reference: `Subscriptions`_

    .. py:method:: create_subscription(customer: str, plan_code: str, authorization: str, start_date: date | None = None)→ dict

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
        :rtype: dict

    .. py:method:: disable_subscription(subscription_code: str, token: str)→ dict

        Disable a subscription

        :param subscription_code: the subscription code
        :type subscription_code: str
        :param token: the token sent to the customer email
        :type token: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: enable_subscription(subscription_code: str, token: str)→ dict

        Enable a subscription

        :param subscription_code: The subscription code
        :type subscription_code: str
        :param token: The token sent to the customer email
        :type token: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: fetch_subscription(id_or_code: str)→ dict

        Get details of a subscription

        :param id_or_code: The subscription id or code
        :type id_or_code: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: generate_update_subscription(subscription_code: str)→ dict

        Generate a link for updating the card on subscription

        :param subscription_code: the subscription code
        :type subscription_code: str

        :return: The response from thw API
        :rtype: dict

    .. py:method:: list_subscriptions(per_page: int | None = None, page: int | None = None, customer: int | None = None, plan_code: int | None = None)→ dict

        List all subscriptions

        :param per_page: The number of subscriptions per page
        :type per_page: int, optional
        :param page: The page number
        :type page: int, optional
        :param customer: The customer number
        :type customer: int, optional
        :param plan_code: The plan code
        :type plan_code: int, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: send_update_subscription_link(subscription_code: str)→ dict

        Email a customer a link for updating the card on their subscription

        :param subscription_code: The subscription code
        :type subscription_code: str

        :return: The response from the API
        :rtype: dict


.. _Subscriptions: https://paystack.com/docs/api/subscription/
