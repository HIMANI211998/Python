#!/usr/bin/env python
# coding: utf-8

# ## Print Statement
# 

# In[1]:


print("Career")
print("Labs")


# ## Variables

# In[2]:


a=10
b=20
a+b


# Variable name can contain digits lowercase,uppercase and underscore.
# Variable name cannot start with digit.
# 

# ## Data Types in Python

# In[1]:


#Assigning different types of data to python variable

a=20
a='himani'
a


# In[2]:


type(a)


# In[3]:


a='himani'
a=10
type(a)


# In[4]:


a='hi'
print(type(a))


# In[5]:


a='anita'
print(type(a))
a='c'
print(type(a))


# ## Python Numbers

# In[6]:


a=23
b=3.4
c=5+9j
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


# In[7]:


a=10
a=a+1
a


# In[8]:


#So you can see there are two different storage locations
a=10
print(id(a))
a=a+1
print(id(a+1))


# In[9]:


#Optimizing storage for numbers between -5 to 256. 
#See a and b point at same memory location as they store same number. Momemt I make changes in a it points to some other location
a=10
b=10
print(id(a))
print(id(b))
a=a+1
print(id(a))


# In[10]:


a = 10
id1 = id(a)
print(id1)
b = a + 2-2
id2 = id(b)
print(id2)


# ## Arithmetic Operators

# In[11]:


10-3


# In[12]:


10.0-3.3


# In[13]:


a=10
b=4
a/b  #Floating point division


# In[14]:


a*b


# In[15]:


#If you want only integer part
a//b #Integer Division


# In[16]:


#Exponent
a**b


# In[17]:


#Remainder
a%b


# In[18]:


2+3*4


# In[19]:


2*3/4 #Doesnt matter the order


# In[20]:


2*3//4 #* first then // .Recommend to put brackets


# In[21]:


print(17//10)


# ## Taking Inputs

# In[22]:


a=input()
print(a)


# In[23]:


a=input()
print(a)
print(type(a))


# In[24]:


#To take an integer
a=int(input())
print(type(a))


# In[25]:


#Add two numbers
a=int(input())
b=int(input())
a+b


# In[26]:


int(3.9)


# In[27]:


a=float(input())

