from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, start_room):
        self.name = name,
        self.current_room = start_room
        self.items = ''
    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print('Do not enter')
    def pick_up(self, itemName, itemDes):
        inventory = Item(itemName, itemDes)
        complete = inventory.name + ' ' + ',' + ' ' + self.items
        print(f"Inventory: {complete}")
        self.items = complete
    ##Not picking up for some reason