'''
PROBLEM 9: 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

ANSWER : 31875000
'''

def main():
    for b in range(1, 1000) : 
    	for a in range(1, b) :
    		c = (b ** 2 + a ** 2) ** 0.5
    		if a + b + c == 1000:
    			print "The product of the Pythagorean triplet (a,b,c) which " \
    			"sum is 1000 is " , a * b * c

if __name__ == "__main__":
    main()