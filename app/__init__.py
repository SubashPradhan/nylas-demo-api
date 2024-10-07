from flask import Flask
from app.api.health import health
from app.config import BaseConfig
from app.api.nylas import nylas

app = Flask(__name__)

app.config.from_object(BaseConfig)
config = app.config

app.register_blueprint(health, url_prefix="/health")
app.register_blueprint(nylas, url_prefix="/nylas")
