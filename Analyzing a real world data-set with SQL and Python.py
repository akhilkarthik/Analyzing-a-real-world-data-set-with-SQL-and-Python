#!/usr/bin/env python
# coding: utf-8

# ## Selected Socioeconomic Indicators in Chicago
# 
# The city of Chicago released a dataset of socioeconomic data to the Chicago City Portal.
# This dataset contains a selection of six socioeconomic indicators of public health significance and a “hardship index,” for each Chicago community area, for the years 2008 – 2012.
# 
# Scores on the hardship index can range from 1 to 100, with a higher index number representing a greater level of hardship.
# 
# A detailed description of the dataset can be found on [the city of Chicago's website](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDB0201ENSkillsNetwork20127838-2021-01-01), but to summarize, the dataset has the following variables:
# 
# *   **Community Area Number** (`ca`): Used to uniquely identify each row of the dataset
# 
# *   **Community Area Name** (`community_area_name`): The name of the region in the city of Chicago
# 
# *   **Percent of Housing Crowded** (`percent_of_housing_crowded`): Percent of occupied housing units with more than one person per room
# 
# *   **Percent Households Below Poverty** (`percent_households_below_poverty`): Percent of households living below the federal poverty line
# 
# *   **Percent Aged 16+ Unemployed** (`percent_aged_16_unemployed`): Percent of persons over the age of 16 years that are unemployed
# 
# *   **Percent Aged 25+ without High School Diploma** (`percent_aged_25_without_high_school_diploma`): Percent of persons over the age of 25 years without a high school education
# 
# *   **Percent Aged Under** 18 or Over 64:Percent of population under 18 or over 64 years of age (`percent_aged_under_18_or_over_64`): (ie. dependents)
# 
# *   **Per Capita Income** (`per_capita_income_`): Community Area per capita income is estimated as the sum of tract-level aggragate incomes divided by the total population
# 
# *   **Hardship Index** (`hardship_index`): Score that incorporates each of the six selected socioeconomic indicators
# 

# In[1]:


# we wwill take a look at the variables in the socioeconomic indicators dataset and do some basic analysis with Python.


# In[2]:


### Connect to the database


# In[3]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[6]:


import csv, sqlite3

con = sqlite3.connect("socioeconomic.db")
cur = con.cursor()


# In[7]:


# Let us first load the SQL extension and establish a connection with the database
# The syntax for connecting to magic sql using sqllite is
# %sql sqlite:///DatabaseName


# In[10]:


get_ipython().run_line_magic('sql', 'sqlite:///socioeconomic.db')


# In[11]:


##### We will first read the csv files  from the given url  into pandas dataframes


# In[12]:


import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')


# In[14]:


# Next we will be using the  df.to_sql() function to convert each csv file  to a table in sqlite  with the csv data loaded in it


# In[15]:


df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")


# #### sql query

# In[17]:


get_ipython().run_line_magic('sql', 'SELECT * FROM chicago_socioeconomic_data limit 5;')


# In[18]:


#### Analysis


# In[19]:


##### How many rows are in the dataset?

get_ipython().run_line_magic('sql', 'SELECT count(*) FROM chicago_socioeconomic_data')


# In[20]:


##### How many community areas in Chicago have a hardship index greater than 50.0?

get_ipython().run_line_magic('sql', 'SELECT count(*) FROM chicago_socioeconomic_data where hardship_index >50')


# In[21]:


##### What is the maximum value of hardship index in this dataset?

get_ipython().run_line_magic('sql', 'SELECT MAX(hardship_index ) FROM chicago_socioeconomic_data')


# In[23]:


##### Which community area which has the highest hardship index?

get_ipython().run_line_magic('sql', 'select community_area_name from chicago_socioeconomic_data where hardship_index = (select max(hardship_index) from chicago_socioeconomic_data)')


# In[25]:


##### Which Chicago community areas have per-capita incomes greater than $60,000?

get_ipython().run_line_magic('sql', 'select community_area_name from chicago_socioeconomic_data where per_capita_income_>60000')


# In[26]:


# Create a scatter plot using the variables `per_capita_income_` and `hardship_index`. 
# Explain the correlation between the two variables.


# In[27]:


import seaborn as sns
from matplotlib import pyplot as plt


# In[37]:


income_vs_hardship = get_ipython().run_line_magic('sql', 'select per_capita_income_,hardship_index from chicago_socioeconomic_data')


# In[42]:


sns.jointplot(x="per_capita_income_",y="hardship_index",data=income_vs_hardship.DataFrame())
plt.show()


# In[ ]:




