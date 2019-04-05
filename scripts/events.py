
import re
import collections
import time

def loadDeck(player,groups):   
   mute()
   init()
   if player == me:
      table.create("f5f6e310-629e-456f-af29-f8df2d11e6b5", playerside() * -60, yaxisMove(), 1, True) # The OK Button
      table.create("54afa74e-b2c4-4010-b407-39909f55481a", 0, yaxisMove(), 1, True) # The Wait! Button
      table.create("a4f448b9-449c-40d1-b387-301e3a1b5fc6", playerside() * 60, yaxisMove(), 1, True) # The Actions? Button
   
