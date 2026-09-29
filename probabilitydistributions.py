#Probability Distributions — Bernoulli, Binomial, and Normal
'''A probability distribution tells us:What possible values a random variable can take and how likely each value is.'''

#Random Variable
'''A random variable is a variable whose value depends on the outcome of a random experiment.
Example: Toss a coin
Possible outcomes:
Heads
Tails
We can represent them as:
X = 1 → Heads
X = 0 → Tails
Here X is a random variable.'''

#2.Probability Distribution
'''A probability distribution tells us the probability associated with each possible value of a random variable.
For example:
One coin toss
X	Meaning	Probability
0	Tails	0.5
1	Heads	0.5
So:P(X=0)=0.5 
   P(X=1)=0.5
This is a Bernoulli distribution.'''


'''                 Probability Distributions
                         |
          +--------------+--------------+
          |              |              |
      Bernoulli       Binomial        Normal
          |              |              |
      One trial      Multiple trials   Continuous
          |              |              |
       0 or 1        Number of       Bell curve
                      successes

Bernoulli = ONE attempt

Binomial = MANY Bernoulli attempts

Normal = Continuous bell-shaped data
'''


#Bernoulli Distribution
'''A Bernoulli distribution represents an experiment with exactly two possible outcomes.

Usually:
Success = 1
Failure = 0

Examples:
Coin → Heads / Tails
Exam → Pass / Fail
Machine → Working / Failed
Email → Spam / Not Spam
Transaction → Fraud / Not Fraud
There is only one trial.'''

#Binomial Distribution
'''
Binomial distribution counts the number of successes in a fixed number of independent Bernoulli trials.
Suppose we toss a coin:1 time,That's Bernoulli.

But suppose we toss it:10 times ,and ask:How many Heads did we get?
That's Binomial Distribution.

The binomial probability formula is:
P(X=k)= {n}p^k(1-p)^(n-k)
        {k}
Symbol	Meaning:
n	Number of trials
k	Number of successes
p	Probability of success
1-p	Probability of failure
n-k	Number of failures
C(n,k)	Number of ways to arrange successes

C(n,k):It means combination.(k
                             n)=n!/k!(n-k)!
'''
'''
Example:
Suppose we toss a fair coin:n = 5 times
Probability of Heads:p=0.5 

Question:
What is the probability of getting exactly 3 Heads?
We have:
n=5 
k=3 (No of sucesss(3 heads))
p=0.5 
Formula: P(X=3) = (53)(0.5)^3(0.5)^2 

We know:(5 3)=10 

Therefore:
P(X=3)=10(0.5)^3(0.5)^2 
      =10(0.5)^5 
      =10/32 
      =0.3125
Therefore:31.25%
'''
#Python — Binomial
import math
n = 5
k = 3
p = 0.5
combination = math.comb(n, k)
probability = (
    combination
    * (p ** k)
    * ((1 - p) ** (n - k))
)
print("Probability:", probability)
print("Percentage:", probability * 100)



#Binomial Mean and Variance
import math
n = 100
p = 0.2

mean = n * p
variance = n * p * (1 - p)
standard_deviation = math.sqrt(variance)

print("Mean:", mean)
print("Variance:", variance)
print("Standard deviation:", standard_deviation)



#Normal Distribution
'''Now we move to a very different type.
The Normal Distribution is a continuous probability distribution with a characteristic bell-shaped curve.
Examples of data that can often be approximately normally distributed include
Heights
Weights
Measurement errors
Some exam scores
Manufacturing measurements'''

#Mean and Standard Deviation

#A normal distribution is mainly described by
#Mean (μ)
#Standard deviation (σ)

'''
Mean
Determines the center of the distribution.

Standard deviation 
Determines how spread out the values are.'''
#Z-Score
mean = 70
standard_deviation = 10
score = 90

z = (score - mean) / standard_deviation

print("Z-score:", z)




'''Is there only one trial with two possible outcomes?
YES → Bernoulli
Example:Will the customer buy or not buy?

Are there n repeated independent trials, each with success/failure, and we're counting successes?
YES → Binomial
Example:Out of 20 customers, how many buy?

Is the variable continuous and approximately bell-shaped?
YES → Normal
Example:
Height
Weight
Measurement'''