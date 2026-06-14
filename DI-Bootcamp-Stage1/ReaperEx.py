
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


def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_largest([1, 2, 3, 4]))  
print(find_largest([10, 20, 5])) 
print("")

def check_letter(word, letter):
    if letter in word:
        print("True")
    else:
        print("False")

check_letter("Hello", "e")  
check_letter("Hello", "a")  

def count_to_number(n):
    for i in range(1, n + 1):
        print(i)
print("")
count_to_number(3)
print("")
count_to_number(5)  