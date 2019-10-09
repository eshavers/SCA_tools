##Sorting dissimilarity matrix
##08/14/19
##E_Shavers

#clear workspace
rm(list=ls())

getwd() # print the current working directory
setwd("D:/Map_Files_Watershed/NC_data/voxels/voxelTestFolder2/strm_13")  # note / instead of \ in windows 

####################################
#load packages
require(seriation)

#create output file
csvfile= "D:/Map_Files_Watershed/NC_data/voxels/voxelTestFolder2/strm_13/R_matrixSort1.csv"
txtFile= "D:/Map_Files_Watershed/NC_data/voxels/voxelTestFolder2/strm_13/R_matrixSort1.txt"

#baa<- numeric(0)
ba<- read.csv("2ndD_dissSimAsNum.csv",header=F)
baa<- as.matrix(ba)
row.names(baa)<- row.names(ba)
bab<- seriate(baa, method= "PCA", control= NULL, margin = c(1,2))
head(get_order(bab),216)

#plot results
pimage(baa, main = "original_order")
pimage(baa, bab, main = "Reordered")

