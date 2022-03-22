from flask import Flask, render_template, redirect

from models.activity import Activity
from models.member import Member
from models.booking import Booking

from controllers.member_controller import members_blueprint
from controllers.activity_controller import activities_blueprint
from controllers.booking_controller import bookings_blueprint
from controllers.extras_controller import extras_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(activities_blueprint)
app.register_blueprint(bookings_blueprint)
app.register_blueprint(extras_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title='Home Page')


if __name__ == '__main__':
    app.run(debug=True)