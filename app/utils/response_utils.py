from typing import Any
from flask import Response, jsonify

def success_response(data=None, status_code=200):
  # type: (Any, int) -> Response
  response = jsonify({"status": "success", "data": data})
  response.status_code = status_code
  return response

def error_response(message="An unexpected error occurece. Please contact support", status_code=500, errors=None):
  # type: (str, int, Any) -> Response
  response = jsonify({"status": "error", "message": message, "errors": errors})
  response.status_code = status_code
  return response