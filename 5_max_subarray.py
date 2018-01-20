from math import inf

def max_crossing(arr, left, right):
	mid = (left + right) // 2
	sum_left, sum_right = -1 * inf, -1 * inf
	max_left, max_right = -1, -1

	s = 0
	for i in range(mid, left-1, -1):
		s += arr[i]
		if s > sum_left:
			sum_left = s
			max_left = i

	s = 0
	for i in range(mid+1, right+1):
		s += arr[i]
		if s > sum_right:
			sum_right = s
			max_right = i

	return (max_left, max_right, sum_left+sum_right)

def max_subarray(arr, left, right):
	if left == right:
		return (left, right, arr[left])

	mid = (left + right) // 2

	left_i, left_j, left_sum = max_subarray(arr, left, mid)
	right_i, right_j, right_sum = max_subarray(arr, mid+1, right)
	cross_i, cross_j, cross_sum = max_crossing(arr, left, right)

	max_left, max_right, max_sum = left_i, left_j, left_sum
	if right_sum > max_sum:
		max_left, max_right, max_sum = right_i, right_j, right_sum
	if cross_sum > max_sum:
		max_left, max_right, max_sum = cross_i, cross_j, cross_sum

	return (max_left, max_right, max_sum)

if __name__ == "__main__":
	arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

	print (max_subarray(arr, 0, len(arr)-1))
