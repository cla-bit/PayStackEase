from paystackease.helpers import AuthReferenceObject
from paystackease import PayStackBase

def main():
    # Interacting with the PayStackBase wrapper
    # make sure to set PAYSTACK_SECRET_KEY env variable
    paystack_client = PayStackBase()
    auth_model1 = AuthReferenceObject(amount=10000, authorization="AUTH_authorization-code", reference="dam1266638dhhe")
    auth_model2 = AuthReferenceObject(amount=10000, authorization="AUTH_authorization-code", reference="dam1266638dhhe")

    # """Implementing all the API endpoints"""
    # # access the API endpoints making a Get request
    # list_bulk = paystack_client.bulk_charges.list_bulk_charge_batches()
    # print(f"List all bulk charges: {list_bulk}")
    #
    # get_bulk_batch = paystack_client.bulk_charges.fetch_bulk_charge_batch(
    #     id_or_code="bulk-id-or-code"
    # )
    # print(f"Fetch a bulk charge of a specific batch: {get_bulk_batch}")
    #
    # get_charge_batch = paystack_client.bulk_charges.fetch_charge_bulk_batch(
    #     id_or_code="BCH_bulk-code", status=STATUS.PENDING.value
    # )
    # print(f"Fetch a charge of a specific batch: {get_charge_batch}")
    #
    # pause_bulk = paystack_client.bulk_charges.pause_bulk_charge_batch(
    #     batch_code="BCH_bulk-code"
    # )
    # print(f"Pause a bulk charge batch: {pause_bulk}")
    #
    # resume_bulk = paystack_client.bulk_charges.resume_bulk_charge_batch(
    #     batch_code="BCH_bulk-code"
    # )
    # print(f"Resume a bulk charge batch: {resume_bulk}")

    # access the API endpoints making a Post request
    init_bulk_charge = paystack_client.bulk_charges.initiate_bulk_charge([auth_model1, auth_model2])
    print(f"Initiated a bulk charge: {init_bulk_charge}")


if __name__ == "__main__":
    main()
