import random
total = random.randrange(3,21)
if total < 17:
    total += random.randrange(1,12)
if total>21:
    total = "bust"

print(total)