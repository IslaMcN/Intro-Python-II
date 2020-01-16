# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    #should have name and description attributes
    def __init__(self,name, description):
        self.name = name,
        self.description = description,
         #should have cardinal direction attributes that point to the correct room
        self.n_to = None,
        self.s_to = None,
        self.e_to = None,
        self.w_to = None,
        self.items = []
    def __str__(self):
   
        return "%s, %s, %s" (self.name, self.description, self.get_exits_string)

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append('n')
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits
    def get_exits_string(self):
        return "Exits: %s"({', '.join(self.get_exits())})
   
