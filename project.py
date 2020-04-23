#!/usr/bin/env python
# coding: utf-8

# In[97]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
nycdata = pd.read_csv('NYC data.csv')
nycdata
#reading in data file


# In[98]:


cases = nycdata['Cases'] #turning cases data into readable array
cases_fit = cases[:16] #chosing section to fit the curve to
hospital = nycdata['Hospitalizations']
deaths = nycdata['Deaths']
x = np.linspace(1,43,43) #creating an x array for the data plot
x_fit = np.linspace(1,16,16) #x array for the fitted section


# In[99]:


n = nycdata.plot() #plot of full data


# In[100]:


import scipy.optimize
def func(x_fit,a,b):
    return a*(b**x_fit) #exponential function to fit the curve to
popt,pcov = scipy.optimize.curve_fit(func,x_fit,cases_fit)
a_fit = popt[0] #a value
b_fit = popt[1] #b value
plt.plot(x,cases)
plt.plot(x_fit,func(x_fit,a_fit,b_fit))


# In[101]:


xx = np.linspace(1,21,21) #looking at fit on larger area of true data
y = a_fit*(b_fit**xx)


# In[102]:


plt.plot(x,cases)
plt.plot(xx,func(xx,a_fit,b_fit))


# In[ ]:





# In[ ]:


#2:


# In[124]:


def rhs(z,t,p):
    z = I,S,E #solution vector of state variables
    p = rep, tinc, tinf #parameter vector
    f = [((-rep/tinf)*I*S),((rep/tinf)*I*S - (E/tinf)),((E/tinc)-(I/tinf))]
    return f
 #f is a function of our three differentials  


# In[143]:


from scipy.integrate import odeint
import numpy as np
#parameters:
rep = 3.0
tinc = 5.2
tinf = 2.9
#initial conditions:
I0 = 2
S0 = 500
E0 = 1
z0 = [I0,S0,E0]
p = [rep,tinc,tinf]


# In[144]:


t = np.linspace(0,200,200)
sol = odeint(rhs, z0, t, args=(p,))


# In[145]:


plt.plot(t, sol)


# In[ ]:





# In[146]:


#3:


# In[150]:


import random
#Define the city box:
xmax = 60
ymax = 30
N = 200 #population
def start():
    for i in range(N):
        x = random.randrange(1,xmax,1)
        y = random.randrange(1,ymax,1)
    return x,y


# In[ ]:


#need: give balls a class? speed, type/color, etc

