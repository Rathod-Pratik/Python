import seaborn as s
# Importing the seaborn library as 's' for data visualization

# s.histplot([1,1,4,4,1,1])
# Example: Histogram plot for a list of values

# data=[2,2,4,4,2]
# s.boxenplot(x=data)
# Example: Boxen plot for a list of values

# data=['a','a','a','a','h','b']
# s.countplot(x=data)
# Example: Count plot for categorical data

data=[[1,2,2,3,3,5,6,7]]
# Example data for heatmap
# s.heatmap(data,annot=True)
# Example: Heatmap with annotation

s.scatterplot(data)
# Scatter plot for the given data

import matplotlib.pyplot as plt
# Importing matplotlib for displaying the plot
plt.show()
# Display the plot window