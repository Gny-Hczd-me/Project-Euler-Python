num=1000
sum=0
while num>0:
	num-=1
	if num%3==0 or num%5==0:
		sum+=num
#sum of all multiples of 3 or 5 below 1000:
print(sum)
