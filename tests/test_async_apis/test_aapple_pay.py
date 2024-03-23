""" Tests for synchronous Apple Pay """

import json
import pytest
from unittest.mock import Mock

from aioresponses import aioresponses
from tests.conftest import async_apple_pay_client, mocked_responses


@pytest.mark.parametrize(
    "use_cursor, next_page, previous_page", [
        (True, 1, 1),  # Testing with all parameters provided
        (False, 1, 2),  # Testing with all parameters provided
        (True, None, None),  # Testing with only use_cursor parameter provided
        (False, None, None),  # Testing with only use_cursor parameter provided
    ]
)
@pytest.mark.asyncio
async def test_list_domains(async_apple_pay_client, mocked_responses, use_cursor, next_page, previous_page):
    """
    This function tests the behavior of the list_domains method with various combinations
    of parameters, including scenarios where some parameters are None.
    """
