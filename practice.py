n = int(input("enter nunber:"))   

for i in range(1 , 11):
 print(f"{n}  X {i} = {n *i}")


# n = int(input("enter nunber:"))   while loop
i = 0
while  (i< 11):
 print(f"{n}  X {i} = {n *i}")
 i += 1

# prime number  print

n = int(input('enter number'))

for i in range(2 , n):
    if ( n % i) == 0:
        
     print('not prime')
    break
else:
     print(" not prime")

     