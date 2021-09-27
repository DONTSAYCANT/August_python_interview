#!/usr/bin/env python
# coding: utf-8

# In[103]:


#reverse a String
a = input("give your string")
output = reversed(a)
print('reversed string:',output)


# In[1]:


#reversed function
a = input("give your sting")
r = reversed(a)
print(r)
output =''.join(r)
print('reversed string:',output)


# In[7]:





# In[4]:


#program to reverse orders of the string without using loops
a = input("give u r str")
b = a.split()
c = b[::-1]
output =' '.join(c)
print(output)


# In[5]:


a ="python is very easy language"
print(a[::-1])


# In[60]:


#how you check every word in a string starts wirh capital

a = input("give your string")
a.istitle()


# In[ ]:


#how u check a specific string should be found in your program
a =input("str")
print('y' in a )#- membership operator
print("z not in a")


# In[ ]:


'''
What is the diff between following expressions
 if list is given as [1,3,5]
 1) list * 3
 2) list*=3
 3) List + 3
 4) List+=[3]
'''
list =[1,3,5]
list * 3
print(list)
#list =[1,3,5]
#list*=3
#print(list)





# In[105]:


a = "ravi is good boy \n ok"
print(a)
#\n,escape


# In[54]:


#sort the elements in a list
a = [14,21,445,134,132,42,536,235,687,11,465,0,3234,134,434,57,56,45,44,33,]
a.sort(reverse = True)
print(a)


# In[58]:


#program to print the number of words in a given sentences
a = "this world is a good place to live"
print(len(a.split()))


# In[71]:


a = {1,2,3,4,5}
b = {2,5}
c = {1,6}
a.issubset(a)


# In[73]:


a ={1:2,2:23,3:4}
print(a[0])


# In[87]:


a = {"name":"gggg", "age":26, "address":"virudhunagar"}
print (a["address"][-5:])


# In[95]:


Li1 = [2,3,"python","hello",4,5,0]
print(Li1[2][::2])


# In[102]:


Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]
print(Li1[5][5][1])


# In[ ]:


list =[1,3,5]
list * 3
print(list)

list =[1,3,5]
list*=3
print(list)


# In[ ]:





# In[ ]:




