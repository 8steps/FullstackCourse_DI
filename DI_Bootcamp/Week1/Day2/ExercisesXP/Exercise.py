#Exercise_1
print("Hello world\n"*4)
#Exercise_2
print((99**3)*8)
#Exercise_3
#>>> 5 < 3 #False
#>>> 3 == 3 #True
#>>> 3 == "3" #False
#>>> "3" > 3 #False
#>>> "Hello" == "hello" #False
#Exercise_4
computer_brand = "Gigabyte"

print(f"I have a {computer_brand} computer.")
#Exercise_5
name = "Daniel"
age = 30
shoe_size = 43
info = f"My name is {name} and my age is {str(age)} and my shoe size is {str(shoe_size)}"

print(info)
#Exercise_6
a = 1
b = 3
if a > b :
    print("Hello world")
else :
    print("Goodbye")    
#Exercise_7
Check_num = int(input("Lets check your number:"))

if Check_num % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd :(")    
#Exercise_8
Name_Test = input("Lets check if our names match :").capitalize()

if Name_Test == "Daniel":
    print("Wow! our names match , here's a Thumbsup 👍")
else :
    print("Too bad our names dont match , here's a Thumbsdown 👎")    
#Exercise_9
Check_height = int(input("What's your height is in CM:"))

if Check_height > 145:
    print("You are tall enough to get on the roller coaster!")
else:
    print("I'm sorry you need to grow abit before riding the roller coaster")   