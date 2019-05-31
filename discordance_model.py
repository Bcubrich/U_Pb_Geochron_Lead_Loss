# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:04:03 2019

@author: bcubrich
"""

import numpy as np
import matplotlib.pyplot as plt


global lambda68
global lambda75
global  u238_u235


lambda68=0.155125*10**-9
lambda75=0.98485*10**-9
u238_u235=137.88



t=np.linspace(0,5,501)
t=t*10**9
pb206_u238=np.e**(lambda68*t)-1
pb207_u235=np.e**(lambda75*t)-1

t_labels_t=t[::100]/(10**9)
t_labels_x=pb207_u235[::100]
t_labels_y=pb206_u238[::100]

t_sample=1880*10**6

disc=0.8

avagadro=(6.0221409*10**23)

pb76=((1/u238_u235)*(np.e**(lambda75*t_sample)-1))/(np.e**(lambda68*t_sample)-1)

u238_sample_est=int(np.around((1/238)*(10**-9)*avagadro,0))*10
#u238_sample=np.linspace(u238_sample_est,u238_sample_est*100,10)
u238_sample=np.array([0.01,0.0125, 0.0175,0.025,0.05,0.1,0.2,0.5,1, 10])*u238_sample_est

pb206_sample=u238_sample*(np.e**(lambda68*t_sample)-1)




pb207_sample=pb206_sample*pb76
u235_sample=pb207_sample/(np.e**(lambda75*t_sample)-1)
#u235_sample=np.linspace(u235_sample_est/100,u235_sample_est*100,10)

sample_207_206=pb207_sample/pb206_sample




pb206_sample+=-min(pb206_sample)*disc
pb207_sample=pb206_sample*pb76

#sample_207_206_2=pb207_sample/pb206_sample

extra_206_loss=0.1
extra_207_loss=0




pb206_u238_sample=pb206_sample/u238_sample
pb207_u235_sample=pb207_sample/u235_sample

t238=np.log(pb206_u238_sample+1)/lambda68
discordance=t238/t_sample*100-100



pb206_test=(1-extra_206_loss)*pb206_sample
pb207_test=(1-extra_207_loss)*pb207_sample
pb206_u238_test=pb206_test/u238_sample
pb207_u235_test=pb207_test/u235_sample

#test_207_206=pb207_test/pb206_test


new_76_age=pb207_test[0]/pb206_test[0]

def age_76(new_76_age):
    t_test=1000
    i=0
    #global diff
    diff=100
    while np.abs(diff)>0.01:
        i+=1
        pb76_test=((1/u238_u235)*(np.e**(lambda75*t_test)-1))/(np.e**(lambda68*t_test)-1)
        diff=new_76_age-pb76_test
        if diff >0:
            t_test+=100000000
        if diff <0:
            t_test+=-100000000
#        print ('{}. {}'.format(i,diff))
#    print (diff)
    while np.abs(diff)>0.0001:
        i+=1
        pb76_test=((1/u238_u235)*(np.e**(lambda75*t_test)-1))/(np.e**(lambda68*t_test)-1)
        diff=new_76_age-pb76_test
        if diff >0:
            t_test+=1000000
        if diff <0:
            t_test+=-1000000
#        print ('{}. {}'.format(i,diff))
    while np.abs(diff)>0.000001:
        i+=1
        pb76_test=((1/u238_u235)*(np.e**(lambda75*t_test)-1))/(np.e**(lambda68*t_test)-1)
        diff=new_76_age-pb76_test
        if diff >0:
            t_test+=10000
        if diff <0:
            t_test+=-10000
#        print ('{}. {}'.format(i,diff))
    while np.abs(diff)>0.0000001:
        i+=1
        pb76_test=((1/u238_u235)*(np.e**(lambda75*t_test)-1))/(np.e**(lambda68*t_test)-1)
        diff=new_76_age-pb76_test
        if diff >0:
            t_test+=1000
        if diff <0:
            t_test+=-1000
#        print ('{}. {}'.format(i,diff))
    return (t_test)

wrong_76=age_76(new_76_age)
discordance_76=wrong_76/t_sample*100-100
        
#%%

'''
------------------------------------------------------------------------------
plotting
------------------------------------------------------------------------------
'''
plt.plot(pb207_u235,pb206_u238)
for x,y,s in zip(t_labels_x,t_labels_y,t_labels_t):
    plt.text(x,y,s)

plt.plot(pb207_u235_sample,pb206_u238_sample, marker='o')
plt.plot(pb207_u235_test,pb206_u238_test, marker='o')