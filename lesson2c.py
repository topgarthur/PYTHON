# python dictionary
person={
    "firstname":"Arthur",
    "lastname":"Ingavo",
    "age":49 ,
    "colors":["blue","green"],
    "salary":100000
}
# show output
print(person)
# print age
print(person["age"])
# print salary
print(person["salary"])

# add new key value 
person["passport"]="B008Hn"

# show output
print(person)

# change age to 34
person["age"]=34
# show output
print(person)

# delete last name 
del person["lastname"]
# show output
print(person)