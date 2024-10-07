from flask import Flask
from app.api.health import health
from app.config import BaseConfig

app = Flask(__name__)

app.config.from_object(BaseConfig)
config = app.config

print(app.config)

app.register_blueprint(health, url_prefix="/health")
