# Define the activity class for gym classes

class Activity:
    def __init__(self, type, date_time, id = None):
        self.type = type
        self.date_time = date_time
        self.id = id