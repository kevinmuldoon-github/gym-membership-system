# Controller for activities / gym-classes

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity

import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("classes", __name__)

@activities_blueprint.route("/classes")
def activities():
    activities = activity_repository.select_all()
    return render_template('classes/index.html' , title = 'Gym Classes' , activities = activities)

# Function to show activity information using member id
@activities_blueprint.route("/classes/<id>", methods=['GET'])
def show_activity(id):
    activity = activity_repository.select(id)
    return render_template('/classes/show_class.html' , title = 'Class Information' , activity = activity)



# Function to delete an activity
@activities_blueprint.route("/classes/<id>/delete" , methods = ['POST'])
def delete_activity(id):
    activity_repository.delete(id)
    return redirect ('/classes') # Redirect user back to the classes page