#########################################
#     Harikrishna Prabhu               ##
#     3333077042                       ##
#########################################
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random
import math

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier


op=input("Enter the option for # feature:\n 1.first 2 or\n 2.13(all)\n")

#################################################################################.     data initialization
##Training data
X_TRAIN=np.genfromtxt("wine_train.csv", delimiter=',')
class_Label_train=X_TRAIN[:,13]
if(op==1):
	given_Data_TRAIN=X_TRAIN[:,0:2]
else:
	given_Data_TRAIN=X_TRAIN[:,0:13]

##Test Data
X_TEST=np.genfromtxt("wine_test.csv", delimiter=',')
class_Label_test=X_TEST[:,13]
if(op==1):
	given_Data_TEST=X_TEST[:,0:2]
else:
	given_Data_TEST=X_TEST[:,0:13]

#standardize data
scaler = StandardScaler() #initializes a StandardScaler object
scaler.fit(given_Data_TRAIN) # (x-mu)/sigma

#Standardizing Train and Test Data
given_Data_TRAIN_std = scaler.transform(given_Data_TRAIN)
given_Data_TEST_std = scaler.transform(given_Data_TEST)

 ######
po=input("Want to check (1)non-normalized data or (2)Normalized data \n ")
if(po==1):
 	binary_model = LinearRegression()
 	#model = LinearRegression()
 	model = OneVsRestClassifier(binary_model)
	model.fit(given_Data_TRAIN,class_Label_train)
	test_pred=model.predict(given_Data_TEST)
	train_pred=model.predict(given_Data_TRAIN)
else:
	binary_model = LinearRegression()
	model = OneVsRestClassifier(binary_model)
	model.fit(given_Data_TRAIN_std,class_Label_train)
	test_pred=model.predict(given_Data_TEST_std)
	train_pred=model.predict(given_Data_TRAIN_std)


#print(test_pred)
'''
length=len(test_pred)
print(length)
test_pred_bin=np.zeros(length)
for i in range(0,length):
	test_pred_bin[i]=round(test_pred[i])
print(test_pred_bin)
'''
accuracy_test=accuracy_score(class_Label_test,test_pred)*100
print("TEST accuracy:"),;print(accuracy_test),;print("%")

accuracy_train=accuracy_score(class_Label_train,train_pred)*100
print("TRAIN accuracy:"),;print(accuracy_train),;print("%")





