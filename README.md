# Playfair Cipher

#### This program takes user input to be used as a key code. The Playfair grid is then filled in using the keycode. The user is then given an encrypted message that they must solve.
<hr/>

## I do not know what a Playfair Cipher is!
Many people are most likely unfamiliar with the Playfair Cipher and how to solve them. I have created a PDF to help explain the entire process. 
From starting with an empty 5x5 square to encrypting a message. You can check out <a href="PlayFair Presentation.pdf">How to create and solve a Playfair Cipher</a>
<hr/>

## How it's made
##### Tech Used: Python HTML CSS Flask Bootstrap
This was my first project created 100% by me. I had chosen Python as it is the language I am most comfortable with. I needed to break this problem into different modules.

###### Creating the 5x5 Grid
I needed to create a 5x5 Grid containing all the English alphabet letters, with the final square containing 2 letters. I created a function named make_square that would be responsible for creating this grid.
It could take in a parameter, and this parameter would be the key code the user would input. The function then capitalizes the key code and removes any element that's not an alphabet character.
Next, the key code has any non-unique element removed, while retaining the order. With this newly formatted key code, the grid starts filling in. Each row can only hold 5 elements,
the grid then adds the key code to each row. Once the key code is finished being added, the alphabet letters are parsed, removing the already existing key code letters, and adding those to the grid.

###### Creating the Digrams
To create a digram we need a phrase. I load phrases in from phrases.txt, into make_digram. The first thing we must do to the phrase is remove all the punctuation. Next, we split the message into pairs and add each pair to a list. Then we verify each pair are different letters, if not, then we add an X between them. If this happens, we rerun our first function, which breaks all the letters back into pairs. We also check to see if the final element has 2 letters, if it is only 1 letter, we add the last letter in the grid to make this a pair. Once every element has 2 letters and each item is unique, we move on to encrypting the message.

###### Encrypting the Message
This is the heart of the program, plain_to_encrypt. We begin by assigning 4 blank variables, these variables will track the row, and column of each letter. Iterating through the grid, when we locate the first letter we record its row and its index. The row we find by using enumerate on the grid, and the index gives us which column the letter will be in. We do this for the second letter as well. Now we check to see if they are in the same column, if they are we add 1 to each of the columns, and if that number is greater than 5, we reset it to 0. We do the same for rows, except shifting right. Lastly if they are in different rows, and different columns, letter ones column is now equal to letter twos column. Letter two's column is equal to letter ones column. We then retrieve the letters from these locations, append them to a new list and print them out.

###### Creating and Pushing to the server
coming soon
<hr/>

## Known Issues
coming soon
<hr/>

Author: Harley Reimels

Contact: Reimels.Harley@gmail.com

