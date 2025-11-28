from view.view import View

class Controller:
    def __init__(self, model, api_client):
        self.model = model
        self.api_client = api_client
        self.current_user = None