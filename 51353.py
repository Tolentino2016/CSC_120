def productOfOdds(x):
	if len(x) == 1:      
		if x[0] % 2 == 0:
			return 1
		else:
			return x[0]	
		
	if x[0] % 2 != 0:
		return x[0] * productOfOdds(x[1:])
	else:
		return productOfOdds(x[1:])
