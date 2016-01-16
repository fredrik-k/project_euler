'''
PROBLEM 1: 

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

ANSWER : 233168
'''

def main():
   	multipleSum = 0
   	done = False

   	for i in range(1,1000) : 
   		if i % 3 == 0 :
   			multipleSum += i
   		elif i % 5 == 0: 
   			multipleSum += i

   	print "Sum of all multiples of 3 and 5 below 1000 is %d" % multipleSum

if __name__ == "__main__":
    main()