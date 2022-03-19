# Testing the activity class

import unittest
from models.activity import Activity

class TestActivity(unittest.TestCase):

    def setUp(self):
        self.activity_1 = Activity("Boxing", "2022-07-15", "19:00")
        self.activity_2 = Activity("Swimming", "2022-12-25" , "12:00")
        self.activity_3 = Activity("Yoga", "2023-01-01" ,"09:00")

    def test_activity_has_type(self):
        self.assertEqual("Boxing",self.activity_1.type)
        self.assertEqual("Swimming",self.activity_2.type)
        self.assertEqual("Yoga",self.activity_3.type)

    def test_activity_has_date(self):
        self.assertEqual("2022-07-15",self.activity_1.date)
        self.assertEqual("2022-12-25",self.activity_2.date)
        self.assertEqual("2023-01-01",self.activity_3.date)

    def test_activity_has_time(self):
        self.assertEqual("19:00",self.activity_1.time)
        self.assertEqual("12:00",self.activity_2.time)
        self.assertEqual("09:00",self.activity_3.time)