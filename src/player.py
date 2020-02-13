from item import Item
import random
# Write a class to hold player information, e.g. what room they are in
# currently.
quiz = {'What is 1+1?': '2', '2*2?': "4", '3-3?': '0', '4/4?': '1'}



class Player:
    def __init__(self, name, start_room):
        self.name = name,
        self.current_room = start_room
        self.items = ''
        self.score = 0
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
    def drop(self, itemName):

        inventory = self.items.split(',')
        ##Now it is an array --  tell it to delete the first item in your list using index
        inventory.pop(0)
        print(inventory)
    def print_score(self, score):
        question = random.shuffle(quiz)
        print(question)
        print(f"Your score: {score}")