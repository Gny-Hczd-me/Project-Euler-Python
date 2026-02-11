from itertools import permutations
a = [0,1,2,3,4,5,6,7,8,9]
listof=[]
num=0
for j in permutations(a):
#make permutations available
    listof.append(j)
for i in range(0,10):
    num+=listof[(10**6)-1][i]*10**(9-i)
print(num)