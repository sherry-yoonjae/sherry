import time
import sys


def duplicate(array):
	newArray = []
	for i in array:
		if i not in newArray:
			newArray.append(i)
	return newArray

if __name__ == '__main__':
	array = []
	for i in range(0,10000):
		array.append(1)
	begin = time.time()
	print '-----------'
	duplicate(array)
	end = time.time()
	print ("time:%f" %(end - begin))
	print '-----------'