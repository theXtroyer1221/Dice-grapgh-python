from collections import Counter
import math
import random

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

numList = []
amountList = []

for i in range(100):
  i = random.randint(1, 6)
  numList.append(i)
  numList.sort()

def checkDuplicate(nums):
  counter = Counter(nums)
  for i in counter:
    amountList.append(counter[i])
    
checkDuplicate(numList)

def unique(nums): 
    unique_list = [] 

    for x in nums: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 

    return unique_list

y_pos = np.arange(6)

plt.bar(y_pos, amountList, align='center', alpha=0.5)
plt.xticks(y_pos, unique(numList))
plt.ylabel('amount of occurence')
plt.title('Result of Dice rolls')
plt.savefig('graph.png') 
