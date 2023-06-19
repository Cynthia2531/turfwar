#importing time
import sys, time

def slowprint(s) :
        for c in s + '\n':
            sys.stdout.write (c)
            sys.stdout.flush()
            time.sleep(1./ 200)
            
import time, sys
from random import randrange
import random
import time

#ascii art and info
welcome = """

 __      __       .__                                  __             __  .__             ___________             _____   __      __               
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   _/  |_|  |__   ____   \__    ___/_ __________/ ____\ /  \    /  \_____ _______ 
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   __\  |  \_/ __ \    |    | |  |  \_  __ \   __\  \   \/\/   /\__  \\_  __  \\
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |  | |   Y  \  ___/    |    | |  |  /|  | \/|  |     \        /  / __ \|  | \/
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   |__| |___|  /\___  >   |____| |____/ |__|   |__|      \__/\  /  (____  /__|   
       \/       \/          \/            \/     \/                            \/     \/                                        \/        \/       

"""
error = """
___________              __       _____       .__.__             .___           
\__    ___/____    _____|  | __ _/ ____\___   |__|  |   ____   __| _/           
  |    |  \__  \  /  ___/  |/ / \   __\__  \  |  |  | _/ __ \ / __ |            
  |    |   / __ \_\___ \|    <   |  |   / __ \|  |  |_\  ___// /_/ |            
  |____|  (____  /____  >__|_ \  |__|  (____  /__|____/\___  >____ |            
               \/     \/     \/             \/             \/     \/            
  _________                                          _____     .__  .__         
 /   _____/__ __   ____  ____  ____   ______ _______/ ____\_ __|  | |  | ___.__.
 \_____  \|  |  \_/ ___\/ ___\/ __ \ /  ___//  ___/\   __\  |  \  | |  |<   |  |
 /        \  |  /\  \__\  \__\  ___/ \___ \ \___ \  |  | |  |  /  |_|  |_\___  |
/_______  /____/  \___  >___  >___  >____  >____  > |__| |____/|____/____/ ____|
        \/            \/    \/    \/     \/     \/                       \/      
"""
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
gameexplain = """
Welcome, you have entered through a rift in the multiverse
to help Grumbot (an AI super computer) expand his knowledge
to help his campaign 'Mumbo for Mayor'. Through this rift you
have ended up back in time to September 2019 when the Turf War
storyline in Hermitcraft Season 7 has just started.
You will be put through 5 different mini games that different
Hermits made in order to solve this mystery of whether grass or
mycellium should be the grass in the shopping district.
          HEP VS Mycellium Reistance who will win. . . .

What you must do is:
In Dodgeball you must find and collect a bottle of Moo-Pop.
In Floatage you must dodge the fireworks coming for you.
In A-Maze you must make your way through the map and collect 10 mycellium.
In Wack-A-Stack you must break an armour stand.
In Showdown you have to collect the grass sources block whilst avoiding cobwebs.
"""
#code for welcome starts
print(welcome)
name = input("What is your name?")
print("Hello " + name)

wannaplay = input("Do you want to play (Y or N)?")

if wannaplay == "Y":
    print("YAY your not leaving ME!!!! •‿•")

elif wannaplay == "N":
    print(error)
    print("Continuing to game")

else:
    print("The only vaild answer is Y or N \nYou don't want to LEAVE rIgHt? ⊙︿⊙")
    print(error)
    print("Continuing to game")

print(gameexplain)   

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
    
#Floatage game
print("Welcome to Floatage, the aim of Floatage is to dodge the fireworks coming to you. The amount of fireworks is randomly chosen.")
#Deicding rockets amount
import random
import time
ranNum = random.randint(1,4)
print("You MUST dodge " + str(ranNum) + " fireworks, you get 5 chances")

direction = ["left", "right", "staystill"]
print("Directions in this game: left, right, staystill")

#starting a score
score = 0

#Rockets are coming
if score < ranNum: 
#rocket1
    rocket1 = input("Rocket is coming fast on your left where do you go?")
    print("Bang the firework has gone off")

    if rocket1 == "staystill" or rocket1 == "right":
        print("Well done added one point to your score.")
        score = score + 1
    elif rocket1 == "left":
        print("You have blown up into pieces, fireworks aren't nice clothes")
    else:
        print("AFKing isn't allowed on this game. What are you doing?")
    print("Your score now is " + str(score) + ".")
    
    time.sleep(3)
if score < ranNum:
#rocket2
    rocket2 = input("Rocket is coming fast on your right where do you go?")
    print("Bang the firework has gone off")

    if rocket2 == "left" or rocket2 == "staystill":
        print("Well done added one point to your score.")
        score = score + 1
    elif rocket2 == "right":
        print("You have blown up into pieces, fireworks aren't nice clothes")
    else:
        print("AFKing isn't allowed on this game. What are you doing?")
    print("Your score now is " + str(score) + ".")
    
time.sleep(3)
if score < ranNum:
#rocket3
    rocket3 = input("Rocket is coming fast on straight to you where do you go?")
    print("Bang the firework has gone off")
    if rocket3 == "left" or rocket3 == "right":
        print("Well done added one point to your score.")
        score = score + 1
    elif rocket3 == "staystill":
        print("You have blown up into pieces, fireworks aren't nice clothes")
    else:
       print("AFKing isn't allowed on this game. What are you doing?")
    print("Your score now is " + str(score) + ".")
    
time.sleep(3)
if score < ranNum:
#rocket4
    rocket4 = input("Rocket is coming fast on your left and right where do you go?")
    print("Bang the firework has gone off")
    if rocket4 == "staystill":
        print("Well done added one point to your score.")
        score = score + 1
    elif rocket4 == "left" or rocket4 == "right":
        print("You have blown up into pieces, fireworks aren't nice clothes")
    else:
        print("AFKing isn't allowed on this game. What are you doing?")
    print("Your score now is " + str(score) + ".")       

time.sleep(3)
if score < ranNum:
#rocket5
    rocket5 = input("Rocket is coming fast on your left and directly to you where do you go?")
    print("Bang the firework has gone off")
    if rocket5 == "right":
        print("Well done added one point to your score.")
        score = score + 1
    elif rocket5 == "left" or rocket5 == "right":
        print("You have blown up into pieces, fireworks aren't nice clothes")
    else:
        print("AFKing isn't allowed on this game. What are you doing?")
    print("Your score now is " + str(score) + ".")
    
time.sleep(3)
print("You have won Floatage, great job.")
print("""Now you have completed this game you have won the turf war
      for the mycellium resistance. You have help Grumbot with his
      campaign and best of all the shopping district will be mycellium.
      Just joking Its all about the principle so it still going to be grass
      its looks better anyways. THE END """)
      

