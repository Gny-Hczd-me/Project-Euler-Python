#Sum of squares of the first 100 natural numbers is
sum1=sum([i**2 for i in range(1,101)])
#Square of the sum of the first 100 natural numbers is
square1=pow(sum([i for i in range(1,101)]),2)
#difference
difference=square1-sum1
print(difference)