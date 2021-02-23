row_1=int(input("Enter row size of matix 1 : "))
column_1=int(input("Enter column size of matix 1 : "))
row_2=int(input("Enter row size of matix 2 : "))
column_2=int(input("Enter row column of matix 2 : "))

print(f"Order is {row_1} x {column_1} * {row_2} x {column_2} and resulting matrix is {row_1} x {column_2}")

matrix_1=[]
matrix_2=[]
matrix_3=[]
for i in range(row_1):
    a=[]
    for j in range(column_1):
        print(f"Enter item [{i+1}][{j+1}]")
        a.append(int(input()))
    matrix_1.append(a)
print("Matrix 1 is : \t")
for i in range(row_1):
    for j in range(column_1):
        print(matrix_1[i][j],end=" ")
    print()

print("\n And for matrix 2 , \n")
for i in range(row_2):
    b=[]
    for j in range(column_2):
        print(f"Enter item [{i+1}][{j+1}]")
        b.append(int(input()))
    matrix_2.append(b)
print(" Matrix 2 is : \t")
for i in range(row_2):
    for j in range(column_2):
        print(matrix_2[i][j],end=" ")
    print()

print("\n Multiplying...\n")

for i in range(row_1):
    for j in range(column_2):
        for k in range(row_2):
            matrix_3[i][j] += matrix_1[i][k] * matrix_2[k][j]
            

for m in matrix_3:
    print(m)
        

    
