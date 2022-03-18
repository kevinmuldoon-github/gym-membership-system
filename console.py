import pdb
from models.activity import Activity
from models.member import Member
from models.booking import Booking

import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

member_1 = Member("Peter La Fleur")
member_repository.create_member(member_1)
member_2 = Member("Arnold Schwarzenegger")
member_repository.create_member(member_2)
member_3 = Member("Ronnie Coleman")
member_repository.create_member(member_3)
