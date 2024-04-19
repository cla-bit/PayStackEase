# PayStackEase Library  

--------------

![Python Versions](https://img.shields.io/badge/python-3.9|3.10|3.11|3.12-blue) ![License](https://img.shields.io/pypi/l/paystackease.svg) ![pypi](https://img.shields.io/pypi/v/paystackease.svg)


**PayStackEase API Library**  is a Python library that simplifies interacting with the Paystack API. 
It provides both asynchronous and synchronous wrappers for various Paystack functionalities, 
making it easier to integrate payment processing into your Python projects.

> 📝: Read more on paystack api documentation: [Paystack API DOCUMENTATION](https://paystack.com/docs/api/)

> 📝: Read more on paystackease api documentation: [PayStackEase DOCUMENTATION](https://paystackease.readthedocs.io/en/latest/)


## Getting Started

You should create a Paystack account to generate a **Paystack Secret Key**. You can see this in the *settings page >> API keys and Webhook section*.

> ⚠️: **Warning:** Do not expose your secret key or commit your secret key to git, or use them in client-side code.

> 💡: **Take Note:**  Public key is to be used from your front-end when integrating using Paystack Inline. In this case you have to use you secret key

> ✅: **Good**: Set your secret key in environment variables as seen: *PAYSTACK_SECRET_KEY=your-secret-key*


## Create a Virtual Environment

1. For Windows:

    * Create virtual environment

        ```
            py -m venv <environment_name>
       ```
    * Activate the virtual environment

        ```
            <environment_name>\Scripts\activate
       ```

2. For Unix/macOS

    * Create virtual environment

        ```
            python3 -m venv <environment_name>
       ```
    * Activate the virtual environment

        ```
            <environment_name>/bin/activate
       ```

----------------------------------------------------------------------

## Install paystackease library:


* #### Install paystackease using pip.

> pip install paystackease

* #### Install paystackease using pipx.

> pipx install paystackease

* #### Install paystackease using poetry.

> poetry add paystackease


## If you want to download the sdist packages directly:

Download the wheel distribution file and install using pip

>  pip install paystackease-2.0.0-py3-none-any.whl 

Download the source distribution file, and install using pip

> pip install paystackease-2.0.0.tar.gz 


## To get a development version of paystackease

Clone from the ``dev`` branch GitHub repository, unzip and install:

> git clone -b dev https://github.com/cla-bit/PayStackEase.git

> cd PayStackEase

> pip install paystackease

----------------------------------------------------------------------

## API usage

-------------------------------------------------------

### Making a Transaction [Synchronous]

If after setting your secret key in environment variables, for a synchronous transaction process 
all you need to do is use the transaction API to make a transaction. 

To create a transaction or initialize a transaction:

* import the Paystack API wrapper.

```apacheconf
    from paystackease import PayStackBase
```

* Create an instance to use the PaystackBase wrapper to interact with the Transaction API.

```apacheconf
    paystack_client = PayStackBase()
```

* Use the instance and call the transaction method to initialize a transaction

```apacheconf
    create_transaction = paystack_client.transactions.initialize(
        email="johndoe@email.com",
        amount=10000000)
    
    print(f"Transaction Created: {create_transaction}")
```

> ✅: **Good**: You can check your Paystack account, go to the Transaction page, and you will see the transaction just created.


# Other Tools
Similar to calling the PayStackBase, you can also call other tools to make your work easy. For example:

* ### Account Type
```apacheconf
    from paystackease import AccountType
    
    val1 = AccountType.PERSONAL.value
    
    print(val1)
```
> "personal"

* ### Convert units to subunits:
```apacheconf
    from paystackease import convert_to_subunit
    
    # amount should be in subunit in this case 10000 kobo = 100 naira
    money = convert_to_subunit(100, Currency.NGN)
    print(money)
```
> 10000

* ### Channels
```apacheconf
    from paystackease import Channels
    
    bank = Channels.BANK.value
    
    print(bank)
```
> "bank"

* ### Currency
```apacheconf
    from paystackease import Currency
    
    val1 = Currency.NGN.value
    
    print(val1)
```
> "NGN"

* ### Document Type
```apacheconf
    from paystackease import DocumentType
    
    val1 = DocumentType.IDENTITY_NUMBER.value
    
    print(val1)
```

> "identityNumber"

Others are: ***EventType, Interval, MobileMoney, PWT, QRCODE, RecipientType, ResendOTP, Resolution, RiskAction, SplitType, STATUS, etc***.
