import json
import os
import threading
import time
import random
import textwrap
from pathlib import Path

# Automatically detects OS and clears the terminal at the start
os.system('clear' if os.name == 'posix' else 'cls')  


#===============================================VARIABLES=========================================================
#Typing animation speed
TextSpeed = 0.03
WIDTH = 120 
BOX_HEIGHT = 10
moveCounter = 0

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m" 
#===============================================VARIABLES=========================================================

#===============================================FUNCTION===========================================================
#Typing animation
def say(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(TextSpeed)
    print()

#Clear Terminal (Cross-platform)
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

#timer function for input
def timed_input(prompt, timeout=10):
    result = [None]
    
    def get_input():
        result[0] = input(prompt)
    
    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    
    if thread.is_alive():
        print("\nTime's up!")
        return None  # No input given
    return result[0]

# dedicated bag when not using render
def bag(bag_items):
    print("-" * WIDTH)
    print(f"  Bag: {', '.join(bag_items)}")
    print("-" * WIDTH)

#Screen function  <--- the main screen supposedly 
def render(bag_items, narration, options, timeout=None):
    clear()

    print("-" * WIDTH)
    print(f"  Bag: {', '.join(bag_items)}")
    print("-" * WIDTH)

    print()
    say(narration)
    print()

    print("_" * WIDTH)
    for option in options:
        print(f"|  {option.ljust(WIDTH - 4)}|")

    print("|" + "_" * (WIDTH - 2) + "|")

    print("-" * WIDTH)

    if timeout is None:
        return input("Choose: ").strip()
    else:
        return timed_input("Choose: ", timeout)

#singular box  <---- ignore this.
def SingleBox(text, ask_input=False, prompt=""):
    
    # Top border
    print("+" + "-" * (WIDTH - 2) + "+")
    
    # Empty rows on top for padding
    for _ in range(BOX_HEIGHT // 2 - 1):
        print("|" + " " * (WIDTH - 2) + "|")
    
    # Text row (centered)
    print(f"|  {text.center(WIDTH - 4)} |")
    
    # Empty row between text and input
    print("|" + " " * (WIDTH - 2) + "|")
    
    if ask_input:
        user_input = input(f"|  {prompt}")
        # Draw bottom AFTER input
        for _ in range(BOX_HEIGHT // 2 - 1):
            print("|" + " " * (WIDTH - 2) + "|")
        print("+" + "-" * (WIDTH - 2) + "+")
        return user_input
    else:
        for _ in range(BOX_HEIGHT // 2 - 1):
            print("|" + " " * (WIDTH - 2) + "|")
        print("+" + "-" * (WIDTH - 2) + "+")
        time.sleep(3)

#save checkpoint and load checkpoint functions (Cross-platform paths) 
def save_checkpoint(data, name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_file = os.path.join(base_dir, "SaveFile", f"{name}.json")
    with open(save_file, "w") as file:
        json.dump(data, file)
    print("                                                                                                      Game saved!")

def load_checkpoint(name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_file = os.path.join(base_dir, "SaveFile", f"{name}.json")
    if os.path.exists(save_file):
        with open(save_file, "r") as file:
            return json.load(file)
    return None

#related to checkpoint. basically the checkpoint numbering system.
def reached(Area, checkpoint_num):
    checkpoint = [None, "Nar1", "Nar2", "Nar3", "Nar4", "Nar5", "Nar6"]
    if Area is None:
        return True
    return checkpoint.index(Area) <= checkpoint_num

def main_menu():
    while True:
        temp = True
        say("1. New Game \n2. Load Game \n3. Delete Save")
        choice = input("Choose an option: ")

        while choice not in ["1", "2", "3"]:
            choice = input("Invalid choice. Please choose 1, 2, or 3: ")

        if choice == "1":   
            while temp == True:
                confirm = input("Please confirm that you want to start a new game (yes/no): ")

                confirm = confirm.lower()
                while confirm not in ["yes", "no", "y", "n"]:
                    confirm = input("Please confirm that you want to start a new game (yes/no): ")
                if confirm == "yes" or confirm == "y":
                    clear()
                    return None, None, [], "start"
                elif confirm == "no" or confirm == "n":
                    temp = False

        elif choice == "2":

            while temp == True:
                print("\n")
                print("Available save files:")
                for file in Path("SaveFile").glob("*.json"):
                    print(f" - {file.stem}")
                Name = input("Enter your name to load: ")
                save = load_checkpoint(Name)
                if save:
                    say("Save file found! Loading game...")
                    return save["name"], save["area"], save["bag"], save["path"]
                else:
                    say("No save file found with that name. Please try again.")
                    temp = False
                        
        elif choice == "3":

            while temp == True:
                print("Available save files:")

                for file in Path("SaveFile").glob("*.json"):
                    print(f" - {file.stem}")
                    
                Name = input("Enter your name to delete save: ")
                base_dir = os.path.dirname(os.path.abspath(__file__))
                save_file = os.path.join(base_dir,"SaveFile", f"{Name}.json")

                if os.path.exists(save_file):
                    os.remove(save_file)
                    say("Save file deleted.")
                    time.sleep(2)
                    clear()
                    break
                else:
                    say("No save file found with that name. Please try again.")
                    temp = False

def gameOver():
    input = input("Would you like to retry? (Yes : y/No : n): ")
    input2 = input.lower()

    while input2 not in ["y", "n"]:
        input = input("Invalid input. Please enter 'y' or 'n'")
        input2 = input.lower()
    
    if input2 == "y":
        pass
    #im gonna pause here please someone help figure how to loop it if not idc ill sitll do it
    

#===============================================FUNCTION===========================================================

#===============================================Story===========================================================

SingleBox("Welcome to the game!", ask_input=True, prompt="Press enter to start...")
Name, Area, bag_items, Path = main_menu()

#START  <-- finish
def intro():
    global Name 
    if Area is None:  # New Game
        say("You had a nightmare where you were chased by a mysterious figure in an unfamiliar area.")
        time.sleep(2)
        time.sleep(1.5)
        print("You got scared ", end = "", flush = True)
        time.sleep(2)
        say("and woke up.") 

        say("You look around to your surroundings.")
        time.sleep(1.5)
        say("The place was dark and cold. You're in a small room with white walls and a single bed.") 
        time.sleep(1.5)
        say("You don't remember a single thing…")
        time.sleep(1.5)
        say("Who are you? Where are you at?")
        time.sleep(3)
        Name = SingleBox("You see an ID tag with your face beside you", ask_input=True, prompt="Enter your name: ")

        #Letting the user confirm their name
        confirm = str(input("Confirm name? (yes : y/no : n): "))
        confirm2 = confirm.lower()
        while confirm2 not in ["y", "n"]:
            print("Invalid choice, please enter y/n")
            confirm = str(input("Confirm name? (y/n): "))
            confirm2 = confirm.lower()
        if confirm2 == "y":
            Name = Name
        elif confirm == "n":
            Name = input("Last try to enter your name: ")
    
        print("\n\n")
        say((("The ID Tag showing that you are known as " + Name).center(WIDTH)))
        save_checkpoint({"name": Name, "area": "Nar1", "bag":bag_items, "path": Path}, Name) #save
        time.sleep(3)

def nar1():
    if reached(Area, 1):
        while True:
            Action = render(bag_items=bag_items,
                narration="You heard a loud banging and scratching sound coming from through the hallway.\n" 
                "You decided to check on it. The light got cut off, where you find it hard to see what is up in front.\n" 
                "The hallway is covered by many scratches and blood. You feel extremely uncomfortable.\n" 
                "As you continue to walk down the hallway. You see a shadow up ahead, screeching and tearing something.\n" 
                "It has a body size that is similar to a size of buff gymnastic. What would you do?",
                options=["1. Approach to it slowly and silently", "2. Shout at it"])
            
            while Action not in ["1", "2"]:
                Action = input("Invalid choice. Please choose 1 or 2: ")

            if Action == "1":
                say("You slowly and silently approach to the shadow.")
                save_checkpoint({"name": Name, "area": "Nar2", "bag":bag_items, "path": Path}, Name) #save
                break
            elif Action == "2":
                say("You shout at the shadow. The shadow crawl quickly into your direction and jumped on you.")
                time.sleep(2)
                say("You got killed.")
                time.sleep(2)
                say("GAME OVER")
                time.sleep(3)
                exit()

def nar2():
    if reached(Area, 2):
        while True:
            Action = render(bag_items=bag_items,
                narration="You are trying to be as quiet as possible, hoping it won’t notice you.\n" 
                "You see a huge black-in-colored aliens biting and tearing apart body.\n" 
                "You got shocked and scared. You decided to leave that area but you stepped on a piece of glass on the floor.\n" 
                "YOU MADE A SOUND.\n" 
                "The alien look into your direction and start chasing you.\n" 
                "You start to run as fast as you can.\n" 
                "You see a corner ahead and take your chance to lost the monster.\n" 
                "There's a locker in front of you and a door just a few meters away.\n" 
                "What will you do? Hide now or try to get into the room and a risk getting caught by the monster.\n",
                options=["1.hide into the locker after the corner","2.Run into the room a few meters away"],timeout=10)
                
            if Action == None:
                say("you missed every hiding spot and got into a dead end" \
                "\nGame Over")
                time.sleep(3)
                exit()
            elif Action == "1":
                say("You hide in the locker and close the door." \
                "\nThe alien passed you" \
                "\nyou're saved.\nYou found an item in the locker and got into the room nearest to you.")
                if "weaponary_key" not in bag_items:
                    bag_items.append("weaponary_key")
                save_checkpoint({"name": Name,"area":"Nar3", "bag":bag_items, "path": Path},Name)
                break
            elif Action == "2":
                say("you got into the room before the monster pass the corner")
                save_checkpoint({"name": Name, "area": "Nar3", "bag":bag_items, "path": Path}, Name) #save
                break
            else:
                say("Invalid choice. Please choose 1 or 2.")

# #Story Continues
def nar3():
    if reached(Area, 3):
        if "weaponary_key" in bag_items:
            say("you found a key when you were hiding in the locker earlier! you keep it in case you need it later.")
            time.sleep(2)
        say("You are saved for now. you catch your breath and calm down.")
        time.sleep(2)
        moveCounter = 2
        while moveCounter > 0:
            Action = render(bag_items=bag_items,
                narration="You scan the room in search for anything useful.\n" \
                "There's a chest in the room. A bed. A table.",
                options=["1.Open the chest","2.Check the bed","3.Check the table"])
            
            if Action == "1":
                say("You opened the chest and found nothing but clothes. you didn't take it.")
                moveCounter -= 1
                time.sleep(3)
            elif Action == "2":
                say("You checked the bed and found a screwdriver. you take it with you.")
                if "screwdriver" not in bag_items:
                    bag_items.append("screwdriver")
                moveCounter -= 1
                time.sleep(3)
            elif Action == "3":
                say("You checked the table and found someone notes. It says 'NTW-2# ### high cha### #### CGT-22##.\n" \
                "You take notes of this.")
                if "Notes" not in bag_items:
                    bag_items.append("Notes")
                moveCounter -= 1
                time.sleep(3)
            else:
                say("Invalid choice. Please choose 1, 2, or 3.")
        say("You hear a scratching sound from the door.\n" \
        "You noticed a vent beside the chest.") 
        time.sleep(1)
        say("you went to the vent and hear a crashing noise behind you.\n" \
        "You pick up the pace")
        save_checkpoint({"name": Name, "area": "Nar4", "bag":bag_items, "path": Path}, Name)
        time.sleep(4) #save

#("Alien is still chasing you at the back!")
def nar4():
    global Path
    if reached(Area, 4):
        clear()
        bag(bag_items)
        say("you found an exit!")
        time.sleep(3)
        if "screwdriver" in bag_items:
            say("The vent door open and you crawled out of the vent.")
            Path = "weaponary_room"
            time.sleep(2)
        else:
            say("The vent door can't be open.\n" \
            "You tried other exit.")
            time.sleep(2)
            say("You found another exit and crawled out of the vent.")
            Path = "laboratory"
            time.sleep(2)
        save_checkpoint({"name": Name, "area": "Nar5", "bag":bag_items, "path": Path}, Name) #save

def nar5():
    if reached(Area,5):
        global Path
        clear()
        bag(bag_items)
        if Path == "weaponary_room":
            weaponary_room()
        if Path == "laboratory":
            laboratory()
        say("\nYou hear a sound coming from the vent.\n" \
        "You get out of the room quickly.")
        time.sleep(3)
        say("You see a big door and got into the room.\n" \
        "It was a big room, like a bridge or control room.")
        time.sleep(2)
        say("There's a shiny thing at the table")
        say("You found a keycard with a security labeled on it")
        time.sleep(3)
        save_checkpoint({"name":Name, "area":"Nar6", "bag":bag_items, "path":Path}, Name)
    
def nar6():
    if reached(Area,6):
        global Path
        clear()
        bag(bag_items)
        say("You take the keycard in case you need it")
        if "keycard" not in bag_items:
            bag_items.append("keycard")
        time.sleep(2)      
                
def weaponary_room():
    say("The room was in shambled.\n" \
    "Dead bodies and scattered weapon.\n" \
    "You know what you got to do.\n" \
    "There's gun from the guard, a chest, armour shelf")
    if "Notes" in bag_items :
        SingleBox("You see the chest has NTW-20 labeled on it")
        time.sleep(3)
    moveCounter = 2
    while moveCounter > 0:
        Action = render(bag_items=bag_items,
            narration="What will you do?",
            options=["1.Check the chest","2.Take the gun","3.Check the armour shelf"])
        
        if Action == "1":
            if "weaponary_key" in bag_items:
                say("The key you found earlier fits the chest.\n" \
                "You opened it and found NTW-20.\n" \
                "You took it with you.")
                if "NTW-20" not in bag_items:
                    bag_items.append("NTW-20")
                bag_items.remove("weaponary_key")
            else:
                say("The chest is locked.\n" \
                "You tried smashing it.")
                chance = random.random()
                if chance < 0.5:
                    say("You cracked the chest open and found NTW-20.\n" \
                    "you took it with you.")
                    if "NTW-20" not in bag_items:
                        bag_items.append("NTW-20")
                else:
                    say("you failed to open the chest.")
            moveCounter -= 1
        elif Action == "2":
            say("You took the gun with you.")
            if "gun" not in bag_items:
                bag_items.append("gun")
            moveCounter -= 1
        elif Action == "3":
            say("You checked the armour shelf and found a kevlar vest.") 
            if "vest" not in bag_items:
                say("You took it with you.")
                bag_items.append("vest")
            elif "vest" in bag_items:
                say("You already have a vest")
            time.sleep(2)
            moveCounter -= 1
        else:
            say("Invalid choice. Please choose 1, 2, or 3.")
            time.sleep(2)

def laboratory():
    say("You landed on your feet.\n" \
    "The room looks like a laboratory or some sort.\n" \
    "There's a broken incubator, messed up table, dead scientist")
    time.sleep(5)
    moveCounter =2
    while moveCounter > 0:
        Action = render(bag_items=bag_items,
            narration="What will you do?",
            options=["1.Check the incubator","2.Check the table","3.Check the scientist"])

        if Action == "1":
            say("You check out the incubator.\n" \
            "There is nothing interesting there other than green slimy liquid")
            moveCounter -= 1
            time.sleep(2)
        elif Action == "2":
            say("You check out the messy table and found some documents.\n" \
            "The alien name is __________ and its weakness is _________ .")
            if "documents" not in bag_items:
                bag_items.append("documents")
            moveCounter -= 1
            time.sleep(2)
        elif Action == "3":
            say("You check out the scientist.\n" \
            "The scientist was still alive surprisingly and grab your arm.\n" \
            "he says to take the documents before dying.\n" \
            "You take note of this.")
            moveCounter -= 1
            time.sleep(2)
        else:
            say("invalid choice. Choose 1, 2 or 3")
            time.sleep(2)

def security_room():
    say("You opened the door with the security card you found at the bridge")
    time.sleep(2)
    say("The room was a real messed.\n" \
    "It's like a massacre has happened here.")
    time.sleep(2)
    say("You checked the CCTV and see a jet at a dock and a monster walked past supplies room")
    say("There's a button that open up the dock, a key for FC-112 the jet at the dock and some sort of fuse.")
    time.sleep(5)
    moveCounter=3
    while moveCounter > 0:
        Action = render(bag_items=bag_items,
            narration="What will you do?",
            options=["1.press the dock button","2.take the key","3.take the fuse","4.Check the CCTV"])
        
        if Action == "1":
            say("the gate of the dock has opened.")
            if "gate_dock" not in bag_items:
                bag_items.append("gate_dock")
            moveCounter -= 1
            time.sleep(2)
        elif Action == "2":
            say("You take the jet key.")
            if "jet_key" not in bag_items:
                bag_items.append("jet_key")
            moveCounter -= 1
            time.sleep(2)
        elif Action == "3":
            say("You take the fuse with you.")
            if "fuse" not in bag_items:
                bag_items.append("fuse")
            moveCounter -= 1
            time.sleep(2)
        elif Action == "4":
            say("You checked the CCTV again.")
            time.sleep(2)
            say("The monster was at different place.")
            moveCounter -= 1
            time.sleep(2)
        else:
            say("invalid choice. Please choose 1, 2, 3 or 4")
            time.sleep(2)

def supply_room():
    say("You arrived at supplies room.")
    time.sleep(2)
    say("The room was a messed.")
    time.sleep(2)
    say("The ration food was splattered everywhere.\n" \
    "The ammunition and consumables has been wrecked")
    time.sleep(2)
    say("There's a box of bomb, smoke bomb and a used vest.")
    time.sleep(3)
    moveCounter = 2
    while moveCounter > 0:
        Action = render(bag_items=bag_items,\
            narration="What will you do?",
            options=["1.Check the box of bomb","2.Take the smokebomb","3.take the vest"])
        
        if Action == "1":
            say("You checked the box full of bomb")
            time.sleep(2)
            say("You take one of them.")
            if "bomb" not in bag_items:
                bag_items.append("bomb")
            moveCounter -= 1
            time.sleep(2)
        elif Action == "2":
            say("You take the smokebomb from the ground")
            if "smokebomb" not in bag_items:
                bag_items.append("smokebomb")
            moveCounter -= 1
            time.sleep(3)
        elif Action == "3":
            if "vest" in bag_items:
                say("you already have a vest.")
                time.sleep(2)
                say("You didn't take it")
            elif "vest" not in bag_items:
                bag_items.append("vest")
                say("You rip the vest out of the dead body.")
                time.sleep(2)
                say("You got a vest.")
            moveCounter -= 1
            time.sleep(2)
        else:
            say("Invalid choices")

def evacuation_room():
    global puzzle
    say("You entered the emergency evacuation room.")
    time.sleep(2)
    say("There an escaped pod but it's locked and needed a fuse ")
    if "fnotes" not in bag_items:
        bag_items.append("fnotes")
    while True:
        Action = render(bag_items=bag_items,
            narration="What would you do?",
            options=["1.try to open the escape pod","2.leave"])

        if Action == "1":
            puzzle = True
            continue #puzzle here

        elif Action == "2":
            say("You decided to leave")
            time.sleep(2)
            break
        else:
            say("Invalid choice. Please choose 1 or 2")
            time.sleep(2)

def ending():
    say("The Alien found you.")
    time.sleep(2)
    say("It is standing at the door, looking at you.")
    time.sleep(2)
    if "gate_dock" or "gun" or "NTW-20" and "smokebomb" in bag_items:   
        while True:    
            Action = render(bag_items=bag_items,
                narration="In spur of the moment,                         \n"\
                "You choose to run to",
                options=["1.Dock","2.Evacuation room","3.Security room"], timeout=10)
            
            if Action == "1":
                say("You run with all your might to the dock.")
                time.sleep(2)
                say("But the Alien is starting to catch up.\n" \
                "So you throw your smoke bomb to confuse the Alien.")
                time.sleep(2)
                bag(bag_items)
                print("\n")
                SingleBox("Throw the smoke bomb",ask_input=True,prompt="Press anything")
                time.sleep(2)
                print("------------------------------------------------------------------------------------------" \
                "----------")
                smoke()
                print("-----------------------------------------------------------------------------------------" \
                "-----------")
                time.sleep(3)
                clear()
                say("poof!") 
                time.sleep(1)
                say("A heavy cloud emerge and you go through it to lose the Alien")
                time.sleep(2)
                say("You got to the dock and head into the Jet\n" \
                "You didn't waste anytime and get it working.")
                time.sleep()
                say("The Alien jump to the jet and you throttle full speed.")
                time.sleep(1)
                say("The Alien grip loosen and it let go of the ship.")
                time.sleep(3)
                say("You take a deep breath sighing relief that this ordeal has gone.\n" \
                "You fly through the galaxy in searching for a hope that there's someone else out there.")
                time.sleep(5)
                clear()
                say("You Got 'Escaped' Ending")
                print("------------------------------------------------------------------------------------------" \
                "--------------------------------")
                jet()
                print("-----------------------------------------------------------------------------------------" \
                "--------------------------------")
                time.sleep(7)
                break

            elif Action == "2":
                say("You run with all your might to the evacuation room.")
                time.sleep(2)
                say("But the Alien is starting to catch up.\n" \
                "So you throw your smoke bomb to confuse the Alien.")
                time.sleep(2)
                bag(bag_items)
                print("\n")
                SingleBox("Throw the smoke bomb",ask_input=True,prompt="Press anything")
                time.sleep(2)
                print("------------------------------------------------------------------------------------------" \
                "--------------------------------")
                smoke()
                print("-----------------------------------------------------------------------------------------" \
                "--------------------------------")
                time.sleep(3)
                clear()
                say("poof!") 
                time.sleep(1)
                say("A heavy cloud emerge and you go through it to lose the Alien.")
                time.sleep(2)
                say("You run to the evacuation room to get to the escape pod.\n"\
                "The hallway that was seemingly short before feels longer now and the monster is gaining up on you.")
                time.sleep(1)
                say("You reach the escape pod!")
                time.sleep(1)
                if puzzle == False:
                    say("The door is jammed.")
                    time.sleep(1)
                    say("You tried to pry it open.")
                    time.sleep(2)
                    # puzzle 
                say("The door opened and you get inside.")
                time.sleep(1)
                say("You slammed the door shut and start turning on the escape pod")
                if "fuse" in bag_items:
                    say("The escape pod start running.")
                    time.sleep(1)
                    say("But...")
                    time.sleep(2)
                    say("All hope lost after the escape pod suddenly stop.")
                    time.sleep(2)
                    say("Your future seems bleak.")
                    time.sleep(1)

                say("the monster pried the door open and grab you. getting ready to slimed you up")
                time.sleep(1)
                say("You muster up all your strength to get your right arm free and stab the Alien eye with a pocket knife.\n" \
                "The Alien throw you off and shriek in pain.")
                time.sleep(1)
                say("You grab your weapon and ready to fight the monster.")
                #battle system
                                        
                say("The lifeless body of the Alien calm you down.")
                time.sleep(2)
                say("After a while, You stand up and go to the bridge slowly.")
                time.sleep(1)
                say("Each step was like lifting a heavy dumbell.")
            

            else:
                say("Invalid choice. Please choose 1, 2 or 3")


# Main part
intro()
nar1()
nar2()
nar3()
nar4()
nar5()

# art placeholder

def smoke():
    print("⠀⠀⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⢀⣀⣤⣤⣤⣤⣀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⠀\n \
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⠤⠤⢤⣄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀  \n \
    ⠀⠀⠀⠀⠀⢀⣤⡶⢛⡭⠖⠚⠛⡿⠶⢶⣿⣿⡿⠛⠛⣉⣀⣀⣀⠀⠉⠻⣷⣾⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀\n \
    ⠀⠀⠀⠀⣰⡿⢃⡼⠛⠀⠀⣀⣴⣶⣶⣾⣿⣿⣦⣘⣿⣿⣿⣿⣿⣿⣦⡄⠸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀ \n \
    ⠀⠀⠀⢰⣿⣁⠊⡋⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠛⠻⢿⣿⡿⢦⣄⡀⠀⠀⠀ \n \
    ⢠⣴⣤⣾⣿⢿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⣟⣀⣈⣿⣿⣦⣤⡄ \n \
    ⠈⠉⠉⠉⣻⠟⠉⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢻⣿⣿⣿⡟⠃ \n \
    ⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠙⣿⣿⠇⠀ \n \
    ⠀⠀⢀⠘⠀⠀⠀⠀⠦⢀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠛⠁⠀⠀ \n \
    ⠀⠀⢸⣆⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⢀⠇⠀⠀⠀ \n \
    ⠀⠀⠀⠙⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠀⠀⠀⠀⠈⠀⠀⠀⠀\n \
    ⠀⠀⠉⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣴⣶⣶⣦⡀⠀⠀⠉⠀⠀\n \
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⡿⠿⢿⣿⣿⠀⠀⠀⠀⠀\n \
    ⠀⠀⠀⠀⠀⠀⠀⢀⣤⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣿⣿⣦⣄⠀⠀⠀\n \
    ⠀⠀⠀⠀⠀⠴⠿⠿⠛⠓⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠉⠉⠛⠛⠛⠋⠀⠘⠛⠀⠀⠀\n \
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠟⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠛⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

def jet():
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣸⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢸⣿⣿⣿⣿⠐⠒⠲⠦⠤⣤⡀⠀⠀⠀⠀⠀⣰⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⣔⡲⠧⠦⠦⢶⣶⣠⣀⣀⣄⡀⠠⠀⠀⠂⢀⣀⣸⣿⣿⠿⢛⣡⠄⣠⣤⣶⣿⣷⠀⠀⠀⠀⣼⣿⣟⠈⠁⠒⠒⠒⠒⠢⠤⠤⠤⡄⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠒⠋⠀⠴⠌⠉⠁⠰⢟⣻⣷⣿⣿⣿⣿⣿⣿⣧⡀⢀⣾⣿⣿⣟⣁⣀⠀⠤⠤⠤⠄⠀⠀⠉⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣙⣽⣿⣷⣿⣿⣿⣿⣿⡿⠿⢍⣛⣟⣿⣾⣿⣿⣧⣄⣀⣀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠆⣀⣀⠔⠀⠀⠀⠀⢀⣤⣷⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⡟⠛⢮⠵⠞⠉⠉⠁⠀⠀⠀⠀⠀⠉⠁⠀⠀⢀⣁⣀⡀⠀⠀⠀⣠⠀⣤⡄\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠠⠆⠂⠐⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣰⣾⡿⠛⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣉⣈⣁⣠⣠⣬⡾⠋⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠰⣼⣿⣿⣿⣿⣿⣿⣿⣿⢟⣡⣾⣿⣿⣿⠧⠴⠒⠒⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉⠉⠉⠉⠁⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⣼⣿⣿⣿⣿⣿⣿⣿⣏⣴⣿⣿⢿⠯⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⡿⠁⢻⣿⣿⢟⢫⡕⡁⡴⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⣿⣿⣿⣿⠿⠋⣿⡋⠉⠀⠀⠀⢠⣾⡿⠅⠝⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⡿⠋⠁⡘⡘⠘⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣟⠍⣂⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n \
⠀⠀⠀⠀⠀⠀⠴⠿⠟⠛⠛⠁⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")