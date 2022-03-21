from db.run_sql import run_sql

from models.activity import Activity
from models.member import Member
from models.booking import Booking

# Function to insert a new activity/class to the gym database
def create_activity(activity):   
    sql = "INSERT INTO activities (type, date, time, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [activity.type , activity.date, activity.time, activity.capacity]
    results = run_sql(sql,values)

    activity.id = results[0]['id']
    return activity

# Function to edit/update a specific activity i.e. gym class
def edit_activity(activity):
    sql = "UPDATE activities SET (type, date, time, capacity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [activity.type , activity.date, activity.time, activity.capacity, activity.id]
    run_sql(sql,values)

# Function to show a select/show a specific activity
def select(id):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = Activity (result['type'] , result['date'] , result['time'] , result['capacity'],  result['id'])
    return activity

# Function to find off-peak activities with spaces
def select_off_peak_activities_with_spaces():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for result in results:
        members = find_members_booked_in_class(result['id'])
        enrolled = len(members)
        capacity = result['capacity']
        time_list = result['time'].split(":")
        time_number = int(time_list[0])
        if time_number >=10 and time_number < 16 and enrolled < capacity:
            activity = Activity (result['type'] , result['date'] , result['time'] , result['capacity'] , result['id'])
            activities.append(activity)
    return activities

# Function to find off-peak activities with spaces
def select_peak_hour_activities_with_spaces():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for result in results:
        members = find_members_booked_in_class(result['id'])
        enrolled = len(members)
        capacity = result['capacity']
        time_list = result['time'].split(":")
        time_number = int(time_list[0])
        if (time_number < 10 or time_number >= 16) and enrolled < capacity:
            activity = Activity (result['type'] , result['date'] , result['time'] , result['capacity'] , result['id'])
            activities.append(activity)
    return activities

# Function to find off-peak activities with spaces
def select_off_peak_activities_with_no_spaces():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for result in results:
        members = find_members_booked_in_class(result['id'])
        enrolled = len(members)
        capacity = result['capacity']
        time_list = result['time'].split(":")
        time_number = int(time_list[0])
        if time_number >10 and time_number < 16 and enrolled == capacity:
            activity = Activity (result['type'] , result['date'] , result['time'] , result['capacity'] , result['id'])
            activities.append(activity)
    return activities

# Function to find all activities that have not reached capacity
def select_activities_with_spaces():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for result in results:
        members = find_members_booked_in_class(result['id'])
        enrolled = len(members)
        capacity = result['capacity']
        if enrolled < capacity:
            activity = Activity (result['type'] , result['date'] , result['time'] , result['capacity'] , result['id'])
            activities.append(activity)
    return activities

# Function to find all activities that are full
def select_activities_with_no_spaces():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for result in results:
        members = find_members_booked_in_class(result['id'])
        enrolled = len(members)
        capacity = result['capacity']
        if enrolled == capacity:
            activity = Activity (result['type'] , result['date'] , result['time'] , result['capacity'] , result['id'])
            activities.append(activity)
    return activities

# Function to select all activities
def select_all():
    activities = []
    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for result in results:
        activity = Activity (result['type'] , result['date'] , result['time'] , result['capacity'] , result['id'])
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
