from random import randint
import random
import time
from os import path
from os import system

system('color 3')
system("title "+'Phone number generator - @Hades_br')
print("     Phone number generator")

amount = int(input("How many keys to generate : "))

def randomPrefix():
    return "".join(map(str, [random.choice([3,5,8,9])]))

def randomNumber():
    return "".join(map(str, [randint(0,9) for i in range(8)]))

def randList():
    phone = str(0) + randomPrefix() + randomNumber() + ":123456"
    return(phone)

def File():
    name = "phoneCombo.txt"
    x = 1
    while path.exists(name):
        name = "phoneCombo(" + str(x) + ").txt"
        x = x + 1
    return name
f = open(File(),"w+")
for i in range(amount):
    phone = randList()
    f.write(phone + "\n")
    print(i," . ",phone)
    time.sleep(0.0005)
f.close()