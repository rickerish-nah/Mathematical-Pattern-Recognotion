import numpy as np
import matplotlib
import math
import plotDecBoundaries as pB



given_Data_TRAIN1 = np.genfromtxt("wine_train.csv", delimiter=',')


collen_TRAIN1=len(given_Data_TRAIN1)
class_Feature_Average_TRAIN1=np.zeros((3,2))

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
print(col_length_1),;print"\t",;print(col_length_2),;print"\t",;print(col_length_3),;print"\t",;print(col_length_1+col_length_2+col_length_3)
for k in range(0,collen_TRAIN1): #Calculating Mean Value
	if k<col_length_1:
		#l1+=1
		class_Feature_Average_TRAIN1[0][0]+=given_Data_TRAIN1[k][0]/(col_length_1)  #MEAN OF FEATURE 1 OF CLASS 1(TRAIN)
		class_Feature_Average_TRAIN1[0][1]+=given_Data_TRAIN1[k][11]/(col_length_1)  #MEAN OF FEATURE 2 OF CLASS 1(TRAIN)
	if k>=col_length_1 and k<(col_length_2+col_length_1):
		#print"Hey Class 2"
		#l2+=1
		class_Feature_Average_TRAIN1[1][0]+=given_Data_TRAIN1[k][0]/(col_length_2)	
		class_Feature_Average_TRAIN1[1][1]+=given_Data_TRAIN1[k][11]/(col_length_2)  
	if k>=(col_length_1+col_length_2): #and k<collen_TRAIN1:
		#print(k)
		#l3+=1
		class_Feature_Average_TRAIN1[2][0]+=given_Data_TRAIN1[k][0]/(col_length_3)  
		class_Feature_Average_TRAIN1[2][1]+=given_Data_TRAIN1[k][11]/(col_length_3)
	k+=1
print(class_Feature_Average_TRAIN1)
error_RATE=0
dist_1=0
dist_2=0
dist_3=0
for k in range(0,collen_TRAIN1):
	dist_1=math.sqrt(((given_Data_TRAIN1[k][0]-class_Feature_Average_TRAIN1[0][0])**2)+((given_Data_TRAIN1[k][1]-class_Feature_Average_TRAIN1[0][1])**2))
	dist_2=math.sqrt(((given_Data_TRAIN1[k][0]-class_Feature_Average_TRAIN1[1][0])**2)+((given_Data_TRAIN1[k][1]-class_Feature_Average_TRAIN1[1][1])**2))
	dist_3=math.sqrt(((given_Data_TRAIN1[k][0]-class_Feature_Average_TRAIN1[2][0])**2)+((given_Data_TRAIN1[k][1]-class_Feature_Average_TRAIN1[2][1])**2))
	if dist_1<dist_2 and dist_1<dist_3 :
		if given_Data_TRAIN1[k][13]!=1:
			error_RATE+=1
	elif dist_2<dist_1 and dist_2<dist_3 : 
		if given_Data_TRAIN1[k][13]!=2:
			error_RATE+=1
	elif dist_3<dist_1 and dist_3<dist_2 : 
		if given_Data_TRAIN1[k][13]!=3:
			error_RATE+=1
	#print'i:',;print(i),;print"D1:",;print(dist_1),;print"D2:",;print(dist_2),;print"D3:",;print(dist_3),;print"Error:",;print(error_RATE)
	k+=1
