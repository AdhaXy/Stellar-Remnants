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

WIDTH = 120 
BOX_HEIGHT = 10
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

say("You run with all your might to the evacuation room.")
time.sleep(2)
say("But the Alien is starting to catch up.\n" \
"So you throw your smoke bomb to confuse the Alien.")
time.sleep(2)
print("\n")
SingleBox("Throw the smoke bomb",ask_input=True,prompt="Press anything")
time.sleep(2)
print("------------------------------------------------------------------------------------------" \
"--------------------------------")
smoke()
print("-----------------------------------------------------------------------------------------" \
"--------------------------------")
time.sleep(3)
say("poof!") 
time.sleep(1)
say("A heavy cloud emerge and you go through it to lose the Alien")
time.sleep(2)