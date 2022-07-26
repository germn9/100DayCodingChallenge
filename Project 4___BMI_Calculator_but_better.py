
#German Krugkov
# 100 days of coding project 4
# BMI calculator but with if elif statements

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

#convert the inputted numbers to float and use BMI = weight/height^2 function to find BMI
bmi = float(weight)/(float(height)**2)
bmi = round(bmi,2)
#print results
print("Height: " + f"{height}" + '\n' + "Weight: " + f"{weight}" '\n' + "BMI: " + f"{bmi}")

if(bmi < 18.5):
    print("you underweight, get some gains")
elif(bmi < 25):
    print("looking good")
elif(bmi < 30):
    print("bad news")
