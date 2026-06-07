import json
import os
import threading
import time
os.system('cls')

#===============================================VARIABLES=========================================================
#Typing animation speed
TextSpeed = 0.025
WIDTH = 120 
BOX_HEIGHT = 10

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m" 

#===============================================Example of usage (Please read to understand)==========================================================

# choice = render(   <--- the choice function
#     bag_items=["Key"],
#     narration="You are in a dark room.",
#     options=["Go left", "Go right"]
# )

# if choice == "Go left":

# print(f"{RED}You took damage!{RESET}") <--- example to change text color
# say(f"{CYAN}{narration.rjust(WIDTH)}{RESET}")
# print(f"{CYAN}You are in a dark room.{RESET}")

# save_checkpoint({"name": Name, "area": "Nar1", "bag": []}, Name)

# # After they pick a room
# save_checkpoint({"name": Name, "area": "Laboratory", "bag": bag_items}, Name)

# # After they pick up an item
# save_checkpoint({"name": Name, "area": "Laboratory", "bag": bag_items}, Name)

# Gives player 10 seconds to answer
# choice = timed_input("  Choose: ", timeout=10)

# if choice is None:
#     say("You hesitated too long... something bad happens!")
# elif choice == "Go left":
#     say("You went left!")

#===============================================FUNCTION===========================================================
#Typing animation
def say(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(TextSpeed)
    print()

#Clear Terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

#Screen function  <--- the main screen supposedly 
def render(bag_items, narration, options):
    clear()
    
    # --- TOP: Bag ---
    print("-" * WIDTH)
    print(f"  Bag: {', '.join(bag_items)}")
    print("-" * WIDTH)
    
    # --- MIDDLE: Narration (right-aligned or centered) ---
    print()
    say(narration.rjust(WIDTH))  # or .center(WIDTH)
    print()
    
    # --- BOTTOM: Options box ---
    print("_" * WIDTH)
    for option in options:
        print(f"|  {option.ljust(WIDTH - 4)}|")
    
    # fill empty rows to keep box shape
    filled = len(options)
    for _ in range(4 - filled):
        print(f"|{' ' * (WIDTH - 2)}|")
    
    print("|" + "_" * (WIDTH - 2) + "|")

        # --- INPUT: Outside the box ---
    print("-" * WIDTH)
    choice = input("  Choose: ").strip()   
    return choice  # return it so you can use it
# choice = timed_input(f"  Choose ({timeout}s): ", timeout=10) <-- will changed
# return choice  

#singular box  <---- ignore this.
def SingleBox(text, ask_input=False, prompt=""):
    
    # Top border
    print("+" + "-" * (WIDTH - 2) + "+")
    
    # Empty rows on top for padding
    for _ in range(BOX_HEIGHT // 2 - 1):
        print("|" + " " * (WIDTH - 2) + "|")
    
    # Text row (centered)
    say(f"|  {text.center(WIDTH - 4)} |")
    
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

#save checkpoint and load checkpoint functions  
def save_checkpoint(data, name):
    save_file = f"{name}.json"
    with open(save_file, "w") as f:
        json.dump(data, f)
    print("                                                                                                      Game saved!")

def load_checkpoint(name):
    save_file = f"{name}.json"
    if os.path.exists(save_file):
        with open(save_file, "r") as f:
            return json.load(f)
    return None

# Player makes a choice
# Area = render(bag_items, narration, options)

# Save right after
# save_checkpoint({
#     "name": Name,
#     "area": Area,
#     "bag": bag_items,
# }, Name)

# Name = input("Enter your name: ")
# save = load_checkpoint(Name)

# if save:
#     choice = SingleBox("Save file found! Continue?", ask_input=True, prompt="Y/N: ")
#     if choice.upper() == "Y":
#         Area = save["area"]
#         bag_items = save["bag"]
#===============================================Story===========================================================x``

#START  <-- finish
say("You were having a dream where you were getting chase by something huge and black in an unfamiliar area.")
say("You got scared and woke up.") 
say("You look around to your surroundings.")
say("The place was dark and cold. You're in a small room with white walls and a single bed.") 
say("You doesn't remember a single thing…")
say("Who are you? Where are you at?")
time.sleep(5)
Name = SingleBox("You see an ID tag with your face beside you", ask_input=True, prompt="Enter your name: ")
print("\n\n")
say((("The ID Tag showing that you are known as " + Name).center(WIDTH)))

# Save1
save_checkpoint({
    "name": Name,
    "area": "Nar1",
    "bag": [],
}, Name)
time.sleep(3)

# #Begin  <---this one next
# say("You heard a loud banging and scratching sound coming from through the hallway.")
# say("You decided to check on it. The light got cut off, where you find it hard to see what is up in front.")
# say("The hallway is covered by many scratches and blood. You feel extremely uncomfortable.")
# say("As you continue to walk down the hallway. You see a shadow up ahead, screeching and tearing something.")
# say("It has a body size that is similar to a size of buff gymnastic.")
# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# Action = input("What would you do? [Approach to it slowly and silently/Shout at it] ")
# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# if Action == "Shout at it":
#     say("You shout at the shadow. The shadow crawl quickly into your direction and jumped on you.")
#     print("You got killed.")
#     print("GAME OVER")
#     exit()
# else:    
#     say("You slowly and silently approach to the shadow.") 

# #Story Continues
# say("You are trying to be as quiet as possible, hoping it won’t notice you.")
# say("You see a huge black-in-colored aliens biting and tearing “your crewmates…?” bodies.")
# say("You got shocked and scared. You decided to leave that area but you stepped on a piece of glass on the floor.")
# say("YOU MADE A SOUND.")
# say("The alien look into your direction and scream at you!!!")
# say("The alien starts to chase you. You begin to run… Very… Very fast…")
# say("You are running as fast as you can, trying to get away from the alien.")
# say("In this dark environment, you are unable to tell your current location, nor knowing where you can hide.")
# say("You run everywhere where you are able to. The alien is chasing aggressively on all fours.") 
# say("You ended up in a long hallway where it leads to a room at the end.")
# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# Locker = input("During the run, you see a locker. [Hide/Run] ")
# print("--------------------------------------------------------------------------------------------------------------------------------------------")
# if Locker == "Hide":
#     say("You hide in the locker and close the door.")
#     say("The alien destroyed the locker as it is running through the hallway.") 
#     print("You got killed.")
#     print("GAME OVER")
#     exit()
# else:
#     say("You decided to run into the room at the end instead of hiding in the locker.")

# #Story Continues
# say("Alien is still chasing you at the back!")
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






# art placeholder