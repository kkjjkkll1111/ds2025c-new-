import random
from itertools import count

answer = random.randint(1,100)
game = False
count = 1
for i in range(7):
    guess = int(input("guess number : "))
    if guess < answer:
        print(f"your number is low, {7 - count} chance left")
    elif guess > answer:
        print(f"your number is high, {7 - count} chance left")
    else:
        game = True
        break
    count += 1
if game:
    print(f"you win!! the answer is {answer}")
else:
    print(f"you lose. the answer is {answer}")

