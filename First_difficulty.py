import random


def easy_difficulty():
    print('This is easy difficulty.')
    while True:
        valid_chambers = [
            '1', '2', '3', '4', '5', '6'
        ]
        valid_response = [
            'f'
        ]
        bullet = input('Which chamber do you want to load the bullet?:  ')
        if bullet in valid_chambers:
            response = input('Type "f" to fire the gun: ')
            if response in valid_response:
                break
            else:
                print('Please type f')
        else:
            print('Please load the bullet on a valid chamber.')

    chamber = random.choice(['1', '2', '3', '4', '5', '6'])
    print(chamber)
    if chamber == bullet:
        print('BANG! You are dead')
    else:
        print('You are alive')


easy_difficulty()
