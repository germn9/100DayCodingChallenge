#German Krugkov
# 100 days of coding project 2
# your life in weeks

age = input("what is your current age in years ")

#convert current age to weeks
age_in_weeks = int(age)*52


years_to_go = 90 - int(age)
#12 months in a year
months_to_go = years_to_go*12
#52 weeks in a year
weeks_to_go = years_to_go*52
#365 days in a year, we don't count leap year
days_to_go = years_to_go * 365

print("current age: " f"{age}" " years old")
print("Years: " f"{years_to_go}")
print("Months: " f"{months_to_go}")
print("Weeks: " f"{weeks_to_go}")
print("Days: " f"{days_to_go}")
print( "until you turn 90")
