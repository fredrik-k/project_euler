'''
PROBLEM 3: 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

ANSWER : 6857
'''

from math import floor

def findDivisor(n) :
	upperLimit = n**0.5
	for i in range(2, int(floor(upperLimit))) :
		if n % i == 0 : 
			return i
	return -1

def findPrimeFactors(n, primeList = []) :
	divisor = findDivisor(n)
	if (divisor > 0) : 
		primeList = findPrimeFactors(divisor, primeList)
		primeList = findPrimeFactors(n / divisor, primeList)
	else :
		primeList.append(n)
	return primeList

def main():
    primeList = findPrimeFactors(600851475143)

    primeList.sort(reverse=True)
    print "Largest prime factor of 600851475143 is " , primeList[0]

if __name__ == "__main__":
    main()