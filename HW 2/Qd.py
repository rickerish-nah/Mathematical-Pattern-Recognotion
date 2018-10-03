import numpy as np
import matplotlib
import math
import plotDecBoundaries as pB


given_Data_TRAIN1 = np.genfromtxt("wine_train.csv", delimiter=',')
given_Data_TEST1 = np.genfromtxt("wine_test.csv", delimiter=',')
collen_TRAIN1=len(given_Data_TRAIN1)
collen_TEST1=len(given_Data_TEST1)
train_DATA=np.zeros((collen_TRAIN1,2))
label_TRAIN=np.zeros(collen_TRAIN1)
avg=np.zeros((3,2))
min_err_TRAIN=100
test_err=0
memory_TRAIN=np.zeros(2)
col_length_1=0
col_length_2=0
col_length_3=0


for i in range(0,collen_TRAIN1):
	if(given_Data_TRAIN1[i][13] ==1):
		col_length_1+=1
	elif(given_Data_TRAIN1[i][13]==2):
		col_length_2+=1
	elif(given_Data_TRAIN1[i][13]==3):
		col_length_3+=1

#print(col_length_1),;print"\t",;print(col_length_2),;print"\t",;print(col_length_3),;print"\t",;print(col_length_1+col_length_2+col_length_3)

for i in range(0,13):
	for j in range(i+1,13): #nCr comination loop
		#print"i:",;print(i),;print"j:",;print(j)
		class_Feature_Average_TRAIN1=np.zeros((3,2))
		#l1=0
		#l2=0
		#l3=0
		for k in range(0,collen_TRAIN1): #Calculating Mean Value
			if k<col_length_1:
				#l1+=1
				class_Feature_Average_TRAIN1[0][0]+=given_Data_TRAIN1[k][i]/(col_length_1)  #MEAN OF FEATURE 1 OF CLASS 1(TRAIN)
				class_Feature_Average_TRAIN1[0][1]+=given_Data_TRAIN1[k][j]/(col_length_1)  #MEAN OF FEATURE 2 OF CLASS 1(TRAIN)
			if k>=col_length_1 and k<(col_length_2+col_length_1):
				#print"Hey Class 2"
				#l2+=1
				class_Feature_Average_TRAIN1[1][0]+=given_Data_TRAIN1[k][i]/(col_length_2)	
				class_Feature_Average_TRAIN1[1][1]+=given_Data_TRAIN1[k][j]/(col_length_2)  
			if k>=(col_length_1+col_length_2): #and k<collen_TRAIN1:
				#print(k)
				#l3+=1
				class_Feature_Average_TRAIN1[2][0]+=given_Data_TRAIN1[k][i]/(col_length_3)  
				class_Feature_Average_TRAIN1[2][1]+=given_Data_TRAIN1[k][j]/(col_length_3)
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
			dist_1_TRAIN=math.sqrt(((given_Data_TRAIN1[k][i]-class_Feature_Average_TRAIN1[0][0])**2)+((given_Data_TRAIN1[k][j]-class_Feature_Average_TRAIN1[0][1])**2))
			dist_2_TRAIN=math.sqrt(((given_Data_TRAIN1[k][i]-class_Feature_Average_TRAIN1[1][0])**2)+((given_Data_TRAIN1[k][j]-class_Feature_Average_TRAIN1[1][1])**2))
			dist_3_TRAIN=math.sqrt(((given_Data_TRAIN1[k][i]-class_Feature_Average_TRAIN1[2][0])**2)+((given_Data_TRAIN1[k][j]-class_Feature_Average_TRAIN1[2][1])**2))
			
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
			k+=1
		if min_err_TRAIN>=error_RATE_TRAIN:
			min_err_TRAIN=error_RATE_TRAIN
			memory_TRAIN[0]=i
			memory_TRAIN[1]=j
			avg[0][0]=class_Feature_Average_TRAIN1[0][0]
			avg[0][1]=class_Feature_Average_TRAIN1[0][1]
			avg[1][0]=class_Feature_Average_TRAIN1[1][0]
			avg[1][1]=class_Feature_Average_TRAIN1[1][1]
			avg[2][0]=class_Feature_Average_TRAIN1[2][0]
			avg[2][1]=class_Feature_Average_TRAIN1[2][1]
		for k in range(0,collen_TEST1): #Test Error Calculation
			dist_1_TEST=math.sqrt(((given_Data_TEST1[k][i]-class_Feature_Average_TRAIN1[0][0])**2)+((given_Data_TEST1[k][j]-class_Feature_Average_TRAIN1[0][1])**2))
			dist_2_TEST=math.sqrt(((given_Data_TEST1[k][i]-class_Feature_Average_TRAIN1[1][0])**2)+((given_Data_TEST1[k][j]-class_Feature_Average_TRAIN1[1][1])**2))
			dist_3_TEST=math.sqrt(((given_Data_TEST1[k][i]-class_Feature_Average_TRAIN1[2][0])**2)+((given_Data_TEST1[k][j]-class_Feature_Average_TRAIN1[2][1])**2))
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
		if(i==memory_TRAIN[0]):
			if(j==memory_TRAIN[1]):
				test_err=error_RATE_TEST

		print"The Error_Rate for the pair(TRAIN) (",;print(i),;print",",;print(j),;print") is: ",;print(error_RATE_TRAIN),;print"\tThe Error_Rate for the pair(TEST) (",;print(i),;print",",;print(j),;print") is: ",;print(error_RATE_TEST)
		#print"The Error_Rate for the pair(TEST) (",;print(i),;print",",;print(j),;print") is: ",;print(error_RATE_TEST)

		j+=1
	i+=1

for k in range(0,collen_TRAIN1):
	train_DATA[k][0]=given_Data_TRAIN1[k][memory_TRAIN[0]]
	train_DATA[k][1]=given_Data_TRAIN1[k][memory_TRAIN[1]]
	label_TRAIN[k]=given_Data_TRAIN1[k][13]
	avg
	label_TRAIN


print"\n\n\nThe Min Error_Rate for the TRAINING pair (",;print(memory_TRAIN[0]),;print",",;print(memory_TRAIN[1]),;print") is: ",;print(min_err_TRAIN)
print"The Error_Rate for the corresponding TEST pair (",;print(memory_TRAIN[0]),;print",",;print(memory_TRAIN[1]),;print") is: ",;print(test_err)
pB.plotDecBoundary(train_DATA[:,0:2],label_TRAIN[:],avg[:,:])

			


		

