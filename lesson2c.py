# python dictionary
person = {
    "firstname" : "Andrew" ,
    "lastname" : "Tate" ,
    "age"  : 25 ,
    "Colors" : [ "black" , "Whtie" ] ,
    "Salary" : 5000 
}
# show output 
print(person)
# print age 
print(person["age"])
# print salary 
print(person["Salary"])

# add new key value
person["passport"] = "B008Hn"
# show output 
print(person)

# change age to 34
person["age"] = 34
# show output 
print(person)
# delete lastname
del person["lastname"]
# show output 
print(person)
