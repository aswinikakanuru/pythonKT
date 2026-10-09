#How Machine Learning Works?

'''Basic ML workflow:

1. Collect Data
       ↓
2. Clean Data
       ↓
3. Prepare Data
       ↓
4. Split Data
       ↓
5. Choose Algorithm
       ↓
6. Train Model
       ↓
7. Evaluate Model
       ↓
8. Tune/Improve Model
       ↓
9. Make Predictions
       ↓
10. Deploy Model'''

#Let's understand each one.

#Step 1 — Collect Data
'''Machine Learning ki data is the foundation.

Data sources:
Databases
CSV files
Excel
APIs
Websites
Sensors
Applications
User activity

First manaki problem solve cheyyadaniki required data collect cheyyali.
Good data → Better model
Bad data → Bad model
'''

#Step 2 — Data Cleaning
'''Real-world data usually perfect ga undadu.
Problems:
Missing values
Duplicate records
Incorrect values
Outliers
Wrong formats

Data cleaning is required before training.
Real-world data lo errors untayi.

Example:
Age = NULL
Salary = -5000
City = Hyderabad / HYD / hyderabad

Ivi correct cheyyali.
'''

#Step 3 — Features and Target
'''This is a very important ML concept.
Features ante model ki input ga iche information.
Target ante manam predict cheyyalanukunna output.

Example:
Area + Bedrooms + Age
            ↓
           ML
            ↓
       House Price
'''

#Step 4 — Training Data and Testing Data
'''We shouldn't train and test the model using exactly the same data.

Usually data ni divide chestham:
Dataset
   |
   ├── Training Data
   |
   └── Testing Data
   
Training Data :Model learns from this data.
Testing Data :Model ni evaluate cheyyadaniki use chestham

Training data ante:Model ki nerpinche data
Testing data ante:Model entha correct ga nerchukundo check chese unseen data'''

#Step 5 — Choose an Algorithm
'''Problem type batti algorithm choose chestham.

Some common algorithms:
Regression:
Linear Regression
Decision Tree Regression
Random Forest Regression
Classification:
Logistic Regression
Decision Tree
Random Forest
K-Nearest Neighbors
Support Vector Machine
Clustering:
K-Means
Hierarchical Clustering

Later each algorithm ni separately detailed ga study cheyyachu.'''

#Step 6 — Training the Model
'''Training means:Algorithm uses training data to learn patterns.

Example:

Training Data
     ↓
ML Algorithm
     ↓
Learn Patterns
     ↓
Trained Model

Suppose house prices:

1000 sq.ft → ₹50 lakh
1500 sq.ft → ₹75 lakh
2000 sq.ft → ₹100 lakh

Model area and price madhya relationship ni learn chestundi.'''

#What is a Model

'''A model is the learned representation of patterns/relationships from training data that can be used to make predictions.

Simple example:
Data
 ↓
Algorithm
 ↓
Training
 ↓
Model

Then:
New Data
   ↓
Trained Model
   ↓
Prediction

Model ante simply:Data nunchi nerchukunna pattern/relationship ni represent chese learned system.'''

#Step 7 — Prediction
'''After training:
New House:
Area = 1800 sq.ft
Bedrooms = 3
Age = 3 years

       ↓

Trained ML Model

       ↓

Predicted Price = ₹90 lakh

This is called prediction/inference.'''


#Step 8 — Model Evaluation
'''Model correct ga work chesthunda?

Daanini evaluate cheyyali.

Different problems ki different metrics use chestham.

Regression metrics:
MAE
MSE
RMSE
R² Score
Classification metrics:
Accuracy
Precision
Recall
F1-score
ROC-AUC

Example:
Actual:
Pass

Predicted:
Pass

→ Correct

If:

Actual:
Fail

Predicted:
Pass

→ Wrong'''


#Types of Machine Learning
'''Machine Learning
│
├── 1. Supervised Learning
│
├── 2. Unsupervised Learning
│
└── 3. Reinforcement Learning'''

