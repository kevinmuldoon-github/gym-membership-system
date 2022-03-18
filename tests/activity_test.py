# Testing the activity class

import unittest
from models.activity import Activity

class TestActivity(unittest.TestCase):

    def setUp(self):
        self.activity_1 = Activity("Boxing", "Monday at 7pm")
        self.activity_2 = Activity("Swimming", "Tuesday at 12pm")
        self.activity_3 = Activity("Yoga", "Saturday at 9am")

    def test_activity_has_type(self):
        self.assertEqual("Boxing",self.activity_1.type)
        self.assertEqual("Swimming",self.activity_2.type)
        self.assertEqual("Yoga",self.activity_3.type)

    def test_activity_has_date_time(self):
        self.assertEqual("Monday at 7pm",self.activity_1.date_time)
        self.assertEqual("Tuesday at 12pm",self.activity_2.date_time)
        self.assertEqual("Saturday at 9am",self.activity_3.date_time)