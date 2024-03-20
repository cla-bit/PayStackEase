.. PayStackEase documentation master file, created by
   sphinx-quickstart on Tue Mar 19 19:42:35 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   usage
   submodules
   paystackease.apis
   paystackease.async_apis
   paystackease.helpers
   errors
   changelog
   howto

==================================================
PayStackEase: Simplified Paystack Integration.
==================================================

**PayStackEase** is a Python library that simplifies interacting with the Paystack API.
It provides both asynchronous and synchronous wrappers for various Paystack functionalities,
making it easier to integrate payment processing into your Python projects.



-------------------
Prerequisites
-------------------

Before you get started with **paystackease** library, ensure you have the following requirements:

* Python 3.9+
* A paystack account: This is to generate the secret key. Click here to create a paystack account: `Paystack Create Account`_


.. _Paystack Create Account: https://paystack.com

---------------------
Target Audience
---------------------

This library is intended for developers familiar with Python and the Paystack API.

**Getting Started**

As at the writing of this documentation, paystackease is still on *TestPYPI* platform, as it is still under tests for best performance.
You can get started by downloading any of the source files here: https://test.pypi.org/project/paystackease/#files

* Install using pip:
   * Built Distribution file (.whl files) i.e the wheel file:

      .. code-block:: console

         >>> pip install paystackease-0.1.2-py3-none-any.whl

   * Source Distribution file (.tar.gz files):

      .. code-block:: console

         >>> pip install paystackease-0.1.2.tar.gz

   .. note::

      It is recommended to install the wheels package (.whl)

* Detailed usage guide: https://paystackease.readthedocs.io/en/latest/
* Official Paystack Documentation: https://paystack.com/docs/api
* Contributing guidelines: https://github.com/cla-bit/PayStackEase/blob/master/CONTRIBUTING.md

----------------------------------------------------------------------

Indices and tables
==================

* :ref:`modindex`
* :ref:`search`
