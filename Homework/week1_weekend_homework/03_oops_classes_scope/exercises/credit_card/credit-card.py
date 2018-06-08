# #Credit Card Validator
# ---

# ## Description
# Using the [Luhn Algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm), also known as "modulus 10", we will be determining the validity of a given credit card number.

# For now, we are just editing the included python file. You will find the skeleton of the `CreditCard` class inside.

# #### Challenge

# We want our class to have its three main properties set on [instantiation](http://en.wikipedia.org/wiki/Instance_(computer_science)) - `card_number`, `card_type`, and `valid`. Look at the code in `credit-card.py`, you'll see this already there.

# If the card number given passes the Luhn algorithm, valid should be true and cardType should be set to 'VISA', 'AMEX', etc. If it does not pass, valid should be false and cardType should be set to "INVALID"

# This way, we can do this:
# ```python
    # myCard = CreditCard('347650202246884')

    # myCard.valid ## true
    # myCard.card_type ## 'AMEX'
    # myCard.card_number ## '347650202246884'
# ```

# There are three instance methods, `determine_card_type`, `check_length`, and `validate`. You may perform these methods in the order you see fit.

# `determine_card_type` should check whether or not the credit card has valid starting numbers and return the card type.

# Visa must start with 4
# Mastercard must start with 51, 52, 53, 54 or 55
# AMEX must start with 34 or 37
# Discover must start with 6011

# `check_length` should check whether or not a credit card number is a valid length.

# Visa, MC and Discover have 16 digits
# AMEX has 15

# `validate` should run the Luhn Algorithm and return true or false.

# ###The Algorithm

# From the right most digit, double the value of every second digit. For example:

# `4 4 8 5 0 4 0 9 9 3 2 8 7 6 1 6`

# becomes

# `8 4 16 5 0 4 0 9 18 3 4 8 14 6 2 6`

# Now, sum all the individual digits together. That is to say, split any numbers with two digits into their individual digits and add them. Like so:

# `8 + 4 + 1 + 6 + 5 + 0 + 4 + 0 + 9 + 1 + 8 + 3 + 4 + 8 + 1 + 4 + 6 + 2 + 6`

# Now take the sum of those numbers and modulo 10.

# 80 % 10

# If the result is 0, the credit card number is valid.

# ### Tests

# Make sure your code passes all the assert tests.

# Write your own assert tests to test any other possible cases where your code might fail.

# ### Hints

# Keep your code super clean and [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself).

# If you are repeating yourself, stop and think about how to better approach the problem.

# Keep your code encapsulated - imagine your CreditCard class is an interface other code will need to read. You want it as separate and unentangled as possible. Your class should not be dependent on any code outside of it - except, of course, code to instantiate it.


class CreditCard:
    __card_digits = []

    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = self.determine_card_type()
        self.valid = self.validate()
        if not self.valid:
            self.card_type = "INVALID"

    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, card_number):
        self.__card_number = card_number
        self.__card_digits = list(int(card_number[i]) for i in range(len(card_number)))


# Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):
        if self.__card_digits[0] == 4:
            return "VISA"
        if self.__card_digits[0] == 5 and self.__card_digits[1] in [1, 2, 3, 4, 5]:
            return "MASTERCARD"
        if self.__card_digits[0] == 3 and self.__card_digits[1] in [4, 7]:
            return "AMEX"
        if self.__card_digits[:4] == [6, 0, 1, 1]:
            return "DISCOVER"
        #no previous condition satisfied, meaning the card is invalid
        return "INVALID"

# Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        if self.card_type in ["VISA", "MASTERCARD", "DISCOVER"]:
            return len(self.card_number) == 16
        if self.card_type == "AMEX":
            return len(self.card_number) == 15
        #no previous condition satisfied, meaning the card is invalid
        return False

# Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        #checks card length
        if not self.check_length():
            return False

        #makes a copy of card digits, so can transform it using Luhn Algorith
        luhn_digits = self.__card_digits[:]

        # iterates from n to -2, every to -2 elements
        #From the right most digit, double the value of every second digit.
        for i in range(len(luhn_digits) -2, -1, -2):
                num = luhn_digits[i] * 2
                #split any numbers with two digits into their individual digits and add them
                if num > 9:
                        num = num - 9
                #updates the digit with the right number
                luhn_digits[i] = num

        #takes the sum of the digits and modulo 10. If the result is 0, the credit card number is valid.
        return (sum(luhn_digits) % 10) == 0


# do not modify assert statements

cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440')

assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')

assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')

assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

cc = CreditCard('379179199857686')

assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')

assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')

assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"


cc = CreditCard('339179199857685')

assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"
