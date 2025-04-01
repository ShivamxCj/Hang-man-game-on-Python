import random
word= ("dog", "cat", "mango", "bike", "house", "books", "duck", "sheep", "laptop")

hangMan= {
    0: ("|  ",
        "| ",
        "|  ",
        "|  "),
    1: ("|  ",
        "| o",
        "| ",
        "|  "),
    2: ("|  ",
        "| o",
        "| |",
        "|  "),
    3: ("|   ",
        "| o ",
        "|/|\\",
        "|    "),
    4: ("|   ",
        "| o ",
        "|/|\\",
        "|/ \\"),
    5: ("|-   ",
        "| o ",
        "|/|\\",
        "|/ \\"),
    6: ("|-|   ",
        "| o ",
        "|/|\\",
        "|/ \\",
        "|    "),
}

def showHangMan(x):
    for i in hangMan[x]:
        print(i)

def displayHint(hint):
    print(" ".join(hint))

def main():
    answer= random.choice(word)
    hint= ["_"]* len(answer)
    wrongGuesses= 0
    correctGuesses= set()
    gameRunning= True

    while gameRunning:
        showHangMan(wrongGuesses)
        displayHint(hint)
        guess= input("enter your word: ").lower()

        if len(guess)!= 1 or not guess.isalpha():
            print("INVALID INPUT!")
            continue

        if guess in correctGuesses:
            print(f"{guess} is already guessed")
            continue

        correctGuesses.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i]=guess
        else:
            wrongGuesses+=1
        
        if "_" not in hint:
            showHangMan(wrongGuesses)
            print(answer)
            print("YOU WIN!!!")
            gameRunning= False
        elif wrongGuesses >= len(hangMan)-1:
            showHangMan(wrongGuesses)
            print("Correct answer is",answer)
            print("YOU LOOSE!!!")
            gameRunning= False


if __name__== "__main__":
    main()