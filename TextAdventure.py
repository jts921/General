import random

# random number generator function
def random_number():
    for x in range (1):
        x = random.randint(1,3)

print("Welcome to the your Adventure\nType 'Start' to begin")

y = input()

if(y == "Start"):
    print("You enter a dungeon with three directions of travel.\nWhich path do you chose? (choose number)")

print("1. North\n2. East\n3. West")

x = input()

if(x == "1"):
    print("You encounter a narrow path\nDo you wish to continue?")

#if(x == "2"):
#    print("fuck")

#if(x == "3"):
#    print("balls")

x = input()
if(x == "yes"):
    x = random_number()
    print(x)
    if(x == 1):
        print("Balls")
    if(x == 2):
        print("Fuck")