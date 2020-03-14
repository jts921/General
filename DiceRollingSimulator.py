print("Would you like to roll a die?")

x = input()

if (x == "yes"):
    import random
    for x in range (1):
        print (random.randint(1,6))

print("Would you like to try again?")

y = input()

if (y == "yes"):
    while (y == "yes"):
        import random
        for x in range (1):
            print (random.randint(1,6))
            print ("Would you like to try again?")
            y = input()

if (y != "yes"):
    print("Thank you for playing")

#random number generator (rng)
#import random
#for x in range (1):
#    print (random.randint(1,6))