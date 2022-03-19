from db.run_sql import run_sql

from models.booking import Booking
from models.activity import Activity
from models.member import Member

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
        booking = Booking(result['member_id'] , result['activity_id'] , result['id'])
        bookings.append(booking)
    return bookings