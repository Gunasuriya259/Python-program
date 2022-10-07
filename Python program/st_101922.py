A = str(input("enter the 1st string : "))
B = str(input("enter the 2nd string : "))

a = len(A)
X = 0
for i in range(a):
    if(A[i] == B[i]):
        X += 1
print("number of matches :" , X)
