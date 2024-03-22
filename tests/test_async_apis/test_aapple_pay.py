""" Tests for synchronous Apple Pay """

import json
import pytest
from aioresponses import aioresponses
from tests.conftest import async_apple_pay_client


@pytest.mark.parametrize(
    "use_cursor, next_page, previous_page", [
        (True, 1, 1),  # Testing with all parameters provided
        (False, 1, 2),  # Testing with all parameters provided
        (True, None, None),  # Testing with only use_cursor parameter provided
        (False, None, None),  # Testing with only use_cursor parameter provided
    ]
)
@pytest.mark.asyncio
async def test_list_domains(async_apple_pay_client, use_cursor, next_page, previous_page):
    with aioresponses as mock_client:
        mock_response = {"status": "success"}
        mock_client.get(
            "https://api.paystack.co/apple-pay/domain",
            payload=mock_response,
            status=200,
        )
        response = await async_apple_pay_client.list_domains(use_cursor=use_cursor, next_page=next_page, previous_page=previous_page)
        assert response == mock_response
