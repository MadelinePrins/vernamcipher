# vernamcipher
Vernam Cipher Message Encryption

The vernam cipher is a simple encryption method that's incredibly difficult to crack.

It works as such:

The user provides a message. For example "hello".

The user provides a key. The key must be the same length as the message.
For example "APPLE". The key's random nature is what drives the success of the vernam cipher.

The message and key are converted into numerical values with the following conversion table.
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
