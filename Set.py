# set is are collotion of the undered items.
# set must be unique & mutable  but set eliment innuteble.


colletion = { 1,2,3,4,"hello", "hey",1,2}
colletion = set()   #empty set  syntex
colletion.add(1)
colletion.add(2)

print(colletion)
print(type(colletion))
print(colletion.pop())



set1  = {1,2,3,4}   
set2 = {3,4,5,6,7,8}

print(set1.union(set2))    # combaines both set values  & return new
print(set1.intersection(set2))   #Combines common values & return new


dictionary = {
    "cat" : "a small animal",
    "table": [" a piece of furniture ", " list of facts & figures"]
}
print(dictionary)

sub = { 
    "python", "javascript", "java", "python"
    "c++" ,"C", "javascript"

}
print(len(sub))


marks = {}
X =int(input("enter phy"))
marks.update({"phy" : X})

X =int(input("enter math"))
marks.update({"math" : X})

X =int(input("enter bio"))
marks.update({"bio" : X})

print(marks)


