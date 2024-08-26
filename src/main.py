from src.interface import FrameworkType
from src.framework_injections import create_injector
from src.config import AppConfig
from src.controllers import FastAPIController, FlaskController

#
# class ENBDLeapApp:
#     def __init__(self, framework_type: FrameworkType, controllers_path=None):
#         self.framework_type = framework_type
#         self.injector = create_injector(framework_type)
#         self.app_config = self.injector.get(AppConfig)
#         self.controllers_path = controllers_path
#
#     def load_controllers(self, app):
#         if self.controllers_path and os.path.isdir(self.controllers_path):
#             for filename in os.listdir(self.controllers_path):
#                 if filename.endswith(".py") and not filename.startswith("__"):
#                     module_name = filename[:-3]
#                     file_path = os.path.join(self.controllers_path, filename)
#                     spec = importlib.util.spec_from_file_location(module_name, file_path)
#                     module = importlib.util.module_from_spec(spec)
#                     spec.loader.exec_module(module)
#
#                     if hasattr(module, 'register_routes'):
#                         module.register_routes(app)
# def create_app(self):
#     if self.framework_type == FrameworkType.FASTAPI:
#         app = FastAPI(debug=self.app_config.DEBUG, title=self.app_config.APP_NAME)
#     elif self.framework_type == FrameworkType.FLASK:
#         app = Flask(__name__)
#     else:
#         raise ValueError(f"Unsupported framework type: {self.framework_type}")
#
#     if self.controllers_path:
#         self.load_controllers(app)
#
#     return app
#
#
# def run(self):
#     app = self.create_app()
#
#     if self.framework_type == FrameworkType.FASTAPI:
#         import uvicorn
#         uvicorn.run(app, host=self.app_config.HOST, port=self.app_config.PORT)
#     elif self.framework_type == FrameworkType.FLASK:
#         app.run(host=self.app_config.HOST, port=self.app_config.PORT)


def create_app(injector, framework_type: FrameworkType):
    if framework_type == FrameworkType.FASTAPI:
        controller = injector.get(FastAPIController)
    elif framework_type == FrameworkType.FLASK:
        controller = injector.get(FlaskController)
    else:
        raise ValueError(f"Unsupported framework type: {framework_type}")

    return controller.get_app()

def main():
    config = AppConfig()
    framework_type = FrameworkType.FLASK  # Change to FrameworkType.FLASK if needed
    injector = create_injector(framework_type)
    app = create_app(injector, framework_type)

    if framework_type == FrameworkType.FASTAPI:
        import uvicorn
        uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT)
    elif framework_type == FrameworkType.FLASK:
        app.run(host=config.APP_HOST, port=config.APP_PORT)

if __name__ == "__main__":
    main()



#************* Usage in Container Level (Testing Needed)**************#

# from enbdleap_python_core import ENBDLeapApp, FrameworkType

# controllers_path = "/path/to/your/controllers"
#
# app = ENBDLeapApp(framework_type=FrameworkType.FASTAPI, controllers_path=controllers_path)
#
# app.run()

#************* #  Controller Initialization from Microservice (Testing Needed)**************#

# from enbdleap_python_core import APIRouter
#
# router = APIRouter()
#
# @router.get("/controller2")
# async def handle_controller2():
#     return {"message": "Hello from Controller 2"}
#
# def register_routes(app):
#     app.include_router(router)

#************* #  Controller Initialization from Microservice (Testing Needed)**************#

# from enbdleap_python_core import Flask
#
# def register_routes(app: Flask):
#     @app.route("/controller1", methods=["GET"])
#     def handle_controller1():
#         return {"message": "Hello from Flask Controller 1"}
