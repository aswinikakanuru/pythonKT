#Probability
'''Probability means the chance of something happening.

Basic formula:
P(Event)=Total number of outcomes/Number of favorable outcomes

#Example: Tossing a coin

A coin has:
1.Head
2.Tail
Total outcomes = 2

Probability of getting Head:

# P(Head)=1/2=0.5=50% chances

So, there is a 50% chance of getting Head.
	​
'''
#Probability of an Event,An event is something we are interested in happening.'''
'''Example:

Rolling a dice.

Event:Getting a number greater than 4.Numbers greater than 4:
5, 6
Therefore:
P(>4)=2/6=1/3'''

#Probability Range:Probability is always between:0≤P(A)≤1
#Probability = 0 (Means impossible)
#Probability = 1 (Means certain)

'''Statistics->Statistics means collecting, organizing, analyzing and understanding data.
Example:Suppose 5 students got these marks:50, 60, 70, 80, 90

We can use statistics to answer questions like:
What is the average?(Mean)
What is the middle value?(Median)
What is the most common value?(Mode)
How spread out are the marks?
'''


#1.Mean
'''Mean = Average
Formula:Mean=Sum of values/Number of values

Example=10,20,30,40,50
mean=10+20+30+40+50/5
mean=150/5=30
numbers=[10,20,30,40,50]
mean=sum(numbers)/len(numbers)
print(mean)'''






#2.Median
'''Median
Median = Middle value
First arrange the data in ascending order.

Example:10, 20, 30, 40, 50
Middle value = 30

What if there are even numbers?
Example:10, 20, 30, 40
There are two middle values:20 and 30
Take their average:
 Median=20+30/2=25 '''







#Mode
'''Mode = Most frequently occurring value
Example:10, 20, 20, 30, 40
20 appears twice.
Other values appear once.'''






#Range
'''Range tells us how far the smallest and largest values are apart.
Formula:Range=Maximum-Minimum

Example:10, 20, 30, 40, 50
Maximum = 50
Minimum = 10
Therefore:Range=50-10=40'''








#Variance
'''Variance tells us how spread out the data is from the mean.
Consider:
A = 10, 10, 10, 10, 10
All values are the same.
There is no spread.
Variance = 0

Now:
B = 2, 5, 10, 15, 18
Values are more spread out.
Therefore, variance is higher.

Small variance  → values are close together
Large variance  → values are spread out'''



#Standard Deviation
'''Standard deviation also tells us how spread out the data is.
It is related to variance:Standard Deviation=sqrt{Variance} 

Example:
If:Variance = 25
Then:SD=sqrt 25=5 
So:Standard Deviation = 5'''




#Short Remember
'''
Mean       → Average
Median     → Middle
Mode       → Most common
Range      → Maximum - Minimum
Variance   → Spread
Std Dev    → Spread (in original units)'''


'''
Population vs Sample

#population
This is an important statistics concept.
Population
The entire group we are studying.
Example:
Marks of all 100 students in a college.
All 100 students = Population

#Sample
A smaller part selected from the population.
Example:
Marks of 20 students selected from those 100 students.
20 students = Sample

Population
   ↓
100 students
   ↓
Select 20 students
   ↓
Sample'''




'''Probability + Statistics Together
#Probability
Suppose a class has:
5 boys
5 girls
Total students:10
If we randomly select one student:
Probability of selecting a boy
P(Boy)=10/5=0.5

#Statistics
Now suppose their marks are:
60, 70, 70, 80, 90
We can calculate statistics:
Mean   = 74
Median = 70
Mode   = 70
Range  = 30'''

#Probability → deals with chance/uncertainty.
#Statistics → deals with data analysis.
'''Probability vs Statistics

Probability	                    Statistics
Deals with chance	           Deals with data
Predicts possible              outcomes	Analyzes observed data
Example: chance of Head	       Example: average marks
Uses random events	           Uses collected data'''

#Very simple memory trick:
#Probability = "What is the chance?"
#Statistics = "What does the data tell us?"'''



#Examples
#1.Probability of getting Head
total_outcomes = 2
favorable_outcomes = 1
probability = favorable_outcomes / total_outcomes
print("Probability of Head:", probability)

#2.Dice has 6 outcomes: 1,2,3,4,5,6
total_outcomes = 6
favorable_outcomes = 1
probability = favorable_outcomes / total_outcomes
print("Probability of getting 6:", probability)

#Probability of Getting an Even Number-Dice
total_outcomes = 6
favorable_outcomes = 3
probability = favorable_outcomes / total_outcomes
print("Probability of getting Even number:", probability)

#3.Mean
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
count = len(numbers)
mean = total / count
print("Mean:", mean)

#Median
numbers=[10,20,30,40,50]
numbers.sort()
n=len(numbers)
middle=n//2
if n%2==1:
    median=numbers[middle]
else:
    median=(numbers[middle-1]+numbers[middle])/2
print(median)


#Mode
numbers=[30,23,30,30,50,23]
frequency={}
for i in numbers:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
mode=max(frequency,key=frequency.get)
print("Mode :",mode)

#Range
numbers=[10,20,30,40,50]
maximum=max(numbers)
minimum=min(numbers)
result=maximum-minimum
print(result)


#Variance -> Let's calculate variance manually.

numbers = [10, 20, 30, 40, 50]

# Calculate mean
mean = sum(numbers) / len(numbers)

# Calculate squared differences
squared_differences = []

for number in numbers:
    difference = number - mean
    squared = difference ** 2
    squared_differences.append(squared)

# Calculate variance
variance = sum(squared_differences) / len(numbers)

print("Mean:", mean)
print("Squared differences:", squared_differences)
print("Variance:", variance)


