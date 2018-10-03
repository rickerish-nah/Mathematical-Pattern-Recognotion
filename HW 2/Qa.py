import numpy as np
import matplotlib
import math
import plotDecBoundaries as pB


given_Data_TRAIN1 = np.genfromtxt("synthetic1_train.csv", delimiter=',')
given_Data_TEST1 = np.genfromtxt("synthetic1_test.csv", delimiter=',')
given_Data_TRAIN2 = np.genfromtxt("synthetic2_train.csv", delimiter=',')
given_Data_TEST2 = np.genfromtxt("synthetic2_test.csv", delimiter=',')
class_Feature_Average_TRAIN1=np.zeros((2,2))
class_Feature_Average_TRAIN2=np.zeros((2,2))
collen_TRAIN1=len(given_Data_TRAIN1)
collen_TRAIN2=len(given_Data_TRAIN2) 
collen_TEST1=len(given_Data_TEST1)
collen_TEST2=len(given_Data_TEST2)
collen=0
error_Rate_TRAIN1=0
error_Rate_TEST1=0
dist_1_TRAIN1=0
dist_2_TRAIN1=0
dist_1_TEST1=0
dist_2_TEST1=0
error_Rate_TRAIN2=0
error_Rate_TEST2=0
dist_1_TRAIN2=0
dist_2_TRAIN2=0
dist_1_TEST2=0
dist_2_TEST2=0
train_1_CLASS1_length=0
train_1_CLASS2_length=0
train_2_CLASS1_length=0
train_2_CLASS2_length=0


for i in range(0,collen_TRAIN1):
	if(given_Data_TRAIN1[i][2] ==1):
		train_1_CLASS1_length+=1
	elif(given_Data_TRAIN1[i][2]==2):
		train_1_CLASS2_length+=1
for i in range(0,collen_TRAIN2):
	if(given_Data_TRAIN2[i][2] ==1):
		train_2_CLASS1_length+=1
	elif(given_Data_TRAIN2[i][2]==2):
		train_2_CLASS2_length+=1
	
#print"\tT1:",;print(train_1_CLASS1_length),;print"\tT2:",;print(train_1_CLASS2_length),;print"\tT1:",;print(train_2_CLASS1_length),;print"\tT2:",;print(train_2_CLASS1_length)


for i in range(0,collen_TRAIN1):
	if(i<train_1_CLASS1_length):
		class_Feature_Average_TRAIN1[0][0]+=given_Data_TRAIN1[i][0]/(train_1_CLASS1_length)  #MEAN OF FEATURE 1 OF CLASS 1(TRAIN)
		class_Feature_Average_TRAIN1[0][1]+=given_Data_TRAIN1[i][1]/(train_1_CLASS1_length)  #MEAN OF FEATURE 2 OF CLASS 1(TRAIN)
	if(i>=train_1_CLASS1_length and i<(train_1_CLASS1_length+train_1_CLASS2_length)):
		class_Feature_Average_TRAIN1[1][0]+=given_Data_TRAIN1[i][0]/(train_1_CLASS2_length)  #MEAN OF FEATURE 1 OF CLASS 2(TRAIN)
		class_Feature_Average_TRAIN1[1][1]+=given_Data_TRAIN1[i][1]/(train_1_CLASS2_length)  #MEAN OF FEATURE 2 OF CLASS 2(TRAIN)
	if(i<train_2_CLASS1_length):
	 	class_Feature_Average_TRAIN2[0][0]+=given_Data_TRAIN2[i][0]/(train_2_CLASS1_length)  #MEAN OF FEATURE 1 OF CLASS 1(TRAIN)
		class_Feature_Average_TRAIN2[0][1]+=given_Data_TRAIN2[i][1]/(train_2_CLASS1_length)  #MEAN OF FEATURE 2 OF CLASS 1(TRAIN)
	if(i>=train_2_CLASS1_length and i<(train_2_CLASS1_length+train_2_CLASS2_length)):
		class_Feature_Average_TRAIN2[1][0]+=given_Data_TRAIN2[i][0]/(train_2_CLASS2_length)  #MEAN OF FEATURE 1 OF CLASS 2(TRAIN)
		class_Feature_Average_TRAIN2[1][1]+=given_Data_TRAIN2[i][1]/(train_2_CLASS2_length)  #MEAN OF FEATURE 2 OF CLASS 2(TRAIN)
	i+=1


