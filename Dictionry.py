

#dictionry are used to store data value in key : value paire 
# and are unorderd , mutable(changebale) & don't allow duplicate keys



info = {
    "Name": "Avinash",
    "Lang": {
        "javascript": "30%",
        "python": "40%",
        "HTML": "50%",
        "CSS": "40%"
    },
    "Age": 24,
    "learning": "coding",
    "marks": 99.01
}

print(info.keys())   # returns keys methods
print(len(info))
print(len(list(info.keys())))
print(info.values())      # all value 
paire=list(info.items())   # returns all ( key , value ) pairs as tuples
print(paire[1])
info.update({"city":"delhi"})
# print(info["Name2"])    #error
print(info.get("Name2"))  #none


print(info)
