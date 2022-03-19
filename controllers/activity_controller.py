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