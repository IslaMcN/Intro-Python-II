# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    #should have name and description attributes
    def __init__(self,name, description, items):
        self.name = name,
        self.description = description,
         #should have cardinal direction attributes that point to the correct room
        self.n_to = None,
        self.s_to = None,
        self.e_to = None,
        self.w_to = None,
        self.items = items
   
