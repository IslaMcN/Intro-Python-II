# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    #should have name and description attributes
    def __init__(self,name, description, items):
        self.name = name,
        self.description = description,
         #should have cardinal direction attributes that point to the correct room
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    def __str__(self):
        display_string = (
            f"------------"
            f"\n{self.name}\n"
            f"\n{self.description}\n"
            f"\n{self.get_exits_string()}\n"
            f"\n Items to pick up: {self.items}\n"
            f"\n If you want to pick up item, press [a]: ")
        return display_string
    def get_room_in_direction(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None
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
        return f"Exits: {', '.join(self.get_exits())}"
    # def leave_behind(self, item):
    #     ##Drop items you are holding
    
   
