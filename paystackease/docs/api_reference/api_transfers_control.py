"""
Demonstrates using Asynchronous and Synchronous Paystack Transfers Control API wrappers.
Shows PayStackBase and AsyncPayStackBase for interacting with Paystack's verification.

Reference: https://paystack.com/docs/api/trasfer-control/ to learn more
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase, ResendOTP


async def main():
    async with AsyncPayStackBase() as paystack_client:
        # # access the API endpoints making a Get request
        get_balance = await paystack_client.transfer_control.check_balance()
        print(f"Balance: {get_balance}")

        get_balance_ledger = (
            await paystack_client.transfer_control.fetch_balance_ledger()
        )
        print(f"Balance Ledger: {get_balance_ledger}")

        # access the API endpoints making a Post request
        resent_otp = await paystack_client.transfer_control.resend_otp(
            transfer_code="TRF_vsyqdmlzble3uii", reason=ResendOTP.RESEND_OTP.value
        )
        print(f"Resend OTP: {resent_otp}")

        disabled_otp = await paystack_client.transfer_control.disable_otp()
        print(f"Disabled OTP: {disabled_otp}")

        final_disable_otp = await paystack_client.transfer_control.finalize_disable_otp(
            otp="928783"
        )
        print(f"Finalized Disable OTP: {final_disable_otp}")

        enable_otp = await paystack_client.transfer_control.enable_otp()
        print(f"Enabled OTP: {enable_otp}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable or pass secret key as keyword argument
    paystack_client = PayStackBase()
    # or paystack_client = PayStackBase(secret_key="secret_key")

    # # access the API endpoints making a Get request
    get_balance = paystack_client.transfer_control.check_balance()
    print(f"Balance: {get_balance}")

    get_balance_ledger = paystack_client.transfer_control.fetch_balance_ledger()
    print(f"Balance Ledger: {get_balance_ledger}")

    # access the API endpoints making a Post request
    resent_otp = paystack_client.transfer_control.resend_otp(
        transfer_code="TRF_vsyqdmlzble3uii", reason=ResendOTP.RESEND_OTP.value
    )
    print(f"Resend OTP: {resent_otp}")

    disabled_otp = paystack_client.transfer_control.disable_otp()
    print(f"Disabled OTP: {disabled_otp}")

    final_disable_otp = paystack_client.transfer_control.finalize_disable_otp(
        otp="928783"
    )
    print(f"Finalized Disable OTP: {final_disable_otp}")

    enable_otp = paystack_client.transfer_control.enable_otp()
    print(f"Enabled OTP: {enable_otp}")


if __name__ == "__main__":
    main()
