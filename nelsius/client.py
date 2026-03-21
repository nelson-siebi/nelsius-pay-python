import requests
from .managers.checkout import CheckoutManager
from .managers.charge import ChargeManager
from .managers.balance import BalanceManager

class Nelsius:
    """
    Nelsius Pay Python SDK Client
    """
    def __init__(self, secret_key, options=None):
        self.secret_key = secret_key
        self.options = options or {}
        self.base_url = self.options.get('base_url', 'https://api.nelsius.com')
        self.verify_ssl = self.options.get('verify_ssl', True)
        
        # Initialize Managers
        self.checkout = CheckoutManager(self)
        self.charge = ChargeManager(self)
        self.balance = BalanceManager(self)

    def request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        headers = {
            'Authorization': f'Bearer {self.secret_key}',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-SDK-Platform': 'python'
        }
        
        try:
            response = requests.request(
                method=method,
                url=url,
                json=data,
                params=params,
                headers=headers,
                verify=self.verify_ssl
            )
            
            # Simple error handling (matching Node.js/PHP behavior)
            return response.json()
            
        except requests.exceptions.RequestException as e:
            return {
                'success': False,
                'message': f'Request failed: {str(e)}',
                'error': str(e)
            }

    def methods(self, country=None, currency=None):
        """
        Get available payment methods
        """
        params = {}
        if country:
            params['country'] = country
        if currency:
            params['currency'] = currency
            
        return self.request('GET', '/api/v1/payment-methods', params=params)
