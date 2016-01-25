'''
PROBLEM 10: 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

ANSWER : Fill in answer when solved
'''

def main():
	primeList = []
	primeList.append(2)
	i = 3
	while  i < 2 * (10 ** 6):
		for p in primeList : 
			if i**0.5 < p : 
				primeList.append(i)
				break
			if i % p == 0 : 
				break
		i += 2
	print "The sum of all primes below two million is ", sum(primeList)

if __name__ == "__main__":
    main()