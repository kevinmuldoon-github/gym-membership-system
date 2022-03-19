# Controller for member functionality

from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member

import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# Main members page
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template('members/index.html' , title = 'Gym Members' , members = members)

# Function to show member information using member id
@members_blueprint.route("/members/<id>", methods=['GET'])
def show_member(id):
    member = member_repository.select(id)
    return render_template('/members/show_member.html' , title = 'Member Information' , member=member)

# Display page and form to edit a member's information
@members_blueprint.route("/members/<id>/edit_member" , methods = ['GET'])
def edit_member(id):

    member = member_repository.select(id) # Find member information

    return render_template('/members/edit_member.html' , title = 'Edit a Member' , member = member)

# Function to delete a member
@members_blueprint.route("/members/<id>/delete" , methods = ['POST'])
def delete_member(id):
    member_repository.delete(id)
    return redirect ('/members') # Redirect user back to the members page

# Display new member page
@members_blueprint.route("/members/new_member", methods = ['GET'])
def new_member():
    return render_template("members/new_member.html" , title = "Add a New Member to the Gym")

# Function to retrieve member information and write new member to database
@members_blueprint.route("/members" , methods = ['POST'])
def create_member():
    name = request.form['name']
    member = Member(name) # Create member object
    member_repository.create_member(member) # Add member to database
    return redirect ('/members') # Redirect user to main members page
