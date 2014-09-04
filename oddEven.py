"""
This is program for finding a given number is odd or even.
This is written just for testing purpose.

Develop by: Ajit kumar ( github/urwithajit)
Date: 4Sept2014
"""
number = int(raw_input("Please a nubmer to check Odd or Even :"))

def check_odd_even(num):
	if num % 2 == 0:
		return "Even"

result = check_odd_even(number)

if result == "Even":
	print(" %d is a even number." % number)
else:
	print(" %d is a Odd number." % number)


