# NelsiusPay Python SDK (V2)

SDK officiel Python pour intégrer la passerelle de paiement **NelsiusPay** dans vos applications Django, Flask, FastAPI ou scripts automatisés.

## Installation

```bash
pip install nelsius-pay
```

## Initialisation

```python
from nelsius_pay import NelsiusClient

client = NelsiusClient(
    api_key="np_live_xxxxxxxxxxxxxxxx",
    secret_key="whsec_xxxxxxxxxxxxxxx"
)
```

## 1. Créer une session de paiement hébergée (Hosted Checkout)

```python
session = client.checkout.create_session(
    amount=5000,
    currency="XAF",
    reference="CMD-94812",
    customer_email="client@example.com",
    customer_phone="+237690000000",
    customer_name="Jean Dupont",
    default_country="CM",  # Cameroun par défaut (ou CI, SN, BJ...)
    return_url="https://monsite.com/commande/succes",
    cancel_url="https://monsite.com/commande/annulee",
    description="Abonnement mensuel Pro"
)

# Redirigez votre client vers l'URL sécurisée :
print(session["data"]["checkout_url"])
```

## 2. Débit direct Mobile Money (Server-to-Server USSD)

```python
charge = client.charges.direct_pay(
    amount=2500,
    currency="XAF",
    operator="orange",  # ou mtn
    phone="699000000",
    customer_name="Alice Ngo",
    reference="REF-8849"
)

print(charge["message"])  # Prompt USSD envoyé sur le téléphone du client
```

## 3. Vérifier un webhook sécurisé HMAC-SHA256

```python
@app.route("/webhooks/nelsius", methods=["POST"])
def nelsius_webhook():
    payload = request.get_data()
    signature = request.headers.get("X-Nelsius-Signature")
    
    try:
        event = client.webhooks.construct_event(payload, signature)
        if event["event"] == "payment.success":
            tx = event["data"]
            print(f"Paiement validé : {tx['amount']} {tx['currency']}")
        return {"status": "ok"}, 200
    except Exception as e:
        return {"error": str(e)}, 400
```

