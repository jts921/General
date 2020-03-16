#random number generator (rng)
import random
for x in range (1):
    x = random.randint(1,2)

print(x)

print("Guess a number.")

user_input = input()

if(x == user_input):
    print("Good Job!")

#if(x != user_input):
#    print("Try Again")

#print (user_input)