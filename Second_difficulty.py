import random


def second_difficulty():
    print("This is medium difficulty.")
    while True:
        valid_chambers = [
            '1', '2', '3', '4', '5', '6'
        ]
        valid_response = [
            'f'
        ]
        bullet = input('Which chamber do you bet on that does not contain the bullets?:  ')
        if bullet in valid_chambers:
            response = input('Type "f" to fire the gun: ')
            if response in valid_response:
                break
            else:
                print('Please type f')
        else:
            print('Please load the bullet on a valid chamber.')

    chamber_medium = []
    chamber = random.sample(['1', '2', '3', '4', '5', '6'], 3)
    chamber_medium.append(chamber)
    print(chamber_medium)
    if bullet in chamber:
        print('You lost the bet, and you are dead!')
    else:
        print("That was lucky, you've won!")


second_difficulty()
