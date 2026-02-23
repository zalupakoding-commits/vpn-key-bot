# CryptoBot API Integration

This script integrates the CryptoBot API for handling cryptocurrency payments.

## Features
- Initiate cryptocurrency payments
- Monitor payment confirmations
- Handle API responses

## Usage
```python
import requests

API_URL = 'https://api.cryptobot.com/payment'

def create_payment(amount, currency):
    payload = {"amount": amount, "currency": currency}
    response = requests.post(API_URL, json=payload)
    return response.json()

if __name__ == '__main__':
    # Example usage
    payment_info = create_payment(100, 'BTC')
    print(payment_info)  
```