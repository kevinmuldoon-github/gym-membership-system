# Test to check booking class is working

import unittest
from models.booking import Booking

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.booking_1 = Booking (1, 1)
        self.booking_2 = Booking (2, 2)
        self.booking_3 = Booking (3, 3)
    
    def test_booking_has_member_id(self):
        self.assertEqual(1,self.booking_1.member_id)
        self.assertEqual(2,self.booking_2.member_id)
        self.assertEqual(3,self.booking_3.member_id)