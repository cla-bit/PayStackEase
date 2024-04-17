import asyncio
from paystackease import PayStackBase, AsyncPayStackBase

# client = PayStackBase()
#
# print(client.transactions.list_transactions())


async def list_transactions():
    """
    List transactions
    Reference: https://paystack.com/docs/api/transaction/
    """
    async with AsyncPayStackBase() as client:
        transactions = await client.transactions.list_transactions()
        print(transactions)

asyncio.run(list_transactions())
