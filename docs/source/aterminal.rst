paystackease.async\_apis.aterminal module
-----------------------------------------

.. :py:currentmodule:: paystackease.async_apis.aterminal

Wrapper for Asynchronous Paystack Terminal APIs. The Terminal API allows you to build delightful in-person payment experiences.

----------------------------------------------------

.. py:class:: AsyncTerminalClientAPI(secret_key: str = None)

    Bases: :py:class:`~paystackease.abase.AsyncPayStackBaseClientAPI`

    Paystack Terminal API Reference: `Terminal`_

    .. py:method:: async commission_terminal(serial_number: str)→ dict

        Activate debug device by linking it to your integration

        :param serial_number: serial number of the device to activate
        :type serial_number: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: async decommission_terminal(serial_number: str)→ dict

        Deactivate debug device by unlinking it from your integration

        :param serial_number: the serial number of the device to be deactivated
        :type serial_number: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: async fetch_event_status(terminal_id: str, event_id: str)→ dict

        Fetch details of a specific event status sent to the terminal

        :param terminal_id: terminal ID the event is sent to
        :type terminal_id: str
        :param event_id: event ID the event is sent to the terminal
        :type event_id: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: async fetch_terminal(terminal_id: str)→ dict

        Get details of a terminal

        :param terminal_id: The terminal id the event is sent to
        :type terminal_id: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: async fetch_terminal_status(terminal_id: str)→ dict

        Fetch the availability of a terminal before sending an event

        :param terminal_id: terminal id the event is sent to
        :type terminal_id: str

        :return: The response from the API
        :rtype: dict

    .. py:method:: async list_terminals(per_page: int, next_cursor: str | None = None, previous_cursor: str | None = None)→ dict

        List the Terminals available on your integration

        :param per_page: The number of terminal records per page
        :type per_page: int, optional
        :param next_cursor:
        :type next_cursor: str, optional
        :param previous_cursor:
        :type previous_cursor: str, optional

        :return: The response from the API
        :rtype: dict

    .. py:method:: async send_event(terminal_id: str, event_type: str, terminal_action: str, data_object: Dict[str, str])→ dict

        Send an event from your application to the Paystack Terminal

        :param terminal_id: The terminal id the event is sent to
        :type terminal_id: str
        :param event_type: The event type to send.
        :type event_type: str
        :param terminal_action: The action to perform on the terminal
        :type terminal_action: str
        :param data_object: parameters needed to perform the specified action.

        :return: The response from the API
        :rtype: dict

    .. note::

        If you pass ``invoice type`` as the ``event_type``, the action can either be [ ``process`` || ``view`` ].

        For ``transaction type`` as the ``event_type``, the action can either be [ ``process`` || ``print`` ].

        For data_object follow as suited: ``[invoice type]: you need to pass {id: invoice_id, reference: offline_reference}. [transaction type], you can pass {id: transaction_id}``

    .. py:method:: async update_terminal(terminal_id: str, terminal_name: str, terminal_address: str)→ dict

        Update details of the terminal

        :param terminal_id: terminal id the event is sent to
        :type terminal_id: str
        :param terminal_name: terminal name
        :type terminal_name: str
        :param terminal_address: terminal address
        :type terminal_address: str

        :return: The response from the API
        :rtype: dict


.. _Terminal: https://paystack.com/docs/api/terminal/
