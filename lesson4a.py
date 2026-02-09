# nested if statements
# These are if statements inside other if statements 
age = 14
weight = 40
if (age>=16) :
    if (weight >= 50) :
        print("You can donate")
    else :
        print("You are underwight")
else :
    print("You are too young to donate")