#Exercise1
my_fav_numbers = [1, 2, 3, 4]

my_fav_numbers += [5, 6]

friend_fav_numbers = [10, 11, 12, 13]

our_fav_numbers = my_fav_numbers + friend_fav_numbers

print(our_fav_numbers)

#Exercise2

New_tuple = (1, 2, 3)

New_List = list(New_tuple)

New_List[2] = 4 

New_tuple = tuple(New_List)

print(New_tuple) #A tuple by itself cannot be changed but you can extract its value change it to a list and than change its values and revert back to tuple .

#Exercise3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.append("Apples")
basket.count("Apples")
basket.clear()
print(basket)

#Exercise4

Num_Count = []
Current_num = 1.5

while Current_num <= 5:
    if Current_num.is_integer():
       Num_Count.append(int(Current_num))
    else:
       Num_Count.append(Current_num)
    Current_num += 0.5      
print(Num_Count)

#Exercise5
i= 0
for i in range(1, 21):
   print(i)
   i+= 1
 
f = 0 
for f in range(1, 21):
   f+= 1
   if f % 2 == 0:
      print(f)

#Exercise6
Name = input("Please enter your name:")

while Name == Name.isdigit() or len(Name) <= 3:
   Name = input("Please enter your name:")
print("thank you")

#Exercise7

List_Input_Fruits = input("please input your favorite fruits separated with \"space\": ")
List_Fruits = List_Input_Fruits.split()
Test_Fruit = input("Please select ONE of those favorite fruits:")

if List_Fruits.count(Test_Fruit) == True :
   print("You chose one of your favorite fruits! Enjoy!")
else:
   print("You chose a new fruit. I hope you enjoy it!")

#Exercise8

Pizza_Toppings = []

while True:
   topping = input('Choose a topping for your pizza (type "quit" to finish): ')
   if topping.lower() == 'quit':
      break
   Pizza_Toppings.append(topping)
   print(f"Adding {topping} to your pizza.")

total_price = 10 + 2.5 * len(Pizza_Toppings)
print("The total toppings that you've chosen are: " + ", ".join(Pizza_Toppings))
print(f"And their price is: ${total_price}")

#Exercise9
Age_Movie = []

while True:
   Age = input("Please enter your age to calculate the price for the movie(type 'quit' to finish): ")
   if Age.lower() == 'quit':
      break
   Age_Movie.append(int(Age))

Total_Price = 0

for age in Age_Movie:
   if age < 3:
      Total_Price += 0
   elif 3 <= age <= 12:
      Total_Price += 10
   else:
      Total_Price += 15

print(f"The total price for the movie is: ${Total_Price}")
