#German Krugkov
# 100 days of coding project 6
# Fizz Buzz

count = int(input("how far to count "))

for count in range(1, count+1) :

    if count%5 == 0 :
        if count%3 == 0 :
            print("FizzBuzz")
        else :
            print("Buzz")
    elif count%3 == 0 :
        print("Fizz")
    else : 
        print(count)


