from room import Room
from player import Player
import random
# Declare all the rooms

room = {
    'highway': Room('Highway', 'You have just been ran over'),
    'parking-lot': Room("Parking lot", "North of you is a Cave entrance. To the South is a highway."),
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
 
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['highway'].s_to = room['parking-lot']
room['parking-lot'].n_to = room['outside']
room['parking-lot'].s_to = room['highway']
room['outside'].n_to = room['foyer']
room['outside'].s_to = room['parking-lot']
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

# Step 1: Entering name and beginning game
user = Player(input("Please enter your name: "), room['outside'])
print(user.name)
print(room['outside'])
# Currently saying "isla" or "i" is not defined but if I put nothing it saying it cannot parse an empty string.
# Takes a name but return room.Room instance is not clean

# Step 2: prompt user to make a choice
# No prompt after telling where player is
direction = ['n', 's', 'e', 'w']
pick = ['a']
get = ['get']
drop = ['drop']
# Step 3: Display new room and loop
trinkets_name = [
    'Sword', 'Rasin', 'MedPack'
]
trinkets_des = [
    'poisoned', 'important', 'light'
]
random.shuffle(trinkets_name)
random.shuffle(trinkets_des)

while True:
    com = input("==> ").lower()
    if com in drop:
        user.drop(trinkets_name[0])
    elif com in get:
        user.pick_up(trinkets_name[0], trinkets_des[0])
    elif com in direction:
        user.travel(com)
        if com == 'n':
            trinkets_name = [
                'Paper', 'Medication', 'Pen'
            ]
            trinkets_des = [
                'LATE NOTICE', 'Dosidoe', 'Dr. Richard NyGaurd'
            ]
            random.shuffle(trinkets_name)
            random.shuffle(trinkets_des)
        elif com == 's':
            trinkets_name = [
                'Charger', 'Pencil', 'Staples'
            ]
            trinkets_des = [
                'Made in China', 'No.2', 'Not for consumption'
            ]
            random.shuffle(trinkets_name)
            random.shuffle(trinkets_des)
        elif com == 'e':
            trinkets_name = [
                'LipStick', 'Elephant Figurine', 'Leave-in Conditioner'
            ]
            trinkets_des = [
                'Honeysuckle', 'Do not get wet', 'All natural'
            ]
            random.shuffle(trinkets_name)
            random.shuffle(trinkets_des)
        elif com == 'w':
            trinkets_name = [
                'Tape', 'Starbucks Cup', 'Hairbrush'
            ]
            trinkets_des = [
                'Durable', 'For cold use only', 'FoxyBae'
            ]
            random.shuffle(trinkets_name)
            random.shuffle(trinkets_des)    
    elif com == "q":
        print("Bye Bye")
        exit()
    else:
        print("Not a command")
