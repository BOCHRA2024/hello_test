def factoriel(n):
	if n==0:
		return 1
	else:
		return n * factoriel(n -1)
number = 5
result = factoriel(number)
printf(f"the factoriel of {number} is {result}.")

