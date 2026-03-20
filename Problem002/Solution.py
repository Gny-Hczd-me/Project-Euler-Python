num1=1
num2=2
sum=num1+num2
sum_of_even=2
while sum<4*10**6:
	num1=num2
	num2=sum
	sum=num1+num2
	if num2%2==0:
		#sum of even-valued Fibonacci numbers
		sum_of_even+=num2
print(sum_of_even)