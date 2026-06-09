import os
import time
import sys

#---------------------------------System------------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pause():
    input("\n  [Press ENTER to continue...]\n")

def divider():
    print("\n" + "─" * 55 + "\n")

#--------------------------------Inventory----------------------------------

def show_inventory(inventory):
    if inventory:
        print(f"  🎒 Inventory: {', '.join(inventory)}")
    else:
        print("  🎒 Inventory: (empty)")
    print()

#-----------------------------------Main------------------------------------

def play():
    clear()
    divider()
    slow_print("        S T E L L A R   R E M N A N T S   ", delay=0.06)
    divider()
    slow_print("  You wake up alone. The crew is gone.")
    slow_print("  Something aboard this ship is hunting you.")
    slow_print("  Find a way home — if you can.")
    divider()
    pause()

    inventory = []
    state = "hub"

    while True:
        if state == "hub":
            state = hub(inventory)
        elif state == "control":
            state = control_panel(inventory)
        elif state == "dock":
            state = evacuation_dock(inventory)
        elif state == "ventilation":
            state = ventilation_control(inventory)
        elif state == "lab":
            state = laboratory(inventory)
        elif state == "ending":
            ending_scene(inventory)
            break
        elif state == "dead":
            dead_scene()
            break

#-------------------------------Navigation----------------------------------

def hub(inventory):
    """Main hub – player chooses where to go."""
    clear()
    divider()
    slow_print("  You drift through the silent corridors of the spaceship.")
    slow_print("  Emergency lights flicker. Something moves in the dark.")
    divider()
    show_inventory(inventory)

    options = [
        ("control",     "Control Panel"),
        ("dock",        "Emergency Evacuation Dock"),
        ("ventilation", "Ventilation Control"),
        ("lab",         "Laboratory"),
    ]
    return choose("Where would you like to go?", options)

#-----------------------------------Control Panel-----------------------------------

def control_panel(inventory):
    clear()
    divider()
    slow_print("  CONTROL PANEL")
    divider()
    slow_print("  There are many devices and computers for you to use. ")
    slow_print("  The captain’s body is died left on the captain’s chair…")
    pause()

    if "captain's keycard" not in inventory:
        slow_print("  You search the captain and find a HIGH-ACCESS KEYCARD.")
        inventory.append("captain's keycard")
        slow_print("  → Obtained: captain's keycard")
        pause()

    slow_print("  You spot a communication device. It could call for help!")
    slow_print("  You activate it — but a 6-digit PIN is required.")

    if "6-digit PIN" in inventory:
        slow_print("  You enter the password...")
        slow_print("  ✅  Connection established!")
        slow_print("  You relay everything that has happened aboard the ship.")
        slow_print("  A reply crackles through: the coordinates of Earth —")
        slow_print("  your home.")
        if "Earth coordinates" not in inventory:
            inventory.append("Earth coordinates")
            slow_print("  → Obtained: Earth coordinates")
        pause()
    else:
        slow_print("  ❌  Password required. You don't have it yet.")
        pause()

    return "hub"

#--------------------------------Evacuation Dock----------------------------

def evacuation_dock(inventory):
    clear()
    divider()
    slow_print("  EMERGENCY EVACUATION DOCK")
    divider()
    slow_print("  You saw there was still one escape pod left for you to use but need to be repaired.")
    slow_print("  A manual on the workshop table.")
    slow_print(" “The pods need a battery in order to function. You can find a battery at the ventilation control room but once you took the battery. The whole spaceship will got shutdown.” ")
    slow_print(" Do you have the Earth coordinate?")
    pause()

    if "Earth coordinates" not in inventory:
        slow_print("  ❌  You have no coordinates to enter yet.")
        pause()
        return "hub"

    if "battery" in inventory:
        slow_print("  You slot the battery into place and punch in the coordinates.")
        slow_print("  The pod hums to life. Launch sequence ready.")
        pause()
        return "ending"
    else:
        slow_print("  You enter the coordinates — but without a battery")
        slow_print("  the pod stays dark and cold.")
        slow_print("  ❌  Battery required.")
        pause()
        return "hub"

