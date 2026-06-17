# What are the results?

my_string = "Hello Class"
my_number = 18
# Exercise 1
print(my_string + my_string * 3) # will only show my string 4 times in the same line .
# Exercise 2
print((my_string + '\n')*2, end='!!!\n') # will show my string twice in new lines and in the a new line !!!
# Exercise 3
print(my_string == my_string.lower()) # will print my string in lower cases 
# Exercise 4
print(my_number // 5) #will show 3
# Exercise 5
print(my_string + "_" * (my_number // 9) + str(my_number)) #will show Hello Class__18
# Exercise 6
print(my_number % len(my_string)) #will show 1
# Exercise 7
print(my_string[8].capitalize()) #will show "A"
# Exercise 8
if my_number % 4 != 0:
    print(my_string[0:4])
else:
    print(my_string[-3])  #will print the if statment 
# Exercise 9
print(bool(len(my_string) > 5)) #will print true
# Exercise 10
print(bool(my_number < 5) + 7) #will print 7
# Exercise 11
print(abs(bool(my_number > 10) - 8)) #will return 7 because its abs
# Exercise 12
print(not bool(None)) #True
# Exercise 13
print(int(my_number is str)) # 0 #its returns false which is 0 in bool
# Exercise 14
print(str(3 == 3 == 3)) #True
# Exercise 15
print(float(3 == 3 == 3)) #1.0
# Exercise 16
print(my_string[my_number // len(my_string)]) # will print e
# Exercise 17
print((' ' not in my_string) * 3.5) #0.0
# Exercise 18
print(f"{len(my_string)} chars in \"{my_string}\"") #11 chars in "Hello Class"
# Exercise 19 (*)
print(ord(my_string[3])) #
# Exercise 20 (*)
result = ""
for c in my_string:
    if 96 < ord(c) < 123:
        result += c
print(result) #ellolass