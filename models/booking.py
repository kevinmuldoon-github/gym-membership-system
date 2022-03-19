# Define the Booking class for taking bookings from customers

from unittest.util import _count_diff_hashable


class Booking:
    def __init__(self,member, activity, id = None):
        self.member = member
        self.activity = activity
        self.id = id