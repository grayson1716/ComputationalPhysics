from random import random

# define pdf to be sampled
def pdf(x):
	return 4 / (1+x*x)

N = int(input('Input number of samples: '))

# initialize variables
mc_chain = 0
sum_sig = 0

# loop, and update the variables for calculation of mean and variance
for i in range(N):
	x = random()
	fx = pdf(x)
	mc_chain += fx
	sum_sig += fx*fx

mc_chain = mc_chain / N
sum_sig = sum_sig / N

print('Mean: %.3f' % mc_chain)
print('Variance: %.3f\n' % (sum_sig - mc_chain*mc_chain))