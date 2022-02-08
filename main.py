'''
Noah Lilly
Programming Fundamentals
David Rios
2-4-22
'''
YourHp = 10
TheirHp = 20
damage = 1
damaged = 0

#imports
import replit
import time
import random

#colors
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
white_back="\033[0;47m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
reset = "\033[0m"

#Methods
def outside():
        replit.clear()
        print(Red+"You left."+reset)
        time.sleep(1)
        Sleep()
        print("Now, where do you go?")
        Sleep()
        print("(1) - Back Inside")
        Sleep()
        print("(2) - To Your Home")
        Sleep()
        print("(3) - Go to McDonalds")
        Sleep()
        Leave = input("Go where?: "+Blue)
        if Leave == "1":
                restart()
        if Leave == "2":
                Sleep()
                print(Red+"You don't have a home"+reset)
                time.sleep(1)
                outside()
        if Leave == "3":
                Sleep()
                print(Red+"You don't see a McDonalds around, only Wendy's..."+reset)
                time.sleep(1)
                outside()
        else:
                Sleep()
                print("Please input a valid option.")
                time.sleep(1)
                outside()

def restart():
        time.sleep(1)
        replit.clear()
        print(reset+"Hello, welcome to "+Blue+"Wendy's!")
        time.sleep(1)
        Sleep()
        All()
def TheirTurn():
        global YourHp
        global TheirHp
        global damaged
        global damage
        replit.clear()
        print(Red+"Manager's Turn!"+reset)
        Sleep()
        Attacked = random.randint(1, 5)
        Attacked = Attacked - damaged
        if Attacked < 1:
                Attacked = random.randint(0, 2)
        print("The manager did "+(str(Attacked))+" damage.")
        YourHp = YourHp - Attacked
        time.sleep(1)
        if YourHp <= 0:
                Sleep()
                print(Red+"You lost and were slapped by the manager."+reset)  
                time.sleep(1)
                YourHp = 10
                TheirHp = 20
                damage = 1
                damaged = 0             
                restart()     
        else:
                Fight()
def Fight():
        global damage
        global damaged
        global YourHp
        global TheirHp
        replit.clear()
        print("Boss Fight!")
        time.sleep(1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Manager: "+(str(TheirHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(1, 5) 
                Attacking = Attacking + damage
                if Attacking > 15:
                        Attacking = random.randint(10, 15)
                print(reset+"You did "+(str(Attacking))+" damage.")
                TheirHp = TheirHp - Attacking 
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print("You called the manager a meanie.")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(2, 3)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print("You defended youself.")
                Sleep()
                time.sleep(1)
                print("Manager's attacks do less damage now")
                damaged = damaged + random.randint(2, 3)
                time.sleep(1)
        if TheirHp <= 0:
                Sleep()
                print(Blue+"You beat the manager!")
                time.sleep(1)
                YourHp = 10
                TheirHp = 20
                damage = 1
                damaged = 0
                restart()
        else:
                TheirTurn()
def Option1():
        print("(1) - Order a Big Mac.")

def Option2():
        print("(2) - Escape!")

def Option3():
        print("(3) - I WANT TO SPEAK TO YOUR MANAGER!")

def Option4():
        print("(4) - Wait.")

def Option5():
        print("(5) - Leave.")

def Sleep():
        time.sleep(0.1)
        print("")

def All():
        print(reset+"What can I get for you?")
        time.sleep(1)
        Sleep()
        Option1()
        Sleep()
        Option2()
        Sleep()
        Option3()
        Sleep()
        Option4()
        Sleep()
        Option5()
        Sleep()
        Answer = (input("Input selection here: "+Blue))
        Sleep()
        if Answer == "1":
                replit.clear()
                print(reset+"Sir, this is a wendy's.")
                time.sleep(1)
                Sleep()
                print("Please go away.")
                time.sleep(1)
                restart()
        if Answer == "2":
                replit.clear()
                print(reset+"You look for a way to escape the Wendy's")
                time.sleep(1)
                Sleep()
                print("You see two ways to escape, (1) the employee's door, (2) the vents.")
                time.sleep(1)
                Sleep()
                Answer2 = input("Which do you choose: "+Blue)
                if Answer2 == "1":
                        Sleep()
                        print(reset+"You go in the employee's door...")
                        time.sleep(1)
                        Sleep()
                        print("There was an employee right infront of the door!")
                        time.sleep(1)
                        Sleep()
                        print("You got caught and brought to the manager.")
                        time.sleep(1)
                        Sleep()
                        print(Red+"The manager slaps you.")
                        time.sleep(1)
                        restart()
                if Answer2 == "2":
                        Sleep()
                        print(reset+"You went into the vents...")
                        time.sleep(1)
                        Sleep()
                        print("You made your way out of the vents and found the managers secret...")
                        time.sleep(1)
                        Sleep()
                        print("You need to get out of there fast!")
                        time.sleep(1)
                        Sleep()
                        print("There is a door in front of you, it has a keypad on it.")
                        time.sleep(1)
                        Sleep()
                        Answer3 = input("Enter (something) in the keypad: "+Blue)
                        if Answer3 == "something":
                                Sleep()
                                print(reset+"It opened!")
                                time.sleep(1)
                                Sleep()
                                print(Red+"The manager was standing right in front of the door, he slaps you.")
                                time.sleep(5)
                                restart()
                        if Answer3 == "_":
                                Sleep()
                                print(reset+"It opened!")
                                time.sleep(1)
                                Sleep()
                                print(Red+"The manager was standing right in front of the door, he slaps you.")
                                time.sleep(5)
                                restart()
                        else:
                                Sleep()
                                print(reset+"It didn't work!")
                                time.sleep(1)
                                Sleep()
                                print(Red+"The manager walks in and slaps you.")
                                time.sleep(2)
                                restart()
                else:
                        Sleep()
                        print(Red+"Because of your failure to pick one of the options, the manager came and slapped you.")
                        time.sleep(5)
                        restart()
        if Answer == "3":
                replit.clear()
                print(Red+"Sir, I AM THE MANAGER!"+reset)
                time.sleep(2)
                replit.clear()
                print("           ")
                time.sleep(0.1)
                replit.clear()
                print("|         |")
                time.sleep(0.1)
                replit.clear()
                print("||       ||")
                time.sleep(0.1)
                replit.clear()
                print("|||     |||")
                time.sleep(0.1)
                replit.clear()
                print("||||   ||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||||||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||F|||||")
                time.sleep(0.1)
                replit.clear()
                print("|||| Fi||||")
                time.sleep(0.1)
                replit.clear()
                print("|||s Fig|||")
                time.sleep(0.1)
                replit.clear()
                print("||ss Figh||")
                time.sleep(0.1)
                replit.clear()
                print("|oss Fight|")
                time.sleep(0.1)
                replit.clear()
                Fight()
                
        if Answer == "4":
                replit.clear()
                print(reset+"You wait...")
                time.sleep(5)
                print("You wait some more...")
                time.sleep(5)
                print("You wait even longer...")
                time.sleep(5)
                print("You wait impatiently...")
                time.sleep(5)
                print(Red+"You give up."+reset)
                time.sleep(1)
                restart()
        if Answer == "5":
                outside()
        else:
                Sleep()
                print("Please input a valid option.")
                time.sleep(1)
                restart()

#Code starts here
print("Hello, welcome to "+Blue+"Wendy's!"+reset)
time.sleep(1)
Sleep()
All()