import random
import time


def main():

    def first_difficulty():
        print('This is easy difficulty.\nThere is only 1 bullet among all 6 chambers.')
        while True:
            valid_chambers = [
                '1', '2', '3', '4', '5', '6'
            ]
            valid_response = [
                'f'
            ]
            bullet = input('Which chamber do you bet on that does not contain the bullet?:  ')
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
            print("You lost the bet, and you are dead!")
        else:
            print("That was lucky, and you are alive!")

    def second_difficulty():
        print("This is medium difficulty.\nThere are 3 bullets among all 6 chambers")
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
        print("Chambers fired! " + " ".join(chamber))
        if bullet in chamber:
            print('You lost the bet, and you are dead!')
        else:
            print("That was lucky, you've won!")

    def third_difficulty():
        print("This is hard difficulty.\nThere are 5 bullets among all 6 chambers.")
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
        chamber = random.sample(['1', '2', '3', '4', '5', '6'], 5)
        chamber_medium.append(chamber)
        print("Chambers fired! " + " ".join(chamber))
        if bullet in chamber:
            print('You lost the bet, and you are dead!')
        else:
            print("That was lucky, you've won!")

    print('This is Russian Roulette. ')
    time.sleep(1.4)
    print("Each gun will have a different number of bullet/s loaded in it. Varying from each difficulties.")
    time.sleep(3.4)
    print("And you will have to bet on which chamber that is not loaded with the bullet/s.")
    time.sleep(3.4)
    while True:
        print("The game difficulties are; 'E' for Easy, 'M' for Medium, and 'H' for Hard")
        main_game_input = input("What difficulty do you want to play in?: ").upper()
        if main_game_input == 'E':
            first_difficulty()
        elif main_game_input == 'M':
            second_difficulty()
        elif main_game_input == 'H':
            third_difficulty()
        else:
            print("Please input a valid option.")


if __name__ == "__main__":
    main()
