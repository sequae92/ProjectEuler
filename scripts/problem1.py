#Problem 1
#Author- Spondon Kundu
#Project Euler

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
max=1000
mul1=3
mul2=5

def sum_of_multiples(max,mul1,mul2):
	multiples=[]
	for i in range(1,max):
		if i%mul1==0 or i%mul2==0:
			multiples.append(i)
	return sum(multiples)

if __name__ == '__main__':
	print(sum_of_multiples(1000,3,5))
