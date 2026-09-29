#What is distribution visualization
'''
Distribution visualization is the graphical representation of how data values are spread, 
commonly using histograms, KDE plots, box plots, and violin plots to understand frequency, 
shape, spread, skewness, and outliers.
'''

'''import matplotlib
import seaborn

print(matplotlib.__version__)
print(seaborn.__version__)'''

#Basic Matplotlib Structure
'''import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("My Graph")
plt.show()'''

#Histogram using Matplotlib
'''A histogram is one of the most important graphs for distributions.
It shows:How frequently values occur within ranges.
Instead of displaying every value separately, we group values into ranges.'''
'''import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]
plt.hist(scores)
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Exam Score Distribution")
plt.show()'''

#Histogram with bins
'''We can specify the number of bins.
plt.hist(scores, bins=5)'''



'''import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]

plt.hist(scores, bins=5)

plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Exam Score Distribution")

plt.show()'''

#Seaborn Histogram -> Seaborn makes statistical graphs easier.
'''import seaborn as sns
import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]

sns.histplot(scores)

plt.title("Exam Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")

plt.show()
'''

#Seaborn Histogram with Bins
#sns.histplot(scores, bins=5)
'''import seaborn as sns
import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]

sns.histplot(scores, bins=5)

plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Exam ScoreS Distribution")

plt.show()'''

#KDE Plot
#KDE means:Kernel Density Estimation
'''It creates a smooth curve representing the distribution of data.
For example:
Density
   |
   |             /\
   |           /    \
   |         /        \
   |_______/____________\____
             Values'''

'''The curve helps us understand the shape of the distribution.'''

'''
#KDE using Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]

sns.kdeplot(scores)

plt.title("KDE Plot")
plt.xlabel("Scores")
plt.ylabel("Density")
plt.show()


#Histogram + KDE (This is very useful.)

import seaborn as sns
import matplotlib.pyplot as plt
scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]
sns.histplot(scores, bins=5, kde=True)
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Exam Score Distribution")
plt.show()'''

#Box Plot
'''Box Plot
A box plot is extremely useful for understanding:
Median
Quartiles
Spread
Outliers
import seaborn as sns
import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]

sns.boxplot(x=scores)

plt.title("Exam Score Box Plot")

plt.show()'''

#Violin Plot
'''A violin plot combines ideas from:
Box plot
KDE'''
#Example:
'''import seaborn as sns
import matplotlib.pyplot as plt
scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]

sns.violinplot(x=scores)
plt.title("Score Distribution")
plt.show() #The shape represents the density of values.'''

#Creating Normal Data,We can generate sample data using NumPy:

'''import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.normal(50, 10, 1000)

sns.histplot(data, kde=True)

plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()'''


'''class_A = [60, 65, 70, 72, 75, 78, 80]
class_B = [50, 55, 60, 62, 65, 68, 70]
#We can compare them:
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(class_A, kde=True, label="Class A")
sns.histplot(class_B, kde=True, label="Class B")

plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.title("Class Score Distributions")

plt.legend()

plt.show()#This helps compare the distributions.'''




'''
Histogram vs KDE vs Box Plot
Visualization	                Main purpose
Histogram	                   Frequency and distribution shape
KDE	                         Smooth density/shape
Box Plot	                      Median, quartiles, spread, outliers
Violin Plot                  	 Distribution shape + summary
ECDF	                         Cumulative distribution
'''

#ECDF

'''ECDF means:
Empirical Cumulative Distribution Function
It answers questions like:
What percentage of observations are less than or equal to a particular value?'''
#Example:

'''import seaborn as sns
import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]

sns.ecdfplot(scores)

plt.xlabel("Score")
plt.ylabel("Proportion")
plt.title("ECDF of Exam Scores")

plt.show()'''


#Rug Plot,A rug plot shows every individual observation as a small mark.
'''import seaborn as sns
import matplotlib.pyplot as plt

scores = [45, 50, 52, 55, 60, 62, 65, 67,
          70, 72, 75, 78, 80, 85, 90]
sns.rugplot(scores)

plt.xlabel("Scores")
plt.title("Rug Plot")
plt.show()'''

'''
Combining Histogram + KDE + Rug
You can combine them:

sns.histplot(scores, kde=True)
sns.rugplot(scores)

plt.show()
Histogram → frequency
KDE       → smooth density
Rug       → individual observations'''

#Distribution of Multiple Columns,Suppose we have:
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Math": [70, 75, 80, 85, 90],
    "Science": [65, 70, 78, 82, 88]
}

df = pd.DataFrame(data)

#We can visualize Math:

sns.histplot(df["Math"], kde=True)

plt.show()
sns.histplot(df["Science"], kde=True)

plt.show()'''


#Using a DataFrame Directly,Seaborn works very well with Pandas.

'''import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": [18, 20, 21, 22, 23, 24, 25, 27, 30]
})

sns.histplot(data=df, x="Age", kde=True)

plt.show()'''


#Distribution by Category,Suppose:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Score": [70, 75, 80, 85, 90, 60, 65, 70, 75, 80],
    "Gender": ["A", "A", "A", "A", "A",
               "B", "B", "B", "B", "B"]
})

#We can visualize:
sns.histplot(
    data=df,
    x="Score",
    hue="Gender",
    kde=True
)

plt.show()#hue means:Separate the visualization according to a categorical column.