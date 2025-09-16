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
#HERO PATH
def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You pick you the glowing sword and the sword and decide to become an adventure")

#VILLAIN PATH
def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
#DONT FORGET TO WRITE STORY
def center_path():
    print("I will make up the story at the end!!!")

if __name__ == "__main__":
    intro()
