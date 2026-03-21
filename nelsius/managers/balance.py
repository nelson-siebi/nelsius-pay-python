class BalanceManager:
    def __init__(self, client):
        self.client = client

    def retrieve(self):
        """
        Get merchant balance
        """
        return self.client.request('GET', '/api/v1/balance')
