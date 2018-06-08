# Week 1 Review Topics

#### Using Git

* Git is a collaboration tool that is universally used by programmers
* Below are the commands in git we will be using the most:
* `git init` - initialize a connection between that folder and git
* `git add` - show off your updates / differences between the repos
* `git commit -m "message here"` - add a message to this instance
* `git pull origin branch_name` - pull down the updates/changes from a repository
* `git push origin branch_name` - push up your changes to a repository
* `git checkout -b branch_name` - change to a different branch on your local machine, or create a new branch on your local machine
* `git status` - tells you what changes are in this folder and what branch you are on
* `git clone` - makes a copy of a targeted repo in a specified folder of your choice

***Notes***

* All of your daily repos will be done with branches

#### Mutable vs. Immutable

* Mutable = Can be changed / mutated
	* Lists
	* Dictionaries
* Immutable = Cannot be changed or mutated
	* Strings
	* Tuples
	
#### String Concatenation

* What does the word `concatenate` mean?
* What are the various ways to concatenate strings?

```
leo = "Leonardo"
raph = "Raphael"
mickey = "Michaelangelo"
donny = "Donnatello"

"The turtles, Leonardo, Raphael, Michaelangelo, Donnatello, are trained by their master Splinter; who was also mutated by the ooze."
```
* Remember that strings are `immutable` so when we concatenate we are making a brand new string, not merging them into one

#### Nested Data Structures

* What are nested data structures.

***Five Min Exercise***

```

jason = {
    "name" : "Jason",
    "hair" : "sexy",
    "height" : "5 feet 9.5 inches",
    "fav_movies" : {
        "John_Wick": {
            "cast" : ["Keanu Reeves", "William Dafoe","Adrianne Palicki", "John Leguizamo"],
            "year" : 2014,
            "rating" :7.2,
        },

        "Pitch_Perfect": {
            "cast" : ["Anna Kendrick", "Brittany Snow", "Rebel Wilson", "Anna Camp"],
            "year" : 2012,
            "rating" : 7.2,
        },

        "The_Usual_Suspects": {
            "cast" : ["Kevin Spacey", "Stephen Baldwin", "Gabriel Byrne", "Kevin Pollak"],
            "year" : 1995,
            "rating" : 8.6,
        },
    },
    "fav_atheletes": [
        "George St. Pierre",
        "Steve Nash",
        "Dominick Cruz",
        "Allen Houston",
    ],
}

```


##### Inheritance and Scope

* If you're having trouble remembering how scope works think about the accronym `LEGB`
	* Local
	* Enclosing
	* Global
	* Built In
* Example: 
	* A function will look for a variable locally (inside itself) first
	* If i can't find the variable it will move up one level to what it is enclosed in (such as a class or if it is a nested function)
	* It will then keep going up if there are multiple function levels until the global scope
	* THEN search the built in scope. 

***NOTES***

* Check out this [stackoverflow answer for class methods vs instance methods.](http://stackoverflow.com/questions/17134653/difference-between-class-and-instance-methods)

##### Notes from Review Session

```
class Player:

    hp = 100

    def __init__(self, name, gender, race):
        self.name = name
        self.gender = gender
        self.race = race
        self.hp = 100
        self.atk = 10
        print("Welcome {}".format(name))

    def attack(self):
        return monster.hp - self.atk 


name = input("Hi what is your name?")
gender = input("Type 1 for Male, enter 2 for Female")
race = input("are you a human, elf, or dwarf")

//Example code, not tested
//if gender != male and gender != female:
//    print("you did not choose an option")


//while player.hp > 0 and monster.hp > 0:
//    run the battle method
//        method option to run or to stay and fight


player = Player(name, gender, race)


class Player:
    def __init__(self, name):
        self.name = name 
        self.gender = "n/a"


player = Player(name=input("What is your name?\n"))


class Game:

    def __init__(self):
        blah = blah

    def gender_setup(self):
        gender = input("enter 1 for female, 2 for male")

        while gender != 1 and gender != 2:
            print("sorry that is not an option")
            self.gender_setup

```


