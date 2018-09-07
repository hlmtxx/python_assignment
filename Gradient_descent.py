
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x=np.arange(0., 10., 0.2)
m=len(x)
print m
x0=np.full(m,1.0)
input_data=np.vstack([x0,x]).T
print(input_data)


# In[2]:


input_data=np.vstack([x0,x])
print(input_data)


# In[3]:


input_data=np.vstack((x0,x))
print(input_data)


# In[4]:


input_data=np.vstack([x0,x]).T
print(input_data[1])


# In[5]:


target_data=2*x+5+np.random.randn(m)
loop_max=10000
epsilon=1e-3
np.random.seed(0)
theta=np.random.randn(2)
alpha=0.001
diff=0.
error=np.zeros(2)
count=0
finish=0
print(theta)


# In[6]:


while count<loop_max:
    count+=1
    sum_m=np.zeros(2)
    for i in range(m):
        dif = (np.dot(theta, input_data[i])-target_data[i])*input_data[i]
        sum_m=sum_m+dif
    
    theta=theta-alpha*sum_m
    
    if np.linalg.norm(theta-error)<epsilon:
        finish=1
        break
    else:
        error=theta
    print ('loop count= %d' % count, '\tw:',theta)
print('loop count = %d' % count, '\tw:',theta)

slope, intercept, r_value, p_value, slope_std_error=stats.linregress(x,target_data)
print('intercept = %s slope = %s' % ( intercept, slope))
plt.plot(x, target_data, 'g*')
plt.plot(x, theta[1]*x+theta[0],'r')
plt.show()


# In[7]:


type(intercept)


# In[9]:


type(theta[1])


# In[13]:


print('intercept =  slope = ', (intercept,slope))


# In[17]:




