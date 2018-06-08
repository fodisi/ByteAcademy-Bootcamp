# Object Oriented Programming Day 1

### Learning Objectives
***Students Will Be Able To...***

* Initialize a class
* Call various methods from within a class
* Import a class

---
### Context

* Python is an object oriented language.
* It allows us to organize our code for efficiency and readability

---
### Lesson

#### Part 1 - What is OOP?

* Object Oriented Programming is the practice of writing your code around `Objects`
* This will become clearer as the lesson moves forward

#### Part 2 - What are Objects?

* Everything in Python is an object
* Every object is an `instance` of a class
* We know about the various data types and data structures. Well take `lists` for example. The moment you create a list you made an `instance` of it. This list now has access to all the methods inside the `list class` of Python3
* lists belong to a list class
* strings belong to a string class
* dictionaries belong to a dictionary class

#### Part 3 - Classes

* A class holds many methods that an object can respond to.
* They are defined with the word `class`
* They are always capitalized
* They are just blueprints for us to use later
* Lets make a class example for Car
* This car will take in three variables when created
* This car will have access to a method called `hello` that will print the make, model, and year to the to your terminal

```
class Car:
	"""
	We are making a car class
	"""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def hello(self):
		print("You have started your car, it is a {year} {make} {model}".format(year = self.year, make = self.make, model = self.model))

my_car = Car(make = "Bugatti", model = "Veyron", year = 2015)

my_car.hello()
```
* `docstring` - notice the three quotes followed by text and more three quotes?
	* This allows us to write multi line strings. 

***Five Min Exercise***

* Make a class of your favorite movie or tv show
* When the class is `instantiated` I want to have the following instance variables
	* self.cast
	* self.characters
	* self.release
	* self.genre
* I also want to be able to use the following methods
	* `.get_cast` will return me a list of cast members real names
	* `.get_characters` will return me a list of the characters in the movie
	* `.get_release` will return me the release date of that movie
	* `.get_genre` will return the genres this movie belongs to

#### Part 4 - Classes Terminology

* `Instantiate` - when we instantiate a class we are creating a new instance of that class.
* The`Car` class is a blueprint. We instantiate it by creating a variable with the Car class.
* This variable is now an `instance` of that care class
* We can use the class over and over again, if we had multiple cars, or in the example of your previous exercise, multiple movies.

#### Part 5 - Instance and Class Variables

* A class variable is a variable you want to be given to every instance of the class
* A instance variable is specific to that instance of the class
* The term `self` is used over and over again throughout class creation. This is referring to the object in that moment in time. (Instance of the object)
* Let's take the class example below

```
class Show:

    cinema = "Hollywood"
    
    def __init__(self, cast, characters, release, genre):
        self.cast = cast
        self.characters = characters
        self.release = release
        self.genre = genre

    def give_cast(self):
        return self.cast

    def give_char(self):
        return self.characters

    def give_date(self):
        return self.release

    def give_genre(self):
        return self.genre

p_cast = "Damian Lewis, Paul Giammatti"
p_char = "Bobby Axelrod, Chuck Rhoades"

p_s_show = Show(p_cast , p_char , 2016, 'Drama')
top_gun = Show("Tom Cruise, Val Kilmer", "Maverick, Iceman", 1986, "Action")
aos = Show("Chloe Bennett, Clark Gregg, Ming-Na Wen", "Skye, Coulson, May", 2013, "Comic")


print(p_s_show.cinema) === "Hollywood"
print(p_s_show.release()) === 2016

print(top_gun.cinema) === "Hollywood"
print(top_gun.release()) === 1986

print(aos.cinema) === "Hollywood"
print(aos.release()) === 2013
```
* `self` allows us to call the instance variables unique to that instance of a class
* We also specified a `class variable` with "cinema", that is a variable available to `EVERY INSTANCE OF THAT CLASS`

***Five Min Exercise***

* Create a class called `Athlete`
* Create three or more instances using that `Athelete` class
* Every athlete has two legs, two arms, and is_rich(true)
* Each athlete has THEIR OWN name, sport, team, height, weight

#### Part 6 - Scope

* Scope works inside out
* The methods and variables that are local will have access to those outside of it, however, the outside does not have access to the inside.
* Think about Russian Nesting Dolls
* `return` is what allows us to move values and variables between two different things
* Take a look at the example below:

```
name = "Jason"

def hello():
	name = "Barry"
	return "Hello " + name

print(hello()) === "Hello Barry"
```
* The above example will print "Hello Barry"
* The `hello` function will look inside of it's local scope for a variable called `name`. Since if found `name` it will not bother looking at any outer scope
* Let's take a look at another example

```
name = "Jason"

def hello():
	name = "World"
	return "Hello " + name
	
def goodbye():
	return "Goodbye " + name

print(hello()) === "Hello World"
print(goodbye()) === "Goodbye Jason"
```

#### MISC

* triple quotes doc string used to comment your code and help others read your code
* If you want to try something else, check out Python Lambdas.
	* [Python Conquers the Universe Lambda Tutorial](https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/)
	* [Python 3 docs](https://docs.python.org/3/tutorial/controlflow.html)

#### Resources

* [Tutorials Point explanation of classes and objects](http://www.tutorialspoint.com/python/python_classes_objects.htm)