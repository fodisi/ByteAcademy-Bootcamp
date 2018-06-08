#Caesar's Cipher
#================

#[Caesar's Cipher](http://en.wikipedia.org/wiki/Caesar_cipher) is named after Julius Caesar, who used it with a shift of three to protect messages of military significance.

#A shift of three to the right would change the letters thusly:

#	A => D
#	B => E
#	C => F
#	...
#	Z => C

#A shift of three to the left would change the letters... 

#	A => X 
#	B => Y 
#	C => Z
#	D => A
#	...

#Of course this offers no communication security whatsoever - except in Roman times when most people couldn't read to begin with.

#But the Caesar Cipher is [still used](http://en.wikipedia.org/wiki/ROT13) in cryptography, in addition to many other methods. So this is your first step into the world of security and data encryption.

#To understand how to complete this challenge, you must first understand the [ASCII](http://en.wikipedia.org/wiki/ASCII) standard. In short, every key on your keyboard has an [assigned numeric value](http://www.asciitable.com/).

#In Python, we use the following methods to get the ASCII decimal value.
#```python
#		ord('a') # => 97
#		ord('A') # => 65
#		ord('x') # => 120
#```

#To get the ASCII character from an integer, we use the `chr` function.
#```python
#		chr(97) # => 'a'
#		chr(65) # => 'A'
#		chr(32) # => ' ' (Yes that's an empty space, it has a value too!)
#```
#[Check out this video for some extra help understanding the Caesar Cipher](https://youtu.be/36xNpbosfTY).
##### Round 1

#Write the `caesar` function that takes two inputs. The first input is a a message as a string. The second input is an integer, which is the number used for shifting in the Caesar Cipher. the `caesar` function should return the shifted message as a string.

#Make sure you ignore spaces, symbols, and numbers. The end user wants to see these characters unchanged in the encrypted cipher. Capital letters should remain capital, and lower case letters should remain lower case.

##### Round 2
#Create a new decrypt function. Again, you'll take two inputs. The first is analready encrypted string, the second input is shift number, The function should return the decrypted message as a string. 

##### Round 3

#Using Python's `assert` write at least 6 tests to test your code output.

##### Extra Resources
#[CS50 video about how a Caesar Cipher works](https://youtu.be/36xNpbosfTY).


from enum import Enum


class Cypher_Mode(Enum):
    ENCRYPT = 1
    DECRYPT = 2


class Cypher():
    
    ##ascii codes for uppercase letters [A, B, C, .., Z]
    __upper_ascii = range(ord('A'), ord('Z') + 1)
    ##ascii codes for lowercase letters [a, b, c, .., z]
    __lower_ascii = range(ord('a'), ord('z') + 1)

    def __apply_cypher(self, message, shift, mode):
        alphabet_size = 26
        encrypted_message = []

        # makes the necessary adjustments to variables, so the algorithm runs properly
        # encrypting: alphabet_size MUST be negative, so it can restart from A/a, when ascii codes reaches Z/z
        #decrypting: shift must be inverted (positive => negative), so we can reverse the encryption
        if mode == Cypher_Mode.ENCRYPT:
            alphabet_size *= -1
        elif mode == Cypher_Mode.DECRYPT:
            shift *= -1
        else:
            return "Invalid parameter MODE"

        #PSEUDOCODE
        # iterates the message
        # if char is a letter, applies the cypher algorithm and change the char in the message
        # otherwise, keeps the original char
        # adds the char to the encrypted message
        for ch in message:
            new_char = ch
            if ch.isalpha():
                ascii_code = ord(ch) + shift
                if (ascii_code not in self.__upper_ascii) and (ascii_code not in self.__lower_ascii):
                    ascii_code += alphabet_size
                new_char = chr(ascii_code)
            encrypted_message.append(new_char)

        return ''.join(encrypted_message)

    #encrypts a message with caesar cypher algorithm using a specific shift number
    def encrypt(self, message, shift):
        return self.__apply_cypher(message, shift, Cypher_Mode.ENCRYPT)

    #decrypts a message with caesar cypher algorithm using a specific shift number
    def decrypt(self, message, shift):
        return self.__apply_cypher(message, shift, Cypher_Mode.DECRYPT)


c = Cypher()

original_message = "a.A 1 b,B _2- wW = xX 3 yY *4 zZ -.,"
encrypted_message = "d.D 1 e,E _2- zZ = aA 3 bB *4 cC -.,"
assert c.encrypt(original_message, 3) == encrypted_message, original_message + 'encrypted successfully with shift 3'
assert c.decrypt(encrypted_message, 3) == original_message, encrypted_message + 'decrypted successfully with shift 3'

original_message = "c.C 1 d,D _2- rR = aA 3 sS *4 zZ -.,"
encrypted_message = "f.F 1 g,G _2- uU = dD 3 vV *4 cC -.,"
assert c.encrypt(original_message, 3) == encrypted_message, original_message + 'encrypted successfully with shift 3'
assert c.decrypt(encrypted_message, 3) == original_message, encrypted_message + 'decrypted successfully with shift 3'

original_message = "123456789.+-*;[]{}<>?!@#$%^&*()_+           123"
assert c.encrypt(original_message, 3) == original_message, original_message + 'not changed'
assert c.decrypt(original_message, 3) == original_message, encrypted_message + 'not changed'

original_message = "a.A 1 b,B _2- wW = xX 3 yY *4 zZ -.,"
encrypted_message = "e.E 1 f,F _2- aA = bB 3 cC *4 dD -.,"
assert c.encrypt(original_message, 4) == encrypted_message, original_message + 'encrypted successfully with shift 4'
assert c.decrypt(encrypted_message, 4) == original_message, encrypted_message + 'decrypted successfully with shift 4'

original_message = "a.A 1 b,B _2- wW = xX 3 yY *4 zZ -.,"
encrypted_message = "b.B 1 c,C _2- xX = yY 3 zZ *4 aA -.,"
assert c.encrypt(original_message, 1) == encrypted_message, original_message + 'encrypted successfully with shift 1'
assert c.decrypt(encrypted_message, 1) == original_message, encrypted_message + 'decrypted successfully with shift 1'

original_message = "a.A 1 b,B _2- wW = xX 3 yY *4 zZ -.,"
encrypted_message = "a.A 1 b,B _2- wW = xX 3 yY *4 zZ -.,"
assert c.encrypt(original_message, 0) == encrypted_message, original_message + 'encrypted successfully with shift 0'
assert c.decrypt(encrypted_message, 0) == original_message, encrypted_message + 'decrypted successfully with shift 0'

