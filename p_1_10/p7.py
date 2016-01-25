'''
PROBLEM (7): 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?

ANSWER : 104743
'''

def main():
	primeList = []
	primeList.append(2)
	i = 3
	while len(primeList) < 10001 :
		for p in primeList : 
			if i**0.5 < p : 
				primeList.append(i)
				break
			if i % p == 0 : 
				break
		i += 2

   	print "The 10001 prime is ", primeList[len(primeList) - 1]

if __name__ == "__main__":
    main()