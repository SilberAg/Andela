#python assignment 5
list = []

def square():
	for i in range(1,20):
		sq = i ** 2
		list.append(sq)
square()

print(list[0:5])