#Standard Variance
import math
numbers=[10,20,30,40,50]
mean=sum(numbers)/len(numbers)
sqdif=[]
for num in numbers:
    dif=num-mean
    sq=dif**2
    sqdif.append(sq)
variance=sum(sqdif)/len(numbers)
standard_deviation=math.sqrt(variance)
print("Mean :",mean)
print("Sqare Differences :",sqdif)
print("varience :",variance)
print("Standard Deviation : ",standard_deviation)

'''Addition Rule
The addition rule is used when we want the probability of:
A OR B
We write:P(A u B) 
For two events:P(A u B)=P(A)+P(B)-P(A ∩ B)
The - P(A ∩ B) part is important because the common part gets counted twice.
AND vs OR

This is extremely important.
OR
Means:
A happens or B happens.
Symbol:A u B 

AND
Means:
A and B both happen.
Symbol:A ∩ B

For example:
A = student knows Java
B = student knows Python
OR
Student knows Java OR Python
AND
Student knows Java AND Python'''




#8. Multiplication Rule
'''For AND, we often use multiplication.
For independent events:
P(A∩B)=P(A)×P(B)'''


#9.Independent Events (Two events are independent if one event does not affect the other.)
'''
First coin toss
Second coin toss
The first toss doesn't change the second toss.
P(A∩B)=P(A)P(B)'''

#10.Dependent Events (Events are dependent when the first event affects the second event)


#Conditional Probability
'''
This is one of the most important probability concepts.
Conditional probability means:
Probability of A happening when we already know that B happened.
We write:P(A|B)
Read it as:
Probability of A given B.
The formula is:
P(A|B)=P(A∩B)/p(B)​

Simple Conditional Probability Example
Suppose a class has 10 students.
6 boys
4 girls
Among the 6 boys:3 know Python

Question:
If we know that the selected student is a boy, what is the probability that the student knows Python?
We are no longer considering all 10 students.
Because we already know:Student = Boy
So our new total is:6 boys
Among those 6:3 know Python
Therefore:
P(Python| Boy) = 3/6 =1/2 = 0.5 = 50%'''

#Without condition:10 students 
# With condition:6 boys -> The condition changes the sample space.

'''Conditional Probability Formula Derivation
P(A∣B)=P(A∩B)​/p(B)
P(A∩B)=P(A∣B)P(B)
This is called the multiplication rule for dependent events.

similarly
P(A∩B)=P(B∣A)P(A)
P(A|B)P(B)=P(B|A)P(A)

This equation leads directly to Bayes' Theorem.

'''

#Bayes' Theorem
'''
Bayes' Theorem helps us answer questions like:We observed some evidence. 
Given that evidence, what is the probability of the original event?'''
#The formula is P(A|B)=P(B|A)P(A)/P(B)
'''Term	Meaning
P(A)	Prior probability
P(B)	Probability of evidence
P(B|A)	Probability of B when A is true
P(A|B)	Probability of A given B
P(A|B)	Posterior probability

The important difference is:
P(B | A)versus P(A | B) they are generally not the same.'''
#example
'''Bayes Example — Medical Test
Let's use a simple example.
Suppose:1% of people have a disease.
Therefore:P(D)=0.01
Suppose a test has:90% positive rate for people who have the disease
So:P(Positive|D)=0.90 
And 5% of healthy people also test positive.
So:P(Positive|Not D)=0.05

Question:If someone gets a positive test result, what is the probability that they actually have the disease?
We want:P(D|Positive)
Step 1 — Identify What We Know
We know:P(D)=0.01 P(Positive|D)=0.90  P(Positive|text{Not D})=0.05 
We want:P(D|Positive)

Step 2 — Find P(Positive)
Positive results can happen in two ways:

Case 1
Person has disease and tests positive.
P(D)P(Positive|D) =0.01 * 0.90 =0.009 

Case 2
Person doesn't have disease but tests positive.
P(Not D)=1-0.01=0.99 
P(Not D)P(Positive|Not D)=0.99*0.05=0.0495
So total positive probability:
P(Positive)=0.009+0.0495  =0.0585

Step 3 — Apply Bayes' Theorem
P(A | B)=P(B | A)(P(A)/p(B)

P(D|Positive) = P(Positive|D)P(D)/P(Positive)

Substitute:

 P(D|Positive)=0.90*0.01/0.0585 
              = 0.009/0.0585 =0.1538 

Therefore=15.38%
This is a classic example of why P(A|B) and P(B|A) are different.'''
p_disease = 0.01

p_positive_given_disease = 0.90

p_positive_given_no_disease = 0.05

p_no_disease = 1 - p_disease

# Total probability of positive test
p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * p_no_disease
)

# Bayes theorem
p_disease_given_positive = (
    p_positive_given_disease * p_disease
    / p_positive
)

print("Probability of disease given positive test:",
      p_disease_given_positive)

'''Total Probability Rule

This is very important for Bayes.

Suppose event B can happen through A or Not A.

Then:P(B) = P(B|A)P(A) + P(B|A^c)P(A^c)

This is called the Law of Total Probability.

For example:

Positive test
       |
       +---- Disease
       |
       +---- No Disease

So:
P(Positive) = P(Positive|Disease)P(Disease) + P(Positive|NoDisease)P(NoDisease) 

Then we use that result in Bayes' theorem.

| Concept    | Meaning                               |
| -----------| ------------------------------------- |
|  P(A)      | Probability of A                      |
|  P(Aᶜ)     | Probability A does not happen         |
|  P(A ∪ B)  | A OR B                                |
|  P(A ∩ B)  | A AND B                               |
|  P(A \| B) | A given B                             |
| Independent| A doesn't affect B                    |
| Dependent  | A affects B                           |
| Bayes      | Helps reverse conditional probability |
'''






