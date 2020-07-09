# Write a class to hold player information, e.g. what room they are in
# currently.


# what info should player have right now?
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    # for now what should the player be able to do in the form of some methods?
        # declare own name
        # move rooms
        # see what room im in
    

    def getName(self):
        return self.name

    def setName(self, inc):
        self.name = inc

    def getRoom(self):
        return self.room

    def current(self):
        print(f"you are currently taking a gander at the {self.room} ")

    def moveTo(self, new_room):
        self.room = new_room
        


# im going to need strings for perdy text output **EDIT I PUT THEM IN THE METHODS FOR THE CLOUT**

    # def current(self):
    #     print(f"{self.name} is currently taking a gander at {self.room} ")

    # def isMoving(self):
    #     print(f"{self.name} is moving to {self.room}")


# i want to test everything to make sure it works properly before i move on
# player = Player("Bob the Mighty", "foyer")
# player.setName("phill the weak") # name change works
# print(player.getName()) # command - who am i 
# print(player.getRoom()) # works may not use though
# player.current() # command where am i
# player.moveTo("Another cool lookin room!")
# player.current()

                                                                                                                                  
                                                                                                                                                              
