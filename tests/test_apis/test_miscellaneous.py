""" Test for synchronous Customers """

import pytest
import responses

from tests.conftest import miscellaneous_client


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
@responses.activate
def test_list_banks(
    miscellaneous_client,
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
        "pay_with_bank_transfer": str(pay_with_bank_transfer),
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

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = miscellaneous_client.list_banks(
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
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response.status == "success"


@responses.activate
def test_countries(miscellaneous_client):
    """Test for synchronous Customers"""
    url = "https://api.paystack.co/country"
    response_data = {"status": "success"}

    responses.add(
        responses.GET,
        url,
        status=200,
        json=response_data,
    )
    response = miscellaneous_client.list_countries()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url
    assert response is not None


@pytest.mark.parametrize(("country",), [("NG",), ("US",)])
@responses.activate
def test_states(miscellaneous_client, country):
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

    responses.add(
        responses.GET,
        expected_url,
        status=200,
        json=response_data,
    )
    response = miscellaneous_client.list_states(country=country)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == expected_url
    assert response.status == "success"