#Supervised Learning
'''In supervised learning, the training data contains:Input + Known Correct Output
The model learns the relationship between them.
Supervised learning lo input tho paatu correct output kuda untundi.
Input + Correct Answer
          ↓
        Model
          ↓
    Learn Pattern
Main supervised learning tasks:
Regression
Classification'''

#Regression
'''Regression is used when the output is a continuous numerical value
(Regression ante number/value predict cheyyadam).

Examples:
House price
Temperature
Salary
Sales
Stock-related forecasting tasks

Example:
Input:
Area = 1500
Output:
Price = ₹75,00,000 (Price is a numerical value)'''

#Classification
'''Classification is used when the output belongs to a category/class.

Examples:
Email → Spam / Not Spam
Student → Pass / Fail
Transaction → Fraud / Genuine
Image → Cat / Dog

Classification ante:Data ni oka category/class lo place cheyyadam.'''

#Unsupervised Learning
'''In unsupervised learning:Training data has no labelled target/output.
The model tries to discover patterns or structure by itself.

Example:
Suppose an e-commerce company has customer data:

Customer A → ₹5000/month
Customer B → ₹5500/month
Customer C → ₹50,000/month
Customer D → ₹60,000/month

We don't provide customer groups.

Algorithm may discover:
Group 1 → Low spending customers
Group 2 → High spending customers
This is called clustering.

Unsupervised learning lo correct answer already provide cheyyamu.
Machine itself data lo patterns/groups discover chestundi.'''

#Clustering
'''Clustering means grouping similar data points together.
Example:
Customers
   ↓
ML Algorithm
   ↓
┌──────────────┐
│ Group 1      │ → Low spenders
│ Group 2      │ → Medium spenders
│ Group 3      │ → High spenders
└──────────────┘

Popular algorithm:K-Means Clustering'''


#Reinforcement Learning
'''
Reinforcement Learning (RL) is based on:
Agent + Environment + Actions + Rewards

Example:
A robot needs to learn how to move.

Agent
  ↓
Takes Action
  ↓
Environment
  ↓
Reward / Penalty
  ↓
Learns

If action is good:+10 reward
If action is bad:-10 penalty
The agent learns which actions produce better results.

Reinforcement Learning lo machine trial and error dwara nerchukuntundi.
Good action:Reward 🎁
Bad action:Penalty ❌
Goal:Maximum reward achieve cheyyadam.

Examples:
Game-playing AI
Robotics
Autonomous systems
Recommendation/control problems
'''


#Supervised vs Unsupervised vs Reinforcement
'''
Type                    Data                Main Goal	                        Example
Supervised	          Labelled	         Predict output	                      House price
Unsupervised	     Unlabelled        	Find patterns/groups	             Customer groups
Reinforcement	      Rewards	          Learn actions	                    Game-playing agent

Easy memory trick:
Supervised     → Teacher available
Unsupervised   → No teacher
Reinforcement  → Reward/Penalty
'''

#Main Need for Machine Learning
'''
Machine Learning is needed mainly because it can
learn patterns from large amounts of data and use those patterns to make predictions or decisions.
Major reasons:
1. Complex problems
Some problems are too complicated to solve with fixed rules.
2.Huge amount of data
Today applications generate enormous amounts of data.
Humans cannot manually analyze all of this efficiently.
ML can process large datasets and learn useful patterns.
3.Automation
ML can automate decisions/predictions.
4. Prediction
ML can use historical data to predict future or unknown outcomes.
5.Personalization
ML can learn individual user preferences.
6.Continuous improvement
With appropriate retraining and monitoring, ML systems can be updated as new data becomes available.

#Example
Website lo millions of users behavior untundi.
Prathi user ki manual rules rayadam impossible.
ML:
User behavior + historical data → patterns → recommendations
generate cheyyadaniki use avuthundi.


'''