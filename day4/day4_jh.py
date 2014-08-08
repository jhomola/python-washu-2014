from math import *

def gcd(a, b):
	if b == 0: 
		return a
	else: return gcd(b, a % b)
	
print gcd(25,130)
print gcd(130,25)
print (25 % 125)
print (2/3)


def primes(limit):
	possible_primes = [True] * limit
	for i in range(2, int(sqrt(limit))):
		if possible_primes[i]:
			j = 0
			while (i**2 + j*i) < limit:
				possible_primes[i**2 + j*i] = False
				j += 1
	return [i for i,x in enumerate(possible_primes) if (x == True) & (i > 1)]
	
print primes(40)


def hanoi(n, source, helper, target):
    print "hanoi( ", n, source, helper, target, " called"
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            print "moving " + str(disk) + " from " + source[1] + " to " + target[1]
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        
source = ([5,4,3,2,1], "source")
target = ([], "target")
helper = ([], "helper")
hanoi(len(source[0]),source,helper,target)

print source, helper, target