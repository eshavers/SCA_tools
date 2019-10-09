# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:25:01 2019

@author: eshavers
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.pylab import savefig
######
def cosTheta(x,y):
    return (sum(x*y)/(math.sqrt(sum(np.square(x)))*math.sqrt(sum(np.square(y)))))
######
os.chdir(r'D:\Map_Files_Watershed\NC_data\voxels\voxelTestFolder2\strm_13')
InputPath= (r'D:\Map_Files_Watershed\NC_data\voxels\voxelTestFolder2\strm_13')
######
arr0= np.loadtxt(r'D:\Map_Files_Watershed\NC_data\voxels\voxelTestFolder2\strm_13\strm_13.txt')

brr0= arr0.reshape(((int(len(arr0[:,0])/27)), 27, (np.shape(arr0)[1])))
#Mcnt= np.arange((np.shape(brr0)[1])*(np.shape(brr0)[2]))
vecCount= np.arange(np.shape(brr0)[0])
columns= np.shape(brr0)[1]
rows= np.shape(brr0)[2]
vecStak=np.zeros(len(brr0[:,0,0]))
for j in range(columns):
    for i in range(rows):
       vectr= brr0[:,j,i]
       vectrSumSq= np.sqrt(sum(i*i for i in vectr))#compute the normal to the vector 'mDif'        
       normVec= (vectr/vectrSumSq)#normalized segment variance values
       vectr_dy= np.gradient(normVec)#slope for derivatives
       dx= np.gradient(vecCount)
       deriv1= (vectr_dy/dx)
       abs_der1= abs(deriv1)
       deriv2= (np.gradient(vectr_dy))/(dx**2)
       abs_der2= abs(deriv2)
       vecStak= np.dstack((vecStak, deriv1))       
vectrs=vecStak[0,:,1:]   
xCnt= np.arange(np.shape(vectrs)[0])
##generate similarity matrix for vectrs
m, n= vectrs.shape
simlty= np.zeros((n,n))
for i in range(n):
    for j in range(n):
        simlty[i,j]= cosTheta(vectrs[:,i],vectrs[:,j])
dissSimlty=abs(1-simlty)
######

with open("2ndD_dissSimMatrix.txt", 'w') as yal:
    np.savetxt(yal, dissSimlty, fmt='%f')  
yal.close()
