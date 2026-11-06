import hmac
import hashlib
import json
from typing import Dict, Any, Union
from .exceptions import NelsiusWebhookError


class WebhookManager:
    def __init__(self, secret: str = None):
        self.secret = secret

    def verify_signature(
        self,
        payload: Union[str, bytes],
        signature_header: str,
        secret: str = None
    ) -> bool:
        """
        Vérifie la signature cryptographique HMAC-SHA256 du webhook NelsiusPay.
        """
        sec = secret or self.secret
        if not sec:
            raise NelsiusWebhookError("Webhook secret must be provided for verification.")

        if isinstance(payload, str):
            payload_bytes = payload.encode("utf-8")
        else:
            payload_bytes = payload

        expected = hmac.new(sec.encode("utf-8"), payload_bytes, hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, signature_header)

    def construct_event(
        self,
        payload: Union[str, bytes],
        signature_header: str,
        secret: str = None
    ) -> Dict[str, Any]:
        """
        Vérifie la signature et retourne le payload JSON décodé de l'événement.
        """
        if not self.verify_signature(payload, signature_header, secret):
            raise NelsiusWebhookError("Invalid webhook signature.")

        if isinstance(payload, bytes):
            payload = payload.decode("utf-8")

        return json.loads(payload)

