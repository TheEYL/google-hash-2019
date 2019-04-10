""" This class represents the photo objects"""

class Photo:
    def __init__(self, id, type):
        self.id = id
        self.type = type[0]
        self.tags = type[2:]
        # print(self.tags)
        # print(type)
