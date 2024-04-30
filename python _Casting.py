#!/usr/bin/env python
# coding: utf-8

# ### Casting Float into Int

# In[1]:


pi = 3.14
print(type(pi))


# In[3]:


num = int(pi)
print("Integer number is:",num)


# In[4]:


print(type(num))


# ### Casting Boolean into int

# In[7]:


flag_true = True
flag_false = False

print(type(flag_false))


# In[8]:


num1 = int(flag_true)
print("integer number is:",num1)


# In[9]:


print(type(num1))


# In[10]:


num2 = int(flag_false)
print("integer number is:",num2)


# ### casting string to an integer

# When converting string type to int type, a string must contain integer value only and should be base-10.

# In[11]:


string_num = "225"
print(type(string_num))


# In[13]:


num1 = int(string_num)

print("Integer number is:",num1)
print(type(num1))


# ###  Float type conversion

# In[ ]:


casting integer to float


# In[14]:


num =725
print(type(num))


# In[15]:


num1 = float(num)
print("Float number is:",num1)


# ### Boolean ---> float 

# In[16]:


flag_true = True
flag_false = False
print(type(flag_true))


# In[17]:


num1 = float(flag_true)
print("Flaot number is:",num1)


# In[18]:


num2 = float(flag_false)
print("Flaot number is:",num2)


# ### String ---> float 

# In[ ]:


string_num = ''


# In[30]:


num1  =10
num2 = 0
num3 = 1
num4 = 12.23

print(type(num1))


# In[31]:


b1 = bool(num1)
b2 = bool(num2)
b3  = bool(num3)
b4 = bool(num4)


# In[33]:


print(b1)
print(b2)
print(b3)
print(b4)


# In[44]:


f_num1 = 25.35
f_num2 = 0.0
f_num3 = 1.0

b1 = bool(f_num1)
b2 = bool(f_num2)
b3 = bool(f_num3)
print(b2)


# In[38]:


print(b1)


# In[39]:


print(b2)


# In[45]:


print(b3)


# ## string to Boolean type
# Give true to all value , even space also , if not give value then show false

# In[52]:


s1 = "False"
s2 = "True"
s3 = "812"
s4 = ""

b1 = bool(s1)
b2 = bool(s2)
b3 = bool(s3)
b4 = bool(s4)

print(b1)
print(b2)
print(b3)
print(b4)


# ##  String type conversion
# In str type conversion, we use the built-in function str() to convert converts variables of other types to a string type. This function returns the string type of object (value).

# ### Casting int to str type

# In[55]:


num = 15
print(type(num))

s1 = str(num)
print(s1)

print(type(s1))


# ### float type to str type

# In[58]:


num = 75.35
print(type(num))

s1 = str(num)
print(s1)
print(type(s1))


# ###  bool type to str type

# In[60]:


b1 = True
b2 = False

print(type(b1))

s1 = str(b1)
s2 = str(b2) 

print(s1)


# In[62]:


print(s2)


# In[65]:


print(type(s1))


# In[ ]:





# In[ ]:





# In[ ]:




