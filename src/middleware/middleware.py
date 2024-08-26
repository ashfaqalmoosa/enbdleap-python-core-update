import logging
from starlette.middleware.base import BaseHTTPMiddleware
from flask import request, jsonify

# FastAPI middleware
class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger = logging.getLogger("LoggerMiddleware")
        logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code}")
        return response

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            logger = logging.getLogger("ErrorHandlerMiddleware")
            logger.error(f"An error occurred: {e}")
            return jsonify({"detail": "Internal Server Error"}), 500

# Flask middleware
def logger_middleware():
    logger = logging.getLogger("LoggerMiddleware")
    logger.info(f"Request: {request.method} {request.url}")

def error_handler_middleware(e):
    logger = logging.getLogger("ErrorHandlerMiddleware")
    logger.error(f"An error occurred: {e}")
    return jsonify({"detail": "Internal Server Error"}), 500
