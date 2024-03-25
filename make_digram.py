# -------------------- Making the DIGRAM ------------------#
import make_sqaure
import server
from flask import request

my_square = make_sqaure.make_square(server.request.form["nm"])
final_letter = make_sqaure.final_letter

# TODO: Word here must be the randomized phrase

def make_digram(word):
    """This Function Splits The Initial Phase Into 2 Letter Pairs"""
    word = word.replace(" ", "")
    if word == "":
        word = input("Enter your message to encode: ").replace(" ", "")
    split_msg = []
    for item in range(0, len(word), 2):
        split_msg.append(word[item:item + 2])
    return digram(split_msg)


def make_initial_digram(wordz):
    word = wordz
    word = word.upper().replace(" ", "")
    split_msg = []
    for item in range(0, len(word), 2):
        split_msg.append(word[item:item + 2])
    return digram(split_msg)


def digram(di_msg):
    # Checks if all digram are different letters. If not adds x then re runs digram maker
    re_string = False
    new_string = ""
    # If final letter is single adds the final letter of the Grid
    for item in enumerate(di_msg):
        if len(item[1]) < 2:
            di_msg[item[0]] = f"{item[1][0]}{final_letter}"
            if di_msg[item[0]][0] == di_msg[item[0]][1]:
                di_msg[item[0]] = f"{item[1][0]}X"
            re_string = True
            break
    # Adds x if same 2 letters
        if item[1][0] == item[1][1]:
            di_msg[item[0]] = f"{item[1][0]}X{item[1][1]}"
            re_string = True
            break

    # Re strings the digram and runs it through digram function
    if re_string:
        for item in di_msg:
            new_string += item
        return make_digram(new_string)

    return di_msg
