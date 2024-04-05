===================
Convert module
===================

This holds a function to convert to subunits in NGN, GHS, USD, ZAR and KES

.. py:function:: convert_to_subunit(amount: int, currency: Currency)→ int

    Convert a subunit amount to a base amount

    :param amount: The amount to convert
    :type amount: int
    :param currency: The Currency type to use for conversion
    :type currency: Currency. This is an Enum class

    :return: The subunit of the amount i.e 100 kobo = 1 Naira (Currency.Naira)
    :rtype: int

**USAGE**

.. code-block:: python

    >>> from paystackease import convert_to_subunit, Currency

    >>> subunit = convert_to_subunit(amount=100, currency=Currency.NGN)
    >>> print(f"Subunit: {subunit}")

This will printed as:

.. code-block:: console

    Subunit: 10000
