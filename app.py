from flask import Flask
from blueprints.weather_endp import weather_bp

app = Flask(__name__)

# Blueprints
app.register_blueprint(weather_bp)