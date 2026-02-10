# Question 2 (5 points)
"""
Using the same dataset (crime.csv) and the column ViolentCrimesPerPop, create two plots using
matplotlib: First, create a histogram that shows how the values are distributed. Second, create
a box plot for the same data.
Each plot must include:
• A clear title
• X-axis label
• Y-axis label
After generating the plots, write comments in your code describing:
• What the histogram shows about how the data values are spread
• What the box plot shows about the median
• Whether the box plot suggests the presence of outliers
Your explanations should be 5–7 sentences total, written as comments.
"""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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

crime_data = pd.read_csv('data/input/crime1.csv')
violent_crimes = crime_data.ViolentCrimesPerPop
#HIstogram
plt.hist(violent_crimes, bins=40)
plt.title('Distribution of Violent Crimes Per Population')
clean_plot(y_label='Frequency', x_label='Violent Crimes Per Population')
plt.savefig('graphs/question02_histogram_violent_crimes.png')
# box plot
plt.figure()
plt.boxplot(violent_crimes)
plt.title('Box Plot of Violent Crimes Per Population')
clean_plot(remove_x_labels=True, y_label='Violent Crimes Per Population')
plt.savefig('graphs/question02_boxplot_violent_crimes.png')

# Response 

"""
1. It shows that the data is right-skewed, with most values clustered around 1.
 This may show that there are some registries with very high violent crime rates,, that pull the distribution to the right.
2. The box plot shows the median is somewhere around 0.4.
3. The box plot doen't suggest the presence of outliers as all values fall within
the lower fence (Q1-1.5*IQR) and upper fence (Q3+1.5*IQR). 
The whiskers extend to the minimum and maximum values, if there were outliers matplot lip would show them as point outside them.


"""