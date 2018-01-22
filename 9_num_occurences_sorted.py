# Find number of occurences in a sorted list

def search_first(arr, item):
	left, right = 0, len(arr) - 1

	while left <= right:
		mid = (left + right) // 2

		if item > arr[mid]:
			left = mid + 1
		elif item < arr[mid]:
			right = mid - 1
		elif mid == 0:
			break
		elif item == arr[mid-1]:
			right = mid - 1
		else:
			break

	if item == arr[mid]:
		if mid == 0:
			return mid
		elif item != arr[mid-1]:
			return mid

	return None

def search_last(arr, item):
	left, right = 0, len(arr) - 1

	while left <= right:
		mid = (left + right) // 2

		if item > arr[mid]:
			left = mid + 1
		elif item < arr[mid]:
			right = mid - 1
		elif mid == len(arr) - 1:
			break
		elif item == arr[mid+1]:
			left = mid + 1
		else:
			break

	if item == arr[mid]:
		if mid == len(arr) - 1:
			return mid
		elif item != arr[mid+1]:
			return mid

	return None

def num_occurences(arr, item):
	i = search_first(arr, item)
	j = search_last(arr, item)

	if i == None or j == None:
		return None
	else:
		return j - i + 1

if __name__ == "__main__":
	arr = [1, 1, 2, 2, 2, 2, 3]
	item = 2
	print (num_occurences(arr, item))

	arr = [1, 1, 2, 2, 2, 2, 3]
	item = 3
	print (num_occurences(arr, item))

	arr = [1, 1, 2, 2, 2, 2, 3]
	item = 1
	print (num_occurences(arr, item))

	arr = [1, 1, 2, 2, 2, 2, 3]
	item = 4
	print (num_occurences(arr, item))
