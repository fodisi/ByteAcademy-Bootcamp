#Arabic to Roman Numerals Challenge
#==================================

#Did you know our numeral system - the symbols we use to represent numbers are called Arabic numerals? Fun fact, because now it gets serious. You're going to be translating Arabic to Italian.

#Write a function called `arabic_to_roman`  an integer as an argument and return a roman numerals string. For example:
#```
#60 >> LX  
#78 >> LXXVIII  
#99 >> XCIX  
#3000 >>> MMM  
#```
#Look up Roman Numerals to get a complete list and jog your memory on its ancient conventions. This is an easy challenge to code, but can be a difficult mental exercise. Don't overcomplicate it!

#Add your own assert statements to the bottom to test your code.


#!/usr/bin/env python3

converter = [(1000, 'M'),
             (900, 'CM'),
             (500, 'D'),
             (400, 'CD'),
             (100, 'C'),
             (90, 'XC'),
             (50, 'L'),
             (40, 'XL'),
             (10, 'X'),
             (9, 'IX'),
             (5, 'V'),
             (4, 'IV'),
             (1, 'I')]

#converts a Arabic number to a roman number
def to_roman(num):
    #zero has no representation in roman numerals.
    #it is called 'nulla', instead.
    if num == 0:
        return 'nulla'

    roman_number = []
    remainder = num

    for arabic, roman in converter:
        #gets the quotient of integer division and the remainder of modulo
        #between the remainder and the Arabic number(integer)
        quotient, remainder = divmod(remainder, arabic)
		
        #adds the representation to the list
        #note that since "roman" is a string, its multiplication
        #by a integer n, will make the roman numeral repeats n times.
        #i.e.: 'a' * 0 = ''; 'a' * 5 = 'aaaaa'
        roman_number.append(roman * quotient)
        if remainder == 0:
            break

    return ''.join(roman_number)

if __name__ == '__main__':
    print(converter)
    while True:
        print('type a positive number')
        num = input()
        if not num.isdigit():
            break
        print(to_roman(int(num)))

