# Controller for activities / gym-classes

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity

import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("classes", __name__)

@activities_blueprint.route("/classes")
def activities():
    off_peak_activities = activity_repository.select_off_peak_activities_with_spaces()
    activities = activity_repository.select_peak_hour_activities_with_spaces()

    total_off_peak_activities = len(activity_repository.select_off_peak_activities_with_spaces())
    total_number_activities = len(activity_repository.select_activities_with_spaces())

    activities_at_capacity = activity_repository.select_activities_with_no_spaces()
    total_activities_at_capacity = len(activities_at_capacity)

    return render_template('/classes/index.html' , title = 'Gym Classes' , off_peak_activities = off_peak_activities , total_off_peak_activities = total_off_peak_activities ,  total_number_activities = total_number_activities ,  activities_at_capacity = activities_at_capacity , total_activities_at_capacity = total_activities_at_capacity ,  activities = activities)

# Function to show activity information using member id
@activities_blueprint.route("/classes/<id>", methods=['GET'])
def show_activity(id):
    activity = activity_repository.select(id)

    if activity is None:
            return redirect ('/404') # if booking does not exist, redirect to 404 page
    else:
        members = activity_repository.find_members_booked_in_class(id)
        enrolled = len(members)
    return render_template('/classes/show_class.html' , title = 'Class Information' , activity = activity, members = members, enrolled = enrolled)

# Display page and form to edit an activity
@activities_blueprint.route("/classes/<id>/edit_class" , methods = ['GET'])
def show_edit_class_page(id):
    activity = activity_repository.select(id) # Find class information
    return render_template('/classes/edit_class.html' , title = 'Edit a Class' , activity = activity)

# Function to edit a member with updated information
@activities_blueprint.route('/classes/<id>/edit' , methods = ['POST'] )
def edit_activity(id):
    type = request.form['type']
    date = request.form['date']
    time = request.form['time']
    capacity = request.form['capacity']
    activity = Activity(type, date, time, capacity, id)
    activity_repository.edit_activity(activity)
    return redirect ('/classes') # Redirect to main classes page

# Display new class page
@activities_blueprint.route("/classes/new_class", methods = ['GET'])
def new_class_page():
    return render_template("/classes/new_class.html" , title = "Add a New Class to the Gym")

# Function to delete an activity
@activities_blueprint.route("/classes/<id>/delete" , methods = ['POST'])
def delete_activity(id):
    activity_repository.delete(id)
    return redirect ('/classes') # Redirect user back to the classes page

# Function to create a new class
@activities_blueprint.route("/classes" , methods = ['POST'])
def create_activity():
    type = request.form['type']
    date = request.form['date']
    time = request.form['time']
    capacity = request.form['capacity']
    activity = Activity(type, date, time, capacity) # Create activity object
    activity_repository.create_activity(activity) # Add new activity to database
    return redirect ('/classes') # Redirect user to main classes page