get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn import datasets
#from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


iris = datasets.load_iris()

iris_data  = np.array(iris.data) 
iris_target= np.array(iris.target)
#print(iris_data.ndim)
#print(iris_data.shape)
#print(iris_target.ndim)
#print(iris_target.shape)
All_Data = np.column_stack((iris_data,iris_target))
                      
#20 samples for each category, 60 in total
ref0=np.array(All_Data[0:20])
ref1=np.array(All_Data[50:70])
ref2=np.array(All_Data[100:120])
ref=np.row_stack((ref0,ref1,ref2))


#compare the distance between this sample with those 60
def dist(a,b): 
    x0=a[0]
    x1=a[1]
    x2=a[2]
    x3=a[3]
    res=np.array([])
    for i in range(0,60):
        
        y0=b[i][0]
        y1=b[i][1]
        y2=b[i][2]
        y3=b[i][3]    
        res = np.append(res, np.sqrt( np.square(x0-y0) + np.square(x1-y1) + np.square(x2-y2) + np.square(x3-y3)  )  )
    return res


"""def Merge_sort(A):
    
    if(A[0]>A[1]):
        temp = A[1]
        A[1] = A[0]
        A[1] = temp
 
    else:
        A[0] = A[0]
        A[1] = A[1]
        
    arry=np.array([A[0],A[1]])
    return arry        

x = np.array([4444,456,456])
Merge_sort(x)"""


#Ascending sort
def Bubble(A): 
    B=np.array(A)
    B_size=B.size
    for i in range (0,B_size):
        for j in range (i+1,B_size):
            if(B[i]>B[j]):
                temp=B[i]
                B[i]=B[j]
                B[j]=temp

    print (B)  
    return B   


#Find K nearest neighbor
def Linear_Compare(D1,D2,K):
    D2_len=D2.size
    res=np.array([])
    for i in range (0,K):
        for j in range (0,D2_len):
            if(D1[i]==D2[j]):
                res = np.append(res,j)
               # ress=j
    return(res)            


#assign the sample into the category where majority in k nearest neighbor belong to
def Decide_target(Data_No,K):
    Final_Res=np.array([])
    for i in range (0,K):
        #print(int(Data_No[i]))
        x=int(Data_No[i])
        #print (ref[x,4])
        Final_Res=np.append(Final_Res,ref[x,4])
    print(Final_Res)
    
    y=Final_Res.size
    t0=t1=t2=0
    for j in range (0,y):
        if(int(Final_Res[j])==0):
            t0=t0+1
        elif (int(Final_Res[j])==1):
            t1=t1+1
        elif (int(Final_Res[j])==2):
            t2=t2+1
    total=np.array([t0,t1,t2])   
    print('{0} {1}'.format("number in each category:", total))
    
    target=-1
    for p in range (0,3):
        if( target < total[p]):
            target=p
             
    return target    
    
a=np.array([5.9, 3. , 5.1, 1.8  ]) 
print(dist(a,ref))
Dist_Oped=np.array(Bubble(dist(a,ref))) 
Data_No=Linear_Compare(Dist_Oped,dist(a,ref),10)
print(Data_No)
classify=Decide_target(Data_No,10)
print('this sample belongs to class {0:d}'.format(classify))