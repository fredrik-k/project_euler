'''
PROBLEM 4: 
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

ANSWER : 906609
'''

def palindrome(num):
    return str(num) == str(num)[::-1]

def main():
    palindromeList = []
    for i in range(100,1000):
    	for k in range(i,1000):
    		if palindrome(i*k) : 
    			palindromeList.append(i*k)
    palindromeList.sort(reverse=True)

    print "Largest palindrome number of the product of two three digit " \
    	  "numbers is %d" % palindromeList[0]

if __name__ == "__main__":
    main()