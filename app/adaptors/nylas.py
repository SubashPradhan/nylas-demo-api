from app.adaptors.adaptor import Adaptor
from flask import current_app

class Nylas(Adaptor):
  def __init__(self, api_key):
    # type: (str) -> None
    self.base_url = current_app.config["NYLAS_BASE_URL"]
    super().__init__(api_key)