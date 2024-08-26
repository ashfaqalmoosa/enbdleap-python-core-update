from fastapi import FastAPI, APIRouter
from src.middleware import LoggerMiddleware, ErrorHandlerMiddleware
from src.config import AppConfig
from injector import inject, singleton

@singleton
class FastAPIController:
    @inject
    def __init__(self, config: AppConfig):
        self.app = FastAPI(debug=config.APP_DEBUG, title=config.APP_NAME)
        self.router = APIRouter()

    def setup_routes(self):
        @self.router.get("/health")
        async def say_hello():
            return {"message": "Hello from FastAPI"}

        self.app.include_router(self.router)

    def setup_middlewares(self):
        self.app.add_middleware(LoggerMiddleware)
        self.app.add_middleware(ErrorHandlerMiddleware)

    def get_app(self):
        self.setup_routes()
        self.setup_middlewares()
        return self.app
