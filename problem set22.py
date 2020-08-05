
#compound interest
def main():
    print("the compound interest for the specify years.")
    p = eval(input("enter the initial principal: "))
    r = eval(input("enter the annual interest rate: "))
    t = eval(input("enter the number of years: "))
    
    for i in range(t):
        p = p * (1 + r/100)
        print("the value in first years is:", p)
                        
    else:
        return

#wind chill
def wind_chil():
    t = float(input("enter temperature in degree farenheit:  "))
    v = float(input("enter wind speed in miles per hour:  "))
    wind_chill = (35.74 + (0.6215 * t)) + ((0.4275 * v) - 35.75)
    if (t <= 50.0) and (v >3<=120.0):
        print(wind_chill)
    else:
        print("enter a valid figures.")  


#order check of x,y,z

def order_check():
    print('order check')
    x = float(input('enter a value for x: '))
    y = float(input('enter a value for y: '))
    z = float(input('enter a value for z: '))
    if x < y < z:
        print('true')
    elif x > y > z:
        print('true')
    else:
        print('false')



#polar cordinates
"""
import math
def polar_cordinates(x,y):
    polar_cordinates = (math.atan2(x,y))
    print(polar_cordinates(x,y))
    x = 3.424
    y = 3.424
r =  (float(input('enter value of x:  ')))
o =  (float(input('enter value for y: ')))


import math


x = float(input('Enter value of x: '))
y = float(input('Enter value of y: '))


radius = math.sqrt( x * x + y * y )
theta = math.atan(y/x)
theta = 180 * theta/math.pi

print('Polar coordinate is: (radius = %0.2f,theta = %0.2f)' %(radius, theta))
"""

#uniform random number between 0 and 1

import random

def unfRaN ():
    unifRandNum = ()
    x = float(input('Enter start number: '))
    y = float(input('Enter end number: '))
    for i in range(0,5):
        z = round(random.uniform(x,y),3)
        unifRandNum = z
        
        #w = max(unifRandNum[:4])
        #r = min(unifRandNum[:4])
        #print(z)
        #print(max(unifRandNum))
        #print(min(unifRandNum))
        
        #min(unifRandNum)
        print(unifRandNum)
        
        #print(w)
        #print(r)
        





#main()
#wind_chil()
#order_check()
unfRaN()