# Nelsius Python SDK

Official Python SDK for the [Nelsius Developer API](https://nelsius.com/api-doc).

## Installation

```bash
pip install nelsius-pay
```

## Quick Start

```python
from nelsius import Nelsius

# Initialize the client
nelsius = Nelsius('your_secret_key', {
    'verify_ssl': False  # Set to False for local development
})

# 1. Get available payment methods
methods = nelsius.methods('CM', 'XAF')
print("Available methods:", methods)

# 2. Create a Checkout Session
session = nelsius.checkout.create_session({
    'amount': 5000,
    'currency': 'XAF',
    'reference': 'ORDER_12345',
    'return_url': 'https://yoursite.com/success',
    'customer': {
        'email': 'client@example.com',
        'name': 'Jean Dupont'
    }
})

if session.get('success'):
    print("Checkout URL:", session['data']['checkout_url'])

# 3. Direct Charge (Mobile Money)
charge = nelsius.charge.create({
    'amount': 2000,
    'currency': 'XAF',
    'payment_method': 'orange_money_cm',
    'phone': '690000000',
    'reference': 'REF_999'
})
print("Charge Result:", charge)
```

## Documentation

For full details on the parameters and responses, visit the [official documentation](https://nelsius.com/docs).
