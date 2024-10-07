from flask import Blueprint, redirect
from app.utils.adaptor_utils import get_nylas_client
from app.utils.response_utils import error_response
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