# Find median of 2 sorted arrays

def medianSorted(a, b):
	m, n = len(a), len(b)
	i, j = 0, 0
	mid = (m + n) // 2
	temp = []

	c = 0
	while c <= mid and i < m and j < n:
		if a[i] < b[j]:
			temp.append(a[i])
			i += 1
		else:
			temp.append(b[j])
			j += 1

		c += 1

	while i < m:
		temp.append(a[i])
		i += 1

	while j < n:
		temp.append(b[j])
		j += 1

	# if unique median exists
	if (m+n) % 2 == 0:
		med = (temp[mid-1] + temp[mid]) / 2
	else:
		med = temp[mid-1]

	return med

if __name__ == "__main__":
	a = [1, 12, 15, 26, 38]
	b = [2, 13, 17, 30, 45]

	m = medianSorted(a, b)
	print (m)

	a = [1, 12, 15]
	b = [2, 13, 17, 26, 38, 30, 45]

	m = medianSorted(a, b)
	print (m)
