a  = input("enter a number :")
print(f"multipliction table of:{a}")
try:
    for i in range(1,11):
        print(f"{int(a)} X{int(a)* i}")
except:                                   # use multipal except 
    print("Invelid input")        

print("sone line code")    



try:
    num = int(input("enter an integer:"))
    a = [2,4]
    print(a[num])
except ValueError:
    print( "Number entered is not an integer:")

except ImportError:
    print("Index Error")


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful.")
finally:
    print("This block is always executed.")




def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)
