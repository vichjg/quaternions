from decimal import DivisionByZero
from warnings import catch_warnings
import math

class quaternion():

	def __init__(self, im_i=0, im_j=0, im_k=0, real=0):
		self.im_i = im_i
		self.im_j = im_j
		self.im_k = im_k
		self.real = real
	
	@staticmethod
	def pure(q):
		if(isinstance(q, quaternion)):
			return quaternion(q.im_i, q.im_j, q.im_k, 0)
		else:
			print("Error in quaternion.pure(q), one parameter quaternion must be especified")
			return [0, 0, 0]

	@staticmethod
	def real(q):
		if(isinstance(q, quaternion)):
			return quaternion(0, 0, 0, q.real)
		else:
			print("Error in quaternion.real(q), one parameter quaternion must be especified")
			return [0, 0, 0]

	@staticmethod
	def modulus(q):
		if(isinstance(q, quaternion)):
			return (q.im_i ** 2 + q.im_j ** 2 + q.im_k ** 2 + q.real ** 2) ** 0.5
		else:
			print("Error in quaternion.modulus(q), one parameter quaternion must be especified")
			return 1.0

	@staticmethod
	def conjugate(q):
		if(isinstance(q, quaternion)):
			i = - q.im_i
			j = - q.im_j
			k = - q.im_k
			r = + q.real
			return quaternion(i, j, k, r)
		else:
			print("Error in quaternion.conjugate(q), one parameter quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def scalar_product(q, r):
		if(isinstance(q, quaternion)):
			return quaternion(q.im_i * r, q.im_j * r, q.im_k * r, q.real * r)
		else:
			print("Error in quaternion.scalar_product(q, r), one parameter quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def versor(q):
		if(isinstance(q, quaternion)):
			return quaternion.scalar_product(q, 1 / quaternion.modulus(q))
		else:
			print("Error in quaternion.versor(q), one parameter quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def trace(q):
		if(isinstance(q, quaternion)):
			return quaternion.add(q, quaternion.conjugate(q)).real
		else:
			print("Error in quaternion.trace(q), one parameter quaternion must be especified")
			return 0.0

	@staticmethod
	def negative(q):
		if(isinstance(q, quaternion)):
			return quaternion.scalar_product(-q.im_i, -q.im_j, -q.im_k, -q.real)
		else:
			print("Error in quaternion.negative(q), one parameter quaternion must be especified")
			return quaternion(0, 0, 0, 0)
	
	@staticmethod
	def inverse(q):
		if(isinstance(q, quaternion)):
			try:
				return quaternion.scalar_product(quaternion.conjugate(q), 1 / (quaternion.modulus(q) ** 2))
			except ZeroDivisionError:
				print("Exception handled in quaternion.inverse(a, b), division by zero")
				return quaternion.infinite()
		else:
			print("Error in quaternion.inverse(q), one parameter quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def add(a, b):
		if(isinstance(a, quaternion) and isinstance(b, quaternion)):
			i = a.im_i + b.im_i
			j = a.im_j + b.im_j
			k = a.im_k + b.im_k
			r = a.real + b.real
			return quaternion(i, j, k, r)
		else:
			print("Error in quaternion.add(a, b), two parameters quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def sub(a, b):
		if(isinstance(a, quaternion) and isinstance(b, quaternion)):
			i = a.im_i - b.im_i
			j = a.im_j - b.im_j
			k = a.im_k - b.im_k
			r = a.real - b.real
			return quaternion(i, j, k, r)
		else:
			print("Error in quaternion.sub(a, b), two parameters quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def product(a, b):
		if(isinstance(a, quaternion) and isinstance(b, quaternion)):
			i = a.real * b.im_i + a.im_i * b.real + a.im_j * b.im_k - a.im_k * b.im_j
			j = a.real * b.im_j - a.im_i * b.im_k + a.im_j * b.real + a.im_k * b.im_i
			k = a.real * b.im_k + a.im_i * b.im_j - a.im_j * b.im_i + a.im_k * b.real
			r = a.real * b.real - a.im_i * b.im_i - a.im_j * b.im_j - a.im_k * b.im_k
		
			return quaternion(i, j, k, r)
		else:
			print("Error in quaternion.product(a, b), two parameters quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def div(a, b):
		if(isinstance(a, quaternion) and isinstance(b, quaternion)):
			return quaternion.product(a, quaternion.inverse(b))
		else:
			print("Error in quaternion.div(a, b), two parameters quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def exp(q):
		if(isinstance(q, quaternion)):
			try:
				a = q.real
				v = quaternion.pure(q)
				angle = quaternion.modulus(v)
				e_a = math.e ** a
				qreal = quaternion(0,0,0,e_a * math.cos(angle))
				qpure = quaternion.scalar_product(v, math.sin(angle) / angle)
				return quaternion.add(qreal, qpure)
			except ZeroDivisionError:
				return quaternion.pure(quaternion.infinite())

		else:
			print("Error in quaternion.exp(q), one parameter quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def log(q):
		if(isinstance(q, quaternion)):
			try:
				a = q.real
				v = quaternion.pure(q)
				angle = quaternion.modulus(v)
				e_a = math.e ** a
				qreal = quaternion(0,0,0,e_a * math.cos(angle))
				qpure = quaternion.scalar_product(v, math.sin(angle) / angle)
				return quaternion.add(qreal, qpure)
			except ZeroDivisionError:
				return quaternion.pure(quaternion.infinite())

		else:
			print("Error in quaternion.log(q), one parameter quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def dotProduct(a, b):
		if(isinstance(a, quaternion) and isinstance(b, quaternion)):
			return quaternion.negative(quaternion.real(quaternion.product(quaternion.pure(a), quaternion.pure(b))))
		else:
			print("Error in quaternion.dotProduct(a, b), two parameters quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def crossProduct(a, b):
		if(isinstance(a, quaternion) and isinstance(b, quaternion)):
			return quaternion.pure(quaternion.product(quaternion.pure(a), quaternion.pure(b)))
		else:
			print("Error in quaternion.crossProduct(a, b), two parameters quaternion must be especified")
			return quaternion(0, 0, 0, 0)

	@staticmethod
	def infinite():
		return quaternion(1e100, 1e100, 1e100, 1e100)

	def __str__(self):
		return "\n[" + str(self.im_i) + "\t" + str(self.im_j) + "\t" + str(self.im_k) + "\t" + str(self.real) + "]\n"
