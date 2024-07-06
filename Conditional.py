# Conditonal Statements  ----> if , elif , else
myage = 19

if( myage >= 18 ):
 print("you can vote")
elif(myage):
 print("not vote")



#Traffic light

light = "no"
if( light == "red"):
 print("stop")
elif(light == "yellow"):
 print("look")
elif(light == "green"):
 print("go")
else:
 print("light is broken")
  


marks = int(input ("enter your marks"))

if (marks >= 80):
    gread ="A"
elif(marks >= 70 and marks< 80):
 grade = "B"
elif( marks >= 60 and marks < 70):
 grade = "C"
else:
 grade ="D"
print(marks,"grade" , grade )

#nesting

age = 34
if ( age >= 18):
 if ( age >= 80):  #nesting 
  print( "you cannot drive")
 else:
  print( "can drive")
else:
 print("not")



 #odd and even print
num = int(input ("enter number"))
if (num %2 == 0):
 print("even")
else:
 print("odd")



# greter number

 a = int(input("first num"))
 b = int(input("second") )
 c = int(input("third"))
 d = int(input("four "))
 if ( a >= b and a >= c and a >= d):
  print("first is greter numbwer",a)
 elif( b >= a and b >= c and b >= d):
  print(" second number ",b)
 elif( c >= a and c >= b and c >=d ):
  print("third id greter",c)
 else: 
  print("four is large", d)


 
x = int (input("remnder number"))
if ( x % 7 == 0):
   print ("remender" )
else :
 print("not a multiple number")




agenumber = int(input(" number:"))

if ( agenumber >= 20):
 print( " adult")
else:
  print("child")