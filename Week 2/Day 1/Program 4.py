num=int(input("enter a number"))
x=num
rev=0
while num>0:
    r=num%10
    rev=(rev*10)+r
    num=num//10
print("reverse of given number is ",rev)
if x==rev:
    print("the num is a palindrome")
    print("true")
else:
    print("the num is not a palindrome")
    print("false")
