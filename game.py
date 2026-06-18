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

#Inventory
def show_inventory(inventory):
    if inventory:
        print(f"  🎒 Inventory: {', '.join(inventory)}")
    else:
        print("  🎒 Inventory: (empty)")
    print()

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
        input("")

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
            clear()
            return None, None, [], "start"
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
    input = input("Would you like to retry? (y/n): ")
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
    if Area is None:  # New Game
        say("You were having a dream where you were getting chase by something huge and black in an unfamiliar area.")
        say("You got scared and woke up.") 
        say("You look around to your surroundings.")
        say("The place was dark and cold. You're in a small room with white walls and a single bed.") 
        say("You doesn't remember a single thing…")
        say("Who are you? Where are you at?")
        time.sleep(3)
        Name = SingleBox("You see an ID tag with your face beside you", ask_input=True, prompt="Enter your name: ")

        #Letting the user confirm their name
        confirm = str(input("Confirm name? (y/n): "))
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
            else:
                pass

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
                "\nyou're saved\nYou found an item in the locker and got into the room nearest to you")
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


# say("Alien is still chasing you at the back!")
def nar4():
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
        if Path == "weaponary room":
            clear()
            bag(bag_items)
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
                        bag()
                    else:
                        pass

# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# Door = input("Enter “Close the door”. ")
# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# say("You are temporary safe. At least for now.")
# say("But the alien is still trying to get in.")
# say("Dealing massive damage onto the door. Biting. Scratching. Screaming through the door.")
# say("The door won’t last any longer…")
# say("You saw a locker and a vent.")
# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# Escape = input("Would you hide in the locker or the vent? [Locker/Vent] ")
# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# if Escape == "Vent":
#     say("You unscrew the vent and crawled inside.")
#     say("The alien broke the door and entered the room.")
#     say("Without hesitation, alien rush into the vent.")
#     say("You are trying to crawl as fast as you can, hoping that the alien won’t catch you.")
#     say("The alien manage to catch up with you in few seconds.")
#     say("You got killed.")
#     say("GAME OVER")
#     exit()
# else:
#     print("--------------------------------------------------------------------------------------------------------------------------------------------")
#     Unscrew = input("Would you unscrew the vents before you hide in the locker? [Yes/No] ")
#     print("--------------------------------------------------------------------------------------------------------------------------------------------")
#     if Unscrew == "Yes":
#         say("You unscrew the vent and hide in the locker.")
#     else:
#         say("You decided to not unscrew the vent.")
#         say("The alien broke the door and entered the room.")
#         say("The alien looked around.")
#         say("The alien targeted onto the locker.")
#         say("The alien bite opened the locker and saw you inside.")
#         say("You got killed.")
#         say("GAME OVER")
#         exit()

# say("The alien broke the door and entered the room.")
# say("The alien heard the sound of you unscrewing the vent.")
# say("The alien ran past your locker and rushed into the vent.")
# say("Leaving you alone in the room.")
# say("You survived. It was a close call.")
# say("You got out from the locker and you saw a dead body of a worker.")
# say("There is a keycard on his hand.")
# say("--------------------------------------------------------------------------------------------------------------------------------------------")
# Keycard = input("Would you take the keycard? [Yes/No] ")
# say("--------------------------------------------------------------------------------------------------------------------------------------------")
# if Keycard == "Yes":
#     say("You took the keycard and put it in your pocket.")
# else:
#     say("You left the keycard.")
    
# #Map
# say("You saw a map on the wall.")
# say("A map for this spaceship!")
# say("You rip off the map and put it in your pocket.")
# say("YOU GOT A MAP!")

# #Flesh
# say("After you got out from the hallway there is a kitchen.")
# say("You went inside and you saw a flesh. ")
# say("It looks like a piece of human flesh…?")
# say("--------------------------------------------------------------------------------------------------------------------------------------------")
# Flesh = input("Would you bring the flesh along? [Yes/No] ")
# say("--------------------------------------------------------------------------------------------------------------------------------------------")
# if Flesh == "Yes":
#     say("You took the flesh.")
# else:
#     say("You decided to not take the flesh.")

# #Next Area
# say("The maps shows few places that might be useful for you to go.")
# say("[Control Panel]")
# say("[Emergency Evacuation Dock]")
# say("[Ventilation Control]")
# say("[Laboratory]")
# say("--------------------------------------------------------------------------------------------------------------------------------------------")
# Area = input("Where would you like to go next? ")
# say("--------------------------------------------------------------------------------------------------------------------------------------------")

# #Hard Part
# if Area == "Control Panel":
#     say("You went to the Control Panel.")
#     say("You found a communication devices that you could look for help.")
#     say("The captain’s body is died left on the captain’s chair…")
#     say("You got a high access keycard from the captain’s body.")
#     say("You were able to call for help but password is required.")
#     print("--------------------------------------------------------------------------------------------------------------------------------------------")
#     Password = input("Enter the password: ")
#     print("--------------------------------------------------------------------------------------------------------------------------------------------")
#     if Password == "FCI-2026":
#         say("You entered the correct password.")
#         say("You called for help by telling them what you had been facing on the spaceship.")
#         say("You received a response from the other side, a coordinate of your home, Earth.")
#     else:
#         say("You entered the wrong password.")
#         print("--------------------------------------------------------------------------------------------------------------------------------------------")
#         Decision = input("What would you like to do next? [Try again/Go to another area] ")
#         print("--------------------------------------------------------------------------------------------------------------------------------------------")
#         if Decision == "Try again":
#             say("You try to enter the password again.")
#             say("You entered the wrong password.")
#             say("You triggered the safety alarm. The alien heard the alarm and rushed into the control panel room.")
#             say("You got killed.")
#             say("GAME OVER")
#             exit()
#         else:
#             say("You decided to go to another area instead of trying to enter the password again.")
#             say("[Control Panel]")
#             say("[Emergency Evacuation Dock]")
#             say("[Ventilation Control]")
#             say("[Laboratory]")
#             print("--------------------------------------------------------------------------------------------------------------------------------------------")
#             Area = input("Where would you like to go next? ")
#             print("--------------------------------------------------------------------------------------------------------------------------------------------")
  

# elif Area == "Emergency Evacuation Dock":
#     say("You went to the Emergency Evacuation Dock.")

# elif Area == "Ventilation Control":
#     say("You went to the Ventilation Control Room.")
#     say("You saw a battery at the corner of the room.")
#     say("Then you heard noises coming out from the vent… ")
#     say("The alien crawl through the vent and ended up at the ventilation control room!")

# elif Area == "Laboratory":
#     say("You went to the Laboratory.")
#     say("There is a tiny note left on a table with 6-digit PIN, is it some kind of password?")
#     say("It written on the note: FCI-2026")
#     say("There is a locked door in the laboratory.")


# Main part
intro()
nar1()
nar2()
nar3()
nar4()

# art placeholder



