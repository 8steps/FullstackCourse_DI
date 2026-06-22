MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

matrix = [list(row) for row in MATRIX_STR.strip().split('\n')]

columns = len(matrix[0])
rows = len(matrix)
decoded_message = ""
for col in range(columns):
    for row in range(rows):
        if matrix[row][col].isalpha() == True:
            decoded_message += matrix[row][col]
        else:
            decoded_message += " "

print(decoded_message)