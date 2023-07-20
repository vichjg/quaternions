from quaternions import quaternion

def main():
	print(quaternion.product(quaternion(1,0,0,0), quaternion(0,1,0,0)))
	print(quaternion.inverse(quaternion(1,2,3,4)))
	print(quaternion.product(quaternion(4,3,2,1), quaternion(1,2,3,4)))
	print(quaternion.product(quaternion(1,1,1,1), quaternion(1,1,1,1)))
	print(quaternion.inverse(quaternion(1,2,3,4)))
	print(quaternion.versor(quaternion(1,1,1,1)))
	print(quaternion.real(quaternion(1,1,1,1)))
	print(quaternion.pure(quaternion(1,1,1,1)))
	print(quaternion(1,1,1,1).real)
	print(quaternion.crossProduct(quaternion(1,1,0,1), quaternion(-1,1,0,1)))
	print(quaternion.inverse(quaternion(0,0,0,0)))
	print(quaternion.inverse(quaternion(1e100,1e100,1e100,1e100)))
	print(quaternion.inverse(quaternion.versor(quaternion(1,1,1,1))))
	print(quaternion.exp(quaternion(1,1,1,1)))
	
if __name__ == '__main__':
	main()
