# Polynomials represeted as arrays
# a = [1,2, 3, 4]
# b = [1, 2, 3]

class Polynomial:
	def __init__(self, pol):
		self.p = pol

	def __mul__(self, pol):
		a, b = self.p, pol.p

		m, n = len(a), len(b)
		pol = [0 for i in range(m+n-1)]

		for i in range(m):
			for j in range(n):
				pol[i+j] += a[i] * b[j]

		return pol

	def __eq__(self, pol):
		return self.p.__eq__(pol)

	def __str__(self):
		return self.p.__str__()

if __name__ == "__main__":
	a = Polynomial([5, 0, 10, 6])
	b = Polynomial([1, 2, 4])
	p = Polynomial([5, 10, 30, 26, 52, 24])

	r = a * b
	print (r)
	print (r == p)