#--------------------------------Ventilation Control--------------------------

def ventilation_control(inventory):
    clear()
    divider()
    slow_print("  VENTILATION CONTROL")
    divider()
    slow_print("  A battery sits in the corner of the room.")
    slow_print("  Then you heard noises coming out from the vent. ")
    slow_print(" The alien crawl through the vent and ended up at the ventilation control room.")

    if "meat" in inventory:
        slow_print("  You hurl the meat out into the corridor.")
        slow_print("  The alien's head snaps toward it. It lunges out of the room.")
        if "battery" not in inventory:
            inventory.append("battery")
            slow_print("  → Obtained: battery")
            slow_print("  ⚠️   The ship's power begins to flicker and die.")
        pause()
        return "hub"
    else:
        slow_print("  You have nothing to bait it off.")
        slow_print("  You got killed.")
        slow_print(" ✖  GAME OVER")
        pause()  

#-------------------------------------Lab------------------------------------

def laboratory(inventory):
    clear()
    divider()
    slow_print("  LABORATORY")
    divider()
    slow_print("  A tiny note on a table catches your eye.")
    slow_print("  Six digits scrawled in a shaking hand — some kind of PIN?")

    if "6-digit PIN" not in inventory:
        inventory.append("6-digit PIN")
        slow_print("  → Obtained: 6-digit PIN")
    pause()

    slow_print("  A heavy door looms at the back of the lab.")
    slow_print("  A keycard reader glows red beside it.")

    if "captain's keycard" in inventory:
        slow_print("  You swipe the keycard. The reader flashes green.")
        pause()
        inner_lab(inventory)
    else:
        slow_print("  ❌  Access denied. Captain's keycard required.")
        pause()

    return "hub"

#----------------------------Inner Lab----------------------------------

def inner_lab(inventory):
    clear()
    divider()
    slow_print("  INNER LABORATORY")
    divider()
    slow_print("  You came into the room. ")
    slow_print(" The room is full of speakers.")
    slow_print("  Photos of the alien is everywhere in the room.")
    slow_print("  You saw many scientific equipment. ")
    slow_print("  A glass incubator in the isolated room was broken. ")
    slow_print(" You got terrified. ")
    pause()

    slow_print(" You found a working computer.")
    slow_print(" You went through the computer and found a video.")
    slow_print(" You played…")
    pause()

    slow_print(" Video Plays: “We are in a room full of Huge-tuned speakers.” ")
    slow_print(" “WE! The professional scientist are collecting DNA and conducting breeding experiment on the alien…” ")
    slow_print(" The video crashed, computer turned off on…")
    pause()

    slow_print(" Documents are spread across the table.")
    pause()

    choice = choose(
        "Would you like to read the documents?",
        [("yes", "Yes"), ("no", "No")]
    )

    if choice == "yes":
        clear()
        divider()
        slow_print("  DOCUMENT — Subject CGT-2399")
        divider()
        slow_print("  • Able to see through the dark.")
        slow_print("  • Extremely fast and agile.")
        slow_print("  • Combination of CGT-0001 DNA (The mother of Subject-CGT) with human DNA.")
        slow_print("  • A natural hunter.")
        slow_print("  • Has a strong, whip-like tail.")
        slow_print("  • Eats any kind of things meat.")
        slow_print("  • Hermaphrodite — reproduces alone, very rapidly.")
        slow_print("  • Implants offspring into living hosts.")
        slow_print("  • Regenerates almost instantly. Fire-proof.")
        slow_print("  • WEAKNESS: high-frequency sound, humans wont be affected.")
        slow_print("  Note: , You will need a huge-tuned speaker to produce a loud pitch of noise.")
        pause()
        slow_print("  You now know exactly how to defeat it.")
        if "alien documents" not in inventory:
            inventory.append("alien documents")
            slow_print("  → Knowledge recorded: alien documents")
        if "speakers" not in inventory:
            slow_print("  You collect the large speakers from the room.")
            inventory.append("speakers")
            slow_print("  → Obtained: speakers")
        pause()
    else:
        slow_print("  You leave the documents untouched.")
        pause()

    #---------------------------------Meat-----------------------------------

