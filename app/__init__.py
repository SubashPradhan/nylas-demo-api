from flask import Flask
from app.api.health import health
from app.config import BaseConfig
from app.api.nylas import nylas
from app.api.auth import auth
import logging

app = Flask(__name__)

app.config.from_object(BaseConfig)
config = app.config

logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s %(message)s',
  datefmt='%m/%d/%Y %I:%M:%S %p'
)

app.register_blueprint(health, url_prefix="/health")
app.register_blueprint(nylas, url_prefix="/nylas")
app.register_blueprint(auth, url_prefix="/auth")
