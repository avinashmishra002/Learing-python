def fun():            #syntex
    print("hello")


fun() #call
print("thank you")


def goodDay(name):     #name is argument
    print("hello"+ name)
    return "ok"
    

a = goodDay("hii")
print(a)


def  func( name , ending = "thank you"):
    print("good day", name)
    print(ending)

func("avinash" )
func("hey")


# factorial(5) = 5 x 4 x 3 x 2 x 1

'''
factorial(5) = 5 x 4 x 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(3) = 3 x 2 x 1
factorial(2) = 2 x 1
factorial(1) = 1
factorial(0) = 1
factorial (n) = n * factorial(n - 1)


'''
def factorial(n):
    if (n==0 or n ==1):
        return 1
    return n * factorial(n - 1)

n = int(input("entr a number"))
print(factorial(n))


def sum( a ,b):
    return a + b
i = sum (123 , 4)
print(i)

def num( x , y):

    return x / y
z = num ( 23 , 5)   
print(z)



def print_hello():
    print('hello')

print_hello()    



def aveg ( a, b , c):
    sum = a + b + c
    avg =sum / 3
    
    print(avg)
    return avg
aveg(1,2,3)    

list = ["delhi" , "pune", " gurgaon", " mumbai","goa"]
hero= [ "saktiman" , "ironman" , "thor", " hulk"]


def print_len(i):
    print(len(i))

def print_list(i):
    for item in i:
        print(item , end=" ")

print_len(hero)




def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)    



def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD=", inr_val,"INR")

converter(1.5)