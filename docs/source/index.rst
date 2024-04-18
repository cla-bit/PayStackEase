.. PayStackEase documentation master file, created by
   sphinx-quickstart on Tue Mar 19 19:42:35 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


==================================================
PayStackEase: Simplified Paystack Integration.
==================================================

**PayStackEase** is a Python library that simplifies interacting with the Paystack API.
It provides both asynchronous and synchronous wrappers for various Paystack functionalities,
making it easier to integrate payment processing into your Python projects.

Paystackease utilizes **requests** and **aiohttp** libraries to make http requests and receives a **PayStackPayStackResponse** object from te server.

-----------------------------

**Prerequisites**

Before you get started with **paystackease** library, ensure you have the following requirements:

* Python 3.9+
* A paystack account: This is to generate the secret key. Click here to create a paystack account: `Paystack Create Account`_


.. _Paystack Create Account: https://paystack.com

--------------

**Target Audience**

This library is intended for developers familiar with Python and the Paystack API
and want to implement payment process using Paystack gateway in their python projects.

---------------

**Getting Started**

**paystackease** is on *PYPI* platform.
See how to install paystackease python library: :doc:`usage`

* Install using pip:

.. code-block:: bash

    $ pip install paystackease


* Install using pipx:

.. code-block:: bash

    $ pipx install paystackease

* Install using poetry:

.. code-block:: bash

    $ poetry add paystackease

If you want to download the sdist packages directly:

* Built Distribution file (.whl files) i.e the wheel file:

   .. code-block:: console

      >>> pip install paystackease-1.0.0-py3-none-any.whl

* Source Distribution file (.tar.gz files):

   .. code-block:: console

      >>> pip install paystackease-1.0.0.tar.gz

   .. note::

      It is recommended to install the wheels package (.whl)

* Detailed usage guide: https://paystackease.readthedocs.io/en/latest/
* Official Paystack Documentation: https://paystack.com/docs/api
* Contributing guidelines: https://github.com/cla-bit/PayStackEase/blob/master/CONTRIBUTING.md


======================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   usage
   submodules
   paystackease.apis
   paystackease.async_apis
   paystackease.helpers
   errors
   changelog
   howto

Indices and tables
==================

* :ref:`modindex`
* :ref:`search`
