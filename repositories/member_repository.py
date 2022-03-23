from db.run_sql import run_sql

from models.member import Member
from models.activity import Activity

# Function to insert a new member to the gym database
def create_member(member):   
    sql = "INSERT INTO members (name, premium, deactivated) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.premium, member.deactivated]
    results = run_sql(sql,values)
    member.id = results[0]['id']
    return member

# Function to edit/update a specific member's information
def edit_member(member):
    sql = "UPDATE members SET (name, premium, deactivated) = (%s, %s, %s) WHERE id = %s"
    values = [member.name, member.premium, member.deactivated, member.id]
    run_sql(sql,values)

# Function to show a select/show a specific member
def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    
    if result:
        member_from_db = result[0]
        member = Member(member_from_db['name'] , member_from_db['premium'] , member_from_db['deactivated'], member_from_db['id'])
    return member

# Function to select all members. Useful for showing all members in forms etc
def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for result in results:
        member = Member(result['name'] , result['premium'] , result['deactivated'], result['id'])
        members.append(member)
    return members

# Function to select active members
def select_active_members():
    members = []
    sql = "SELECT * FROM members WHERE deactivated = %s"
    values = ['False']
    results = run_sql(sql, values)

    for result in results:
        member = Member(result['name'] , result['premium'] , result['deactivated'], result['id'])
        members.append(member)
    return members

# Function to select inactive members
def select_deactived_members():
    members = []
    sql = "SELECT * FROM members WHERE deactivated = %s"
    values = ['True']
    results = run_sql(sql, values)

    for result in results:
        member = Member(result['name'] , result['premium'] , result['deactivated'], result['id'])
        members.append(member)
    return members

# Function to select standard members
def select_standard_active_members():
    members = []
    sql = "SELECT * FROM members WHERE premium = %s AND deactivated = %s"
    values = ['False' , 'False']
    results = run_sql(sql, values)

    for result in results:
        member = Member(result['name'] , result['premium'] , result['deactivated'], result['id'])
        members.append(member)
    return members

# Function to select premium members
def select_premium_active_members():
    members = []
    sql = "SELECT * FROM members WHERE premium = %s AND deactivated = %s"
    values = ['True' , 'False']
    results = run_sql(sql, values)

    for result in results:
        member = Member(result['name'] , result['premium'] , result['deactivated'], result['id'])
        members.append(member)
    return members

# Function to delete a specific gym member
def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql,values)

# Function to delete all members
def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

# Function to find the classes a member is booked into
def find_activities_for_member(id):
    activities = []
    sql = "SELECT activities.* FROM activities INNER JOIN bookings ON activities.id = bookings.activity_id WHERE bookings.member_id=%s"
    values = [id]
    results = run_sql(sql,values)
    
    for result in results:
        activity = Activity(result['type'], result['date'], result['time'] , result['capacity'] , result['id'])
        activities.append(activity)
    return activities