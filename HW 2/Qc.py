import numpy as np
import matplotlib
import math
import plotDecBoundaries as pB


given_Data_TRAIN1 = np.genfromtxt("wine_train.csv", delimiter=',')
given_Data_TEST1 = np.genfromtxt("wine_test.csv", delimiter=',')

class_Feature_Average_TRAIN1=np.zeros((3,2))


collen_TRAIN1=len(given_Data_TRAIN1)

collen_TEST1=len(given_Data_TEST1)
train_DATA=np.zeros((collen_TRAIN1))
collen=0
error_Rate_TRAIN1=0
error_Rate_TEST1=0
dist_1_TRAIN1=0
dist_2_TRAIN1=0
dist_1_TEST1=0
dist_2_TEST1=0

train_1_CLASS1_length=0
train_1_CLASS2_length=0
train_1_CLASS3_length=0


for i in range(0,collen_TRAIN1):
	if(given_Data_TRAIN1[i][13] ==1):
		train_1_CLASS1_length+=1
	if(given_Data_TRAIN1[i][13]==2):
		train_1_CLASS2_length+=1
	if(given_Data_TRAIN1[i][13] ==3):
		train_1_CLASS3_length+=1
	
	
print"\tT1:",;print(train_1_CLASS1_length),;print"\tT2:",;print(train_1_CLASS2_length),;print"\tT3:",;print(train_1_CLASS3_length)


for k in range(0,collen_TRAIN1): #Calculating Mean Value
	if k<train_1_CLASS1_length:		
		class_Feature_Average_TRAIN1[0][0]+=given_Data_TRAIN1[k][0]/(train_1_CLASS1_length)  #MEAN OF FEATURE 1 OF CLASS 1(TRAIN)
		class_Feature_Average_TRAIN1[0][1]+=given_Data_TRAIN1[k][1]/(train_1_CLASS1_length)  #MEAN OF FEATURE 2 OF CLASS 1(TRAIN)
	if k>=train_1_CLASS1_length and k<(train_1_CLASS2_length+train_1_CLASS1_length):
		class_Feature_Average_TRAIN1[1][0]+=given_Data_TRAIN1[k][0]/(train_1_CLASS2_length)	
		class_Feature_Average_TRAIN1[1][1]+=given_Data_TRAIN1[k][1]/(train_1_CLASS2_length)  
	if k>=(train_1_CLASS1_length+train_1_CLASS2_length): #and k<collen_TRAIN1:
		class_Feature_Average_TRAIN1[2][0]+=given_Data_TRAIN1[k][0]/(train_1_CLASS3_length)  
		class_Feature_Average_TRAIN1[2][1]+=given_Data_TRAIN1[k][1]/(train_1_CLASS3_length)
	k+=1
error_RATE_TRAIN=0
dist_1_TRAIN=0
dist_2_TRAIN=0
dist_3_TRAIN=0
error_RATE_TEST=0
dist_1_TEST=0
dist_2_TEST=0
dist_3_TEST=0
for k in range(0,collen_TRAIN1):
	dist_1_TRAIN=math.sqrt(((given_Data_TRAIN1[k][0]-class_Feature_Average_TRAIN1[0][0])**2)+((given_Data_TRAIN1[k][1]-class_Feature_Average_TRAIN1[0][1])**2))
	dist_2_TRAIN=math.sqrt(((given_Data_TRAIN1[k][0]-class_Feature_Average_TRAIN1[1][0])**2)+((given_Data_TRAIN1[k][1]-class_Feature_Average_TRAIN1[1][1])**2))
	dist_3_TRAIN=math.sqrt(((given_Data_TRAIN1[k][0]-class_Feature_Average_TRAIN1[2][0])**2)+((given_Data_TRAIN1[k][1]-class_Feature_Average_TRAIN1[2][1])**2))
	dist_1_TEST=math.sqrt(((given_Data_TEST1[k][0]-class_Feature_Average_TRAIN1[0][0])**2)+((given_Data_TEST1[k][1]-class_Feature_Average_TRAIN1[0][1])**2))
	dist_2_TEST=math.sqrt(((given_Data_TEST1[k][0]-class_Feature_Average_TRAIN1[1][0])**2)+((given_Data_TEST1[k][1]-class_Feature_Average_TRAIN1[1][1])**2))
	dist_3_TEST=math.sqrt(((given_Data_TEST1[k][0]-class_Feature_Average_TRAIN1[2][0])**2)+((given_Data_TEST1[k][1]-class_Feature_Average_TRAIN1[2][1])**2))
					
	#TRAIN
	if dist_1_TRAIN<dist_2_TRAIN and dist_1_TRAIN<dist_3_TRAIN :
		if given_Data_TRAIN1[k][13]!=1:
			error_RATE_TRAIN+=1
	elif dist_2_TRAIN<dist_1_TRAIN and dist_2_TRAIN<dist_3_TRAIN : 
		if given_Data_TRAIN1[k][13]!=2:
			error_RATE_TRAIN+=1
	elif dist_3_TRAIN<dist_1_TRAIN and dist_3_TRAIN<dist_2_TRAIN : 
		if given_Data_TRAIN1[k][13]!=3:
			error_RATE_TRAIN+=1	
	
	#TEST
	if dist_1_TEST<dist_2_TEST and dist_1_TEST<dist_3_TEST :
		if given_Data_TEST1[k][13]!=1:
			error_RATE_TEST+=1
	elif dist_2_TEST<dist_1_TEST and dist_2_TEST<dist_3_TEST : 
		if given_Data_TEST1[k][13]!=2:
			error_RATE_TEST+=1
	elif dist_3_TEST<dist_1_TEST and dist_3_TEST<dist_2_TEST : 
		if given_Data_TEST1[k][13]!=3:
			error_RATE_TEST+=1		
	k+=1
'''for k in range(0,collen_TRAIN1):
	train_DATA[k][0]=given_Data_TRAIN1[k][0]
	train_DATA[k][1]=given_Data_TRAIN1[k][1]'''


print"Mean Values for Train 1:"
print(class_Feature_Average_TRAIN1)

print"\n\nError_Rate of Train 1:",;print(error_RATE_TRAIN)
print"Error_Rate of Test 1:",;print(error_RATE_TEST)

print"Error_Rate Ratio of Train 1:",;print(error_RATE_TRAIN),;print"/",;print(collen_TRAIN1)
print"Error_Rate Ratio of Test 1:",;print(error_RATE_TEST),;print"/",;print(collen_TEST1)


pB.plotDecBoundary(given_Data_TRAIN1[:,0:2],given_Data_TRAIN1[:,13],class_Feature_Average_TRAIN1)


