import random

guess=random.randint(1,100)
print(guess)

while True:

    try:
       
        guess_input= int(input("Guess the number between 1 and 100 :"))
        if guess_input > guess:
            print(" Too High!")
        elif  guess_input < guess:
            print("Too Low!")
        else : 
            print("Congratulations you Guessed the correct Number")
            break
    except  ValueError:
        print("Please enter valid input")
        
    





