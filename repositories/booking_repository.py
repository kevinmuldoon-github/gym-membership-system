from db.run_sql import run_sql

from models.booking import Booking
from models.activity import Activity
from models.member import Member

import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository

# Function to insert a new booking to the gym database
def create_booking(booking):   
    sql = "INSERT INTO bookings (member_id, activity_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id , booking.activity.id]
    results = run_sql(sql,values)

    booking.id = results[0]['id']
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



# Function to delete a specific booking
def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql,values)

# Function to delete all bookings
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)