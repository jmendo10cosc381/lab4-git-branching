def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You win the duel and you take the squirrel with you.")
    print("You then find out that the squirrel was actually part of the royal family.")
    print("You decide to send the royal family a ransom for the squirrel.")
    print("The royal family then sends a hero to save the squirrel.")
    print("You and the hero fight and you lose with the hero saving the squirrel.")
#DONT FORGET TO WRITE STORY
def center_path():
    print("I will make up the story at the end!!!")

if __name__ == "__main__":
    intro()
