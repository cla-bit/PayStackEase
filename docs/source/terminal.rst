===========================================
Terminal Module
===========================================

.. :py:currentmodule:: paystackease.apis.terminal

Wrapper for Paystack Terminal APIs. The Terminal API allows you to build delightful in-person payment experiences.

-------------

.. py:class:: TerminalClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.base.PayStackBaseClientAPI`

    Paystack Terminal API Reference: `Terminal`_

    .. py:method:: commission_terminal(serial_number: str)→ PayStackResponse

        Activate debug device by linking it to your integration

        :param serial_number: serial number of the device to activate
        :type serial_number: str

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: decommission_terminal(serial_number: str)→ PayStackResponse

        Deactivate debug device by unlinking it from your integration

        :param serial_number: the serial number of the device to be deactivated
        :type serial_number: str

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: fetch_event_status(terminal_id: str, event_id: str)→ PayStackResponse

        Fetch details of a specific event status sent to the terminal

        :param terminal_id: terminal ID the event is sent to
        :type terminal_id: str
        :param event_id: event ID the event is sent to the terminal
        :type event_id: str

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: fetch_terminal(terminal_id: str)→ PayStackResponse

        Get details of a terminal

        :param terminal_id: The terminal id the event is sent to
        :type terminal_id: str

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: fetch_terminal_status(terminal_id: str)→ PayStackResponse

        Fetch the availability of a terminal before sending an event

        :param terminal_id: terminal id the event is sent to
        :type terminal_id: str

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: list_terminals(per_page: int = 50, next_cursor: bool | None = True, previous_cursor: bool | None = True)→ PayStackResponse

        List the Terminals available on your integration

        :param per_page: The number of terminal records per page. (default: 50)
        :type per_page: int, optional
        :param next_cursor: (default: True)
        :type next_cursor: bool, optional
        :param previous_cursor: (default: True)
        :type previous_cursor: bool, optional

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: send_event(terminal_id: str, event_type: str, terminal_action: str, data_object: Dict[str, str])→ PayStackResponse

        Send an event from your application to the Paystack Terminal

        :param terminal_id: The terminal id the event is sent to
        :type terminal_id: str
        :param event_type: The event type to send.
        :type event_type: str
        :param terminal_action: The action to perform on the terminal
        :type terminal_action: str
        :param data_object: parameters needed to perform the specified action.

        :return: The response from the API
        :rtype: PayStackResponse object

    .. py:method:: update_terminal(terminal_id: str, terminal_name: str, terminal_address: str)→ PayStackResponse

        Update details of the terminal

        :param terminal_id: terminal id the event is sent to
        :type terminal_id: str
        :param terminal_name: terminal name
        :type terminal_name: str
        :param terminal_address: terminal address
        :type terminal_address: str

        :return: The response from the API
        :rtype: PayStackResponse object

.. note::

    If you pass ``invoice type`` as the ``event_type``, the action can either be [ ``process`` || ``view`` ].
    For ``transaction type`` as the ``event_type``, the action can either be [ ``process`` || ``print`` ].

    **Use the string values of the ``EventType`` and ``EventAction``.**

    For data_object follows as suited: ``[invoice type]``: you need to pass ``{id: invoice_id, reference: offline_reference}``. ``[transaction type]``, you can pass ``{id: transaction_id}``


.. _Terminal: https://paystack.com/docs/api/terminal/
