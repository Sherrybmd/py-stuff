import random


words = ["redacted", "company", "amusement"]
question = ""
display = []
answer = ""


def update():
    for letter in display:
        print(letter, end = " ")
    print()  #just to make sure we go next line, i'm bad i know

def pick_question():
    global display, question

    question = random.choice(words)

    # make word look like '_ _ _ _' to guess
    for letter in question:
        display.append("_")

def ask_user():
    global answer
    answer = input("take a guess: \n>")

def check_answer():
    global display
    for position in range(len(question)):
        for l in answer:
            letter = question[position]
            if letter == l:
                display[position] = l


def check_win():

    if "_" in display or "" in display:
        return False
    else:
        return True

def play():

    pick_question()
    while check_win() is False:

        update()
        ask_user()
        check_answer()
    print("--you win!--")
    print(">", end=" ")
    for letter in display:
        print(letter, end=" ")
play()
