from flask import Blueprint, redirect
from app.utils.adaptor_utils import get_nylas_client
from app.utils.response_utils import error_response, success_response
from flask import request
import logging
log = logging.getLogger(__name__)

nylas = Blueprint("nylas", __name__)

@nylas.route("/connect", methods=["GET"])
def register_mailbox():
  # type: () -> None
  try:
    nylas_adaptor = get_nylas_client()
    authentication_request = nylas_adaptor.generate_authentication_url()
    return redirect(authentication_request)
  except Exception as e:
    return error_response("An error occurred while generating authentication url, please try again", status_code=503, errors=str(e))
  

@nylas.route("callback", methods=["GET"])
def callback_uri():
  # type: () -> None
  try:
    code = request.args.get("code")
    nylas_adaptor = get_nylas_client()
    response = nylas_adaptor.exchange_code_for_token(code)
    log.info("Authentication successfull")
    return success_response(response)  # TODO: this should redirect to frontend, we should have way to store the grant ID.
  except Exception as e:
    log.error("Authentication failed during code exchange", str(e))
    return error_response("Authentication failed", status_code=503, errors=str(e))


