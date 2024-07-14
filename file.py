# file input / output 
# python can be used to perform opertion on a file. (read & write data)

'''
types of all files

1. Tesx files : txt , docs , .log , character forms
2. Binary files : mp4 , mov , .png 
'''

#open , read & close file

f = open("my.txt" ,"r")
# data = f.read()
line1 = f.readline()

print(line1)
line2 =f .readline()
print(line2)
f.close()



f = open("demo.txt", "r+")      #read and overwrite (start)
f.write("new and ")
print(f.read())
f.close()



#with syntax

with open("demo.txt","r") as f:  #alias
    data = f.read()
    print(data)
    


with open("demo.txt","w") as f: 
   data = f.write("this is new data")
   print(data)



#deleting file

import os
os.remove("my.txt")      #delete


with open("prectise.txt","r") as f:
   data = f.read()

new_data = data. replace("java","python")  
print(new_data) 

with open("prectise.txt","w") as f:
    f.write(new_data)


def check_for_word():
    word = "learnig"
    with open("prectice.txt","r") as f:
        data = f.read()
        if (data.find(word)) != -1:
         print("found")
        else:
           print("not found")  

check_for_word()          

def check_for_line():
    word = "python"
    data = True
    line_no = 1
    with open("prectice.txt","r") as f:
        while data:
         data = f.readline()
         if (word in data):
          print(line_no)
          return
         line_no +=1
    return -1
        

print(check_for_line())       

with open("prectice.txt", "r")as f:
    data =f .read()
    print(data)

    num = ""
    for i in range(len(data)):
        if (data[i] == (",")):
            print(int(num))
            num = ""
        else:
            num += data[i]    

count = 0
with open("demo.txt","r") as f:
    data = f.read()
    print(data)


    num = data.split(",")
    for val in num:
        if(int(val)% 2 == 0):
            count +=1
print(count)



# Reading a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, world!")


# Iterators and Generators
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)


# decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()



# create a class in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("avinash", 25)
print(person.greet())  



#  list comprehension

squares = [x**2 for x in range(10)]
print(squares)  