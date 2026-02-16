for i in range(10,100):
	if i%10!=0:
		for j in range(i,100):
			if j%10!=0:
				if i/j==(i//10)/(j%10):
					if i%10==j//10:
						if i/j<1:
							print(i,"/",j) #four fractions