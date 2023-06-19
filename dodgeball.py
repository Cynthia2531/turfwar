#In Dodgeball you must find and collect a bottle of Moo-Pop.
#In Floatage you must dodge the fireworks coming for you.
#In A-Maze you must make your way through the map and collect 10 mycellium.
#In Wack-A-Stack you must break an armour stand.
#In Showdown you have to collect the grass sources block whilst avoiding cobwebs.
moopop = """
                                    ((########(
                                ,,&&&&&%%%%%%%%%%.
                                ((###############
                                ((##############/
                                ((&&&&&&&&&&&&&&&
                                      ((#%%(
                                    ((**/(((
                                     //(#@@(
                                    ((&@&%%((
                                  ((@@@@@&@@@%/
                                */((@@@@@@@@@%/
                              **//&@@@@#((@@@@@@@//
                            *((@@@@@@@@@@@@@@@@@@@#//
                           (#@@@@@@@@@@@@&&@@&((@@@@@/
                          ((#@@@@@@@@@@@@@@@@@@@@@@@@//
                          //#@@@@@@@@@@@@@@@@@@@@@@@@//
                         //&@@@@@@@@@%%&@@@@@@@@@@@@@@@
                        (/%&&@@@@@@@@@@@@@@@@@@@@@@@@%&
                        //%&&&&@@@@@@@@@@@@@@@&&&%/#&&&
                        //%&&&&&%&&&&&&&&&&&&&%%&&&&&&&
                        //%@@&&&&&%%&&&&%&&&&&&&&&&&&@@
                       //(%@@@@@&&&&&&&%%%%&&&&&&&@@@@@
                        /(%@@@@@@@@@&&&&&&&&&&@@@@@@@@@
                         /#@@@@@@@%%@@@@@@@@@@@@@@@@@@@
                         \\@@@@@@@@@@@@@@@@@@@@@@@@@@//
                          \\@@@@@@@@@@@@@@@@@@@@@@@@//
                           \\@@@@@@@@@@@@@@@@@@@@@@@//
                             \\@@@@@@@@@@@@@@@@@@#//
                              \#@@@@@@@@@@@@@@@@@@/
                              """

#Dodgeball
#Varibles
leftright1 = "You are now outside of the court facing the team area. There is a elevator down in front of you and to the side the locker areas for the team."
#def functions
def backward1():
  directions = ["forward", "left", "right"]
  userInput = ""
  while userInput not in directions:
    print("Options: forward/left/right")
    userInput = input()
    if userInput == "forward":
      print("You have fallen into the elevator. You should look around, it is quite interesting here.")
      elevator()
    elif userInput == "left":
      lockersleft()
    elif userInput == "right":
      lockersright()
    else:
      print("Please enter a valid option.")

def elevator():
  directions = ["right", "left"]
  userInput = ""
  while userInput not in directions:
    print("Options: left/right")
    userInput = input()
    if userInput == "left":
      elevatorlook()
    elif userInput == "right":
      elevatorlook()
    else:
      print("Please enter a valid option.")
    
def lockersleft():
  print("These look like lockers maybe the Moo-Pop is here.")
  directions = ["right"]
  userInput = ""
  while userInput not in directions:
      print("Option: right")
      userInput = input()
      if userInput == "right":
        print("You have fallen into the elevator. You should look around, it is quite interesting here.")
        elevator()
      else:
        print("Please enter a valid option.")

def lockersright():
  print("These look like lockers maybe the Moo-Pop is here.")
  directions = ["left"]
  userInput = ""
  while userInput not in directions:
      print("Options: left")
      userInput = input()
      if userInput == "left":
        print("You have fallen into the elevator. You should look around, it is quite interesting here.")
        elevator()
      else:
        print("Please enter a valid option.")

def elevatorlook():
    print("To your left is lockers do you want to investigate?")
    TorF = ["Y"]
    userInput = ""
    while userInput not in TorF:
      print("Options: Y/N")
      userInput = input()
      if userInput == "Y":
        print("You look and see boxes you look inside and see the precious Moo-Pop")
        print(moopop)
        print("Moving to next game, Floatage")
      else:
        print("Please enter a vaild option.")
        
#Code for dodgeball
print("Welcome to Dodgeball you are right now in the middle of the court. Try to find the Moo-Pop")
directions = ["left","right","forward"]
print("Where would you like to go?")
userInput = ""
while userInput not in directions:
  print("Options: left/right/backward")
  userInput = input()
  if userInput == "left":
    print("You have bumped into the fence of the court. There is a barrier to the left and in front of you.")
    print(leftright1)
    backward1()
  elif userInput == "right":
    print("You have moved to the right side of the court. There is a barrier to the right and infront of you.")
    print(leftright1)
    backward1()
  elif userInput == "backward":
    print("You are now outside of the court facing the team area. There is a elevator down in front of you and to the side the locker areas for the team.")
    backward1()
  else: 
    print("Please enter a valid option.")


