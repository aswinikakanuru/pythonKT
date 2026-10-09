'''What is Pandas?
Pandas is a Python library used for:
Data analysis
Data manipulation
Cleaning data
Reading/writing files
Working with tables
Handling missing values
Filtering and sorting data
Preparing data for Machine Learning

Think of Pandas as Excel inside Python.'''


'''
Why do we use Pandas?
Suppose you have 10 lakh employee records.
Doing this manually in Excel can become difficult.
With Pandas, you can easily:
df[df["Salary"] > 30000]
This gives employees whose salary is greater than ₹30,000.
'''

'''Main Data Structures in Pandas
Pandas mainly has two important data structures:
1. Series
One-dimensional data.

2. DataFrame
Two-dimensional tabular data.

Think:
Series    → One column
DataFrame → Complete table'''

#Pandas Series -> A Series is a one-dimensional labeled array.
import pandas as pd
nums=pd.Series([10,20,30,40,50])
print(nums) #By default, Pandas creates indexes starting from 0.

#Creating Series with Custom Index
import pandas as pd
marks=pd.Series([90,87,98],index=["Maths","Physics","English"])
print(marks)
print(marks["Maths"])

#Series from Dictionary
import pandas as pd
data={
    "Maths":98,
    "English":95,
    "Physics":90
}
marrks=pd.Series(data)
print(marrks) #Pandas automatically uses dictionary keys as indexes.

#DataFrame -> A DataFrame is the most important Pandas structure.
#It represents data in rows and columns.
import pandas as pd
dataa={
    "Name":["Aswini","Ruchitha","Santhosh","Sumanth"],
    "Age":[22,21,20,23],
    "Salary":[30000,40000,35000,50000]
}
df=pd.DataFrame(dataa)
print(df)

#Creating DataFrame from List
data = [
    ["Ravi", 22, 30000],
    ["Anu", 24, 40000],
    ["Priya", 23, 35000],
    ["Ashu",22,25000],
    ["Sumanth",23,30000],
    ["Santhosh",20,20000]
]
df = pd.DataFrame(
    data,
    columns=["Name", "Age", "Salary"]
)
print(df)
#Important DataFrame Functions,Now let's learn the functions you will use frequently.
#head() Displays the first rows.
print(df.head()) #By default, it shows first 5 rows.
print(df.head(2))
#tail()Displays the last rows.
print(df.tail()) #Last 5 rows by default.
print(df.tail(2))
#shape,Shows the number of rows and columns.
print(df.shape)
#columns,Shows column names.
print(df.columns)
#index,Shows DataFrame indexes.
print(df.index)
#dtypes,Shows data type of every column.
print(df.dtypes)
#info(),One of the most important Pandas functions.
'''It gives:
Number of rows
Number of columns
Column names
Non-null values
Data types
Memory usage

Example:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 Name      3 non-null object
 Age       3 non-null int64
 Salary    3 non-null int64
When you receive a new dataset, info() is usually one of the first functions to use.'''
df.info()
#describe(),Provides statistical information for numerical columns.
print(df.describe())
#Selecting a Column
print(df["Name"])
#Selecting Multiple Columns
print(df[["Name", "Salary"]])
#Selecting Rows using iloc,iloc means integer-location based indexing.
print(df.iloc[0])#Gets the first row.
print(df.iloc[1])#Gets the second row.
#loc,loc is used for label-based selection.
print(df.loc[0])
#If we have custom indexes:
'''df = pd.DataFrame(
    {
        "Name": ["Ravi", "Anu", "Priya"],
        "Age": [22, 24, 23]
    },
    index=["A", "B", "C"]
)
print(df.loc["B"])'''
'''
iloc vs loc
Very important for interviews.
Function	 Based on
iloc	    Integer position
loc	        Label/index
'''
#Adding a New Column
df["Department"] = ["IT", "HR", "IT","Developer","QA","IT"]

#Creating a Column using Existing Columns
df["AnnualSalary"] = df["Salary"] * 12
print(df)
