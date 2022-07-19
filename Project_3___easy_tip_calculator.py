#German Krugkov
# 100 days of coding project 3
# tip calculator


total_cost = float(input("what is the total bill? "))
tip = float(input("what percentage tip would you like to add? "))
split = int(input("how many people is this split into? "))

tip_in_dollars = round(total_cost * (tip/100), 2)
total_with_tip = round(total_cost + tip_in_dollars, 2)
cost_per_person = round(total_with_tip / split, 2)

print("total cost: " f"{total_cost}")
print("cost of tip: " f"{tip_in_dollars}")
print("total with tip: " f"{total_with_tip}")
print("cost per person: " f"{cost_per_person}")
