def factorial(num):
	if num == 0:
		return 1
	return factorial(num-1)*num

num = int(input("ENTER: "))
print(factorial(num))