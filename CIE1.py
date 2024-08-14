#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('mtcars.csv')
plt.hist(df['mpg'], bins=10, edgecolor='black')
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.title('Histogram of MPG')
plt.show()
counts, bin_edges = np.histogram(df['mpg'], bins=10)
max_freq_index = np.argmax(counts)
interval_with_max_freq = (bin_edges[max_freq_index], bin_edges[max_freq_index + 1])

interval_with_max_freq


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('mtcars.csv')

plt.scatter(df['wt'], df['mpg'], color='blue')
plt.xlabel('Weight of Car (1000 lbs)')
plt.ylabel('Miles Per Gallon (MPG)')
plt.title('Scatter Plot of Weight vs MPG')
plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mtcars.csv')


transmission_counts = df['am'].value_counts()


plt.bar(transmission_counts.index, transmission_counts.values, color='orange')
plt.xlabel('Transmission Type')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Transmission Types')
plt.xticks([0, 1], ['Automatic', 'Manual'])
plt.show()


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('mtcars.csv')

plt.boxplot(df['mpg'], vert=False)
plt.xlabel('MPG')
plt.title('Box Plot')
plt.show()

five_number_summary = df['mpg'].describe(percentiles=[0.25, 0.5, 0.75])[['min', '25%', '50%', '75%', 'max']]

five_number_summary


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