if "meat" not in inventory:
    slow_print("  In a storage locker you find a vacuum-sealed pack of meat")
    slow_print("  (emergency rations — at least that's what it says).")
    inventory.append("meat")
    slow_print("  → Obtained: meat")
    pause()

#-----------------------------endings-------------------------------------

def ending_scene(inventory):
    clear()
    divider()
    slow_print("  FINAL CHOICE")
    divider()
    show_inventory(inventory)

    options = [("kill", "Kill the alien"), ("survive", "Just survive and escape")]
    choice = choose("What is your plan?", options)

    if choice == "kill":
        _ending_kill(inventory)
    else:
        _ending_survive(inventory)

#--------------------------------------Kill--------------------------------

def _ending_kill(inventory):
    clear()
    divider()
    if "alien documents" in inventory and "speakers" in inventory:
        slow_print("  GOOD ENDING — The Hunter Silenced")
        divider()
        slow_print("  You haul the speakers to the Control Panel and wire them in.")
        slow_print("  Then you bang chairs against consoles — a wild, clanging racket.")
        slow_print("  Claws scrape the corridor floor…")
        slow_print("  It's coming…")
        pause()
        slow_print("  You see it!")
        slow_print("  You trigger the speakers immediately!")
        slow_print("  The alien freezes. Its screech cuts off mid-cry.")
        slow_print("  You push the volume higher. It collapses, motionless.")
        slow_print("  You leave the speakers running and walk away.")
        pause()
        slow_print("  Back at the dock, you board the escape pod.")
        slow_print("  The hatch seals. The countdown begins.")
        slow_print("  You launch into the dark — and this time, the dark is empty.")
        slow_print("  Ahead, a pale blue dot.")
        pause()
        slow_print("  Home…")
        divider()
        slow_print("    YOU SURVIVED!  ")
        slow_print("    ★  THE END  ★     ")
        slow_print("    Thanks  for playing!    ")
    else:
        slow_print("  BAD ENDING — Courage Without Knowledge")
        divider()
        slow_print("  You fashion a shield from scrap metal, grab a kitchen knife.")
        slow_print("  You hunt the alien down and stab it once — clean hit.")
        pause()
        slow_print("  Its tail cracks across the room like a whip.")
        slow_print("  You slam into the bulkhead. Everything goes white.")
        slow_print("  When your vision clears, it's already above you.")
        slow_print("  You got killed…")
        divider()
        slow_print("  ✖  GAME OVER")
    pause()

#-----------------------------------Escape----------------------------------

def _ending_survive(inventory):
    clear()
    divider()
    slow_print("  BAD ENDING — An Uninvited Passenger")
    divider()
    slow_print("  You sprint to the dock, slamming every door behind you.")
    slow_print("  You close as much as you can to buy time.")
    slow_print("  You dive into the pod, battery in, coordinates locked.")
    pause()
    slow_print("  T-minus Ten… Nine… Eight…")
    slow_print("  The dock door buckles. The alien bursts through.")
    slow_print("  Its claw finds your arm. You scream.")
    slow_print("  Using your last strength to push it off…")
    slow_print("  Three. Two. One. LAUNCH.")
    pause()
    slow_print("  The pod rockets free. You made it — barely.")
    slow_print("  You slump against the seat, clutching your wound.")
    slow_print("  The stars blur past. Earth grows on the viewport.")
    pause()
    slow_print("  Something began to grow inside you…")
    slow_print("  Something that shouldn't be there…")
    slow_print("  Follow you home…")
    divider()
    slow_print("  ✖  GAME OVER")
    pause()

    #--------------------------------Replay--------------------------------

    divider()
    replay = input("  Play again? (y/n) > ").strip().lower()
    if replay == "y":
        play()
    else:
        slow_print("  Thanks for playing. Who's the hunter…")
        print()


if __name__ == "__main__":
    play()