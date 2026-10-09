#What is a Machine Learning Algorithm
'''A Machine Learning algorithm is a mathematical method that allows a computer to learn patterns 
from data and use those patterns to make predictions or decisions.

                  Machine Learning
                          |
          +---------------+---------------+
          |               |               |
     Supervised      Unsupervised    Reinforcement
      Learning         Learning         Learning
          |               |               |
     Labeled Data     Unlabeled Data    Reward/Penalty
'''

##Supervised Learning##

'''In Supervised Learning, the training data contains both:

Input → Features
Output → Target/Label

The two major supervised learning problems are:
Supervised Learning
       |
       +------ Regression
       |
       +------ Classification
       
#Regression : Regression is used when the output is a continuous numerical value.

Linear Regression:
One of the simplest and most important ML algorithms.
It tries to find a straight-line relationship between input and output.
The basic equation is:y = mx + b 
Where:
x = input
y = predicted output
m = slope
b = intercept

#ExAMPLE:
Experience → Salary
1 → 4
2 → 5
3 → 7
4 → ?
5 → 10
Linear Regression finds the best-fitting line through the data.
Advantages:
Simple
Easy to understand
Fast
Good baseline model
Disadvantages:
Assumes a linear relationship
Doesn't work well for complex patterns
Sensitive to outliers


#Multiple Linear Regression
When there are multiple input features, we use Multiple Linear Regression.

For example, house price depends on:
Area
Bedrooms
Location
Age
Parking

Formula becomes approximately:
y = b + w1x1 + w2x2 + w3x3 + ... + wnxn 

Example:
House Price =
Area contribution
+ Bedrooms contribution
+ Location contribution
+ Parking contribution
+ ...


#Polynomial Regression
Sometimes the relationship isn't a straight line.
For example:
x → y

1 → 2
2 → 5
3 → 10
4 → 17

The relationship may be curved.
Polynomial Regression can model such relationships.
Example: y = b + w_1x + w_2x^2 or higher powers.
Used when Data has a curved relationship.
 '''

#Classification :Classification predicts a category/class.
'''
Email → Spam / Not Spam
Disease → Positive / Negative
Transaction → Fraud / Genuine
Student → Pass / Fail
Image → Cat / Dog
Telugu-English
Output category/class laga unte Classification.
Logistic Regression

Despite its name, Logistic Regression is mainly a classification algorithm.
It is commonly used for binary classification.
Example:
Student information
       ↓
Logistic Regression
       ↓
Pass / Fail
It produces a probability.

For example:
Probability of Pass = 0.87
Then we can use a threshold:
0.87 > 0.5
       ↓
Pass

It uses the sigmoid function to map values approximately between 0 and 1.
σ(z)=1/1+e−z

Applications:
Spam detection
Customer churn
Fraud detection
Medical classification
Loan default prediction


#Decision Tree
A Decision Tree makes decisions using a tree-like structure.

Example:

             Attendance > 75%?
                 /       \
               Yes        No
                |          |
          Study > 4?      Fail
           /     \
         Yes      No
          |        |
        Pass      Fail

The model repeatedly asks questions about features.


Real-life example
Loan approval:
Income > ₹50,000?
       |
    +--+--+
    |     |
   Yes    No
    |      |
Credit    Reject
score?

Advantages:
Easy to understand
Easy to visualize
Handles numerical and categorical features
Requires relatively little preprocessing

Disadvantage:
Decision trees can overfit easily.

'''

#Random Forest :Random Forest is an ensemble learning algorithm based on many decision trees.
'''
Random Forest is an ensemble learning algorithm based on many decision trees.
(Oka decision tree meeda depend avvakunda chala trees create chesi, vaatini combine chesi final prediction istundi.)
Instead of:One Decision Tree
we create:
Tree 1
Tree 2
Tree 3
Tree 4
...
Tree 100

Then combine their predictions.
For classification:
Tree 1 → Cat
Tree 2 → Cat
Tree 3 → Dog
Tree 4 → Cat
Tree 5 → Cat

Final → Cat

This is similar to majority voting.
Advantages:
Usually better than a single decision tree
Reduces overfitting compared with one tree
Works well on many tabular datasets
Can estimate feature importance

'''
#K-Nearest Neighbors — KNN

'''KNN makes predictions based on nearby data points.
(New data point ki daggaraga unna existing points ni chusi class decide chestundi.)

Suppose we have:
Red points = Class A
Blue points = Class B

For a new point, KNN looks at the closest points.
If:
K = 5
and the nearest 5 points are:
A
A
A
B
A
Then prediction is A
'''

#Support Vector Machine — SVM
'''
SVM tries to find the best boundary/hyperplane that separates different classes.
Example:
Class A      |      Class B
● ● ●        |        ▲ ▲ ▲
● ● ●        |        ▲ ▲ ▲
             |
        Decision boundary

SVM tries to maximize the margin between classes.

#Naive Bayes
Naive Bayes is based on Bayes' theorem.
Bayes theorem:

 P(A|B)={P(B|A)P(A)}/{P(B)} 

 It calculates the probability of a class given the observed features.
Example
Email:
"Congratulations! You won money!"
Naive Bayes may calculate:
P(Spam | Words)
and
P(Not Spam | Words)
Then choose the class with higher probability.

Common applications:
Spam detection
Text classification
Sentiment analysis
Document classification
Why "Naive"?

It makes a simplifying assumption that features are conditionally independent given the class.  
'''



