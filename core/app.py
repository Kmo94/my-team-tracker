from model.model import Model
from api.sportsdata_api import SportsDataAPI
from controller.controller import Controller


class App: 
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(App, cls).__new__(cls)
            cls.__instance._initialize()
        
        return cls.__instance
    
    def _initialize(self):
        self.api_client = SportsDataAPI()
        self.model = Model()
        self.controller = Controller(self.model, self.api_client)
    
    def run(self):
        self.controller.login_flow()
        self.controller.main_loop()