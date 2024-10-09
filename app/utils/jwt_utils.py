from typing import Dict, Any
import jwt
import logging
from flask import current_app

log = logging.getLogger(__name__)
def generate_jwt_token(payload):
  # type: (Dict[str, Any]) -> str
  try:
    jwt_token = jwt.encode(payload, current_app.config["JWT_SECRET_KEY"] , algorithm="HS256")
    return jwt_token
  except Exception as e:
    log.error("An error occurred while generating JWT token", str(e))
    raise