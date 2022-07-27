#German Krugkov
# 100 days of coding project 7
# random password generator

import random
from random import randint


len = int(input("how long of a password "))

password = ""

for len in range(1, len+1) :

    a = random.randint(48,126)

    b = chr(a)

    password += b

print(password)