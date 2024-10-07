from app.adaptors.nylas import Nylas
from flask import g, current_app

def get_nylas_client():
  if "nylas_adaptor" not in g:
    g.nylas_adaptor = Nylas(current_app.config["NYLAS_API_KEY"])
  return g.nylas_adaptor