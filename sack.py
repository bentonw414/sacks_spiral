import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

def get_prime_info(prime,axis_vals):#this is used to translate the value of the prime number into the values for the polar plot
    lower_index = 0
    upper_index = 0#this the square value in
    difference = 0
    for i in range(len(axis_vals)):#iterate over the loop until we find where the lower square is
        if prime > axis_vals[i] and prime < axis_vals[i + 1]:
            lower_index = i
            upper_index = i + 1
            difference = axis_vals[upper_index] - axis_vals[lower_index]
            break
        if prime == axis_vals[i]:
            lower_index = i
            difference = 1
            break
    r = lower_index + (prime - axis_vals[lower_index])/(difference)
    theta = 2*math.pi*((prime - axis_vals[lower_index])/difference)

    return (r,theta)

def spiral(num_primes = 10000, axis = 'squares', bg_clr = 'navy', size = (6,6), pt_clr = 'aqua'):
    axis_vals = [0]
    rvals = []
    thetavals = []
    dt = pd.read_csv("primes-to-100k.txt",delim_whitespace=True)
    dt = dt.head(num_primes).values

    if isinstance(axis,list):
        axis_vals = axis
    elif isinstance(axis,str):
        if axis == 'squares':#make the axis values into the set of squares
            for i in range(100000):#this makes the axis reference values
                if i**2 > dt[-1]:
                    axis_vals.append(i**2)
                    break
                else:
                    axis_vals.append(i**2)
        else:
            print("Please give a valid axis string.")
            return

    for i in dt:
        if i[0] > axis_vals[-1]:
            break
        information = get_prime_info(i[0],axis_vals)
        #print(information)
        rvals.append(information[0])
        thetavals.append(information[1])

    f=plt.figure(facecolor = bg_clr,figsize=size)
    ax = f.add_subplot(111,projection='polar')
    ax.plot(thetavals,rvals,'*', ms=.75,color=pt_clr)#note that we plot (theta,r) and not (r,theta) ():
    plt.axis('off')
    plt.show()

#I need to add something to make a short custom axis not throw errors or give weird graphs (basically just update the num_primes value depending on which restriction it has)
