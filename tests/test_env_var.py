""" Tests for the Environment variables """

import os

import pytest
from paystackease.core import EnvConfig, SecretKeyError
from conftest import env_var


def test_secret_key(env_var):
    secret_key = "test_secret_key"
    env = env_var.secret_key()
    assert env == secret_key


def test_no_secret_key():
    """Test for no secret key"""
    os.environ.get("PAYSTACK_SECRET_KEY", None)
    client = EnvConfig()
    if client.secret_key() is None:
        with pytest.raises(SecretKeyError):
            client.secret_key()
