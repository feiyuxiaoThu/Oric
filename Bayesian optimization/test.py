import numpy as np
import cPickle as pickle
import scipy
import combo
import os
import urllib
# import matplotlib.pyplot as plt
def download():
    if not os.path.exists('data/s5-210.csv'):

        if not os.path.exists('data'):
            os.mkdir('data')
            
        print('Downloading...')
        urllib.urlretrieve('http://www.tsudalab.org/files/s5-210.csv', 'data/s5-210.csv')
        print('Done')
def load_data():
    download()
    A =  np.asarray( np.loadtxt('data/s5-210.csv',skiprows=1,delimiter=',') )
    X = A[:,0:3]
    t  = -A[:,3]
    return X, t
# Load the data. 
# X is the N x d dimensional matrix. Each row of X denotes the d-dimensional feature vector of search candidate. 
# t is the N-dimensional vector that represents the corresponding negative energy of search candidates. 
# ( It is of course unknown in practice. )
X, t = load_data()
 
# Normalize the mean and standard deviation along the each column of X to 0 and 1, respectively
X = combo.misc.centering( X )
# Declare the class for calling the simulator. 
# In this tutorial, we simply refer to the value of t. 
# If you want to apply combo to other problems, you have to customize this class. 
class simulator:
    def __init__( self ):
        _, self.t = load_data()
    
    def __call__( self, action ):
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
config.load('config.ini')
config.show()
# design of policy

# Declaring the bayesian policy is performed by 
search = combo.search.bayes_policy( simulator(), X, config)

# if you want to use the random policy as baseline, define in the same manner: 
#search = combo.search.random_policy(simulator(), X, config)

# set the seed parameter 
search.set_seed( 0 )

# Execute the bayes search.  
# The file_name determines the name of output file which is generated after the search process. 
# If not defining, the file_name automatically become 'bayes_search_00x.dump', where x is the seed.  
search.run( gp, file_name='TS' )

# If you already have the training data ( train_X, train_t ), you can use it 
# search.run( gp , train_X = train_X, train_t = train_t )
# load 
# with open('res/TS.dump') as f:
        # res =pickle.load(f)
		# print res.fx
# print res.max_fx