from room import Room
from player import Player
# Declare all the rooms
 
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['candle', 'crystal']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['Golden Key']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['Cat Skull']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['Old Notebook']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['Empty box']),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

###Step 1: Entering name and beginning game
user = Player(input("Please enter your name: "), room['outside'])
print(user.name)
print(room['outside'])
##Currently saying "isla" or "i" is not defined but if I put nothing it saying it cannot parse an empty string.
#Takes a name but return room.Room instance is not clean

##Step 2: prompt user to make a choice
#No prompt after telling where player is
direction = ['n', 's', 'e', 'w']
pick = 'a'
#Step 3: Display new room and loop

while True:
    com = input("==> ").lower()
    if com in pick:
        user.pick_up(room.items)
    elif com in direction:
        user.travel(com)
       
    elif com =="q":
        print("Bye Bye")
        exit()
    else:
        print("Not a command")