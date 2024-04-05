""" Test for synchronous Customers """

import pytest

from tests.conftest import async_miscellaneous_client, mocked_responses


@pytest.mark.asyncio
@pytest.mark.parametrize(
    (
        "country",
        "use_cursor",
        "per_page",
        "pay_with_bank_transfer",
        "pay_with_bank",
        "enabled_for_notification",
        "next_cursor",
        "previous_cursor",
        "gateway",
        "channel_type",
        "currency",
    ),
    [
        (
            "ghana",
            True,
            1,
            True,
            True,
            True,
            "next",
            "previous",
            "emandate",
            "mobile_money",
            "NGN",
        ),
        (None, False, None, False, False, False, None, None, None, None, None),
    ],
)
async def test_list_banks(
    async_miscellaneous_client,
    mocked_responses,
    country,
    use_cursor,
    per_page,
    pay_with_bank_transfer,
    pay_with_bank,
    enabled_for_notification,
    next_cursor,
    previous_cursor,
    gateway,
    channel_type,
    currency,
):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/bank"
    response_data = {"status": "success"}
    url_params = {
        "country": country,
        "use_cursor": str(use_cursor),
        "perPage": per_page,
        "supports_transfer": str(pay_with_bank_transfer),
        "pay_with_bank": str(pay_with_bank),
        "enabled_for_verification": str(enabled_for_notification),
        "next": next_cursor,
        "previous": previous_cursor,
        "gateway": gateway,
        "type": channel_type,
        "currency": currency,
    }
    # Construct the expected URL with parameters
    query_string = "&".join(
        f"{key}={value}" for key, value in url_params.items() if value is not None
    )
    expected_url = url + ("?" + query_string if query_string else "")

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_miscellaneous_client.list_banks(
        country=country,
        use_cursor=use_cursor,
        per_page=per_page,
        pay_with_bank_transfer=pay_with_bank_transfer,
        pay_with_bank=pay_with_bank,
        enabled_for_verification=enabled_for_notification,
        next_cursor=next_cursor,
        previous_cursor=previous_cursor,
        gateway=gateway,
        channel_type=channel_type,
        currency=currency,
    )
    print(response)
    # mocked_responses.assert_called()
    # assert response is not None


@pytest.mark.asyncio
async def test_countries(async_miscellaneous_client, mocked_responses):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/country"
    response_data = {"status": "success"}

    mocked_responses.get(
        url,
        status=200,
        payload=response_data,
    )
    response = await async_miscellaneous_client.list_countries()
    mocked_responses.assert_called()
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.parametrize(("country",), [("NG",), ("US",)])
async def test_states(async_miscellaneous_client, mocked_responses, country):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/address_verification/states"
    response_data = {"status": "success"}
    url_params = {
        "country": country,
    }
    # Construct the expected URL with parameters
    query_string = "&".join(
        f"{key}={value}" for key, value in url_params.items() if value is not None
    )
    expected_url = url + ("?" + query_string if query_string else "")

    mocked_responses.get(
        expected_url,
        status=200,
        payload=response_data,
    )
    response = await async_miscellaneous_client.list_states(country=country)
    mocked_responses.assert_called()
    assert response is not None
