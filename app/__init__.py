from flask import Flask
from app.api.health import health

app = Flask(__name__)

app.register_blueprint(health, url_prefix="/health")
