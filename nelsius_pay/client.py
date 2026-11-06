import requests
from typing import Optional, Dict, Any
from .checkout import CheckoutManager
from .charges import ChargeManager
from .webhooks import WebhookManager
from .exceptions import NelsiusApiError


class NelsiusClient:
    """
    Client principal pour interagir avec l'API NelsiusPay V2.
    """
    BASE_URL = "https://api.nelsiuspay.com/api/v1"

    def __init__(
        self,
        api_key: str,
        secret_key: Optional[str] = None,
        base_url: Optional[str] = None,
        mode: str = "live"
    ):
        self.api_key = api_key
        self.secret_key = secret_key
        self.mode = mode.lower()
        self.base_url = (base_url or self.BASE_URL).rstrip("/")

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "NelsiusPay-Python-SDK/2.0.0",
        })

        self.checkout = CheckoutManager(self)
        self.charges = ChargeManager(self)
        self.webhooks = WebhookManager(self.secret_key)

    def request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.request(method=method, url=url, json=data, params=params, timeout=30)
            json_resp = response.json() if response.content else {}
            if not response.ok:
                msg = json_resp.get("message") or json_resp.get("error") or f"HTTP {response.status_code}"
                raise NelsiusApiError(msg, status_code=response.status_code, response_data=json_resp)
            return json_resp
        except requests.RequestException as e:
            raise NelsiusApiError(f"Network error: {str(e)}")

