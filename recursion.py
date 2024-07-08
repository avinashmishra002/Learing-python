# loop and recursion is't  similar but, 


def func( n):
    if( n==0):    # base case    , stoping
        return
    print(n)
    func( n -1)
func(5)



def fact (n):

    if (n == 0 or n == 1):
        return 1
    return fact(n - 1) * n
print(fact(6))

def recn(n):
    if(n == 0):
        return 
    print(n)
    recn( n - 1)

recn(5)

def sum (n):
    if (n ==0):
        return 0
    return sum( n - 1) + n
num=sum(10)
print(num)

def li ( list , index =0):
    if(index == len(list) ):
        return
    print(list[index])
    li(list,index+1)

fruits=["mango","apple", "banana"]
li(fruits)