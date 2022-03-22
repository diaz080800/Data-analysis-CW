#!/usr/bin/env python
# coding: utf-8

# # Week 3
# By: Christopher Diaz Montoya
# ID: 24707686

# ## Import libraries

# In[1]:


import pandas as pd # Imported library to import and view data
import matplotlib.pyplot as plt # Imported to plot graphs
import seaborn as sns # imported to plot graphs and heatmap
sns.set_theme(style="darkgrid") # For graph style

print("Libraries imported.")


# ## Import data

# In[2]:


# Here pd.read_csv() is used to import csv from file path entered
df = pd.read_csv(r"C:\Users\chris\Downloads\Uni\EHU year 2\Data analysis\Week 3\train.csv") # Imports data with pandas
df.head() # To display head and view columns


# ## Check data set

# In[3]:


df.isna().sum() # To check missing values


# In[4]:


df = df.drop("Loan_ID", 1)
df.info() # To check if data is numerical and all the entries


# ## Feature exploration

# In[5]:


# Amount accepted and rejected in percentage numbers
print(df["Loan_Status"].value_counts(normalize = True)*100) 
# Used to see the column which shows how many people got approved in a barchart
df["Loan_Status"].value_counts(normalize = True).plot.bar(title = "Loan status")


# In[6]:


# Creates graphs with columns against the weekly sales which helps see correlations if any
columns = ["Gender","Married", "Dependents", "Education", "Self_Employed", "Credit_History", "Property_Area"]
# For loop to go over every column
for i in columns:
    # Seaborn pairplot histogram for all columns with loan status on x axis
    # Normalize helps see the gender in accordance to percentage and not amount
    # Cross tab learnt last semsester to show data in column
    y = pd.crosstab(df["Loan_Status"], df[i], normalize = "columns")
    y.plot(kind = "bar", width = .5)


# In[7]:


# Continious values have a different graph
numColumns = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term"]

# Learnt this in lectue slides
for z in numColumns: # For loop to make a graph for each column
    # for each loop until every column in numColumns has a graph
    # shows column in numColumns against Loan_status
    df.boxplot(column = z, by = "Loan_Status") # Plots graph
    plt.show() # Shows graphs


# ## Further exploration
# Here extra things were checked to see correlation between different attributes such as gender and pay  

# In[8]:


# Using seaborn to make graphs, expermented with hue and grid and graph style at the beginning
sns.scatterplot(data = df, x = "Education", y = "ApplicantIncome", hue = "Education").grid()


# In[9]:


sns.scatterplot(data = df, x = "Education", y = "LoanAmount", hue = "Education").grid()


# In[10]:


# Different form of seaborn graph used
sns.regplot(data = df, x = "LoanAmount", y = "ApplicantIncome", color = "r")


# In[11]:


# Created bins to check different incomes, learnt last semester
bins = [0,2500,4000,6000,81000]
groups = ["Low","Average","High", "Very high"]
# pandas helps cut into groups in applicant income
df["Income_cat"] = pd.cut(df['ApplicantIncome'], bins, labels = groups)


# In[12]:


# Prints amount in each group
print(pd.crosstab(df["Income_cat"],df["Loan_Status"]))
# Cross tab learnt last semester to show frequency in a group
Income_bin = pd.crosstab(df["Income_cat"], df["Loan_Status"])
# Bar graph used to easily see data
Income_bin.div(Income_bin.sum(1), axis=0).plot(kind = "bar")
plt.xlabel("Applicants Income")
plt.ylabel("Percentage")
plt.show()


# In[13]:


sns.scatterplot(data = df, x = "Credit_History", y = "ApplicantIncome", hue = "Credit_History")


# In[15]:


sns.scatterplot(data = df, x = "Property_Area", y = "ApplicantIncome", hue = "Property_Area")


# In[16]:


sns.scatterplot(data = df, x = "Property_Area", y = "LoanAmount", hue = "Property_Area")


# In[17]:


sns.scatterplot(data = df, x = "Self_Employed", y = "LoanAmount", hue = "Self_Employed")


# In[18]:


sns.scatterplot(data = df, x = "Self_Employed", y = "ApplicantIncome", hue = "Self_Employed")


# ## Heat map and final data prep

# In[19]:


# Data all transformed to numerical type
for i in columns: # For loop to loop over each column in columns list
    df[i] = pd.get_dummies(df[i]) # Get dummies transformation on each
 
df["Loan_Status"] = pd.get_dummies(df["Loan_Status"]) # Get dummies for yes and no in this column


# In[20]:


# Last graphs would not work unless data was transformed
df.plot.scatter(x = "Gender", y = "ApplicantIncome").grid()


# In[21]:


df.plot.scatter(x = "Gender", y = "LoanAmount").grid()


# In[22]:


correspondent = df.corr() # Checks correlation in df
plt.subplots(figsize = (10, 10)) # Size of heat map
sns.heatmap(correspondent, cmap = "YlGnBu", vmin = -1.0, annot = True) # Creates heatmap


# In[23]:


# For loop to fill all columns with missing values with the mode ready to split data
for z in columns and numColumns:
    # Missing data filled wit mode
    df[z] = df[z].fillna(df[z]).mode()[0]
# Shows missing values left
df.isnull().sum()

