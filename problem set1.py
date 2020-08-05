def Hello():
    x = 'Hello, Worldmessage'
    for i in range(10):
        print(x)


def simplify():
    a = 2
    b = 2
    if (not(a<b)):
        print('yes')
    elif not(a>b):
        print('yes')
    else:
        return


import random
def randoInt():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    x = random.randint(a,b)
    print(x)

import random
def randRa():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    #x = random.randint(a,b)
    if a and b in range(7):
        y = random.randrange(a,b)
        x = random.randrange(a,b)
        print('Random number: ','(', y,')',',','(', x,')' )
        print('Sum of Random numbers: ','(',y + x,')')
    else:
        print('no')

import math
def Value():
    t = float(input('Enter value for t: '))
    value = round((math.sin(2*t)) + (math.sin(3*t)),4)
    print(value)



import math
def displace():
    x0 = float(input('Enter initial position x0 of the object: '))
    v0 = float(input('Enter the velocity v0 in meters per second of the object: '))
    t = float(input('Enter time t in seconds: '))
    G = 9.80665
    displacement = round((x0 + (v0 * t)) - ((G * t)*2/2),4)
    print('The displacement of the object at position (x0)', x0, ', velocit (v0)', v0, 'and Time (t) is:', displacement) 


#Hello()
#simplify()
#randoInt()
#randRa()
#Value()
displace()