##Created by Ryan Tolentino
##@RT_Design
## May 19,2016
## Guithix, Saradomin, and Zamorack

from sys import exit
import time

def zamorakRoom():
    print("You enter the room and step inside to see complete darkeness.\n The door suddenly slams shut... thud\nYou begin to panic and and instantly pull on the door handle\nThe door handle snaps off.\nWhile you are facing the door the entire room lights up in flame\nThen from the flames a large figure approaches.\nThe figure stood about eight feet tall and has red wings that almost look like the devil..\nThe figure halts about 20 paces in front of you\nIt then spoke, I am Zamorak god of chaos, with the elements of destruction and power\nIf you choose this path you must drink the Zamorak wine and devour this human heart")
    
    while True:
        drink = input("Yes/No:Do you drink the Zamorack wine and eat the Zamorack heart: ")

        if drink == "Yes" :
            print("You grab the jug of wine in your left hand and pick up the bloody heart in your right\nand shove the heart down your throat and rise it off with the wine you suddenly\nbecome light headed and stumble into the fire\nYou then wake in a dark room shirtless and branded with a giant red w on your chest\nYou then see a bright red orb light up in the center of the room\nYou race over to the orb and the orb asks you ")
            die = int(input (" How many worlds do you destory?[0-20]: "))
            if die >= 10:
                print("You are too evil and you have chosen the right path you may now\nenter the gold room.")
                goldRoom()
            elif die < 10:
                dead("You are too soft and you have chosen the wrong path... The only way out is death")
            else:
                print("Error: you did not enter a number")
        elif drink == "No" :
            print("This is not for me you scream you race over to the door and kick it open and slam the door behind you")
            darkRoom()
        else:
            dead("Error not a correct response")
            

def guthixRoom():
    print ("You enter the room and step inside to see complete darkeness.\nThe door suddenly slams shut... thud\nYou begin to panic and and instantly pull on the door handle\nThe door handle snaps off.\nwhile you are facing the door the entire room lights up in green flame\nThen from the flames a large figure approaches.\nThe figure stood about eight feet tall and has green wings...\nThe figure halts about 20 paces in front of you\nIt then spoke, I am Guthix god of balance I am not good or evil\nIf you choose this path you must walk this tight rope over the green flame. ")

    while True:
          drink = input("Yes/No:Do you walk the tight rope over the green flame?: ")

          if drink == "Yes" :
              print("You inch forward and start to walk to tight rope and suddenly Guthix cuts the tight rope and you fall helplessly\ninto the green flame.\nYou then wake in a dark room shirtless and branded with a giant green flame on your chest\nYou then see a bright green orb light up in the center of the room\nYou race over to the orb and the orb asks you")
              die = int(input("In order to kill 50 terrible people some innocent people have to die as well how many innocent people die?"))
              if die >= 10:
                  print("You are well balanced and understand that the wolrd needs balance you have chosen the right path you may now\nenter the gold room.")
                  goldRoom()
              elif die < 10:
                  dead("prompt you are not balanced enough. The world needs balance and you have not chosen the right path The only way out is death")
              else:
                  print("Error: inncorrect response")
          elif drink == "No" :
              print("This is not for me you scream you race over to the door and kick it open and slam the door behind u")
              darkRoom()
          else:
            dead("Error not a correct response")
            
            
            
            
            
def saradominRoom():
    print("You enter the room and step inside to see complete darkeness.\nThe door suddenly slams shut... thud\nYou begin to panic and and instantly pull on the door handle\nThe door handle snaps off.\nwhile you are facing the door the entire room lights up in blue flames\nThen from the flames a large figure approaches.\nThe figure stood about eight feet tall and has blue wings...\nThe figure halts about 20 paces in front of you\nIt then spoke, I am Saradomin god of order and wisom\nIf you choose this path you must drink the Wine of Saradomin  ")
    while True:
         drink= input("Yes/No:Do you drink the Saradomin wine: ")
         if drink == "Yes" :
             print("You then awake in a dark room shirtless and branded with a giant yellow star on your chest\nYou then see a bright blue orb light up in the center of the room\nYou race over to the orb and the orb asks you")
             die = int(input("There are 50 people in a room how many people in the room surivive."))
             if die >= 49:
                 print("You are well balanced and understand that the world needs order and wisdom you have chosen the right path you may now\nenter the gold room.")
                 goldRoom()
             elif die <= 50:
                 print("you are not balanced enough. The world needs balance and you have not chosen the right path The only way out is death I'm sorry my son...")
             else:
                 print("Error: inncorrect response")
         elif drink == "No":
             print("This is not for me you scream you race over to the door and kick it open and slam the door behind u")
             darkRoom()
         else:
            dead("Error not a correct response")
                       
                       
def goldRoom():
    print("You open the door to the gold room and seen mountains of gold...")
    gold = input(" How many gold pieces do you take? [0-100]:  ")

    if "0" in gold or "1" in gold:

        how_much = int(gold)
    else: dead("You did not pick a number")

    if how_much < 50:
        print ("You're not Greedy.... You suddenly awake naked under a tree in Lumbridge")
        exit(0)
    else:
        dead("You're Greedy... You are locked in the gold room with all the gold for the rest of eternity\nThere is no escape the only way to exit is to kill yourself.")
        


def dead(why):
    print(why)
    exit(0)


def darkRoom():
    print("There are three doors above each door is a bright shinning light\n The door to the left has a red beaming light above the door and on the door is a giant w written in red...\n The door straight ahead had a light blue light above the door and on the door is a giant yellow four pointed star...\n The door to the right has a light green beaming light above the door and on the door is a giant green flame ...")
    door = input(" What door do you take? [Left,Straight,Right]: ")

    if door == "Left" :
        zamorakRoom()
    elif door == "Straight" :
        guthixRoom()
    elif door == "Right":
        saradominRoom()
    else:
        dead("You stumble around the room and fall on a stake")

def gameMenu():
    print(" Welcome")
    print("---------------------------------------------------------------------------------")
    play = input("Yes/No: Do you want to play Guithix, Saradomin, and Zamorack,\n created by Ryan Tolentino?: ")
    if play ==  "Yes":
        darkRoom()
    elif play == "No":
        exit(0)
    else:
        print("Error: Inncorect response")
        gameMenu()

gameMenu()

##Created by Ryan Tolentino
##@RT_Design
## May 19,2016
## Guithix, Saradomin, and Zamorack
