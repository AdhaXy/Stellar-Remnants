import json
import os
import time
os.system('cls')

#Intro Part
print("You were having a dream where you were getting chase by something huge and black in an unfamiliar area.")
time.sleep(5) 
print("You got scared and woke up.") 
print("You look around to your surroundings.")
print("It is very dark and very unfamiliar. It looks futuristic.") 
print("You doesn't remember a single thing…")
print("Who are you? Where are you at?")
print("You see an ID tag right beside you. You are…")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
Name = input("What is your name? ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
print("The ID Tag showing that you are known as " + Name)

#Begin
print("You heard a loud banging and scratching sound coming from through the hallway.")
print("You decided to check on it. The light got cut off, where you find it hard to see what is up in front.")
print("The hallway is covered by many scratches and blood. You feel extremely uncomfortable.")
print("As you continue to walk down the hallway. You see a shadow up ahead, screeching and tearing something.")
print("It has a body size that is similar to a size of buff gymnastic.")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
Action = input("What would you do? [Approach to it slowly and silently/Shout at it] ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
if Action == "Shout at it":
    print("You shout at the shadow. The shadow crawl quickly into your direction and jumped on you.")
    print("You got killed.")
    print("GAME OVER")
    exit()
else:    
    print("You slowly and silently approach to the shadow.") 

#Story Continues
print("You are trying to be as quiet as possible, hoping it won’t notice you.")
print("You see a huge black-in-colored aliens biting and tearing “your crewmates…?” bodies.")
print("You got shocked and scared. You decided to leave that area but you stepped on a piece of glass on the floor.")
print("YOU MADE A SOUND.")
print("The alien look into your direction and scream at you!!!")
print("The alien starts to chase you. You begin to run… Very… Very fast…")
print("You are running as fast as you can, trying to get away from the alien.")
print("In this dark environment, you are unable to tell your current location, nor knowing where you can hide.")
print("You run everywhere where you are able to. The alien is chasing aggressively on all fours.") 
print("You ended up in a long hallway where it leads to a room at the end.")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
Locker = input("During the run, you see a locker. [Hide/Run] ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
if Locker == "Hide":
    print("You hide in the locker and close the door.")
    print("The alien destroyed the locker as it is running through the hallway.") 
    print("You got killed.")
    print("GAME OVER")
    exit()
else:
    print("You decided to run into the room at the end instead of hiding in the locker.")

#Story Continues
print("Alien is still chasing you at the back!")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
Door = input("Enter “Close the door”. ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
print("You are temporary safe. At least for now.")
print("But the alien is still trying to get in.")
print("Dealing massive damage onto the door. Biting. Scratching. Screaming through the door.")
print("The door won’t last any longer…")
print("You saw a locker and a vent.")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
Escape = input("Would you hide in the locker or the vent? [Locker/Vent] ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
if Escape == "Vent":
    print("You unscrew the vent and crawled inside.")
    print("The alien broke the door and entered the room.")
    print("Without hesitation, alien rush into the vent.")
    print("You are trying to crawl as fast as you can, hoping that the alien won’t catch you.")
    print("The alien manage to catch up with you in few seconds.")
    print("You got killed.")
    print("GAME OVER")
    exit()
else:
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    Unscrew = input("Would you unscrew the vents before you hide in the locker? [Yes/No] ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    if Unscrew == "Yes":
        print("You unscrew the vent and hide in the locker.")
    else:
        print("You decided to not unscrew the vent.")
        print("The alien broke the door and entered the room.")
        print("The alien looked around.")
        print("The alien targeted onto the locker.")
        print("The alien bite opened the locker and saw you inside.")
        print("You got killed.")
        print("GAME OVER")
        exit()

print("The alien broke the door and entered the room.")
print("The alien heard the sound of you unscrewing the vent.")
print("The alien ran past your locker and rushed into the vent.")
print("Leaving you alone in the room.")
print("You survived. It was a close call.")
print("You got out from the locker and you saw a dead body of a worker.")
print("There is a keycard on his hand.")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
Keycard = input("Would you take the keycard? [Yes/No] ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
if Keycard == "Yes":
    print("You took the keycard and put it in your pocket.")
else:
    print("You left the keycard.")

#Map
print("You saw a map on the wall.")
print("A map for this spaceship!")
print("You rip off the map and put it in your pocket.")
print("YOU GOT A MAP!")

#Flesh
print("After you got out from the hallway there is a kitchen.")
print("You went inside and you saw a flesh. ")
print("It looks like a piece of human flesh…?")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
Flesh = input("Would you bring the flesh along? [Yes/No] ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
if Flesh == "Yes":
    print("You took the flesh.")
else:
    print("You decided to not take the flesh.")

#Next Area
print("The maps shows few places that might be useful for you to go.")
print("[Control Panel]")
print("[Emergency Evacuation Dock]")
print("[Ventilation Control]")
print("[Laboratory]")
print("--------------------------------------------------------------------------------------------------------------------------------------------")
Area = input("Where would you like to go next? ")
print("--------------------------------------------------------------------------------------------------------------------------------------------")

#Hard Part
if Area == "Control Panel":
    print("You went to the Control Panel.")
    print("You found a communication devices that you could look for help.")
    print("The captain’s body is died left on the captain’s chair…")
    print("You got a high access keycard from the captain’s body.")
    print("You were able to call for help but password is required.")
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    Password = input("Enter the password: ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    if Password == "FCI-2026":
        print("You entered the correct password.")
        print("You called for help by telling them what you had been facing on the spaceship.")
        print("You received a response from the other side, a coordinate of your home, Earth.")
    else:
        print("You entered the wrong password.")
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        Decision = input("What would you like to do next? [Try again/Go to another area] ")
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
        if Decision == "Try again":
            print("You try to enter the password again.")
            print("You entered the wrong password.")
            print("You triggered the safety alarm. The alien heard the alarm and rushed into the control panel room.")
            print("You got killed.")
            print("GAME OVER")
            exit()
        else:
            print("You decided to go to another area instead of trying to enter the password again.")
            print("[Control Panel]")
            print("[Emergency Evacuation Dock]")
            print("[Ventilation Control]")
            print("[Laboratory]")
            print("--------------------------------------------------------------------------------------------------------------------------------------------")
            Area = input("Where would you like to go next? ")
            print("--------------------------------------------------------------------------------------------------------------------------------------------")
  

elif Area == "Emergency Evacuation Dock":
    print("You went to the Emergency Evacuation Dock.")

elif Area == "Ventilation Control":
    print("You went to the Ventilation Control Room.")
    print("You saw a battery at the corner of the room.")
    print("Then you heard noises coming out from the vent… ")
    print("The alien crawl through the vent and ended up at the ventilation control room!")

elif Area == "Laboratory":
    print("You went to the Laboratory.")
    print("There is a tiny note left on a table with 6-digit PIN, is it some kind of password?")
    print("It written on the note: FCI-2026")
    print("There is a locked door in the laboratory.")


# Main part









# Function part

# Typewriter effect function
def typewrite(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print() 


#screen function
WIDTH = 80 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def render(bag_items, narration, options):
    clear()
    
    # --- TOP: Bag ---
    print("-" * WIDTH)
    print(f"  Bag: {', '.join(bag_items)}")
    print("-" * WIDTH)
    
    # --- MIDDLE: Narration (right-aligned or centered) ---
    print()
    print(narration.rjust(WIDTH))  # or .center(WIDTH)
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



# art placeholder