from flask import Blueprint, redirect, make_response
from app.utils.adaptor_utils import get_nylas_client
from app.utils.response_utils import error_response, success_response
from app.utils.jwt_utils import generate_jwt_token
from flask import request
import datetime
import logging
from app.api import verify_user_and_token

log = logging.getLogger(__name__)

nylas = Blueprint("nylas", __name__)

@nylas.route("/connect", methods=["GET"])
def register_mailbox():
  # type: () -> None
  try:
    nylas_adaptor = get_nylas_client()
    authentication_request = nylas_adaptor.generate_authentication_url()
    authentication_url = {"redirect_url": authentication_request}
    return success_response(authentication_url)
  except Exception as e:
    return error_response("An error occurred while generating authentication url, please try again", status_code=503, errors=str(e))
  

@nylas.route("/callback", methods=["GET"])
def callback_uri():
  # type: () -> None
  try:
    code = request.args.get("code")
    nylas_adaptor = get_nylas_client()
    response = nylas_adaptor.exchange_code_for_token(code)
    grant_id = response.get("grant_id")
    email = response.get("email")
    payload = {
      "grant_id": grant_id,
      "email": email,
      "exp": datetime.datetime.now() + datetime.timedelta(hours=1)
    }
    token = generate_jwt_token(payload)
    frontend_url = "http://localhost:3000/nylas-demo"
    resp = make_response(redirect(frontend_url))
    resp.set_cookie("token", token, httponly=True, secure=False)
    return resp
  except Exception as e:
    log.error("Authentication failed during code exchange", str(e))
    return error_response("Authentication failed", status_code=503, errors=str(e))

@nylas.route("/threads", methods=["GET"])
@verify_user_and_token
def get_threads(decoded_token):
  try:
    next_cursor = request.args.get("next_cursor")
    folder = request.args.get("folder")
    grant_id = decoded_token.get("grant_id")
    nylas_adaptor = get_nylas_client()
    threads = nylas_adaptor.get_threads_by_grant_id(grant_id, next_cursor, folder)
    return success_response(threads)
  except Exception as e:
    log.error("Threads fetching failed", str(e))
    return error_response("Failed to fetch threads", 503, errors=str(e))


@nylas.route("/folders", methods=["GET"])
@verify_user_and_token
def get_folders(decoded_token):
  try:
    grant_id = decoded_token.get("grant_id")
    nylas_adaptor = get_nylas_client()
    folders = nylas_adaptor.get_folders_by_grant_id(grant_id)
    return success_response(folders)
  except Exception as e:
    log.error("Folders fetching failed", str(e))
    return error_response("Failed to fetch folders", 503, errors=str(e))

