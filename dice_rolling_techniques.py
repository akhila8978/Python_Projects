import random

while True:
    choice=input('Roll the dice ? (y/n):').lower()
    if choice =='y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'{die1},{die2}')
    elif choice == 'n':
        print("THANKS FOR PLAYING")
        break
    else:
        print("Invalid choice!")


----- to choose no of times to roll the dice -----

import random

while True:
    choice=input('Roll the dice ? (y/n):').lower()
    if choice =='y':
        roll=int(input())
        for i in range(roll):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print(f' roll{i+1} : {die1},{die2}')
    elif choice == 'n':
        print("THANKS FOR PLAYING")
        break
    else:
        print("Invalid choice!")

            

            
