# PayStackEase Library  ![paystackease](docs/images/paystackease.png)

Paystack is a technology company solving payments problems for ambitious businesses. 

This **PayStackEase API Library** consists of **Paystack API** asynchronous and synchronous wrappers, which can be integrated into python projects to interact with **Paystack**.

> 📝: Read more on paystack api: https://paystack.com/docs/api/


Getting Started
================================================================

You should create a Paystack account to generate a **Paystack Secret Key**. You can see this in the settings page >> API keys and Webhook section.

> ⚠️: **Warning:** Do not expose your secret key or commit your secret key to git, or use them in client-side code.

> 💡: **Take Note:**  Public key is to be used from your front-end when integrating using Paystack Inline. In this case you have to use you secret key

> ✅: **Good**: Set your secret key in environment variables as seen: *PAYSTACK_SECRET_KEY=your-secret-key*

# Install paystackease library:
* #### Install paystackease using pip.
> pip install paystackease

or Download the wheel distribution file and install using pip
>  pip install paystackease-0.1.2-py3-none-any.whl 

or Download the source distribution file, change directory and install using pip
> cd 
> 
> pip install paystackease-0.1.2.tar.gz 

or clone from the github repository:
> git clone https://github.com/cla-bit/PayStackEase.git

# Making a Transaction

If after setting your secret key in environment variables, all you need to do is use the transaction API to make a transaction. 
To make a transaction or initialize a transaction:

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

> ✅: **Good**: You can check your Paystack account, go to the Transaction page and you will see the transaction just created.


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

Others are: ***EventType, Interval, MobileMoney, PWT, QRCODE, RecipientType, ResendOTP, Resolution, RiskAction, SplitType, STATUS, and USSD***.
