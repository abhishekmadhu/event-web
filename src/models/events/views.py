from flask import Blueprint, request, render_template
from werkzeug.utils import redirect

__author__ = "abhishekmadhu"

event_blueprint = Blueprint('events', __name__)


@event_blueprint.route('/home', methods=['GET'])
def events_home():
    return render_template("home.html")


@event_blueprint.route('/new', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        # check if event is not already present by title
        pass

        # if not, add the event

    # render the page for that event
    return render_template('users/register.html')

    # try redirecting later on
    # return redirect(url_for(".events_home"))
