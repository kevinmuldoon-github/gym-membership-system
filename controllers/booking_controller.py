# Controller for booking functionality

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking

import repositories.booking_repository as booking_repository
import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template('bookings/index.html' , title = 'Bookings' , bookings = bookings)

# Function to show booking information using booking id
@bookings_blueprint.route("/bookings/<id>", methods=['GET'])
def show_booking(id):
    booking = booking_repository.select(id)
    activity = activity_repository.select(booking.activity)
    member = member_repository.select(booking.member)
    return render_template('/bookings/show_booking.html' , title = 'Booking Information' , booking = booking, activity = activity, member = member)


# Display page and form to edit a booking
@bookings_blueprint.route("/bookings/<id>/edit_booking" , methods = ['GET'])
def show_edit_booking_page(id):
    premium_class = False
    booking = booking_repository.select(id) # Find booking information
    activity = activity_repository.select(booking.activity)
    activity_time_string = activity.split(":")
    time_number = int(activity_time_string[0])
    if time_number >10 and time_number < 16:
        members = member_repository.select_active_members()
    else:
        premium_class = True
        members = member_repository.select_premium_active_members()
    member = member_repository.select(booking.member)
    

    return render_template('/bookings/edit_booking.html' , title = 'Edit a Booking' , booking = booking, premium_class = premium_class ,member = member, members = members, activity = activity)

# Function to edit a booking with updated information
@bookings_blueprint.route('/bookings/<id>/edit' , methods = ['POST'] )
def edit_booking(id):
    original_booking = booking_repository.select(id)
    member_id = request.form['member_id']
    member = member_repository.select(member_id)
    activity = activity_repository.select(original_booking.activity_id)
    booking = Booking (member, activity, id) # Create booking object
    booking_repository.edit_booking(booking) # Edit booking in database
    return redirect ('/bookings') # Redirect to main bookings page


# Display new booking page
@bookings_blueprint.route("/bookings/new_booking", methods = ['GET'])
def new_booking_page():
    members = member_repository.select_active_members()
    number_standard_active_members = len(member_repository.select_standard_active_members())
    number_premium_active_members = len(member_repository.select_premium_active_members())
    off_peak_activities = activity_repository.select_off_peak_activities_with_spaces()
    activities = activity_repository.select_activities_with_spaces()

    number_off_peak_activities = len(activity_repository.select_off_peak_activities_with_spaces())
    total_number_activities = len(activity_repository.select_activities_with_spaces())

    activities_at_capacity = activity_repository.select_activities_with_no_spaces()

    return render_template("bookings/new_booking.html" , title = "Book a Member Into a Class", members = members , number_off_peak_activities = number_off_peak_activities , total_number_activities = total_number_activities , number_standard_active_members = number_standard_active_members , number_premium_active_members = number_premium_active_members ,  off_peak_activities = off_peak_activities , activities_at_capacity = activities_at_capacity,  activities = activities)

# Function to create a new booking from a form submission
@bookings_blueprint.route("/bookings" , methods = ['POST'])
def create_booking():
    member_id = request.form['member_id']
    member = member_repository.select(member_id)
    activity_id =request.form['activity_id']
    activity = activity_repository.select(activity_id)
    booking = Booking(member, activity) # Create booking object
    booking_repository.create_booking(booking) # Add booking to database
    return redirect ('/bookings') # Redirect user to main booking page

# Function to delete a booking
@bookings_blueprint.route("/bookings/<id>/delete" , methods = ['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect ('/bookings') # Redirect user back to the main bookings page