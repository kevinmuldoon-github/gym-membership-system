# The member class uses name instead of first and last name
# This is a simple way of allowing longer names e.g. middle names

class Member:

    def __init__(self, name, id = None):
        self.name = name
        self.id = id

