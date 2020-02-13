
# * Create a file called `item.py` and add an `Item` class in there.

#   * The item should have `name` and `description` attributes.

#      * Hint: the name should be one word for ease in parsing later.

#   * This will be the _base class_ for specialized item types to be declared
#     later.
## associated with player and room

class Item:
    def __init__(self, name, description):
        # Hint: the name should be one word for ease in parsing later.
        self.name = name
        self.description = description
        
        
        print(f"{self.name}, engraved it says {self.description}")
    def treasure(self):
        print("Ohhhh you found treasure!!")
        return 0
# items = Item('Sword', 'Shiny pointy thing that could kill')
# print(items.name)
# print(items.description)

        