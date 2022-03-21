from flask import Flask, render_template, redirect

from models.activity import Activity
from models.member import Member
from models.booking import Booking

from controllers.member_controller import members_blueprint
from controllers.activity_controller import activities_blueprint
from controllers.booking_controller import bookings_blueprint

import repositories.activity_repository as activity_repository
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(activities_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title='Home Page')

@app.route('/site-map')
def site_map():
    return render_template('site_map.html', title='Sitemap')

@app.route('/what_have_you_done')
def what_have_you_done():
    return render_template('what_have_you_done.html', title='What Have You Done?')

@app.route('/seeded_database')
def seeded_the_database():
    return render_template('seeded_database.html', title='You Have Successfully Seeded the Database')

@app.route('/time_to_dance')
def time_to_dance():
    return render_template('time_to_dance.html', title='Time to Dance!')


# Function to delete absolutely everything
@app.route("/delete-everything" , methods = ['POST'])
def delete_everything():
    booking_repository.delete_all()
    activity_repository.delete_all()
    member_repository.delete_all()
    return redirect ('/what_have_you_done')

@app.route('/seed_database')
def seed_database():
    member_1 = Member("Peter La Fleur", "True", "False")
    member_repository.create_member(member_1)
    member_2 = Member("Arnold Schwarzenegger","False", "True")
    member_repository.create_member(member_2)
    member_3 = Member("Ronnie Coleman", "False", "False")
    member_repository.create_member(member_3)
    member_4 = Member("Jane Fonda", "True", "False")
    member_repository.create_member(member_4)
    member_5 = Member("Milla Jovovich","False", "True")
    member_repository.create_member(member_5)
    member_6 = Member("Halle Berry", "False", "False")
    member_repository.create_member(member_6)
    

    activity_1 = Activity("Boxing", "2022-07-15", "19:00", 5)
    activity_repository.create_activity(activity_1)
    activity_2 = Activity("Swimming", "2022-12-25" , "12:00", 3)
    activity_repository.create_activity(activity_2)
    activity_3 = Activity("Yoga", "2023-01-01" ,"09:00", 10)
    activity_repository.create_activity(activity_3)
    activity_4 = Activity("Kettlebells", "2022-09-10", "14:00", 5)
    activity_repository.create_activity(activity_4)
    activity_5 = Activity("Strength & Conditioning", "2022-08-17" , "17:00", 3)
    activity_repository.create_activity(activity_5)
    activity_6 = Activity("Zumba", "2022-10-08" ,"18:30", 10)
    activity_repository.create_activity(activity_6)

    booking_1 = Booking (member_1, activity_1)
    booking_repository.create_booking(booking_1)
    booking_2 = Booking (member_1, activity_2)
    booking_repository.create_booking(booking_2)
    booking_3 = Booking (member_3, activity_3)
    booking_repository.create_booking(booking_3)
    booking_4 = Booking (member_3, activity_5)
    booking_repository.create_booking(booking_4)
    booking_5 = Booking (member_3, activity_2)
    booking_repository.create_booking(booking_5)
    booking_6 = Booking (member_3, activity_2)
    booking_repository.create_booking(booking_6)
    return redirect ('/seeded_database') # Redirect user back to the home page

if __name__ == '__main__':
    app.run(debug=True)