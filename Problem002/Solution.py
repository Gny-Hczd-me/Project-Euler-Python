num1, num2=1,2
next_fib=num1+num2
sum_of_even=2 #the first even Fibonacci number
while next_fib<4_000_000:
	num1=num2
	num2=next_fib
	next_fib=num1+num2
	if num2%2==0:
		#sum of even-valued Fibonacci numbers
		sum_of_even+=num2
print(sum_of_even)