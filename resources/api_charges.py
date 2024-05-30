"""
Examples
"""

import asyncio
from paystackease import PayStackBase, AsyncPayStackBase


async def main():
    """Implementing all the API endpoints"""
    async with AsyncPayStackBase() as paystack_client:
        # access the API endpoints making a Get request
        check_pend_charge = await paystack_client.charges.check_pending_charge(reference="c05e7jxueiviclo")
        print(f"Check pending charge: {check_pend_charge}")

        # access the API endpoints making a Post request
        create_charge = await paystack_client.charges.create_charge(
            email="email@gmail.com",
            amount=1000,
            authorization_code="AUTH_nii6s41xsr",
            metadata={
                "custom_fields": {
                    "value": "test",
                    "display_name": "test-display",
                    "variable_name": "test-variable",
                }
            }
        )
        print(f"Create charge: {create_charge.charge_url}")  # access the charge url from PayStackResponse

        submit_pin = await paystack_client.charges.submit_pin(
            pin=1234, reference="c05e7jxueiviclo"
        )
        print(f"Submit pin: {submit_pin}")

        submit_otp = await paystack_client.charges.submit_otp(
            otp=123456, reference="c05e7jxueiviclo"
        )
        print(f"Submit otp: {submit_otp}")

        submit_phone = await paystack_client.charges.submit_phone(
            phone="08012345678", reference="c05e7jxueiviclo"
        )
        print(f"Submit phone: {submit_phone}")

        submit_birthday = await paystack_client.charges.submit_birthday(
            birthday="1994-02-23", reference="c05e7jxueiviclo"
        )
        print(f"Submit birthday: {submit_birthday}")

        submit_address = await paystack_client.charges.submit_address(
            reference="c05e7jxueiviclo",
            address="140 N 2ND ST",
            city="Stroudsburg",
            state="PA",
            zipcode="18360",
        )
        print(f"Submit address: {submit_address}")


asyncio.run(main())


def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()

    """ Implementing all the API endpoints """
    # access the API endpoints making a Get request
    check_pend_charge = paystack_client.charges.check_pending_charge(reference="c05e7jxueiviclo")
    print(f"Check pending charge: {check_pend_charge}")

    # access the API endpoints making a Post request
    create_charge = paystack_client.charges.create_charge(
        email="email@gmail.com",
        amount=100,
        authorization_code="AUTH_nii6s41xsr",
        metadata={
            "custom_fields": {
                "value": "test",
                "display_name": "test-display",
                "variable_name": "test-variable",
            }
        }
    )
    print(f"Create charge: {create_charge.charge_url}")  # access the charge url from PayStackResponse

    submit_pin = paystack_client.charges.submit_pin(
        pin=1234, reference="c05e7jxueiviclo"
    )
    print(f"Submit pin: {submit_pin}")

    submit_otp = paystack_client.charges.submit_otp(
        otp=123456, reference="c05e7jxueiviclo"
    )
    print(f"Submit otp: {submit_otp}")

    submit_phone = paystack_client.charges.submit_phone(
        phone="08012345678", reference="c05e7jxueiviclo"
    )
    print(f"Submit phone: {submit_phone}")

    submit_birthday = paystack_client.charges.submit_birthday(
        birthday="1994-02-23", reference="c05e7jxueiviclo"
    )
    print(f"Submit birthday: {submit_birthday}")

    submit_address = paystack_client.charges.submit_address(
        reference="c05e7jxueiviclo",
        address="140 N 2ND ST",
        city="Stroudsburg",
        state="PA",
        zipcode="18360",
    )
    print(f"Submit address: {submit_address}")


if __name__ == "__main__":
    main()
