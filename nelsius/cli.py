import argparse
import sys
import json
from .client import Nelsius

def main():
    parser = argparse.ArgumentParser(description="Nelsius Pay CLI - Interface ligne de commande officielle")
    parser.add_argument('--key', help="Votre Secret Key (ou utilise la variable d'environnement NELSIUS_SECRET_KEY)")
    
    subparsers = parser.add_subparsers(dest='command', help='Commandes disponibles')

    # Commande Balance
    subparsers.add_parser('balance', help='Consulter votre solde')

    # Commande Methods
    method_parser = subparsers.add_parser('methods', help='Lister les méthodes de paiement')
    method_parser.add_argument('--country', default='CM', help='Code pays (ex: CM, CI)')
    method_parser.add_argument('--currency', default='XAF', help='Code devise (ex: XAF, XOF)')

    # Commande Checkout
    checkout_parser = subparsers.add_parser('checkout', help='Créer une session de paiement')
    checkout_parser.add_argument('--amount', type=int, required=True, help='Montant')
    checkout_parser.add_argument('--currency', default='XAF', help='Devise')
    checkout_parser.add_argument('--ref', required=True, help='Référence unique')

    args = parser.parse_args()

    # Récupération de la clé
    import os
    secret_key = args.key or os.environ.get('NELSIUS_SECRET_KEY')
    
    if not secret_key:
        print("Erreur: Clé secrète manquante. Utilisez --key ou positionnez la variable d'environement NELSIUS_SECRET_KEY.")
        sys.exit(1)

    client = Nelsius(secret_key)

    try:
        if args.command == 'balance':
            result = client.balance.retrieve()
            print(json.dumps(result, indent=2))
        
        elif args.command == 'methods':
            result = client.methods(args.country, args.currency)
            print(json.dumps(result, indent=2))
            
        elif args.command == 'checkout':
            result = client.checkout.create_session({
                'amount': args.amount,
                'currency': args.currency,
                'reference': args.ref,
                'return_url': 'https://example.com/success'
            })
            print(json.dumps(result, indent=2))
        else:
            parser.print_help()
            
    except Exception as e:
        print(f"Erreur lors de l'exécution : {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
