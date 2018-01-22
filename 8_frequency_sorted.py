# To check if element is the dominant in a sorted array, i.e., occures more than
# n/2 times.

def search_first(arr, item):
	left, right = 0, len(arr) - 1

	while left <= right:
		mid = (left + right) // 2

		if item > arr[mid]:
			left = mid + 1
		elif item < arr[mid]:
			right = mid - 1
		elif item == arr[mid - 1]:
			right = mid - 1
		else:
			break

	if item == arr[mid] and mid > 0 and arr[mid - 1] != item:
		return mid
	else:
		return None

def is_dominant(arr, item):
	index = search_first(arr, item)
	n = len(arr)

	if index == None:
		return False
	elif arr[index+n//2] == item:
		return True
	else:
		return False


if __name__ == "__main__":
	arr = [1, 2, 3, 3, 3, 3, 10]
	item = 3
	print (is_dominant(arr, item))

	arr = [1, 2, 3, 3, 3, 4, 10]
	item = 3
	print (is_dominant(arr, item))

	arr = [1, 1, 2, 4, 4, 4, 6, 6]
	item = 4
	print (is_dominant(arr, item))

	arr = [1, 1, 2, 4, 4, 4, 6, 6]
	item = -4
	print (is_dominant(arr, item))

	arr = [1, 1, 2, 4, 4, 4, 6, 6]
	item = 17
	print (is_dominant(arr, item))
