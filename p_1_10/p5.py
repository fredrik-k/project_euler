'''
PROBLEM 5: 
2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

ANSWER : 232792560
'''

def main():
	i = 1
	while True :
		divisible = True 
		for k in range(3,21) : 
			if (i * 20) % k != 0 :
				divisible = False 
				break
		if divisible : 
			break
		i += 1
	print "Smallest number evenly divisible with all the numbers from 1 to 20" \
    	  " is %d " % (i*20)

if __name__ == "__main__":
    main()