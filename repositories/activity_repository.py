from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member
from models.booking import Booking

# Function to insert a new activity/class to the gym database
def create_activity(activity):   
    sql = "INSERT INTO activities (type, date, time) VALUES (%s, %s, %s) RETURNING id"
    values = [activity.type , activity.date, activity.time]
    results = run_sql(sql,values)

    activity.id = results[0]['id']
    return activity

# Function to edit/update a specific activity i.e. gym class
def edit_activity(activity):
    sql = "UPDATE activities SET (type, date, time) = (%s, %s, %s) WHERE id = %s"
    values = [activity.type , activity.date, activity.time, activity.id]
    run_sql(sql,values)

# Function to show a select/show a specific activity
def select(id):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = Activity (result['type'] , result['date'] , result['time'] , result['id'])
    return activity


# Function to select all activities
def select_all():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for result in results:
        activity = Activity (result['type'] , result['date'] , result['time'] , result['id'])
        activities.append(activity)
    return activities


# Function to delete a specific activity
def delete(id):
    sql = "DELETE FROM activities WHERE id = %s"
    values = [id]
    run_sql(sql,values)

# Function to delete all activities
def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)

# Function to find members booked into a specific class
def find_members_booked_in_class(id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON members.id = bookings.member_id WHERE bookings.activity_id = %s"
    values = [id]
    results = run_sql(sql,values)
    
    for result in results:
        member = Member(result['name'] , result['premium'] , result['deactivated'], result['id'])
        members.append(member)
    return members
