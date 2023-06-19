#Floatage game
print("Welcome to Floatage, the aim of Floatage is to dodge the fireworks coming to you. The amount of fireworks is randomly chosen.")
#Deicding rockets amount
import random
import time
ranNum = random.randint(1,4)
print("You MUST dodge " + str(ranNum) + " fireworks, you get 5 chances")

direction = ["left", "right", "staystill"]
print("Directions in this game: left, right, staystill")

#rocket1 = input("Rocket is coming fast on your left where do you go?")
#rocket2 = input("Rocket is coming fast on your right where do you go?")
#rocket3 = input("Rocket is coming fast on straight to you where do you go?")
#rocket4 = input("Rocket is coming fast on your left and right where do you go?")
#rocket5 = input("Rocket is coming fast on your left and directly to you where do you go?")

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
    sprint("Bang the firework has gone off")
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
