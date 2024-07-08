def greaTest(a , b , c):
    if (a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif( c > b and c > a):
        return c
a = 14
b = 25
c = 37

print(greaTest( a , b , c))



# temperature
# c/5 = (f- 32)/9    formula

def f_to_c (f):
    return 5*(f-32)/9
f = int(input("enter temperature in F:"))
c = f_to_c(f)
print(f"{round(c, 2)} degree °C")


'''
sum(n) = 1 
'''



def sum(n):
    if ( n == 1):
        return 1
    return sum ( n - 1) + n
print(sum(5))

def pattern(n):
    if(n == 0):
     return
     print("*" * n)
     pattern ( n - 1)

pattern(3)    


def inc_to_cm(inc):
    return inc * 2.54
n = int(input("enter a number:"))

print(f"the value in cms is { inc_to_cm(n)}")

def ml ( n ):
    for i in range( 1, 11):
        print(n*i)

ml(5)        
