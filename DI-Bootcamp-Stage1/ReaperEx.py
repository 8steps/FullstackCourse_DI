
def repeat_word(word, times):
    i=0
    while i < times:
        print(word)
        i +=1


repeat_word("Hello", 3)
print("")
repeat_word("Goodbye", 2)
print("")

def check_sign(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

check_sign(10)  # Output: "Positive"
check_sign(-5)  # Output: "Negative"
check_sign(0)   # Output: "Zero"
print("")

print_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for day in print_days:
    print(day)  

find_largest = [3, 7, 2, 9, 5]
largest = find_largest[0] 
for num in find_largest:
    if num > largest:
        largest = num
print(f"The largest number is: {largest}")  
