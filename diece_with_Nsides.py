import random
import time
import numpy as np
def OneDieS(trials, sides):
    c1=time.clock()
    print("---------------------------------------------------")
    print("Number of sides = ", sides)
    print("Number of trials = ", trials)
    Sides = np.linspace(1,sides,sides)
    histogram = []
    for s in range(sides):
        histogram.append(0)
    

    r = 0
    for t in range(trials):
        r = int(random.random()*sides)
        histogram[r] = histogram[r] + 1
 
    mean = round(sum(Sides*histogram/trials),3)
    var = round(sum(pow(Sides,2)*histogram/trials)-pow(mean,2),3)
    stand=round(pow(var,1/2),4)
    theomean=round((sides+1)/2,3)
    theovar=round(1/sides*sum(pow(Sides,2))-pow(theomean,2),3)
    theostand=round(pow(theovar,1/2),5)
    deltamean=round(abs(mean-theomean)/theomean*100,5)
    deltavar=round(abs(var-theovar)/theovar*100,5)
    deltastand=round(abs(stand-theostand)/theostand*100,5)
    print('expmean:',mean,'theomean:',theomean )
    print('expvariance:',var,'theovar:',theovar)
    print('expstandev:',stand,'theostand:',theostand)
    print('error of mean',deltamean,'%')
    print('error of variance',deltavar,'%')
    print('error of standard deviation',deltastand,'%')
   
    print("s, N_s, N_s-N/6, N_s/N, N_s/N-1/6")
    j = 0
    while j < sides:
        print(j+1, histogram[j],round( histogram[j]-trials/sides,3), round(histogram[j]/trials,3), round(histogram[j]/trials-1/6),3)
        j = j + 1
    
    c2=time.clock()
    print("Elapsed time =", c2-c1)



 
def run():
 
    OneDieS(10, 6)
    OneDieS(100, 6)
    OneDieS(1000, 6)
    OneDieS(6000, 6)
 
run()
