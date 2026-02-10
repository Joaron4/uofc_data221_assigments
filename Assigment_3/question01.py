# Question 1 (5 points)
""""
Load crime.csv into a pandas DataFrame. Focus on the column ViolentCrimesPerPop. Using
Python, compute and print the following statistical measures for this column:
• Mean
• Median
• Standard deviation
• Minimum value
• Maximum value
After computing these values, write comments in your code (using #) answering the following:
• Compare the mean and median. Does the distribution look symmetric or skewed? Explain
briefly.
• If there are extreme values (very large or very small), which statistic is more affected: mean
or median? Explain why.
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

crime_data = pd.read_csv('data/input/crime1.csv')
violent_crimes = crime_data.ViolentCrimesPerPop

mean_value = violent_crimes.mean()
median_value = violent_crimes.median()
standard_deviation = violent_crimes.std()
min_value = violent_crimes.min()
max_value = violent_crimes.max()    

print(f"""
Mean: {mean_value}
Median: {median_value}
Standard Deviation: {standard_deviation}
Minimum Value: {min_value} 
Maximum Value: {max_value}
""")

# Response

"""
The distribution would be skewed to the right because the mean is higher than the median. 
This tells us that there are some higher values in the dataset that are pulling the mean up, 
while the median remains less affected by these extreme values. if it was symetrically distributed, 
the mean and median would be closer together.
The mean would be the more affected as it is a sum of all values divided by the number of values, so extreme values 
can distort the mean by making the sum bigger and thus the mean higher.
Pd. ALso I graphs the distribution and it shows extreme values on the right side of the graph, 
which confirms that the mean is being pulled up by those higher values (specifically the value 1.0).
"""

def clean_plot( remove_left=False, 
                remove_bottom=False, 
                remove_y_labels=False, 
                remove_x_labels=False, 
                y_label=None,
                x_label=None):
    ax = plt.gca()
    ax.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if remove_left:
        ax.spines['left'].set_visible(False)
    if remove_bottom:
        ax.spines['bottom'].set_visible(False)
    if y_label is not None:
        ax.set_ylabel(y_label)
    if remove_y_labels:
        ax.set_yticklabels([])
        ax.set_yticks([])
        if y_label is None:
            ax.set_ylabel('')
    if x_label is not None:
        ax.set_xlabel(x_label)
    if remove_x_labels:
        ax.set_xticklabels([])
        ax.set_xticks([])
        if x_label is None:
            ax.set_xlabel('')
        
  
   
  

plt.hist(violent_crimes, bins=40)
clean_plot(remove_left=True,remove_y_labels= True)
plt.title('Distribution of Violent Crimes Per Population')
plt.savefig('graphs/question01_violent_distribution.png')