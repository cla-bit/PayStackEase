# Apple Pay

### The Apple Pay API allows you register your application's top-level domain or subdomain.

#### This API wrapper imlements both the Asynchronous and Synchronous requests

*Reference: https://paystack.com/docs/api/apple-pay/*
________________________________

>  Ensure you have set your environment variable: ***PAYSTACK_SECRET_KEY*** as this is meant to be hidden.
> 
> or you can include it directly in the secret_key parameter.
>   ```
>       PayStackBase(secret_key="your-secret-key-here")
>       AsynPayStackBase(secret_key="your-secret-key-here")
>   ```

You can call the PayStackBase API wrapper or the AsyncPayStackBase API wrapper 
for synchronous and asynchronous requests to the API respectively, 
depending on your choice if you want to implement synchronous or 
asynchronous requests in your project.

In using the Asynchronous API request wrapper, ensure you import **asyncio** library as well.

```apacheconf
    import asyncio
    from paystackease import PayStackBase, AsyncPayStackBase
```


ASYNCHRONOUS SUPPORT : *AsyncPayStackBase*
================================================
----------------------------------------------------------------

* ## Register Domain
Register a top-level domain or subdomain for your Apple Pay integration.

```apacheconf
    async def main():
        # Implementing all the API endpoints
        async with AsyncPayStackBase() as paystack_client:
            # access the API endpoints making a Post request
            register_domain = await paystack_client.apple_pay.register_domain(domain_name="example")
            print(f"Register domain: {register_domain}")

    asyncio.run(main())
```

* ## List Domains
Lists all registered domains on your integration. Returns an empty array if no domains have been added.
```apacheconf
    async def main():
        # Implementing all the API endpoints
        async with AsyncPayStackBase() as paystack_client:
            # access the API endpoints making a Get request
            list_domains = await paystack_client.apple_pay.list_domains()
            print(f"List all domains: {list_domains}")

    asyncio.run(main())
```

* ## Unregister Domains
Unregister a top-level domain or subdomain previously used for your Apple Pay integration.
```apacheconf
    async def main():
        # Implementing all the API endpoints
        async with AsyncPayStackBase() as paystack_client:
            # # access the API endpoints making a Delete request
            unregister_domain = await paystack_client.apple_pay.unregister_domain(domain_name="example")

    asyncio.run(main())
```


SYNCHRONOUS SUPPORT : *PayStackBase*
================================================
----------------------------------------------------------------

* ## Register Domain
Register a top-level domain or subdomain for your Apple Pay integration.

```apacheconf
    def main():
        paystack_client = PayStackBase()
        # Implementing all the API endpoints """
        # access the API endpoints making a Post request
        register_domain = paystack_client.apple_pay.register_domain(domain_name="example")
        print(f"Register domain: {register_domain}")
    
    if __name__ == "__main__":
        main()
```

* ## List Domains
Lists all registered domains on your integration. Returns an empty array if no domains have been added.
```apacheconf
    def main():
        paystack_client = PayStackBase()
        # Implementing all the API endpoints """
        # access the API endpoints making a Get request
        list_domains = paystack_client.apple_pay.list_domains()
        print(f"List all domains: {list_domains}")
    
    if __name__ == "__main__":
        main()
```

* ## Unregister Domains
Unregister a top-level domain or subdomain previously used for your Apple Pay integration.
```apacheconf
    def main():
        paystack_client = PayStackBase()
        # Implementing all the API endpoints """
        # access the API endpoints making a Delete request
        unregister_domain = paystack_client.apple_pay.unregister_domain(domain_name="example")
        print(f"Unregister domain: {unregister_domain}")
    
    if __name__ == "__main__":
        main()
```

