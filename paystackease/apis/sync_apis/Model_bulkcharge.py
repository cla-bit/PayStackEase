from pydantic import BaseModel

class BulkChargeItem(BaseModel):
    authorization: str  # A string for the authorization code
    amount: int         # An integer for the amount
    reference: str      # A string for the reference
