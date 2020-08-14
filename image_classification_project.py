# -*- coding: utf-8 -*-
"""Image_Classification_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I4_gCo_EoHcoJib6Y81PvLx6Qtm7WMrB
"""

# Commented out IPython magic to ensure Python compatibility.
#IMPORTING DEPENDENCIES

import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# %matplotlib inline

from google.colab import drive
drive.mount('/content/gdrive')

url='https://raw.githubusercontent.com/rimchoudhury/ML_Projects/master/mnist_test.csv'

#using pandas to read the database stored in github
data= pd.read_csv(url)

#Viewing column heads
data.head()

#Extracting data from the data-set and vieing them up-close
data.iloc[3,1:].values

a=data.iloc[3,1:].values

# reshaping the extracted data into a reasonable size
a=a.reshape(28,28).astype('uint8')
plt.imshow(a)

#Preparing the data
# Separating labels and Data-values

df_x= data.iloc[:,1:]
df_y = data.iloc[:,0]

# Creating test and train sizes/batches
x_train,x_test,y_train,y_test = train_test_split(df_x,df_y,test_size=0.2,random_state=4)

# Check Data
x_train.head()

# Check Data
y_train.head()

# Calling Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100)

# Fit the Model
rf.fit(x_train,y_train)

#rediction on Test Data
pred = rf.predict(x_test)

pred

# Check Prediction Accuracy
s = y_test.values

# Calculate no. of correctly predicted values
count=0
for i in range(len(pred)):
  if pred[i] == s[i]:
    count=count+1

count

# Total values that the Prediction code was run on
len(pred)

# Accuracy % value 
(count/len(pred))*100