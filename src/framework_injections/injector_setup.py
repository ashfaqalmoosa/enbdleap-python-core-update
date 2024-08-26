from injector import Injector, Module, singleton
from src.config import AppConfig
from src.interface import FrameworkType
from src.controllers import FastAPIController, FlaskController

class AppModule(Module):
    def configure(self, binder):
        binder.bind(AppConfig, to=AppConfig, scope=singleton)
        binder.bind(FrameworkType, to=FrameworkType.FASTAPI, scope=singleton)

def create_injector(framework_type: FrameworkType):
    return Injector([AppModule()])
