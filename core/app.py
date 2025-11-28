from model.model import Model
from api.sportsdata_api import SportsDataAPI
from controller.controller import Controller

class App:
    def __init__(self):
        self.model = Model()
        self.api_client = SportsDataAPI()
        self.controller = Controller(self.model, self.api_client)