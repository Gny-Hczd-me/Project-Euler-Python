s=1
for i in range(2,21):
	s*=i #20!
for j in [2,3,5,7,11,13,17,19]: #prime numbers up to 20
	while all((s//j)%x==0 for x in range(2,21)):
		s=s//j
print(s) #the smallest number that can be divided by each of the numbers from 1 to 20 without any remainder.