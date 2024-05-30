"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase, EventType


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        all_terminals = await paystack_client.terminal.list_terminals()
        print(f"All Terminals: {all_terminals}")

        get_terminal = await paystack_client.terminal.fetch_terminal(
            terminal_id="terminal-id-here"
        )
        print(f"Terminal Detail: {get_terminal}")

        get_terminal_status = await paystack_client.terminal.fetch_terminal_status(
            terminal_id="terminal-id-here"
        )
        print(f"Terminal Status Detail: {get_terminal_status}")

        get_terminal_event_status = await paystack_client.terminal.fetch_event_status(
            terminal_id="terminal-id-here", event_id="event-id-here"
        )
        print(f"Terminal Event Status Detail: {get_terminal_event_status}")

        # access the API endpoints making a Post request
        create_event = await paystack_client.terminal.send_event(
            terminal_id="terminal-id-here",
            event_type=EventType.INVOICE.value,
            terminal_action="terminal-action-here",
            data_object={"key": "value"},
        )
        print(f"Created Event: {create_event}")

        commission_terminal = await paystack_client.terminal.commission_terminal(
            serial_number="serial-number-here"
        )
        print(f"Commissioned Terminal: {commission_terminal}")

        decommission_terminal = await paystack_client.terminal.decommission_terminal(
            serial_number="serial-number-here"
        )
        print(f"Decommissioned Terminal: {decommission_terminal}")

        # access the API endpoints making a Put request
        update_terminal = await paystack_client.terminal.update_terminal(
            terminal_id="terminal-id-here",
            terminal_name="terminal-name-here",
            terminal_address="address-here",
        )
        print(f"Updated Terminal: {update_terminal}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    all_terminals = paystack_client.terminal.list_terminals()
    print(f"All Terminals: {all_terminals}")

    get_terminal = paystack_client.terminal.fetch_terminal(
        terminal_id="terminal-id-here"
    )
    print(f"Terminal Detail: {get_terminal}")

    get_terminal_status = paystack_client.terminal.fetch_terminal_status(
        terminal_id="terminal-id-here"
    )
    print(f"Terminal Status Detail: {get_terminal_status}")

    get_terminal_event_status = paystack_client.terminal.fetch_event_status(
        terminal_id="terminal-id-here", event_id="event-id-here"
    )
    print(f"Terminal Event Status Detail: {get_terminal_event_status}")

    # access the API endpoints making a Post request
    create_event = paystack_client.terminal.send_event(
        terminal_id="terminal-id-here",
        event_type=EventType.INVOICE.value,
        terminal_action="terminal-action-here",
        data_object={"key": "value"},
    )
    print(f"Created Event: {create_event}")

    commission_terminal = paystack_client.terminal.commission_terminal(
        serial_number="serial-number-here"
    )
    print(f"Commissioned Terminal: {commission_terminal}")

    decommission_terminal = paystack_client.terminal.decommission_terminal(
        serial_number="serial-number-here"
    )
    print(f"Decommissioned Terminal: {decommission_terminal}")

    # access the API endpoints making a Put request
    update_terminal = paystack_client.terminal.update_terminal(
        terminal_id="terminal-id-here",
        terminal_name="terminal-name-here",
        terminal_address="address-here",
    )
    print(f"Updated Terminal: {update_terminal}")


if __name__ == "__main__":
    main()
