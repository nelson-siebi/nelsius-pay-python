from typing import Optional, Dict, Any, List


class CheckoutManager:
    def __init__(self, client):
        self.client = client

    def create_session(
        self,
        amount: float,
        currency: str = "XAF",
        reference: Optional[str] = None,
        customer_email: Optional[str] = None,
        customer_phone: Optional[str] = None,
        customer_name: Optional[str] = None,
        default_country: str = "CM",
        allowed_countries: Optional[List[str]] = None,
        return_url: Optional[str] = None,
        cancel_url: Optional[str] = None,
        description: Optional[str] = None,
        fee_bearer: str = "merchant",
        payment_methods: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Crée une session de paiement hébergée (Hosted Checkout).
        """
        payload = {
            "amount": amount,
            "currency": currency.upper(),
            "default_country": default_country.upper(),
            "fee_bearer": fee_bearer,
        }
        if reference:
            payload["reference"] = reference
        if customer_email:
            payload["customer_email"] = customer_email
        if customer_phone:
            payload["customer_phone"] = customer_phone
        if customer_name:
            payload["customer_name"] = customer_name
        if allowed_countries:
            payload["allowed_countries"] = allowed_countries
        if return_url:
            payload["return_url"] = return_url
        if cancel_url:
            payload["cancel_url"] = cancel_url
        if description:
            payload["description"] = description
        if payment_methods:
            payload["payment_methods"] = payment_methods
        if metadata:
            payload["metadata"] = metadata

        return self.client.request("POST", "/checkout/initiate", data=payload)

    def get_session(self, session_id: str) -> Dict[str, Any]:
        """
        Récupère les détails d'une session de paiement par son code de transaction.
        """
        return self.client.request("GET", f"/checkout/{session_id}")

    def check_status(self, session_id: str) -> Dict[str, Any]:
        """
        Vérifie le statut en temps réel d'une transaction.
        """
        return self.client.request("GET", f"/checkout/{session_id}/status")

