#!python assignment 4
balance = 0; 
a = input("Please enter a value:\n 1: Deposit\n 2: withdraw\n 3: End Transactions\n")
a = int(a)

while(a == 1 or a == 2):
	a = input("Please enter a value:\n 1: Deposit\n 2: Withdraw\n 3: End Transactions\n 4: Check balance\n ")
	a = int(a)
	compile(a,balance)
	



def compile(c,d):
	if(c == 1):
		amount = int(input("Enter the amount to Deposit\n"))
		d = d + int(amount)
		print("money was deposited and the balance is {}\n".format(balance))
	elif(c == 2):
		amount = int(input("Enter the amount to withdraw\n"))
		d = d - int(amount)
		print("Money was withdrawn and the balance is {}\n".format(balance))
	elif(c == 3):
		pass
	elif(c == 4):
		print("The balance is {}".format(balance))
	else:
		print("Invalid input")
