from paystackease.helpers import AuthReferenceObject, CustomMetaData, CustomMetaField, VirtualPaymentModel, QRCODE, QRPayment, USSDPayment, USSD, ChargeBankModel, BankDetails, ExpiryInfo
from paystackease import PayStackBase

def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()
    meta_field = CustomMetaField(value="Text value", display_name="Text Testing", variable_name="Test variable")
    metadata = CustomMetaData(custom_fields=[meta_field])
    auth_model1 = AuthReferenceObject(amount=10000, authorization="AUTH_authorization-code", reference="dam1266638dhhe")
    bank_details = ChargeBankModel(bank=BankDetails(code="057", account_number="0000000000"), bank_transfer=ExpiryInfo(account_expires_at="2023-09-12T13:10:00Z"))
    qr_pay = QRPayment(provider=QRCODE.SCAN_TO_PAY)
    ussd_pay = USSDPayment(type=USSD.ZENITH_BANK)
    virtual = VirtualPaymentModel(qr=qr_pay, ussd=ussd_pay)


    # access the API endpoints making a Post request
    init_charges = paystack_client.charges.create_charge(email="text@example.com", metadata=metadata,
                                                         auth_ref=auth_model1, bank_charge=bank_details, virtual_pay=virtual)
    print(f"Initiated a charges: {init_charges}")


if __name__ == "__main__":
    main()
