#!/usr/bin/env python
# coding: utf-8

# In[3]:


coins = [2, 3, 5, 10,  15]
amount = int(input("Masukan jumlah target :"))

count = 0

for coin in coins:
    while amount >= coin:
        amount -= coin
        count += 1
        
print("Jumlah koin yang di perlukan :", count)


# In[ ]:





# In[ ]:




