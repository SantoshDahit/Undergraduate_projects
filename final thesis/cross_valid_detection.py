# -*- coding: utf-8 -*-
"""Cross_VALID_Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S1AexSl7znkQXGqdsyJHqorXxOjjNdpO
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('kddcup99_csv.csv1')

x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
df

df.describe()

df['label'].value_counts()

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# extract numerical attributes and scale it to have zero mean and unit variance  
cols = df.select_dtypes(include=['float64','int64']).columns
sc_df = scaler.fit_transform(df.select_dtypes(include=['float64','int64']))


# turn the result back to a dataframe
sc_df1 = pd.DataFrame(sc_df, columns = cols)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

# extract categorical attributes from both training and test sets 
catdf1 = df.select_dtypes(include=['object']).copy()


# encode the categorical attributes
dfcat = catdf1.apply(encoder.fit_transform)


# separate target column from encoded data 
encdf = dfcat.drop(['label'], axis=1)
cat_ydf = dfcat[['label']].copy()

train_x1= pd.concat([sc_df1,encdf],axis=1)
train_y = cat_ydf
train_x = train_x1
train_x.shape

train_y.shape



df.dropna(inplace=True,axis=1)

df

## k-fold cross validation demonstration by scikit-learn library
from numpy import array
from sklearn.model_selection import KFold

kf = KFold(n_splits = 5, shuffle=True)

for i in range(5):
  result = next(kf.split(df),None)
  x_train = train_x.iloc[result[0]]
  x_test = train_x.iloc[result[1]]
  y_train = train_y.iloc[result[0]]
  y_test = train_y.iloc[result[1]]

x_test

y_test

y_train

x_train

x_test.shape,x_train.shape

y_test.shape, y_train.shape

from sklearn import metrics
import time
from sklearn.ensemble import RandomForestClassifier
rfe = RandomForestClassifier();
start_time = time.time() 
rfe =rfe.fit(x_train, y_train)
end_time = time.time() 
print("RF_Training time: ", end_time-start_time)

start_time = time.time() 
y_test_pred1 = rfe.predict(x_train) 
end_time = time.time() 
print("RF_Testing time: ", end_time-start_time)

#RFE
from sklearn import metrics
y_pred1 = rfe.predict(x_test)

from sklearn.metrics import precision_score, f1_score, recall_score, classification_report,accuracy_score
print ("RFE_Accuracy:", accuracy_score(y_test,y_pred1 ))
print ("RFE_F1 score:", f1_score(y_test, y_pred1, average='weighted'))
print ("RFE_Recall:", recall_score(y_test, y_pred1, average='weighted'))
print ("RFE_Precision:", precision_score(y_test, y_pred1, average='weighted'))
print ("RFE_clasification:",classification_report(y_test, y_pred1))

from sklearn import metrics
from sklearn.linear_model import LogisticRegression
LGR_Classifier = LogisticRegression(n_jobs=-1, random_state=0)
start_time = time.time() 
LGR_Classifier.fit(x_train, y_train);
end_time = time.time() 
print("LGR_Classifier_Training time: ", end_time-start_time)
start_time = time.time() 
y_test_pred2 = LGR_Classifier.predict(x_train) 
end_time = time.time() 
print("LGR_Classifier_Testing time: ", end_time-start_time)

#LGR_Classifier
from sklearn import metrics
y_pred2 = LGR_Classifier.predict(x_test)

from sklearn.metrics import precision_score, f1_score, recall_score, classification_report,accuracy_score
print ("LGR_Classifier_Accuracy:", accuracy_score(y_test,y_pred2 ))
print ("LGR_Classifier_F1 score:", f1_score(y_test, y_pred2, average='weighted'))
print ("LGR_Classifier_Recall:", recall_score(y_test, y_pred2, average='weighted'))
print ("LGR_Classifier_Precision:", precision_score(y_test, y_pred2, average='weighted'))
print ("LGR_Classifierr_clasification:",classification_report(y_test, y_pred2))

from sklearn import metrics
from sklearn import svm
import time
#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel
start_time = time.time() 
#Train the model using the training sets
clf.fit(x_train, y_train)
end_time = time.time() 
print("SVM_Training time: ", end_time-start_time)

start_time = time.time() 
y_test_pred = clf.predict(x_train) 
end_time = time.time() 
print("SVM_Testing time: ", end_time-start_time)

from sklearn import metrics
y_pred = clf.predict(x_test)

from sklearn.metrics import precision_score, f1_score, recall_score, classification_report, accuracy_score
print ("SVM_Accuracy:", accuracy_score(y_test,y_pred))
print ("SVM_F1 score:", f1_score(y_test, y_pred, average='weighted'))
print ("SVM_Recall:", recall_score(y_test, y_pred, average='weighted'))
print ("SVM_Precision:", precision_score(y_test, y_pred, average='weighted'))
print ("SVM_clasification:",classification_report(y_test, y_pred))