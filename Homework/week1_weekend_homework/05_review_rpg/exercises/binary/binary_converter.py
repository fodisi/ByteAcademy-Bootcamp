#Binary Converter
#================

#In this exercise you will be making functions that convert between base 10 numbers and binary.

#Binary notation is based on powers of 2. Each digit is a power of 2. The first digit is 2^0, second 2^1, etc... You then add all of the digits together.

#For example, 101 is 5 (4 + 1). 110 is 6 (4 + 2). 1100 is 12 (8 + 4)  
#Here is a chart of some base 2 vs base 10 notation numbers:  

#        0.....0  
#        1.....1  
#        10.....2  
#        11.....3  
#        100.....4  
#        101.....5  
#        110.....6  
#        111.....7  
#        1000.....8  
#        1001.....9  
#        1010.....10  
#        1011.....11  
#        1100.....12  
#        1101.....13

#####Step 1

#Write a method that takes binary numbers and outputs a base 10 number.

#        binary_to_decimal(1011) ## returns 11

#####Step 2

#Write a method that takes decimal numbers and returns it in binary notation.

#        decimal_to_binary(12) ## 1100

#Resources
#----------
#[How to Convert Decimal to Binary](http://www.wikihow.com/Convert-from-Decimal-to-Binary)

#[Harvard lecture on Binary](https://www.youtube.com/v/lhlBWlhS7Vg&amp;start=421&amp;end=1106)

#[Harvard tutorial on Binary](https://www.youtube.com/v/hacBFrgtQjQ)


#### HOW TO CONVERT DECIMALS TO BINARY ##########
#convert 4 to binary
# 4 / 2 = 2(quotient);            4 mod 2 = 0(remainder)
# 2 / 2 = 1(quotient);            2 mod 2 = 0(remainder)
#quotient(1) < 2, then:
#puts together the last quotient (1) 
#with the remainders, from bottom to top,
#resulting in 100
##################################################

#Converts a decimal number to its binary representation
def decimal_to_binary(num):
    binary = []
    quotient = num
    remainder = 0

    while quotient > 1:
        #inserts the remainder to the binary list number.
        #inserts at position=0, because binary numbers are formed 
        #by reading remainders in reversed order (from bottom to top)
        binary.insert(0, quotient % 2)
        quotient = quotient // 2
    
    #inserts the last remainder and adds it to the list
    binary.insert(0, quotient % 2)

    s = (str(digit) for digit in binary)
    return int(''.join(s))

#### HOW TO CONVERT BINARY TO DECIMALS ##########
#How to convert binary to decimal
#The decimal number is equal to the sum of binary digits (dn) times their power of 2 (2n):
#decimal = d0×20 + d1×21 + d2×22 + ...
#Example
#Find the decimal value of 111001(base_2):
#binary number:  1	    1	    1	    0	    0	    1
#power of 2:	 2^5    2^4	    2^3	    2^2	    2^1	    2^0
#111001(base_2) = 1*2^5 + 1*2^4 + 1*2^3 + 0*2^2 + 0*2^1 + 1*2^0 = 57(base_10)
##################################################

#Converts a binary number to its decimal representation
def binary_to_decimal(num):
#splits the digits of a number into a list, i.e., 11001 = [1,1,0,0,1]
    digits = list(int(digit) for digit in str(num))
    
    #sets the power to size(num) -1, considering 0-based index
    power = len(digits) -1
    decimal_number = 0
    #iterates the digits' list, multiplying the digit by 2**power, where power == index of the digit in the list.
    for i in range(0, len(digits)):
        decimal_number += digits[i] * (2**power)
        power -= 1

    return decimal_number

def lazy_decimal_to_binary(num):
        return int("{0:b}".format(num))

def lazy_binary_to_decimal(num):
        return int(str(num), 2)


while True:
        print('type a number or "anything else" to exit')
        x = input()
        if not x.isdigit():
                break
        bin_n = decimal_to_binary(int(x))
        print("custom convertions")
        print(bin_n)
        print(binary_to_decimal(bin_n))

        print('python conversions')
        print(lazy_decimal_to_binary(int(x)))
        print(lazy_binary_to_decimal(bin_n))