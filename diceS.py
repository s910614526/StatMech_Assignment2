import random
import time
import numpy as np
def NDieS(trials):
    sides=random.randint(19,20)
    numberof_dice=random.randint(9,10)
    trials=trials*   numberof_dice
    c1=time.clock()
    print("---------------------------------------------------")
    print("Number of sides = ", sides)
    print("Number of trials = ", trials)
    print("Number of dices = ",    numberof_dice)
    Sides = np.linspace(1,sides,sides)
    
    histogram = []
    
    for s in range(sides):
        histogram.append(0)
    

    r = 0
    for t in range(trials):
        r = int(random.random()*sides)
       
        histogram[r] = histogram[r] + 1
    Hmat=np.array(histogram)
    SidesTr=Sides.T
    
    
    
    mean = round(sum(SidesTr*Hmat/trials),3)
    var = round(sum(pow(SidesTr,2)*Hmat/trials)-pow(mean,2),3)
    stand=round(pow(var,1/2),4)
    theomean=round((sides+1)/2,3)
    theovar=round( (1/sides*sum(pow(Sides,2))-pow((sides+1)/2,2)),3)
    theostand=round(pow(theovar,1/2),5)
    deltamean=round(abs(mean-theomean)/theomean*100,5)
    deltavar=abs(var-theovar)/theovar*100
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
 
     NDieS(100)
     NDieS(100)
     NDieS(100)
     NDieS(100)
     NDieS(100)
     NDieS(100)
 
 
run()
