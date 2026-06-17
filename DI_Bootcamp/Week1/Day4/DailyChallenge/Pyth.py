#Challenge1
num_input = int(input("Please input a number:"))
len_input = int(input("Please input the length:"))

Output = []
i = 0
while len(Output) != len_input:
    i+=1
    Output.append((num_input)*i)

print(Output)

#Challenge2
Word_input = str(input("Please input a word:"))

New_Word = ""

for char in  Word_input:
    if not New_Word or char != New_Word[-1]:
        New_Word += char
print(New_Word)