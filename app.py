from flask import Flask
from blueprints.weather_endp import weather_bp

app = Flask(__name__)

app.register_blueprint(weather_bp)