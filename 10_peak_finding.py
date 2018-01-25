def peak(arr):
	n = len(arr)
	left, right = 0, n - 1

	while left <= right:
		mid = (left + right) // 2

		if mid == 0 and arr[mid] > arr[mid+1]:
			return mid
		elif mid == n - 1 and arr[mid] > arr[mid-1]:
			return mid
		elif arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
			return mid
		elif arr[mid] < arr[mid+1]:
			left = mid + 1
		else:
			right = mid - 1

	return mid

arr = [5, 10, 20, 15]
p = peak(arr)
print (arr[p])

arr = [10, 20, 15, 2, 23, 90, 67]
p = peak(arr)
print (arr[p])
