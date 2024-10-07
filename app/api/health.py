from flask import Blueprint, Response
from app.utils.response_utils import success_response
health = Blueprint("health", __name__)

@health.route("/", methods=["GET"])
def health_check():
  # type: () -> Response
  return success_response()