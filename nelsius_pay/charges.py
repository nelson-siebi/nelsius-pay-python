from typing import Optional, Dict, Any


class ChargeManager:
    def __init__(self, client):
        self.client = client

    def direct_pay(
        self,
        amount: float,
        operator: str,
        phone: str,
        currency: str = "XAF",
        customer_name: Optional[str] = None,
        customer_email: Optional[str] = None,
        reference: Optional[str] = None,
        return_url: Optional[str] = None,
        cancel_url: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Déclenche un débit Mobile Money direct serveur-à-serveur avec prompt USSD sur le téléphone du client.
        """
        payload = {
            "amount": amount,
            "currency": currency.upper(),
            "operator": operator,
            "phone": phone,
        }
        if customer_name:
            payload["name"] = customer_name
        if customer_email:
            payload["email"] = customer_email
        if reference:
            payload["reference"] = reference
        if return_url:
            payload["return_url"] = return_url
        if cancel_url:
            payload["cancel_url"] = cancel_url
        if metadata:
            payload["metadata"] = metadata

        return self.client.request("POST", "/payments/charge", data=payload)

