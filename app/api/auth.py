from flask import Blueprint, Response, current_app
from app.utils.response_utils import error_response, success_response
from app.utils.jwt_utils import generate_jwt_token
from flask import request
import jwt

auth = Blueprint("auth", __name__)

@auth.route("/user", methods=["GET"])
def get_user_info():
  # type: () -> Response
  token = request.cookies.get("token")
  print("What is happening",token)
  if not token:
    return error_response("Unauthorized", 401)
  
  try:
    decoded_token = jwt.decode(token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
    print("This is decoded token", decoded_token)
    return success_response(decoded_token)
  except jwt.ExpiredSignatureError:
    return error_response("Token has expired please reauthenticate", 401)
  except jwt.InvalidTokenError:
    return error_response("Invalid token", 401)