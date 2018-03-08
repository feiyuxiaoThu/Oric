#-*- coding: UTF-8 -*- 
# -------------------------------------------------------------
# Two-probe Configuration
# -------------------------------------------------------------

# -------------------------------------------------------------
# Left Electrode
# -------------------------------------------------------------

#ML
#random number for input
import numpy as np
import csv

test=np.loadtxt('/home/xiao/combo/result_jsh')
#test=[1,2,4,2,1,3]
# with open('D:\data.csv') as f:
    # datareader = csv.reader(f);
#test = numpy.loadtxt(open("data.csv","rb"),delimiter=",",skiprows=0)

#A
if int(test[0]) == 1:
	print '1'
elif int(test[0]) == 2:
	print '2'
elif int(test[0]) == 4:
	print '4'