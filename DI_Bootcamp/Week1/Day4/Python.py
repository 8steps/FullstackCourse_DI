people = ["Rick", "Morty" , "Beth"]

#for person in people:
 #   if len(person) <= 4:
  #      print(person)

def say_hello(Person):
    print(f"Hello to you {Person}")

map_people = filter(lambda person: len(person) <= 4 , people)
People_Hello = list(map_people) 

for person in People_Hello:
    say_hello(person)