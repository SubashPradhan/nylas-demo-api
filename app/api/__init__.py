import functools
from typing import Any, Callable, TypeVar, cast
from flask import request, current_app
from app.utils.response_utils import error_response, success_response
import jwt

Function = TypeVar("Function", bound=Callable[..., Any])

def verify_user_and_token(func):
    # type: (Function) -> Function
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        # type: (*Any, **Any) -> Any
        access_token = request.headers.get("Authorization")
        if not access_token or not access_token.startswith("Bearer "):
            return error_response("Access Token required", 401)

        access_token = access_token.split(" ")[1]
        try:
          decoded_token = jwt.decode(access_token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
          return func(decoded_token=decoded_token, *args, **kwargs)
        except jwt.ExpiredSignatureError:
          return error_response("Token has expired please reauthenticate", 401)
        except jwt.InvalidTokenError:
          return error_response("Invalid token", 401)

    return cast(Function, decorator)