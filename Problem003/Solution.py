num=2
a=600851475143
max=0
while num<a:
	if all(num%i!=0 for i in range(2,int(pow(num,0.5))+1)):
		while a%num==0:
			a=a/num
			max=num
	num+=1
print(num)
#largest prime factor of the number 600851475143
	