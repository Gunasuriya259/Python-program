x = int(input("Enter Number of Sentences : "))
a = []
y = []

for i in range(0,x):
    b = input("Enter a String : ")
    a.append(b)

for i in range(0,x):
    d = len(a[i].split())
    y.append(d)

print("String With Max Word Count :" , a)
print("Max Word in a String :" , max(y))
