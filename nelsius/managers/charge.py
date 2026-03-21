class ChargeManager:
    def __init__(self, client):
        self.client = client

    def create(self, data):
        """
        Initiate a direct charge (Mobile Money, etc.)
        """
        return self.client.request('POST', '/api/v1/charges', data=data)

    def retrieve(self, charge_id):
        """
        Retrieve a charge status
        """
        return self.client.request('GET', f'/api/v1/charges/{charge_id}')
