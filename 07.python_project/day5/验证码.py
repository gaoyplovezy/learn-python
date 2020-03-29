__author__ = "zyx"
import random

a = ''
for i in range(5):
    b = random.randint(0,5)
    if b == i:
        a += chr(random.randint(65,90))
    else:
        a += str(random.randint(0,9))
print(a)



