# Testing the activity class

import unittest
from models.activity import Activity

class TestActivity(unittest.TestCase):

    def setUp(self):
        self.activity_1 = Activity("Boxing", "4 July", "7pm")
        self.activity_2 = Activity("Swimming", "25 December" , "12pm")
        self.activity_3 = Activity("Yoga", "01 January" ,"9am")

    def test_activity_has_type(self):
        self.assertEqual("Boxing",self.activity_1.type)
        self.assertEqual("Swimming",self.activity_2.type)
        self.assertEqual("Yoga",self.activity_3.type)

    def test_activity_has_date(self):
        self.assertEqual("4 July",self.activity_1.date)
        self.assertEqual("25 December",self.activity_2.date)
        self.assertEqual("01 January",self.activity_3.date)

    def test_activity_has_time(self):
        self.assertEqual("7pm",self.activity_1.time)
        self.assertEqual("12pm",self.activity_2.time)
        self.assertEqual("9am",self.activity_3.time)