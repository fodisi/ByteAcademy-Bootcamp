# Python Fundamentals

### Learning Objectives

***Students Will Be Able To...***

* Create a variable in python
* Assign the different data structures to variables
* Write python statements using control flow
* Write python statements using loops and iteration

---
### Context

* The fundamentals of programming translate throughout every language
* Like learning any new language we're going to start with the basics and build up
* If you wanted to learn english you wouldn't start by reading a novel, but with the alphabet

---

### Lesson

#### Part 1 - Variables

* Variables are a way to store and save data for use
* This is called `assignment`. You are assigning a value to a variable
* Declaring Variables
	* Do not need to use `var`
	* Cannot start with a number
	* Cannot declare with special characters
	* Written in snake case
* Open up Python in the terminal

```
name = "Jason"
fav_num = 8
turtles = ["Raph", "Leo", "Mickey", "Donny"]
```
* variable declaration -  `name`, `fav_num` , `turtles`
* assignment - `=`
* values - `"Jason"`, `8`

#### Part 2 - Data Types

* Now you may have noticed that variables can hold different `types` of values
* These are called `Data Types`
	* Strings
		* Strings are immutable. Once they are declared they cannot be changed. You can add strings together to create a new string but you cannot mutate an already existing one
	* Numbers
		* Floats
			* decimals
		* Integers
			* whole number
	* Booleans
		* 0
		* False

#### Part 3 - Math Operators and Boolean Operators

* Python comes with the following symbols for mathematical operators.
* The language also supports PEMDAS
* `==`, `!=`, `<=`, `>=`, `<`, `>`
* Chaining Operators

```
1 < 2 < 3
//Is 1 less than two AND is two less than three
```
* Python also comes with these boolean operators
	* `and` / `or` / `not`
	
***Five Min Exercise***

```
"A" == "A"
// True or False?

"5" == "5"
// True or False?

8.00 == 8
// True or False?

2 == "2"
// True or False?

Declare three variables and assign them three random numbers.
Pass those variables to each other through chaining operators so that it will return True

Pass those variables to each other through chaining operators so that it will return False

For example: x < y < z == True || x < z < y == False
```


#### Part 4 - Control Flow

* Now we have reached `if/else` statements
* If an expression you passed in is `True` do something
* Else do something else

```
if expression == true:
	run code

if name == "Jason":
	print("That is an awesome name")
else:
	print("You should get a different name")

if number > 100:
	print("That's a big number")
elif number > 50 && number < 100:
	print("That's a medium number")
else:
	print("Your number is puny")
```
* Things to note
	* You don't need parenthesis
	* Put a semi colon after the expression you want to evaluate
	* `if` to `elif` to `else`
	* Tab to show what part of the function belongs where


#### Part 5 - Lists and Indexing

* What if you wanted to store more data.
* Can be assigned to variables
* Can hold different data types at once
* The values are indexed for us starting at zero

```
my_list = ["Jason", "Anna Kendrick", 2015, True]

my_list[0] == "Jason"

my_list[2] == 2015
```
* Just a heads up indexing through a list is similar to indexing with strings.
* the value at index zero will be the first element in the list, or the first letter in a string

#### Part 6 - Functions and Statements

* We declare our functions with the word `def` for define
* Functions follow the same naming principles as declaring variables
	* Snake case
	* Do not start with numbers or special characters
* Remember how we used white space to organize our code with if/else statements. Well that idea holds true everywhere in Python

```
def my_name():
	print("My name is Jason")
```
* Functions allow us to build code that is reusable
* This follows the concept of `DRY - Don't Repeat Yourself`
* Functions can also take parameters. These allow our functions to be more dynamic

```
5 + 5 = 10

2 + 4 = 6

def add(x,y):
	print(x + y)
```
* Putting it all together
* Let's make a function that will take in a parameter



#### Part 7 - Methods for Help

* `len()`
* `pop()`
* `append()`
* `split()`


***Five Min Exercise***

* Declare two variables: hero and color
* Assign them whatever you want
* Write a if else statement that will...
	* print("Mashed Potatoes") if hero == color or False
	* print("Tacos") if hero is not the same as color
	* print("Oysters") otherwise
	
#### Part 8 - For Loop

* Earlier we made this list 

```
my_list = ["Jason", "Anna Kendrick", 2015, True]
```
* What if I wanted to print out all those values to the terminal

```
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
```
* This seems really repetitive
* One of the core functionalities of programming are loops
* `Loops` are used to run a code block (a piece of code) over and over again until a condition is met

```
for item in my_list:
	print(item)

"Jason"
"Anna Kendrick"
2015
True
```
* What we just saw was a `for loop` in Python 
* `item` is a placeholder for the current element in the list. The word item could be any name you want it to be. 
* Here's one more example using `range()` method

```
for num in range(6):
	print(num)

1
2
3
4
5
```
* Same concept here. `num` is just a placeholder. You could write anything there and it will still work. `for xyz in range(6): print(xyz)`
* `range()` is a built in method
	* Remember we already saw some built in methods with `len()`, `append()` and the like
* `range()` will take in `ONE OR TWO` numbers.
	* `If only ONE number is entered` it will return to you a list from zero up to but not including that number. (That's why we only got up to 5 and not 6 in the example)
	* `If TWO numbers are entered` it will return a list for all numbers between the two. Not including the second number	

#### Part 9 - While Loop

* There is one more powerful `loop` we can utilize
* This is the `While Loop`
* Like the `For Loop` we use this to run a code block over and over again.
* The main difference is instead of passing an `iterable` data structure, we will be running the code block until a condition is no longer true.
* The below example may look similar to what you saw in the pre-work. 

```
i = 0

while i < 10:
	print(i)
	i+=1

print("All Done");

1
2
3
4
5
6
7
8
9
All Done
```
* Reading this code we
	* Assign a variable to zero
	* Run a while loop
	* The condition is if `i < 10`
	* If the condition is true run the code block
	* Increment the variable `i` by one
* If the condition is false the loop will end and the next statement will be run
* Be careful with `While Loops`. If you do not have anything to change the condition to `False` you will run into an infinite loop



