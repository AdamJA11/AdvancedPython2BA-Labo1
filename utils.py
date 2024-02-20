import cmath
import scipy.integrate as integ
import scipy.special as special

def fact(n):
	a = 1
	for i in range(1, n+1):
		a = i *a
	return 	a
		
	


def roots(a, b, c):
	d = (b**2) -(4*a*c)
	if d <0:
		return (None, None)
	elif d == 0:
		return (-b/(2*a))
	else:
		return ((-b + cmath.sqrt(d))/2*a) , ((-b - cmath.sqrt(d))/2*a)
	
	

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	result = integ.quad(lambda x: eval(function), lower, upper)

	return result

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
