a = float (input ("Enter the length of side 1 = ") )
b = float (input ("Enter the length of side 2 = ") )
c = float (input ("Enter the length of side 3 = ") )
if (a == b and a == c):
     print ("The Triangle is isolateral")
elif (a == b or b == c or a == c):
     print ("The Triangle is isoscale")
else:
     print ("The Triangle is scalene")
