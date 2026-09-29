import math
numbers = [10, 20, 30, 40, 50]

# Mean
mean = sum(numbers) / len(numbers)

# Squared differences
squared_differences = []

for x in numbers:
    difference = x - mean
    squared_difference = difference ** 2
    squared_differences.append(squared_difference)

# Population variance
variance = sum(squared_differences) / len(numbers)

# Standard deviation
standard_deviation = math.sqrt(variance )

print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)

#Skewness
'''
Now we come to Skewness.Skewness tells us about the asymmetry of a distribution.
In simple words:Which direction does the distribution have a longer tail?
There are three common cases:
Positive Skew
Negative Skew
Zero Skew

Symmetric Distribution:Imagine a perfectly balanced distribution:
              /\
             /  \
            /    \
           /      \
__________/        \__________
Both sides are approximately equal.

Skewness:0
For a perfectly symmetric normal distribution:Mean ≈ Median ≈ Mode



1.Positive Skewness
Positive skew means the distribution has a longer tail toward the right.

       /\
      /  \
     /    \
    /      \____
___/             \____________

The tail stretches toward larger values.
Right-skewed=Positive skewness





2.Negative Skewness
Negative skew means the longer tail is toward the left.
____________
          __/
       __/
     _/
    /\
   /  \
__/    \
Left-skewed=Negative skewness
Example:
Suppose an exam is very easy and most students score highly:
50, 80, 85, 90, 92, 95, 98
A few low scores may create a longer left tail.
'''

'''Long tail → RIGHT
             ↓
       Positive skew


Long tail ← LEFT
             ↓
       Negative skew'''


from scipy.stats import skew
data = [10, 11, 12, 13, 14, 15, 100]
result = skew(data)
print("Skewness:", result)

'''
Mean: The arithmetic average of the observations.
Variance: The average squared deviation from the mean for a population, or its sample counterpart using \(n-1\).
Standard deviation: The square root of variance, measuring spread in the original units.
Skewness: A measure of the asymmetry of a distribution; positive indicates a longer right tail and negative a longer left tail.
'''