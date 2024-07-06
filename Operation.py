# Arithmetic Operators

a = 5
b = 7

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  # remainder
print(a ** b)  # power # a^b

# relationl operations, comparison

c = 10
d = 15

print(c == d)
print(c != d)
print(c >= d)
print(c <= d)
print(c > d)
print(c < d)

# Assingment operators
# (=,+=,-=,*=,/=,%=,**=)
num = 10
num += 6   #num + num  
num **= 5

print("num",num)



#Logical oprators
 #( not , and , or)  return bool value
a = 20
b = 25
print(not True)  # single oprent useing
print(not  (a > b))

val1 = True
val2 = True  # dono value sach hogi tabhi  true hoga
print("and operater" ,val1 and val2)

val1 = False
val2 = True  # koi bhi value sach hogi true 
print("or operater" ,val1 or val2)
print("or operater" ,(a == b )or (a < b))