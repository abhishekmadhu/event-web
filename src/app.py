from flask import Flask
from flask import Blueprint, request, render_template
from src.models.events.views import event_blueprint
from src.common.database import Database

__author__ = "abhishekmadhu"

app = Flask(__name__)

app.config.from_object('config')
app.secret_key = "abhishek"


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/')  # www.myweb.com/api/login
def home_template():
    return render_template('home.html')


app.register_blueprint(event_blueprint, url_prefix="/events")
if __name__ == "__main__":
    app.run()
