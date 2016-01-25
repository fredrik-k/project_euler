'''
PROBLEM 6:
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

ANSWER: 25164150
'''

def main() :
	sumSqr = 0
	sqrSum = 0
	for i in range(1,101) : 
		sumSqr += i**2
		sqrSum += i

	print "The difference between the sum of squares and the squared sum of " \
	      "the one hunderd first numbers is ", sqrSum**2 - sumSqr

if __name__ == "__main__":
    main()