import time

def smoke():
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

TextSpeed = 0.03
def say(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(TextSpeed)
    print()

def red(text):
    width = len(text) + 6
    result = RED + "┌" + "─" * width + "┐" +  "\n"
    result += "|" + text.center(width) + "|" +  "\n"
    result += "└" + "─" * width + "┘" +  RESET
    return result

def blue(text):
    width = len(text) + 6
    result = BLUE + "┌" + "─" * width + "┐" +  "\n"
    result += "|" + text.center(width) + "|" +  "\n"
    result += "└" + "─" * width + "┘" +  RESET
    return result

def green(text):
    width = len(text) + 6
    result = GREEN + "┌" + "─" * width + "┐" +  "\n"
    result += "|" + text.center(width) + "|" +  "\n"
    result += "└" + "─" * width + "┘" +  RESET
    return result

def yellow(text):
    width = len(text) + 6
    result = YELLOW + "┌" + "─" * width + "┐" +  "\n"
    result += "|" + text.center(width) + "|" +  "\n"
    result += "└" + "─" * width + "┘" +  RESET
    return result

WIDTH = 120 
BOX_HEIGHT = 10
def render(narration, options, timeout=None):

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

# ===================== SKETCH ONLY — one round of the puzzle, to react to, not final code =====================

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m" 

def show_card(text):
    width = len(text) + 6
    print("┌" + "─" * width + "┐" + "==")
    print("│" + text.center(width) + "│" + "=-")
    print("└" + "─" * width + "┘"+"-_")

def pod_puzzle(max_tries):
    global puzzle

    # the fixed correct pairs for this run (left fragment -> right fragment)
    pairs = [("NTW", "-20"), ("CGT", "-22"), ("FC", "-112")]

    say("A small panel lights up. Fragments of a code, scattered and incomplete, blink at you.")
    time.sleep(2)

    for left, correct_right in pairs:
        attempts_left = max_tries
        solved_this_one = False

        while attempts_left > 0 and not solved_this_one:
            print()
            show_card(left)
            print()
            guess = input("What matches this fragment? ").strip()

            if guess == correct_right:
                say("The panel blinks green. That fragment locks into place.")
                solved_this_one = True
            else:
                attempts_left -= 1
                if attempts_left > 0:
                    say(f"Nothing happens. ({attempts_left} attempt(s) left for this one)")
                else:
                    say("The panel flashes red and locks that slot. No more tries.")

        if not solved_this_one:
            puzzle = False
            return False  # failed this round entirely

    puzzle = True
    say("The final fragment clicks into place. The pod hums to life.")
    return True

# pod_puzzle(2)  

def puzzled(max_tries):
    global puzzle
    print("U picked up a card that show a hint.\n" \
    "Blue = red\n" \
    "green = green\n" \
    "yellow = blue\n")

    # wires = [("blue","red"),("green","green"),("black","blue")]

    print("a small light show the wires.")
    attempt = max_tries
    # for left, right in wires:
    solved = False
    while attempt > 0 and not solved:
        print ("----------------------------------------------------------------------------------------------")
        print( blue("right"))
        choice = render(narration=red("red") + "\n" + blue("blue") + "\n" + green("green"),
                options=["1.red","2.blue","3.green"])
        if choice == "1":
            solved = True 
        elif choice == "2" or choice =="3":
            say("you got it wrong!\n" \
            "The wire shocked you!")
            attempt -= 1
            if attempt > 0:
                say("You try again")
            elif attempt == 0:
                say("You stopped")
    solved = False
    while attempt > 0 and not solved:
        print ("----------------------------------------------------------------------------------------------")
        print( blue("right"))
        choice = render(narration=red("red") + "\n" + blue("blue") + "\n" + green("green"),
                options=["1.red","2.blue","3.green"])
        if choice == "1":
            solved = True 
        elif choice == "2" or choice =="3":
            say("you got it wrong!\n" \
            "The wire shocked you!")
            attempt -= 1
            if attempt > 0:
                say("You try again")
            elif attempt == 0:
                say("You stopped")
    solved = False
    while attempt > 0 and not solved:
        print ("----------------------------------------------------------------------------------------------")
        print( blue("right"))
        choice = render(narration=red("red") + "\n" + blue("blue") + "\n" + green("green"),
                options=["1.red","2.blue","3.green"])
        if choice == "1":
            solved = True 
        elif choice == "2" or choice =="3":
            say("you got it wrong!\n" \
            "The wire shocked you!")
            attempt -= 1
            if attempt > 0:
                say("You try again")
            elif attempt == 0:
                say("You stopped")
    if solved == False:
        say("the shocked was too strong. You stop trying")
        puzzle = False
        return False
    elif solved == True:
        say("The room make a noise signaling its start to come back to life")
        puzzle = True
        return True

    
# print ("----------------------------------------------------------------------------------------------")
# print( blue("right"))
# print("there's 3 other wires")
# render(narration=blue("red") + "\n" + blue("blue") + "\n" + blue("green"),
# options=["1.red","2.blue","3.black"])
puzzled(2)