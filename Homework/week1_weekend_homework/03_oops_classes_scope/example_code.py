class TV_Show:
    def __init__(self, show, cast, characters, release, genre):
        self.show = show
        self.cast = cast
        self.characters  = characters
        self.release = release
        self.genre = genre
    def my_show(self):
        return ("My Favorite Show Is {}".format(self.show))
    def my_cast(self):
        pass
    def my_characters(self):
        pass
    def my_release(self):
        pass

    def my_genre(self):
        pass

jasons_show = TV_Show(show = "The Black Donnellys", cast = ["I don't remember", "Olivia Wilde"], characters = ["Donnelly Brothers", "some bad irish people", "some bad italian people"], release = 2008, genre = "Badass")

print(jasons_show.my_show())




# class Car:
#     """
#         We're making a class for Cars
#         the car is my lover
#     """
#     wheels = 4 # this is a class variable    
#     def __init__(self, make, model, year):
#         self.make   =   make
#         self.model  =   model #this is an instance variable
#         self.year   =   year

#     def hello(self):
#         print("You have a started your car, it is a {year} {make} {model}".format(year = self.year, make=self.make, model=self.model))

#     def how_many(self):
#         print("You have {x} wheels".format(x = self.wheels))

#     def blah(self, x):
#         print("this is ", x)


# my_car = Car(make="Bugatti", model="Veyron", year="2080")
# henry_car = Car(make="Audi", model="R8", year="2016")
# my_car.hello()
# my_car.how_many()
# henry_car.hello()
# henry_car.how_many()
























class Athlete:

    legs = 2
    arms = 2
    is_rich = True

    def __init__(self, name, sport, team, weight):
        self.name = name
        self.team = team
        self.sport = sport
        self.weight = weight

    def appendages(self):
        return(self.arms + self.legs)

jeff = Athlete(name='jeff', sport='swimming', team='sharks', weight=500)
jason = Athlete(name='jason', sport='crickey', team='spellers', weight=500)

print(jeff.appendages())


