#!/usr/bin/env python
# coding: utf-8

# In[7]:


binary = input("Enter a binary number:")


BinaryToDecimal(binary)

def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print("The decimal value is:", decimal)


# In[ ]:




