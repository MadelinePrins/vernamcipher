"""
---------------------------
@Author: Madeline Jade Prins
@Description: A simple program that takes a message and key and returns an
    encrypted version of the message using the Vernam Cipher algorithm.

@Github: https://github.com/MadelinePrins
---------------------------
"""

class vernam():

    def __init__(self):
        #things that a vernam object is going to have
        self.message = ""
        self.key = ""
        self.encryptedmessage = ""
        self.msgLength = 0
        self.keyLength = 0
        #simplified ascii table including only punctuation, 0-9, A-Z, and a-z
        self.asciiDict = {
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
        }

    """
    Prompts user for the message and save the length of the message
    """
    def get_message(self):
        print("Enter plain text message below. Punctuation allowed. Case sensitive.")
        self.message = str(input())
        print("Your message is :", self.message)
        self.msgLength = len(self.message)
        print("message length: ", self.msgLength)

    """
    Prompts user for the key and ensures that it's the same length as the message.
    Reprompts user if it isn't the correct length.
    """
    def get_key(self):
        print("Enter key of the same length as message")
        self.key = str(input())
        self.keyLength = len(self.key)
        if(self.msgLength != self.keyLength):
            print("Key length is not the same as message length.")
            print("Your message was ", self.msgLength, " characters.")
            print("Your key must also be ", self.msgLength, " characters.")
            print("RE-ENTER a new key below:")
            self.get_key()
        else:
            print("Key accepted")
        return

    """
    Loops through all of the characters in a token (string that's passed in) and converts
    each character to a corresponding numerical value grabbed from 'asciiDict'. Note that the
    numerical values are a simplified version of the ascii table including only punctuation,
    A-Z, a-z, and 0-9.
    @return an array of integers representing the numerical equivalents of the string.
    """
    def convert_characters(self, token):
        asciiConversion = []
        #for each of the characters, find the corresponding ascii character and sub it
        for char in token:
            for key, value in self.asciiDict.items():
                if char == value:
                    conv = key
            asciiConversion.append(conv)
        return asciiConversion

    """
    Calls the conversion method on the message and keys provided by the user. Sums the
    corresponding indeces of the two converted strings.
    @return an array of the summed integers.
    """
    def add_key_message(self):
        #convert the message and keys into ascii and put them in these objs
        aMessage = self.convert_characters(self.message)
        aKey = self.convert_characters(self.key)
        summed = [] #empty array to hold the sums
        #sum up the corresponding array values
        for i in range(0,self.msgLength):
            sum = aMessage[i] + aKey[i]
            if(sum > 93):
                sum = sum - 93
            summed.append(sum)
        return summed

    """
    Calls the addition function that sums the key and message. Converts each of the
    numerical values in the array returned to the corresponding value in the ascii dictionary.
    @return a string of the encrypted message
    """
    def encrypt_message(self):
        sums = self.add_key_message()
        encrypted = ""
        for number in sums:
            #grab the corresponding ascii value from the dictionary
            encrypted += self.asciiDict[number]
        print("encrypted message: ", encrypted)

#utility details
def main():
    vernamCiph = vernam() #create object of class vernam
    vernamCiph.get_message()
    vernamCiph.get_key()
    vernamCiph.encrypt_message()
if __name__ == "__main__":
    main()
