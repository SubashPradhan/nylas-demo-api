from app.adaptors.adaptor import Adaptor
from flask import current_app, Response
from typing import Union
from app.utils.response_utils import error_response
import requests
import logging

log = logging.getLogger(__name__)
class Nylas(Adaptor):
  def __init__(self, api_key):
    # type: (str) -> None
    super().__init__(api_key)
    self.base_url = current_app.config["NYLAS_BASE_URL"]
    self.api_key = current_app.config["NYLAS_API_KEY"]
    self.client_id = current_app.config["NYLAS_CLIENT_ID"]
    self.redirect_uri = current_app.config["NYLAS_REDIRECT_URI"]
    self.headers = {
      "content_type": "application/json",
      "Authorization": "Bearer {}".format(self.api_key)
    }

  def generate_authentication_url(self):
    # type: () -> Union[str, Response]
    """
    Nylas hosted authentication docs: https://developer.nylas.com/docs/api/v3/admin/#get-/v3/connect/auth
    """
    try:
      authentication_params = {
        "client_id": self.client_id,
        "redirect_uri": self.redirect_uri,
        "response_type": "code"
      }
      authentication_url = f"{self.base_url}/connect/auth"
      response = requests.get(authentication_url, authentication_params)
      return response.url
    except Exception as e:
      return error_response(str(e), 503)
    
  def exchange_code_for_token(self, code):
    """
    Nylas Token exchange: https://developer.nylas.com/docs/v3/auth/hosted-oauth-accesstoken/#exchange-code-for-access-token
    """
    # type: (str) -> Union[Dict[str, Any], Response]
    try:
      code_exchange_url = f"{self.base_url}/connect/token"
      payload = {
        "client_id": self.client_id,
        "client_secret": self.api_key,
        "redirect_uri": self.redirect_uri,
        "grant_type": "authorization_code",
        "code": code
      }
      response = requests.post(code_exchange_url, json=payload)
      result = response.json()
      return result
    except Exception as e:
      return error_response("An error occurred during authentication", status_code=503, errors=str(e))
    
  def get_threads_by_grant_id(self, grant_id):
    """
    Nylas threads endpoint: https://developer.nylas.com/docs/api/v3/ecc/#get-/v3/grants/-grant_id-/threads
    """
    # type: (str) -> Union[Dict[str, Any], Response]
    try:
      threads_url = f"{self.base_url}/grants/{grant_id}/threads?limit=20"
      response = requests.get(threads_url, headers=self.headers)
      return response.json()
    except Exception as e:
      log.error("An error occurred while fetching threads", str(e))
      return error_response("An error occurred while fetching threads using Nylas API", 503, errors=str(e))