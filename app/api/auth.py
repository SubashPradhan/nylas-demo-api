from flask import Blueprint, Response, current_app
from app.utils.response_utils import error_response, success_response
from app.utils.jwt_utils import generate_jwt_token
from app.api import verify_user_and_token
from typing import Dict, Any, Union
auth = Blueprint("auth", __name__)

@auth.route("/user", methods=["GET"])
@verify_user_and_token
def get_user_info(decoded_token):
  # type: (Union[Dict[str,Any], None]) -> Response
  if decoded_token:
    return success_response(decoded_token)
  else:
    return error_response("Invalid token", 401)