print"FINAL:  Error:",;print(error_RATE)
'''
collen=collen_TRAIN1
for i in range(0,collen/2):
	class_Feature_Average_TRAIN1[0][0]+=given_Data_TRAIN1[i][0]/(collen/2)  #MEAN OF FEATURE 1 OF CLASS 1(TRAIN)
	class_Feature_Average_TRAIN1[0][1]+=given_Data_TRAIN1[i][1]/(collen/2)  #MEAN OF FEATURE 2 OF CLASS 1(TRAIN)
	


	#class_Feature_Average_TEST1[0][0]+=given_Data_TEST1[i][0]/(collen/2)
	#class_Feature_Average_TEST1[0][1]+=given_Data_TEST1[i][1]/(collen/2)
	class_Feature_Average_TRAIN2[0][0]+=given_Data_TRAIN2[i][0]/(collen/2)  #MEAN OF FEATURE 1 OF CLASS 1(TRAIN)
	class_Feature_Average_TRAIN2[0][1]+=given_Data_TRAIN2[i][1]/(collen/2)  #MEAN OF FEATURE 2 OF CLASS 1(TRAIN)
	#class_Feature_Average_TEST2[0][0]+=given_Data_TEST2[i][0]/(collen/2)
	#class_Feature_Average_TEST2[0][1]+=given_Data_TEST2[i][1]/(collen/2)
	i+=1
for j in range(i,collen):
	class_Feature_Average_TRAIN1[1][0]+=given_Data_TRAIN1[j][0]/(collen/2)  #MEAN OF FEATURE 1 OF CLASS 2(TRAIN)
	class_Feature_Average_TRAIN1[1][1]+=given_Data_TRAIN1[j][1]/(collen/2)  #MEAN OF FEATURE 2 OF CLASS 2(TRAIN)
	#class_Feature_Average_TEST1[1][0]+=given_Data_TEST1[j][0]/(collen/2)
	#class_Feature_Average_TEST1[1][1]+=given_Data_TEST1[j][1]/(collen/2)
	class_Feature_Average_TRAIN2[1][0]+=given_Data_TRAIN2[j][0]/(collen/2)  #MEAN OF FEATURE 1 OF CLASS 2(TRAIN)
	class_Feature_Average_TRAIN2[1][1]+=given_Data_TRAIN2[j][1]/(collen/2)  #MEAN OF FEATURE 2 OF CLASS 2(TRAIN)
	#class_Feature_Average_TEST2[1][0]+=given_Data_TEST2[j][0]/(collen/2)
	#class_Feature_Average_TEST2[1][1]+=given_Data_TEST2[j][1]/(collen/2)
	i+=1

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

for i in range(0,collen):
	dist_1_TRAIN1=math.sqrt(((given_Data_TRAIN1[i][0]-class_Feature_Average_TRAIN1[0][0])**2)+((given_Data_TRAIN1[i][1]-class_Feature_Average_TRAIN1[0][1])**2))
	dist_2_TRAIN1=math.sqrt(((given_Data_TRAIN1[i][0]-class_Feature_Average_TRAIN1[1][0])**2)+((given_Data_TRAIN1[i][1]-class_Feature_Average_TRAIN1[1][1])**2))

	dist_1_TEST1=math.sqrt(((given_Data_TEST1[i][0]-class_Feature_Average_TRAIN1[0][0])**2)+((given_Data_TEST1[i][1]-class_Feature_Average_TRAIN1[0][1])**2))
	dist_2_TEST1=math.sqrt(((given_Data_TEST1[i][0]-class_Feature_Average_TRAIN1[1][0])**2)+((given_Data_TEST1[i][1]-class_Feature_Average_TRAIN1[1][1])**2))

	dist_1_TRAIN2=math.sqrt(((given_Data_TRAIN2[i][0]-class_Feature_Average_TRAIN2[0][0])**2)+((given_Data_TRAIN2[i][1]-class_Feature_Average_TRAIN2[0][1])**2))
	dist_2_TRAIN2=math.sqrt(((given_Data_TRAIN2[i][0]-class_Feature_Average_TRAIN2[1][0])**2)+((given_Data_TRAIN2[i][1]-class_Feature_Average_TRAIN2[1][1])**2))

	dist_1_TEST2=math.sqrt(((given_Data_TEST2[i][0]-class_Feature_Average_TRAIN2[0][0])**2)+((given_Data_TRAIN2[i][1]-class_Feature_Average_TRAIN2[0][1])**2))
	dist_2_TEST2=math.sqrt(((given_Data_TEST2[i][0]-class_Feature_Average_TRAIN2[1][0])**2)+((given_Data_TRAIN2[i][1]-class_Feature_Average_TRAIN2[1][1])**2))

	if dist_1_TRAIN1<dist_2_TRAIN1:
		if given_Data_TRAIN1[i][2]!=1:
			error_Rate_TRAIN1+=1
	else :
		if given_Data_TRAIN1[i][2]!=2:
			error_Rate_TRAIN1+=1
	

	if dist_1_TEST1<dist_2_TEST1:
		if given_Data_TEST1[i][2]!=1:
			error_Rate_TEST1+=1
	else :
		if given_Data_TEST1[i][2]!=2:
			error_Rate_TEST1+=1
	
	#print"Error_Rate of Train 1:",;print(error_Rate_TRAIN1),;print"Error_Rate of Test 1:",;print(error_Rate_TEST1)
	if dist_1_TRAIN2<dist_2_TRAIN2:
		if given_Data_TRAIN2[i][2]!=1:
			error_Rate_TRAIN2+=1
	else :
		if given_Data_TRAIN2[i][2]!=2:
			error_Rate_TRAIN2+=1

	
	if dist_1_TEST2<dist_2_TEST2:
		if given_Data_TEST2[i][2]!=1:
			error_Rate_TEST2+=1
	else :
		if given_Data_TEST2[i][2]!=2:
			error_Rate_TEST2+=1
	#print"Error_Rate of Train 2:",;print(error_Rate_TRAIN2),;print"Error_Rate of Test 2:",;print(error_Rate_TEST2)
	i+=1


print"Error_Rate of Train 1:",;print(error_Rate_TRAIN1)
print"Error_Rate of Test 1:",;print(error_Rate_TEST1)
print"Error_Rate of Train 2:",;print(error_Rate_TRAIN2)
print"Error_Rate of TEST 2:",;print(error_Rate_TEST2)
print(given_Data_TRAIN1[:,2])
pB.plotDecBoundary(given_Data_TRAIN1[:,0:2],given_Data_TRAIN1[:,2],class_Feature_Average_TRAIN1)
#pB.plotDecBoundary(given_Data_TEST1[:,0:2],given_Data_TEST1[:,2],class_Feature_Average_TEST1)
#pB.plotDecBoundary(given_Data_TRAIN2[:,0:2],given_Data_TRAIN2[:,2],class_Feature_Average_TRAIN2)
#pB.plotDecBoundary(given_Data_TEST2[:,0:2],given_Data_TEST2[:,2],class_Feature_Average_TEST2)'''
