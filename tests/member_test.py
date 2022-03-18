# Testing the member class

import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member_1 = Member("Peter La Fleur")
        self.member_2 = Member("Arnold Schwarzenegger")
        self.member_3 = Member("Ronnie Coleman")
    
    def test_members_have_name(self):
        self.assertEqual("Peter La Fleur",self.member_1.name)
        self.assertEqual("Arnold Schwarzenegger",self.member_2.name)
        self.assertEqual("Ronnie Coleman",self.member_3.name)