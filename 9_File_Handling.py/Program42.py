# The game() function in a program lets a user play a game and returns the score as an integer.You need to read a file "hi-score.txt" which is either blank or contains the hi-score.You need to write a program to update the  hi score whenever the game () function breaks the hiscore.

import random

def game():
    score=random.randint(1,100)
    with open("hiscore.txt") as f:
        hiscore= f.read()
        if hiscore != "":
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"Your Score :{score}")

    if score>hiscore:
        with open("hiscore.txt","w") as f:
            f.write(str(score))
            print(f"Highest score is {score}")

    else:
        print(f"Highest score is {hiscore}")
    return score


game()
