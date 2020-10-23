#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("StudentsPerformance.csv")


# In[64]:


df.head()


# In[67]:


df.tail()


# In[4]:


df.T


# In[66]:


df


# In[5]:


df.info()


# In[6]:


# Dataframe is error free i.e that is no null values is there


# In[8]:


df.isnull().sum()


# In[9]:


#  Numerical Variables : Math score, Reading score and Writing score.
#  Categorical Variables : Gender, Race/ethnicity, Parental level of education, Lunch and Test preparation course.


# In[10]:


df.describe()


# In[21]:


sns.countplot(df['math score'])
plt.title('Math Score',fontsize = 20)


# In[ ]:


#  Above graph shows the graphical visualization of the marks in math.


# In[22]:


sns.countplot(df['reading score'])
plt.title('reading Score',fontsize = 20)


# In[85]:


#  Above graph shows the graphical visualization of marks in reading score.


# In[86]:


sns.countplot(df['writing score'])
plt.title('Writing Score',fontsize = 20)


# In[87]:


#  Above graph shows the graphical visualization of marks in writing score.


# In[92]:


plt.figure(figsize=(6,5))
plt.title('Math Score',fontsize = 20)
sns.violinplot(y='math score',data=df,color='y',linewidth=2)


# In[ ]:


# Upper violin graph shows that the maximum number of students in maths score 50 to 80 % marks.


# In[91]:


plt.figure(figsize=(6,5))
plt.title('Reading Score',fontsize = 20)
sns.violinplot(y='reading score',data=df,color='r',linewidth=2)


# In[ ]:


# Upper violin graph shows that the maximum number of students in reding score 50 to 80 % marks.


# In[90]:


plt.figure(figsize=(6,5))
plt.title('Writing Score',fontsize = 20)
sns.violinplot(y='writing score',data=df,color='b',linewidth=2)


# In[88]:


# Upper violin graph shows that the maximum number of students in writing score 55 to 85 % marks.


# In[44]:


plt.figure(figsize=(6,5))
plt.title('Gender',fontsize = 20)
df['gender'].value_counts().plot.pie(autopct="%1.1f%%")


# In[47]:


plt.figure(figsize=(6,5))
plt.title('Race/Ethnicity',fontsize = 20)
df['race/ethnicity'].value_counts().plot.pie(autopct="%1.1f%%")


# In[48]:


plt.figure(figsize=(6,5))
plt.title('parental level of education',fontsize = 20)
df['parental level of education'].value_counts().plot.pie(autopct="%1.1f%%")


# In[50]:


plt.figure(figsize=(6,5))
plt.title('Math Scores')
sns.barplot(x="gender", y="math score", data=df)


# In[51]:


plt.figure(figsize=(6,5))
plt.title('Reading Scores')
sns.barplot(x="gender", y="reading score", data=df)


# In[52]:


plt.figure(figsize=(6,5))
plt.title('Writing Scores')
sns.barplot(x="gender", y="writing score", data=df)


# In[96]:


plt.figure(figsize=(6,5))
plt.title('Math Scores')
sns.barplot(x="test preparation course", y="math score", data=df,hue="gender")

print("\nThis graph shows the difference in marks of males and females who completed and not completed\ntest preparation course in math subject")


# In[97]:


plt.figure(figsize=(6,5))
plt.title('Reading Scores')
sns.barplot(x="test preparation course", y="reading score", data=df,hue="gender")
print("\n This graph shows the difference in marks of males and females who completed and not completed\ntest preparation course in Reading subject")


# In[98]:


plt.figure(figsize=(6,5))
plt.title('Writing Scores')
sns.barplot(x="test preparation course", y="writing score", data=df,hue="gender")
print("This graph shows the difference in marks of males and females who completed and not completed\ntest preparation course in writing subject")


# In[57]:


#  So the students (male and female) who completed the test preparation course scored higher in all three subjects.


# In[60]:


plt.figure(figsize=(15,5))
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9,
                      wspace=0.5, hspace=0.2)
plt.subplot(131)
plt.title('Math Scores')
sns.barplot(x="race/ethnicity", y="math score", hue="test preparation course", data=df)
plt.subplot(132)
plt.title('Reading Scores')
sns.barplot(hue="test preparation course", y="reading score", x="race/ethnicity", data=df)
plt.subplot(133)
plt.title('Writing Scores')
sns.barplot(hue="test preparation course", y="writing score", x= 'race/ethnicity',data=df)

plt.show()


# In[61]:


#   Highest number of Students who belongs to Group E has completed the test preperation course in Math and Reading and scored highest.
#   Highest number of Students who belongs to Group D and E has completed the test preperation course in Writing and scored highest.


# In[72]:


#  Number of Girl Students Scoring 90 in all the Subjects
df[(df['gender'] == 'female') &
     (df['math score'] > 90) & 
     (df['writing score'] > 90) &
     (df['reading score'] > 90)]


# In[73]:


#  Number of Boy Students Scoring 90 in all the Subjects
df[(df['gender'] == 'male') &
     (df['math score'] > 90) & 
     (df['writing score'] > 90) &
     (df['reading score'] > 90)]


# In[84]:


#   scores secured by Boys and Girls

df.groupby(['gender']).agg(['min','median','max'])


# In[82]:


#   Effect of Lunch on Student's Performnce

df[['lunch','gender','math score','writing score','reading score']].groupby(['lunch','gender']).agg('median')


# In[81]:


#  Effect of Test Preparation Course on Scores
df[['test preparation course',
      'gender',
      'math score',
      'writing score',
      'reading score']].groupby(['test preparation course','gender']).agg('median')


# In[ ]:


# Hence,this is all about student performance analysis.
#   Akhil Bhall

