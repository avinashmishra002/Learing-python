friends = ["apple", "orange", 3 ,6 ,245.34, False, "name" , "rohan"]

print(friends[1])

friends [0] ="banana"   # lists are mutable

print(friends[1:7])

#Methods-----------


friends.append("jonny")
print(friends)

l1 = [1,2,77,43,5,4,66]
# l1.sort()
l1.reverse()
print(l1)

a = 1
b = 5
print(not False)
print(not (a >= b))

num_list = "0123456789"
print[0:5]


a = list (("a", "b", "c","d"))
print(a)
print(type(a))


marks = [ 2,3,4,5,6,76]
print(len(marks))   #lenth
print(type(marks))   # data type
print(marks[3])      # index
print(marks[1:4])     # slicing



# list methods


list = [ 10 , 20 , 30 , 40 , 50]

list.append(6)
list.sort()
print(list.sort(reverse=True))   #decending
list.reverse()
list.insert(0,0)        # ( index , elemnt)
# list.remove()
list.pop(3)   # ( index)
print(list)
