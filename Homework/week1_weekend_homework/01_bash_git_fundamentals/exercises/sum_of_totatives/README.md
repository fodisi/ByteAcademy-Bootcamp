# Divided We Fall part 2
---

##### Description
* Divisors of a number are those numbers that divide it evenly;

```
divisors of 60 = 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60
```
* Totatives of a number are numbers that are coprime to it.
* Coprime - two numbers that have no common factor but 1

```
totatives of 30 = 1, 7, 11, 13, 17, 19, 23, and 29
```
* Totient - the sum of the totatives

##### Challenge

* Write a function that takes an integer as an argument, and returns a list with three elements.
* The first element is a list of the totatives of that integer.
* The second element is the sum of the totatives of that integer.
* The third element is the number of totatives the integer has.

#####Example
```
[input]
60

[output]
[[1, 7, 11, 13, 17, 19, 23, 29], 120, 8]
```

##### RESOURCES

* _Hint_: You can write seperate functions. Each function will create one of the elements of the list that you return. The functions can call each other!

* [High Order Functions](http://effbot.org/pyfaq/how-do-you-make-a-higher-order-function-in-python.htm)
