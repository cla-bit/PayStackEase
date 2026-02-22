from typing import List

from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import ValidationInfo


class BulkChargeItem(BaseModel):
    """
    Represents a single bulk charge item for payment processing.

    This model validates that each charge item contains the required fields
    with proper formatting and values before being processed in a bulk operation.

    Attributes:
        authorization (str): The authorization code for the payment method.
            Must be a non-empty string after stripping whitespace.
        amount (int): The charge amount in the smallest currency unit
            (e.g., cents for USD). Must be greater than 0.
        reference (str): A unique reference identifier for this charge.
            Must be a non-empty string after stripping whitespace.

    Example:
        >>> charge = BulkChargeItem(
        ...     authorization="AUTH_12345",
        ...     amount=1000,
        ...     reference="REF_001"
        ... )
        >>> print(charge.authorization)
        'AUTH_12345'
    """
    authorization: str
    amount: int
    reference: str

    @field_validator("authorization", "reference")
    def validate_non_empty(cls, value: str, info: ValidationInfo):
        """
        Validate that string fields are not empty or just whitespace.

        This validator is applied to both 'authorization' and 'reference' fields.
        It ensures that these fields contain meaningful data by checking that
        they are not None, empty strings, or strings containing only whitespace.

        Args:
            value (str): The field value to validate.
            info (FieldValidationInfo): Validation context containing field name.

        Returns:
            str: The stripped value if validation passes.

        Raises:
            ValueError: If the value is None, empty, or only whitespace.

        Example:
            >>> BulkChargeItem.validate_non_empty("  test  ", info)
            'test'
            >>> BulkChargeItem.validate_non_empty("", info)  # Raises ValueError
        """
        if not value or not value.strip():
            raise ValueError(f"{info.field_name} cannot be empty")
        return value.strip()

    @field_validator("amount")
    def validate_amount(cls, value: int, info: ValidationInfo):
        """
        Validate that the amount is a positive integer.

        Ensures that the charge amount is greater than zero since negative
        or zero amounts are not valid for processing charges.

        Args:
            value (int): The amount value to validate.
            info (FieldValidationInfo): Validation context containing field name.

        Returns:
            int: The validated amount if it's positive.

        Raises:
            ValueError: If the amount is less than or equal to 0.

        Example:
            >>> BulkChargeItem.validate_amount(1000, info)
            1000
            >>> BulkChargeItem.validate_amount(0, info)  # Raises ValueError
        """
        if value <= 0:
            raise ValueError(f"{info.field_name} must be greater than 0")
        return value


class BulkChargeListObject(BaseModel):
    """
    Container for a list of bulk charge items with comprehensive validation.

    This model accepts and validates a list of charge dictionaries, ensuring
    each dictionary contains exactly the required fields with no missing or
    extra keys. It provides a property to easily convert the validated items
    to a format suitable for API requests.

    Attributes:
        charges (List[BulkChargeItem]): A list of validated BulkChargeItem
            objects. Each item must contain exactly 'authorization', 'amount',
            and 'reference' keys.

    Example:
        >>> data = {
        ...     "charges": [
        ...         {"authorization": "AUTH1", "amount": 1000, "reference": "REF1"},
        ...         {"authorization": "AUTH2", "amount": 2000, "reference": "REF2"}
        ...     ]
        ... }
        >>> bulk_charges = BulkChargeListObject(**data)
        >>> api_ready_list = bulk_charges.use_as_list
        >>> print(api_ready_list)
        [{'authorization': 'AUTH1', 'amount': 1000, 'reference': 'REF1'}, ...]
    """
    charges: List[BulkChargeItem]

    @field_validator("charges", mode="before")
    def validate_charges(cls, value) -> List:
        """
        Validate the charges list before parsing into BulkChargeItem objects.

        This pre-validation ensures that the input is properly structured:
        - The value must be a list
        - Each item in the list must be a dictionary
        - Each dictionary must have exactly the required keys:
          'authorization', 'amount', and 'reference'
        - No missing or extra keys are allowed

        Args:
            value: The raw input value to validate (should be a list of dicts).

        Returns:
            List: The validated list, ready for further processing.

        Raises:
            ValueError: If the input is not a list, if any item is not a dict,
                or if any dict has missing or extra keys.

        Example:
            >>> # Valid input
            >>> BulkChargeListObject.validate_charges([
            ...     {"authorization": "A1", "amount": 100, "reference": "R1"}
            ... ])

            >>> # Invalid - missing keys
            >>> BulkChargeListObject.validate_charges([
            ...     {"authorization": "A1", "amount": 100}  # Raises ValueError
            ... ])

            >>> # Invalid - extra keys
            >>> BulkChargeListObject.validate_charges([
            ...     {"authorization": "A1", "amount": 100,
            ...      "reference": "R1", "extra": "field"}  # Raises ValueError
            ... ])
        """
        if not isinstance(value, list):
            raise ValueError("charges must be a list")

        # Validate each dictionary has exactly the required keys
        required_keys = {'authorization', 'amount', 'reference'}

        for i, item in enumerate(value):
            if not isinstance(item, dict):
                raise ValueError(f'Item at index {i} must be a dictionary')

            # Check for exact key match
            item_keys = set(item.keys())

            # Check for missing keys
            missing_keys = required_keys - item_keys
            if missing_keys:
                raise ValueError(f'Item at index {i} missing required keys: {missing_keys}')

            # Check for extra keys
            extra_keys = item_keys - required_keys
            if extra_keys:
                raise ValueError(f'Item at index {i} has extra keys: {extra_keys}')
        return value

    @property
    def use_as_list(self):
        """
        Convert the validated charges to a list of dictionaries for API use.

        This property provides a convenient way to transform the validated
        BulkChargeItem objects back into a simple list of dictionaries,
        suitable for JSON serialization when making API requests to external
        services.

        Returns:
            List[dict]: A list of dictionaries, each containing the validated
                charge data in the format expected by payment APIs.

        Example:
            >>> bulk_charges = BulkChargeListObject(**data)
            >>> payload = bulk_charges.use_as_list
            >>> response = requests.post(
            ...     'https://api.example.com/charges',
            ...     json=payload
            ... )
        """
        return [charge.model_dump() for charge in self.charges]

