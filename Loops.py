# while loop



i = 5  #iterators

while  i >= 1:
    print(i)
    i -= 1   # condition

 
print("end loop")
    
      
# 1 to 100 print
x = 1
while x <= 100:
    print(x)
    x += 1

print( "end")


# 100 to 1 print

p = 100

while p >= 1:  # stoping Condition
    print(p)
    p -= 1


n = int(input("enter num"))
table = 1

while table <= 10:
    print( n * table)
    table += 1
    





li =[ 2,3,4,5,6,7,8]
hero =[ "a" , "b ", " c" , "d"]
idx = 0
while idx < len(hero):
    print(hero[idx])
    idx += 1


li = (2, 3, 4, 5, 6, 7, 8)
x = 3
i = 0

while i < len(li):
    if li[i] == x:
        print("found", i)
       
    i += 1

li = (2, 3, 4, 5, 6, 7, 8)
x = 3
i = 0

while i < len(li):
    if li[i] == x:
        print("found", i)
        break  # Exit the loop after finding the element
    i += 1


n = 7

sum = 0
for i in range(1, n+1):
    sum += i
    print("total:", sum)
    

n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
    print("total:", sum)


n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
    print("factorial:", fact)
    

i = 1
while i <= 6:
    print(i)
    i +=1

i = 0 
while i <= 5:
    print("abcd")
    i = i+ 1


name = ["avi", " aman ", False, " 123"]
i = 0
while  (i<len(name)):
    print(name[i])
    i +=1
 

list = [ 1,2,3,4,5]
i = 0
while (i <len(list)):
    print(list[i])
    i += 1
    

n = int(input( "enter a  your num: "))
i = 1
sum = 0
while( i <= n):
    sum += i
    i +=1
    print(sum)


n = int(input('enter your number'))
product = 1
for i in range(1 , n+1):
    product = product * i
print(f"the fectorial of {n} is {product}")


# star pattern

n = int(input("enter num"))
for i in range(1, n+1):
 
    print(" "* (n-i), end="")
    print("*" *(2*i-1), end="")
    print("")




n = int (input( 'enter a number'))
for i in range(1, n+1):
    print("*"* i , end="")
    print("")
 
n = int(input("rnter a number"))
for i in range(1, n +1):
    if (i==1 or i==n):
     print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n - 2), end="" )
        print("*", end="")
    print("")    