from math import *

def f(mu, sigam2, x):
    return 1/sqrt(2*pi*sigam2)*exp(-0.5*(x-mu)**2/sigam2)


def update(mean1,var1,mean2,var2):
    new_mean = (var2*mean1 + var1*mean2)/(var1+var2)
    new_var = 1/(1/var1+1/var2)
    return [new_mean,new_var]

def predict(mean1, var1,mean2,var2):
    new_mean = mean1+mean2
    new_var = var1+var2
    return [new_mean,new_var]



print(f(10.,4.,8.))
print(update(10.,8.,13.,2.))
print(predict(10.,4.,12.,4.))

mmeasurements = [5.,6.,7.,9.,10.]
motion=[1.,1.,2.,1.,1.]
meaasurement_sig=4.
motion_sig = 2.
mu = 0.
sig = 10000.


for n in range(len(mmeasurements)):
    [mu,sig] = update(mu,sig,mmeasurements[n],meaasurement_sig)
    print("update: ",[mu,sig])
    [mu,sig] = predict(mu,sig,motion[n],motion_sig)
    print("predict: ",[mu,sig])
