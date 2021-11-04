from rest_framework.response import Response
from rest_framework.views import exception_handler

from constants.error_enum import ErrorEnum as Err


def custom_exception_handler(exc, content) -> Response:
    handlers = {
        "JwtException": _jwt_validate_error
    }
    response = exception_handler(exc, content)
    exc_class = exc.__class__.__name__

    if exc_class in handlers:
        return handlers[exc_class](exc, content)
    return response


def _jwt_validate_error(exc, content) -> Response:
    return Response(Err.jwt_error.msg, Err.jwt_error.code)
