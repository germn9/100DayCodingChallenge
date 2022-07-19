#German Krugkov
# 100 days of coding project 1
# BMI calculator

height = input("Enter your height: ")
weight = input("Enter your weight: ")

#convert the inputted numbers to float and use BMI = weight/height^2 function to find BMI
bmi = float(weight)/(float(height)**2)
bmi = round(bmi,2)
#print results
print("Height: " + f"{height}" + '\n' + "Weight: " + f"{weight}" '\n' + "BMI: " + f"{bmi}")


