# 1. Simple interest
def simpleinterest(principle, rate, time) :
    answer = principle * rate * time
    print("This is simple interest" , answer)
# call the function
simpleinterest(300000 , 0.12 , 5)

# 2. bmi 
def bmi(weight , height) :
    answer = weight / (height* height)
    print("Your BMI is" , answer)
# call the function
bmi(57.5 , 1.3)

# 3. Area of a triangle
def area(base , height) :
    answer = (base * height) / 2
    print("The area is" , answer)
# call the function
area(10 , 6)
