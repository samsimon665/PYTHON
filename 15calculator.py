def add():
	n1 = int(input("Enter first number: ")) 
	n2 = int(input("Enter second number: "))
	return n1 + n2
	
def subtract():
	n1 = int(input("Enter first number: "))
	n2 = int(input("Enter second number: "))
	return n1 - n2
	
def multiply():
	n1 = int(input("Enter first number: "))
	n2 = int(input("Enter second number: "))
	return n1 * n2
	
def divide():
	n1 = int(input("Enter first number: "))
	n2 = int(input("Enter second number: "))
	return n1 / n2
	
choice = input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
		
if choice == '1': 
	print("The sum is:", add())
			
elif choice == '2': 
	print("The difference is:", subtract())
			
elif choice == '3':
	print("The product is: ", multiply())
			
elif choice == '4': 
	print("The quotient is: ", divide())
			
else:
	print("incorrect choice!!")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
