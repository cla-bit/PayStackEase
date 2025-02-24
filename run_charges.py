from datetime import datetime, date
from paystackease.helpers import BulkChargeObject, CustomMetaData, CustomMetaField, VirtualPaymentModel, QRCODE, QRPayment, USSDPayment, USSD, BankDetails, ExpiryInfo, Bearer
from paystackease import PayStackBase

def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()
    meta_field = CustomMetaField(value="Text value", display_name="Text Testing", variable_name="Test variable")
    metadata = CustomMetaData(custom_fields=[meta_field])
    auth_model1 = BulkChargeObject(amount=10000)
    auth_model2 = BulkChargeObject(amount=20000, authorization_code="AUTH_f5yarskyfm", reference="3tJSYz4o6Oxp6XyIyG1x_w")
    bank = BankDetails(code="011", account_number="0000000000")
    bank_transfer = ExpiryInfo(account_expires_at=datetime.now().isoformat())
    qr_pay = QRPayment(provider=QRCODE.VISA)
    ussd_pay = USSDPayment(type=USSD.ZENITH_BANK)
    virtual = VirtualPaymentModel(ussd=ussd_pay)
    birthday = date(1994, 12, 25)


    # access the API endpoints making a Post request
    # init_charges = paystack_client.charges.create_charge(
    #     email="text@example.com", metadata=metadata, auth_ref=auth_model1,
    #     bank=bank
    # )  # just passing the auth_model1(only 'amount' was passed) and bank only
    # print(f"Initiated a charges: {init_charges}")
    # init_charges = paystack_client.charges.create_charge(
    #     email="text@example.com", metadata=metadata, auth_ref=auth_model2,
    # )  # just passing the auth_model2 only
    # init_charges = paystack_client.charges.create_charge(
    #     email="text@example.com", metadata=metadata, auth_ref=auth_model1, virtual_pay=virtual,
    #     bearer=Bearer.SUB_ACCOUNT
    # )  # just passing auth_model1 and virtual(ussd parameter only).
    # init_charges = paystack_client.charges.create_charge(
    #     email="text@example.com", metadata=metadata, auth_ref=auth_model1, virtual_pay=virtual
    # )  # just passing auth_model1 and virtual(qr parameter only).
    # submit_birthday = paystack_client.charges.check_pending_charge("kshorocoh7flm0o")
    # print(f"Submit Birthday: {submit_birthday}")

    # print(f"Initiated a charges: {init_charges}")


if __name__ == "__main__":
    main()
