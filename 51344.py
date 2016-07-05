def containsVowel(x):
	y = x.lower()
	vowels=["a","e","i","o","u","y"]
	if len(y) == 0:
		return False
	elif  y[0] in vowels:
		return True
	else:
		return containsVowel(y[1:])
