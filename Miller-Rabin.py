import math

def getNumbers():
	n = int(input('Enter the number: '))
	x = n-1
	s = 0
	while x % 2 == 0:
		x = x/2
		s = s+1
	d = int(x)
	return {'n': n, 'd': d, 's': s}

def testPrime(a, **nums):
	for i in range(0,nums['s']):
		if pow(a,(pow(2,i) * nums['d']),nums['n']) in (1, nums['n']-1):
			return 0
			break
	return 1

nums = getNumbers()
#print (nums)
if nums['n'] < 2047:
	a = [2]
elif nums['n'] < 1373653:
	a = [2,3]
elif nums['n'] < 25326001:
	a = [2,3,5]
elif nums['n'] < 2152302898747:
	a = [2,3,5,7,11]
elif nums['n'] < 3474749660383:
	a = [2,3,5,7,11,13]
elif nums['n'] < 341550071728321:
	a = [2,3,5,7,11,13,17]
elif nums['n'] < 3825123056546413051:
	a = [2,3,5,7,11,13,17,19,23]
else:
	a = [2,3,5,7,11,13,17,19,23,29,31,37]

result = 0

for i in a:
	result = testPrime(i, **nums) + result

if result == 0:
	print("%d is a Prime number" % (nums['n']))
else: 
	print("%d is a Composite number" % (nums['n']))
