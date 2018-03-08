# -*- coding:utf-8 -*-
import numpy as np
import cPickle as pickle
import scipy
import combo
import os
import urllib
import csv



def load_data():
    A =  np.asarray( np.loadtxt('/home/xiao/folder/result_all.csv',skiprows=1,delimiter=',') )

      
    print A.shape
    print A
    X = A
    #print X.shape[0]
    return X

# Load the data.
# X is the N x d dimensional matrix. Each row of X denotes the d-dimensional feature vector of search candidate. 
# t is the N-dimensional vector that represents the corresponding negative energy of search candidates. 
# ( It is of course unknown in practice. )
X = load_data()
 
# Normalize the mean and standard deviation along the each column of X to 0 and 1, respectively
#X = combo.misc.centering( X )

# Declare the class for calling the simulator. 
# In this tutorial, we simply refer to the value of t. 
# If you want to apply combo to other problems, you have to customize this class. 
class simulator:
    def __init__( self ):
        print 'Call simulator'
        self.t = np.zeros(X.shape[0])
        print 'Hello!'
        #print action
        
    def __call__( self, action ):
        print action
        temp = X[action,:]
	print 'Temp'
	print temp
        #print temp.shape[0]
        #np.savetxt('result_jsh',temp,fmt='%d',newline='\n')
	np.savetxt('result_jsh',temp,fmt='%d',delimiter=',')
        #os.system('/home/app/mpich-3.2/bin/mpirun -np 12 atkpython /home/xiao/folder/calculator.py >> model.log')
	os.system('mpirun -np 12 atkpython /home/xiao/folder/calculator.py >> model.log')
	#os.system('python /home/xiao/combo/debug.py >> model.log')
	#/home/app/mpich-3.2/bin/mpirun -np 12 atkpython /home/xiao/combo/calculator.py >> model.log
	#item=[2.3]

	#with open('data.csv','w') as data:
		#writer = csv.writer(data)
    		#writer.writerow(item)

        #os.system('atkpython /home/xiao/combo/debug.py >> model.log')
        #etot=np.loadtxt(open("/home/xiao/combo/result_all.txt","rb"))        
        #etot=np.loadtxt("/home/xiao/combo/result_all.txt")
	#etot=np.loadtxt(open("/home/xiao/folder/data.csv","rb"),delimiter=",",skiprows=0) 
	#etot =  np.asarray( np.loadtxt('/home/xiao/combo/data.csv',skiprows=0,delimiter=',') )
	#etot=np.loadtxt('/home/xiao/folder/data.txt')
	ff=open('/home/xiao/folder/dataout')
	reader = ff.readlines()
	etot = map(float, reader)
	print etot
	for player in etot:	
		self.t[action]=-player
        print X[action,:]
        #print action
        return self.t[action]


# Define the generative model of GPs. 
# In Combo, to use the GP inference, we have to define three elements: 
# kernel, mean of GP prior and likelihood. 

## Define the kernel 
## The ordinary Gaussian kernel is defined by 
cov = combo.gp.cov.gauss( X.shape[1], ard = False )

## If you want to use the Gaussian ARD kernel, set 'ard' to 'True'
## cov = combo.gp.cov.gauss(X.shape[1], ard = True )

## Define the mean of GP prior
## To employ the constant value as the mean of GP prior, write as below: 
mean = combo.gp.mean.const()
## Also, define the zero mean, i.e., always takes zero as 
# mean = combo.gp.mean.zero()

## Define the likelihood 
## define isotoropic Gaussian likelihood as bellow:
lik = combo.gp.lik.gauss()

# Finally, declare the generative model of Gaussian process as 
gp = combo.gp.model(lik=lik, mean = mean, cov = cov)

# set the configure for COMBO
# To modify the configure of COMBO,  you have to edit the configure files. 
# Please check 'config.ini' if you want to know how to write the configure file 
# loading the configure files, write as follows:
config = combo.misc.set_config()
config.load('/home/xiao/combo/config.ini')
config.show()

# design of policy

# Declaring the bayesian policy is performed by 
search = combo.search.bayes_policy( simulator(), X, config)

# if you want to use the random policy as baseline, define in the same manner: 
#search = combo.search.random_policy(simulator(), X, config)

# set the seed parameter 
search.set_seed( 1 )

# Execute the bayes search.  
# The file_name determines the name of output file which is generated after the search process. 
# If not defining, the file_name automatically become 'bayes_search_00x.dump', where x is the seed.  
search.run( gp, file_name='TS' )

# If you already have the training data ( train_X, train_t ), you can use it 
# search.run( gp , train_X = train_X, train_t = train_t )


# The result of searching is summarized in the class search.res
# res.fx: observed negative energy at each step
# res.max_fx: the current maximum value of the negative energy that has been obserbed until each step
# res.config: the configure files when search was performed
#plt.plot(search.res.max_fx)

# load 
#with open('res/TS.dump') as f1:
#        res =pickle.load(f1)

#print res.fx
#print res.max_fx

