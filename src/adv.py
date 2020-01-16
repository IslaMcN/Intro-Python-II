from room import Room
from player import Player
# Declare all the rooms

room = {
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
user = Player(raw_input("Please enter your name: "), room['outside'])
print(user.name, user.current_room)

##Currently saying "isla" or "i" is not defined but if I put nothing it saying it cannot parse an empty string.
#Takes a name but return room.Room instance is not clean

##Step 2: prompt user to make a choice

#Step 3: Display new room and loop

def handler(com, player):
    while True:
        com.input("=> ").lower()
        if com == 'n':
        #Go north
            if player.current_room.n_to != None:
            #Put player in room
                player.current_room = player.current_room.n_to
            #Read off room info
                room_descritpion(player.current_room)
            else:
                print('Do NOT enter')
        elif com == 's':
        #Go south
            if player.current_room.s_to != None:
            #Put player in room
                player.current_room = player.current_room.s_to
            #Read off room info
                room_description(player.current_room)
            else:
                print('There is nothing for you here')
        elif com == 'e':
        #Go east
            if player.current_room.e_to != None:
            #Put player in room
                player.current_room = player.current_room.e_to
            #Read off room info
                room_description(player.current_room)
            else:
                print('Turn around and try again')
        elif com == 'w':
        #Go west
            if player.current_room.w_to != None:
            #Put player in room
                player.current_room = player.current_room.w_to
            #Read off room info
                room_description(player.current_room)
            else:
                print('This is not da way')
        elif com == 'q':
            print('Bye, Bye!')
        else:
            print('I do not know what that means. Try n, s, e, w, or q')


def room_description(room):
    print('You are in {room.name}')
    print(room.description)

room_description(user.current_room)


