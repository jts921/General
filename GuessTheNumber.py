#random number generator (rng)
import random
for x in range (1):
    x = int(random.randint(1,10))

#print(x)

print("Guess a number.")

y = int(input())

while(x!=y):
    if(x<y):
        print("Too High")
        print("Try Again")
        y = int(input())
    if(x>y):
        print("Too Low")
        print("Try Again")
        y = int(input())

if(x == y):
    print("Good job")