##Unsupervised Learning##
'''
Unsupervised Learning
(Data untundi kani correct answer/label undadu. Algorithm itself patterns/groups discover chestundi)
In Unsupervised Learning, we don't provide target labels.
Example:
Customer data:
Age
Income
Purchases
Visits

There is no:
Customer Type = ?
The algorithm discovers patterns/groups itself.

##Main Unsupervised Algorithms
Unsupervised Learning
        |
        +------ Clustering
        |
        +------ Dimensionality Reduction
        |
        +------ Association
        |
        +------ Anomaly Detection

#K-Means Clustering : K-Means groups similar data points into K clusters.
(Similar data points ni same group/cluster lo place chestundi.)
Suppose customer data contains:
Age
Income
Spending

We can ask:K = 3
The algorithm may discover:
Cluster 1 → Low-income customers
Cluster 2 → Middle-income customers
Cluster 3 → High-income customers

Basic process:
Choose K
Select initial centroids
Assign points to nearest centroid
Recalculate centroids
Repeat
Stop when clusters stabilize


#Hierarchical Clustering : Hierarchical clustering creates a hierarchy of clusters.
It is often represented using a dendrogram.
There are two common approaches:

1.Agglomerative:
Start with:A B C D E
Each point is its own cluster.
Then:
A+B
C+D
Then:AB + CD and so on.

2.Divisive : Start with one large cluster and split it.



### DBSCAN ##
DBSCAN means:Density-Based Spatial Clustering of Applications with Noise
(Dense ga unna points ni group chestundi; isolated points ni noise/outlier ga identify cheyyagaladu.)
It groups points based on density.
It can also identify noise/outliers.

Example:
● ● ●
 ● ●

                 ×

      ▲ ▲ ▲
       ▲ ▲

The isolated × may be detected as noise.
Advantages:
Can find irregularly shaped clusters
Detects noise
Doesn't require choosing number of clusters beforehand


##PCA — Principal Component Analysis
(Features chala ekkuva unnappudu important information ni maintain chestu dimensions ni reduce cheyyadaniki PCA use chestham.)
PCA is a dimensionality reduction technique.
Suppose we have:100 features
Maybe many features contain overlapping information.
PCA can transform them into fewer components:
100 features
      ↓
PCA
      ↓
10 principal components

This can help with:
Visualization
Reducing dimensionality
Faster training
Removing redundancy



#Association Rule Learning
This discovers relationships between items.
Very famous example:
Market Basket Analysis
Suppose customers frequently buy:
Bread + Butter
and sometimes:
Bread + Butter + Milk

The algorithm can discover relationships such as:
If customer buys Bread
        ↓
Maybe recommend Butter
Important concepts:
Support
Confidence
Lift
Popular algorithm:Apriori



#Anomaly Detection:Anomaly detection finds unusual observations.
Example:
Normal transactions:
₹500
₹800
₹1200
₹700
₹900
Suddenly:
₹5,00,000
This could be an anomaly.

Applications:
Fraud detection
Network security
Manufacturing defects
System monitoring

Algorithms include:
Isolation Forest
One-Class SVM
Local Outlier Factor
'''

#Reinforcement Learning
'''Reinforcement Learning is different from supervised learning.
(Trial and error method lo agent learn chestundi. Correct action ki reward, wrong action ki penalty vastundi.)
An agent interacts with an environment.

       Action
Agent ---------> Environment
  ↑                  |
  |                  |
  +----- Reward <----+

The agent learns through:
Actions
Rewards
Penalties

Example:Game-playing AI:
Move → Win → +10 reward
Move → Lose → -10 reward

Over time, the agent learns which actions are better.


#Q-Learning
Q-Learning is a popular reinforcement learning algorithm.
It learns a value called:Q-value
The Q-value tells the agent how useful an action is in a particular state.

Example:
State = Robot at Room A
Action 1 → Move left
Action 2 → Move right
Action 3 → Move forward

The algorithm learns which action gives the best long-term reward.'''


'''
#Important Algorithm Comparison
Algorithm	                            Type	                                Main Use
Linear Regression	                   Supervised	                   Numerical prediction
Polynomial Regression	            Supervised	              Nonlinear numerical prediction
Logistic Regression	                   Supervised	                    Classification
Decision Tree	                          Supervised	                Classification/Regression
Random Forest	                      Supervised/Ensemble           	  Classification/Regression
KNN	                                  Supervised	                Classification/Regression
SVM	                                  Supervised	                Classification/Regression
Naive Bayes	                           Supervised	                     Classification
K-Means	                           Unsupervised                    	 Clustering
Hierarchical Clustering	             Unsupervised	                      Clustering
DBSCAN	                                  Unsupervised	                   Clustering + noise
PCA	                             Unsupervised technique	         Dimensionality reduction
Apriori	                           Unsupervised	                     Association rules
Isolation Forest	                    Unsupervised	                     Anomaly detection
Q-Learning	                           Reinforcement	                 Sequential decision-making
Neural Networks	              Supervised/Unsupervised/etc.	    Complex pattern learning
CNN	                                   Deep Learning	                       Images/vision
RNN/LSTM	                            Deep Learning                  	Sequential data
Transformer	                            Deep Learning	                  NLP, multimodal AI, sequences
'''