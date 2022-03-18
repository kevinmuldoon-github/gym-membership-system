# Define the Booking class for taking bookings from customers

from unittest.util import _count_diff_hashable


class Booking:
    def __init__(self,member_id, class_id, id = None):
        self.member_id = member_id
        self.class_id = class_id
        self.id = id