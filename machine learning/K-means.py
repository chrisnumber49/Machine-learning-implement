get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iris = datasets.load_iris()		#create sample (unclassified)
iris_data  = np.array(iris.data) 
iris_target= np.full((60,1), -1) 
print(iris_data.ndim)
print(iris_data.shape)
print(iris_target.ndim)
print(iris_target.shape)
ref0=np.array(iris_data[0:20])
ref1=np.array(iris_data[50:70])
ref2=np.array(iris_data[100:120])
ref=np.row_stack((ref0,ref1,ref2))
print(ref.shape)
Alliris_Data = np.column_stack((ref,iris_target))

#bad distribution		#randomly assign initial cluster centers
#classify_S_length = np.random.uniform(4.3,7.9,(3,1))
#classify_S_width = np.random.uniform(2,4,(3,1)) 
#classify_P_length = np.random.uniform(0.1,2.5,(3,1)) 
#classify_P_width = np.random.uniform(0.1,2.5,(3,1)) 
#classify_target = np.array([0,1,2])
#classify_target = classify_target[:, np.newaxis]
#classify_Data = np.column_stack((classify_S_length,classify_S_width,classify_P_length,classify_P_width,classify_target))
#classify_Data

#fair distribution		#assign initial cluster centers
classify0=np.array(iris_data[75])
classify1=np.array(iris_data[125])  #1,2,0
classify2=np.array(iris_data[25])   #0,1,2
classify=np.row_stack((classify0,classify1,classify2))
classify_target = np.array([0,1,2])
classify_target = classify_target[:, np.newaxis]
classify=np.column_stack((classify,classify_target))
classify

def distance(a,b):		#calculate the distance to each cluster center
    x0=a[0]
    x1=a[1]
    x2=a[2]
    x3=a[3]
    res=np.array([])
    for i in range(0,3):
        
        y0=b[i][0]
        y1=b[i][1]
        y2=b[i][2]
        y3=b[i][3]    
        res = np.append(res, np.sqrt( np.square(x0-y0) + np.square(x1-y1) + np.square(x2-y2) + np.square(x3-y3)  )  )
    return res
	
def Bubble(A):		#Ascending sort
    B=np.array(A)
    B_size=B.size
    for i in range (0,B_size):
        for j in range (i+1,B_size):
            if(B[i]>B[j]):
                temp=B[i]
                B[i]=B[j]
                B[j]=temp 
    return B
	
def find_closest_number(D1,D2):		#find the closest cluster 
    D2_len=D2.size
    for i in range (0,D2_len):
        if(D1[0]==D2[i]):
             res = i
    return res
	
def recalculate(a,b):		#recalculate the cluster center
    x=np.array(a)
    y=np.array(b)
    recal=np.array([])
    for i in range(0,4):
        tem=(x[i]+y[i])/2
        recal=np.append(recal,tem)
    return recal
	
for i in range(0,60):		
    Dist=np.array(distance(Alliris_Data[i],classify)) 
    Dist_Oped=np.array(Bubble(Dist))
    num=find_closest_number(Dist_Oped,Dist)
    Alliris_Data[i][4]=num #
    
    newclassify=np.array(recalculate(Alliris_Data[i],classify[num])) 
    for j in range(0,4):
        classify[num][j]=newclassify[j]
print(Alliris_Data)
print(classify)
