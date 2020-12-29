# vernamcipher
Vernam Cipher Message Encryption

The vernam cipher is a simple encryption method that's incredibly difficult to crack.

It works as such:

The user provides a message. For example "hello".

The user provides a key. The key must be the same length as the message.
For example "APPLE". The key's random nature is what drives the success of the vernam cipher.

The message and key are converted into numerical values with the following conversion table.

0: "!", 1: "\"", 2: "#", 3: "$", 4: "%", 5: "&", 6: "\'", 7: "(", 8: ")",
      9: "*", 10: "+", 11: ",", 12: "-", 13: ".", 14: "/", 15: "0", 16: "1", 17: "2", 18: "3",
      19: "4", 20: "5", 21: "6", 22: "7", 23: "8", 24: "9", 25: ":", 26: ";", 27: "<", 28: "=",
      29: ">", 30: "?", 31: "@", 32: "A", 33: "B", 34: "C", 35: "D", 36: "E", 37: "F", 38: "G",
      39: "H", 40: "I", 41: "J", 42: "K", 43: "L", 44: "M", 45: "N", 46: "O", 47: "P", 48: "Q",
      49: "R", 50: "S", 51: "T", 52: "U", 53: "V", 54: "W", 55: "X", 56: "Y", 57: "Z", 58: "[",
      59: "\\", 60: "]", 61: "^", 62: "_", 63: "`", 64: "a", 65: "b", 66: "c", 67: "d", 68: "e",
      69: "f", 70: "g", 71: "h", 72: "i", 73: "j", 74: "k", 75: "l", 76: "m", 77: "n", 78: "o",
      79: "p", 80: "q", 81: "r", 82: "s", 83: "t", 84: "u", 85: "v", 86: "w", 87: "x", 88: "y",
      89: "z", 90: "{", 91: "|", 92: "}", 93: "~"
      
This conversion table is not necessary to use and can be substituted with a simpler 0-26 if
only using non case sensitive lettering.

Therefore, "hello" becomes:

  h  e  l  l  o
  71 68 75 75 78

And "APPLE" becomes:

  A  P  P  L  E
  32 47 47 43 36

Then the corresponding values from each of these lists of numbers is added together.
This is why the message and key are of the same length.

(71 + 32) (68 + 47) (75 + 47) (75 + 43) (78 + 36)
103 115 122 118 114

Then we use this list of numbers to convert back to the corresponding letters from the conversion
table we used previously. However, as you can see, some of these numbers exceed the maximum value set
in the conversion table (93). Therefore, if any of the values is greater than 93, we subtract by 93.

So, 103 115 122 118 114 becomes:

10 22 29 25 21

Then we can easily  convert to the corresponding letters. 10 22 29 25 21 becomes:

+ 7 > : 6

This is our encrypted message!

To decrypt the message you have to have the key, but you can follow the same method to work backwards.

The more times you use the same key with messages, the easier it will become to crack the code.
