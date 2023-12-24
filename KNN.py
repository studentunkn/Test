import numpy as np
temp = 0
for i in range(1,10,1):
    r = np.random.randint(1,10,size=1);
    r=0.1*r
    temp +=r
    print(temp)