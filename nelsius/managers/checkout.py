class CheckoutManager:
    def __init__(self, client):
        self.client = client

    def create_session(self, data):
        """
        Create a hosted checkout session
        """
        return self.client.request('POST', '/api/v1/checkout/sessions', data=data)

    def retrieve(self, session_id):
        """
        Retrieve a checkout session status
        """
        return self.client.request('GET', f'/api/v1/checkout/sessions/{session_id}')
