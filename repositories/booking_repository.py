import pdb

from db.run_sql import run_sql

from models.booking import Booking
from models.activity import Activity
from models.member import Member

import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository

# Function to insert a new booking to the gym database
def create_booking(booking):   
    sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id , booking.activity.id]
    results = run_sql(sql,values)

    booking.id = results[0]['id']
    return booking

# Function to edit/update a specific booking
def edit_booking(booking):
    sql = "UPDATE bookings SET (member_id, activity_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id , booking.activity.id, booking.id]
    run_sql(sql,values)

# Function to show a select/show a specific booking
def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        booking = Booking(result['member_id'], result['activity_id'], result['id'])
    return booking

# Function to select all bookings
def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result['member_id'])
        activity = activity_repository.select(result['activity_id'])
        booking = Booking(member , activity , result['id'])
        bookings.append(booking)
    return bookings

# Function to see if booking exists
def does_booking_already_exist(member_id, activity_id):
    booking_exists = False
    sql = "SELECT COUNT(*) FROM bookings WHERE member_id=%s AND activity_id=%s THEN TRUE"
    values = [member_id, activity_id]
    result = run_sql(sql, values)

    if result ==0 :
        booking_exists = True
    return booking_exists

# Function to delete a specific booking
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql,values)

# Function to delete all bookings
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)