import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

i = 0

for num in list_of_numbers:
    test_num = target_number - num
    if test_num in list_of_numbers:
        print(f"{test_num} and {num} sums to the target_number {target_number}")
        i+=1
        if i == 2:   
          break
