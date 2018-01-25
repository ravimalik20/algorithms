# Selection problem. Calculate i-th order statistics of the list

import random

def partition(arr, p):
	i, j = 1, 1
	arr[p], arr[0] = arr[0], arr[p]

	while j < len(arr):
		if arr[j] < arr[0]:
			arr[j], arr[i] = arr[i], arr[j]
			i += 1

		j += 1

	arr[i-1], arr[0] = arr[0], arr[i-1]

	return i-1

def rselect(arr, i):
	n = len(arr)

	if n == 1:
		return arr[0]

	p = random.randrange(0, n)
	j = partition(arr, p)

	if j == i:
		return arr[j]
	elif j > i:
		return rselect(arr[0:j], i)
	else:
		return rselect(arr[j+1:n], i-j-1)


if __name__ == "__main__":
	arr = [12, 34, 1, 45, 2 , 76, 23]

	print (arr)
	print (sorted(arr))

	print ("{}: {}".format(4, rselect(arr, 4)))
	print ("{}: {}".format(1, rselect(arr, 1)))
	print ("{}: {}".format(0, rselect(arr, 0)))
	print ("{}: {}".format(6, rselect(arr, 6)))
