import random
winning_number=random.randint(1,100)
guess=1
guessed_number=int(input())
game_over=False
while not game_over:
    if winning_number==guessed_number:
        print(f"\U0001F973 Congrats! You Won! And You Guessed This Number In {guess} Attempts!!!")
        game_over=True
    else:
        if winning_number>guessed_number:
            print("\U0001F61E OOPS! It's Low.")
        else:
            print("\U0001F61E OOPS! It's High.")
        guess+=1
        guessed_number=int(input("Guess Again : "))
