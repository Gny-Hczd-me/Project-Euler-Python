num=2
a=600851475143
max=0
while num<a:
	if all(num%i!=0 for i in range(2,int(pow(num,0.5))+1)):
		if a%num==0:
			max=num
			a=a/max
	num+=1
print(max)
#largest prime factor of the number 600851475143
	