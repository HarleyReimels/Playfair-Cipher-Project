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
coming soon

###### Encrypting the Message
coming soon

###### Creating and Pushing to the server
coming soon
<hr/>

## Known Issues
coming soon
<hr/>

Author: Harley Reimels

Contact: Reimels.Harley@gmail.com

