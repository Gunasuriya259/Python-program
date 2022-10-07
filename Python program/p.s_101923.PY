def isperfectsquare (x) :

     if (x >= 0) :
                  sr = int (math.sqrt (x) )
                  return ( (sr*sr) == x)
     return false
x = 5

if (isperfectsquare (x) ) :
           print ("TRUE")
else:
            print ("FALSE")
