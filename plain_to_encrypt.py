import make_digram
import make_sqaure
import random
import server
from flask import request

# This will be replaced with an api or a much larger list of quotes
# Chooses a quote at random
with(open("phrases.txt")) as p:
    phrase = p.readlines()
    phrase = phrase[random.randint(0, len(phrase)-1)].strip()

# Run this one for python terminal output
my_square = make_digram.my_square
# Assign the grids final letter
final_letter = f"/{make_sqaure.final_letter}"

my_di = make_digram.make_initial_digram(phrase)


def plain_to_encrypt(my_dia):
    """This Function returns the location of each of the original letters (x,y)"""
    encrypted_text = []

    letter_one_row = ""
    letter_one_col = ""
    letter_two_row = ""
    letter_two_col = ""

    # Loops through each Digram to find its row and column
    for pair in my_dia:
        # Assigns First and Second letter of Digram
        letter_one = pair[0]
        letter_two = pair[1]

        # Loops through each row of the grid
        for row in enumerate(my_square):
            if letter_one in row[1]:
                # Assigns the column to the index position
                letter_one_col = row[1].index(letter_one)
                # Assigns the Row to the enumerate (0-4)
                letter_one_row = row[0]

            # Check if letter is in last square, if so corrects the digits
            elif letter_one in my_square[4][4].split("/"):
                letter_one_col = my_square[4][4].index(letter_one)


                if letter_one_col == 0:
                    letter_one_col = 4
                elif letter_one_col == 2:
                    letter_one_col = 5
                letter_one_row = 4

        for row in enumerate(my_square):
            if letter_two in row[1]:
                letter_two_col = row[1].index(letter_two)
                letter_two_row = row[0]

            elif letter_two in my_square[4][4].split("/"):
                letter_two_col = my_square[4][4].index(letter_two)

                if letter_two_col == 0:
                    letter_two_col = 4
                elif letter_two_col == 2:
                    letter_two_col = 5
                letter_two_row = 4
        encrypted_text.append((letter_one_row, letter_one_col))
        encrypted_text.append((letter_two_row, letter_two_col))

    return encrypted_text

# README Encrpyted text is correct, review final encrypt
def final_encrpyt():
    plain = plain_to_encrypt(my_di)

    e_letters = []
    for item in range(0, len(plain), 2):

        new_letter_one = ""
        new_letter_two = ""
        letter_one = plain[item]
        letter_two = plain[item+1]

        # Letter one and letter two are the coordinates (x, y) where x is the row and y is the column
      
        # Checks of letters are in same row and are in the same final block
        if letter_one[1] == 4 and letter_two[1] == 5 and letter_one[0] == letter_two[0]:
            new_rounded_one = 4
            new_letter_one = (letter_one[0], new_rounded_one, 2)
            new_rounded_two = 0
            new_letter_two = (letter_two[0], new_rounded_two)

        # Checks if letters are in the same row
        elif letter_one[0] == letter_two[0]:
            # If second digit on right shift is greater than 5, assigns it value 0 otherwise adds + 1
            if letter_one[1] + 1 >= 5:
                new_rounded_one = 0
                new_letter_one = (letter_one[0], new_rounded_one)
            else:
                new_letter_one = (letter_one[0], letter_one[1] + 1)
            
            
            if letter_two[1] + 1 == 5:
                new_rounded_two = 0
                new_letter_two = (letter_two[0], new_rounded_two)
            else:
                new_letter_two = (letter_two[0], letter_two[1] + 1)


        # Checks if letters are in same column
        elif letter_one[1] == letter_two[1] or letter_one[1] == 4 and letter_two[1] == 5:
            # If second digit on right shift is greater than 5, assigns it value 0 otherwise adds + 1
            if letter_one[0] + 1 == 5:
                new_rounded_one = 0
                new_letter_one = (new_rounded_one, letter_one[1])
            else:
                new_letter_one = (letter_one[0] + 1, letter_one[1])

            if letter_two[0] + 1 >= 5:
                new_rounded_two = 0
                new_letter_two = (new_rounded_two, letter_one[1])

            else:
                new_letter_two = (letter_two[0] + 1, letter_two[1])

        # Final statement solves for the square
        # Different Columns and Different Rows
        else:
            # If the position is the last position in the grid
            if letter_one[1] == 5:
                new_letter_two = (letter_two[0], 4)
                new_letter_one = (letter_one[0], letter_two[1])
            elif letter_two[1] == 5:
                new_letter_one = (letter_one[0], 4)
                new_letter_two = (letter_two[0], letter_one[1])
            else:
                new_letter_one = (letter_one[0], letter_two[1])
                new_letter_two = (letter_two[0], letter_one[1])

        e_letters.append(new_letter_one)
        e_letters.append(new_letter_two)

    encrypted_text = ""
    for item in e_letters:
        if len(item) > 2:
            print(item)
            encrypted_text += (my_square[item[0]][item[1]][item[2]])
        else:
            encrypted_text += (my_square[item[0]][item[1]])

    finalized_encrypted_text = make_digram.make_digram(encrypted_text.replace(final_letter, ""))


    return finalized_encrypted_text