for i in range(0,collen_TRAIN1):# all lengths are same
	dist_1_TRAIN1=math.sqrt(((given_Data_TRAIN1[i][0]-class_Feature_Average_TRAIN1[0][0])**2)+((given_Data_TRAIN1[i][1]-class_Feature_Average_TRAIN1[0][1])**2))
	dist_2_TRAIN1=math.sqrt(((given_Data_TRAIN1[i][0]-class_Feature_Average_TRAIN1[1][0])**2)+((given_Data_TRAIN1[i][1]-class_Feature_Average_TRAIN1[1][1])**2))

	dist_1_TEST1=math.sqrt(((given_Data_TEST1[i][0]-class_Feature_Average_TRAIN1[0][0])**2)+((given_Data_TEST1[i][1]-class_Feature_Average_TRAIN1[0][1])**2))
	dist_2_TEST1=math.sqrt(((given_Data_TEST1[i][0]-class_Feature_Average_TRAIN1[1][0])**2)+((given_Data_TEST1[i][1]-class_Feature_Average_TRAIN1[1][1])**2))

	dist_1_TRAIN2=math.sqrt(((given_Data_TRAIN2[i][0]-class_Feature_Average_TRAIN2[0][0])**2)+((given_Data_TRAIN2[i][1]-class_Feature_Average_TRAIN2[0][1])**2))
	dist_2_TRAIN2=math.sqrt(((given_Data_TRAIN2[i][0]-class_Feature_Average_TRAIN2[1][0])**2)+((given_Data_TRAIN2[i][1]-class_Feature_Average_TRAIN2[1][1])**2))

	dist_1_TEST2=math.sqrt(((given_Data_TEST2[i][0]-class_Feature_Average_TRAIN2[0][0])**2)+((given_Data_TEST2[i][1]-class_Feature_Average_TRAIN2[0][1])**2))
	dist_2_TEST2=math.sqrt(((given_Data_TEST2[i][0]-class_Feature_Average_TRAIN2[1][0])**2)+((given_Data_TEST2[i][1]-class_Feature_Average_TRAIN2[1][1])**2))
	#For Train_1
	if dist_1_TRAIN1<dist_2_TRAIN1:
		if given_Data_TRAIN1[i][2]!=1:
			error_Rate_TRAIN1+=1
	else :
		if given_Data_TRAIN1[i][2]!=2:
			error_Rate_TRAIN1+=1
	
	#For Test_1
	if dist_1_TEST1<dist_2_TEST1:
		if given_Data_TEST1[i][2]!=1:
			error_Rate_TEST1+=1
	else :
		if given_Data_TEST1[i][2]!=2:
			error_Rate_TEST1+=1
	#For Train_2
	if dist_1_TRAIN2<dist_2_TRAIN2:
		if given_Data_TRAIN2[i][2]!=1:
			error_Rate_TRAIN2+=1
	else :
		if given_Data_TRAIN2[i][2]!=2:
			error_Rate_TRAIN2+=1

	#For Test_2
	if dist_1_TEST2<dist_2_TEST2:
		if given_Data_TEST2[i][2]!=1:
			error_Rate_TEST2+=1
	else :
		if given_Data_TEST2[i][2]!=2:
			error_Rate_TEST2+=1
	#print"i:",;print(i),;print"\tDistance 1:",;print(dist_1_TEST2),;print"\t Distance_2:",;print(dist_2_TEST2),;print"\t error_Rate_TEST2:",;print(error_Rate_TEST2)
	#print"i:",;print(i),;print"\tDistance 1:",;print(dist_1_TRAIN2),;print"\t Distance_2:",;print(dist_2_TRAIN2),;print"\t error_Rate_TEST2:",;print(error_Rate_TRAIN2)
	i+=1


print"Mean Values for Train 1:"
print(class_Feature_Average_TRAIN1)
print"\n\nMean Values for Train 2:"
print(class_Feature_Average_TRAIN2)
print"\n\nError_Rate of Train 1:",;print(error_Rate_TRAIN1)
print"Error_Rate of Test 1:",;print(error_Rate_TEST1)
print"Error_Rate of Train 2:",;print(error_Rate_TRAIN2)
print"Error_Rate of TEST 2:",;print(error_Rate_TEST2)
print"Error_Rate Ratio of Train 1:",;print(error_Rate_TRAIN1),;print"/",;print(collen_TRAIN1)
print"Error_Rate Ratio of Test 1:",;print(error_Rate_TEST1),;print"/",;print(collen_TEST1)
print"Error_Rate Ratio of Train 2:",;print(error_Rate_TRAIN2),;print"/",;print(collen_TRAIN2)
print"Error_Rate Ratio of Test 2:",;print(error_Rate_TEST2),;print"/",;print(collen_TEST2)

#pB.plotDecBoundary(given_Data_TRAIN1[:,0:2],given_Data_TRAIN1[:,2],class_Feature_Average_TRAIN1)

pB.plotDecBoundary(given_Data_TRAIN2[:,0:2],given_Data_TRAIN2[:,2],class_Feature_Average_TRAIN2)

