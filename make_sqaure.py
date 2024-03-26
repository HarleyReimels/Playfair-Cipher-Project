################## THE PLAYFAIR CIPHER ##################

final_letter = ""

def make_square(sqr=""):
    '''The purpose of make_square is to take in a word/phrase/sentence and plave it into a 5x5 grid using only unique letters'''
    global final_letter
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
    square = []
    # Make letters capitalized for easier comparison. Removes any non alpha element.
    keyword = sqr.upper()
    keyword = "".join(e for e in keyword if e.isalpha())


    # Maintains set order
    def unique(sequence):
        ''' Loop through sequence, if X is not in seen, add it to seen. Return all original letters in order of appearence.'''
        seen = set()
        return [x for x in sequence if not (x in seen or seen.add(x))]

    # kw is now only unique letters in order of appearance
    kw = unique(keyword)

    # Measures size of kw, adds the appropriate amount of lists based off kw size
    if len(kw) <= 5:
        square.append(kw)
    elif len(kw) > 5 and len(kw) < 11:
        square.append(kw[:5])
        square.append(kw[5:10])
    elif len(kw) > 11 and len(kw) < 16:
        square.append(kw[:5])
        square.append(kw[5:10])
        square.append(kw[10:15])
    elif len(kw) > 16 and len(kw) < 21:
        square.append(kw[:5])
        square.append(kw[5:10])
        square.append(kw[10:15])
        square.append(kw[15:20])
    elif len(kw) >= 21:
        square.append(kw[:5])
        square.append(kw[5:10])
        square.append(kw[10:15])
        square.append(kw[15:20])
        square.append(kw[20:])

    # We can not be sure the size of the square currently, as it is dependent on the keyword the user had entered
    # previously.

    # Checks each letter in alphabet is in the square
    # Setting up row one in square *Each list represents a row*
    for letter in alphabet:
        # If the first row is less than 5 letters
        if len(square[0]) < 5:
            # If the letter does not already exist, add the letter. Repeat until list 1 has 5 elemets.
            if letter not in square[0]:
                square[0].append(letter)
        else:
            break
    # We do not know if we need to add extra list spaces, we do this to not index out of range
    square.append([])

    # Setting up row two, verifies no same letters in row one or two
    for letter in alphabet:
        if len(square[1]) < 5:
            if letter not in square[0] and letter not in square[1]:
                square[1].append(letter)
        else:
            break
    square.append([])

    # Setting up row three, verifies no same letters in row one or two or three
    for letter in alphabet:
        if len(square[2]) < 5:
            if letter not in square[0] and letter not in square[1] and letter not in square[2]:
                square[2].append(letter)
        else:
            break
    square.append([])

    # Setting up row four, verifies no same letters in row one or two or three or four
    for letter in alphabet:
        if len(square[3]) < 5:
            if letter not in square[0] and letter not in square[1] and letter not in square[2] and letter not in square[3]:
                square[3].append(letter)
        else:
            break
    square.append([])

    # Setting up row five, verifies no same letters in row one or two or three or four or five
    for letter in alphabet:
        if len(square[4]) < 5:
            if letter not in square[0] and letter not in square[1] and letter not in square[2] and letter not in square[
                3] \
                    and letter not in square[4]:
                square[4].append(letter)
        else:
            break

    # Finding my missing letter and adding it to last spot on list
    for letter in alphabet:
        if len(square[4]) <= 5:
            if letter not in square[0] and letter not in square[1] and letter not in square[2] and letter not in square[
                3] \
                    and letter not in square[4]:
                # Final letter will be called later when making digrams
                final_letter = letter
                square[4][4] = f"{square[4][4]}/{letter}"
        else:
            break



    # We do not need all of the extra empty lists we created, this gives us our 5 rows
    square = square[:5]
    return square
    # Old print method when it was used exclusively in python. Can be removed.
def print_square(square):
    for item in square:
        print(*item)
