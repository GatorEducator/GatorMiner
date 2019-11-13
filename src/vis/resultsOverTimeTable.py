# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 

### Basic multi line plot to visualize multiple results
## Pyplot tutorial 124 used as a base. 
# Available from https://python-graph-gallery.com/124-spaghetti-plot/
# Matplotlib: https://pypi.org/project/matplotlib/ 
# pip install matplotlib
# pandas: https://pandas.pydata.org/pandas-docs/stable/install.html 
# sudo pip3 install pandas


# Scan in data here
df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14), 'y10': np.random.randn(10)+range(2,12) })
 
# style
plt.style.use('seaborn-darkgrid')
# plt.style.use('dark_background') # can use different styles
 
# create a color palette
palette = plt.get_cmap('Set1')
 
# multiple line plot
num=0
for column in df.drop('x', axis=1):
    num+=1
    plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)
 
# Add legend
plt.legend(loc=2, ncol=2)
 
# Add titles
plt.title("Results over Time", loc='left', fontsize=12, fontweight=2, color='black')
plt.xlabel("Time")
plt.ylabel("Score")
plt.show()