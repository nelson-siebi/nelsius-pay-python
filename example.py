import os
import sys

# Add current directory to path so we can import 'nelsius' without installing
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from nelsius import Nelsius

# Configuration
SECRET_KEY = "sk_test_..." # Remplacez par votre clé réelle
BASE_URL = "https://api.nelsius.com" # Utilise le backend en ligne par défaut

client = Nelsius(SECRET_KEY, {
    'base_url': BASE_URL,
    # 'verify_ssl': False # Désactivez uniquement pour le test en local
})

def run_tests():
    print("--- Testing Payment Methods ---")
    methods = client.methods('CM')
    print(methods)

    print("\n--- Testing Checkout Session ---")
    session = client.checkout.create_session({
        'amount': 3500,
        'currency': 'XAF',
        'reference': 'PY_TEST_1',
        'return_url': 'http://localhost/success',
        'customer': {
            'email': 'python@test.com',
            'name': 'Python User'
        }
    })
    print(session)

    print("\n--- Testing Merchant Balance ---")
    balance = client.balance.retrieve()
    print(balance)

if __name__ == "__main__":
    run_tests()
