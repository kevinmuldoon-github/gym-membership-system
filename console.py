import pdb
from models.activity import Activity
from models.member import Member
from models.booking import Booking

import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import repositories.date_repository as date_repository

member_1 = Member("Peter La Fleur")
member_repository.create_member(member_1)
member_2 = Member("Arnold Schwarzenegger")
member_repository.create_member(member_2)
member_3 = Member("Ronnie Coleman")
member_repository.create_member(member_3)

activity_1 = Activity("Boxing", "2022-07-15", "19:00")
activity_repository.create_activity(activity_1)
activity_2 = Activity("Swimming", "2022-12-25" , "12:00")
activity_repository.create_activity(activity_2)
activity_3 = Activity("Yoga", "2023-01-01" ,"09:00")
activity_repository.create_activity(activity_3)

booking_1 = Booking (member_1, activity_1)
booking_repository.create_booking(booking_1)
booking_2 = Booking (member_2, activity_2)
booking_repository.create_booking(booking_2)
booking_3 = Booking (member_3, activity_3)
booking_repository.create_booking(booking_3)

my_date = "2022-12-25"
date = date_repository.convert_date(my_date) # Convert date format
print(date)