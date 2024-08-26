from flask import Flask, jsonify
from src.middleware import logger_middleware, error_handler_middleware
from src.config import AppConfig
from injector import inject, singleton

@singleton
class FlaskController:
    @inject
    def __init__(self, config: AppConfig):
        self.app = Flask(__name__)
        self.config = config

    def setup_routes(self):
        @self.app.route("/health", methods=["GET"])
        def say_hello():
            return jsonify({"message": "Hello from Flask"})

    def setup_middlewares(self):
        self.app.before_request(logger_middleware)
        self.app.register_error_handler(Exception, error_handler_middleware)

    def get_app(self):
        self.setup_routes()
        self.setup_middlewares()
        return self.app
