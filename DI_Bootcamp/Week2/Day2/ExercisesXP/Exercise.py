#Exercise1
def display_message():
    print("I am learning about functions in Python.")

display_message()

#Exercise2
def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in Wonderland")

#Exercise3
def describe_city(city, country= "Unknown"):
    print(f"{city} is in {country}")

describe_city("Tel aviv")
describe_city("Reykjavik", "Iceland")

#Exercise4

import random 

def Accept_num(Num):
    rand = random.randint(1, 100)
    if Num == rand :
        print("You have succeded in gussing the number!")
    else:
        print(f"You have failed in gussing the number! Your number was: {Num} , but the random was: {rand}")

Guess = int(input("what's the number your'e gussing:"))

Accept_num(Guess)

#Exercise5
def make_shirt(Size="Large", Text="I love Python!"):
    print(f"The shirt's size is {Size} and is says {Text}")

make_shirt("Large")
make_shirt("medium")
make_shirt("Small", "Hello!")

#Exercise6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician)

show_magicians(magician_names)

def make_great(magician_names):
    for magician in magician_names:
        print(f"{magician} the Great!")

make_great(magician_names)

#Exercise7
def get_random_temp():
    return random.randint(-10, 40)

def main():
    temp = get_random_temp()
    print(f"The temperature is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, it's freezing! Wear some extra layers today!")
    elif temp < 16:
        print("Quite chilly! Don't forget your coat.") 
    elif temp < 23:
        print("Nice weather.")
    elif temp < 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()