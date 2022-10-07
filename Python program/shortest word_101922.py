srt = str(input("First String : "))
rts = str(input("Second Strig : "))

if len(rts) > len(srt):
    print("The Word With shortest Length :" , srt)
elif len(srt) == len(rts):
    print("Both Words" , srt , "and" ,rts , "Have Same Number of Letters")
else:
    print("The Word With shortest Length :" , rts)
