
def main():
	#write your code here
	num1 = input("Enter the first number: ")
	num2 = input("Enter the second number: ")
	operation = input("Choose the operation (+, -, /, *): ")
	valid_operations = ["-", "+","*","/"]
	if not(num1.isdigit() and num2.isdigit()):
		print ("invalid input")
	else:
		if operation == valid_operations[0]:
			result = float(num1) - float(num2)
			print (result)
		elif operation == valid_operations[1]:
			result = float(num1) + float(num2)
			print (result)
		elif operation == valid_operations[2]:
			result = float(num1) * float(num2)
			print (result)
		elif operation == valid_operations[3]:
			result = float(num1) / float(num2)
			print ("The answer is", result)
		else:
			print ("invalid operation")
	pass




if __name__ == '__main__':
	main()
