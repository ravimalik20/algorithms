def __common_prefix(str1, str2):
	i = 0
	common = ""

	while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
		common += str1[i]
		i += 1

	return common

def longest_common_prefix(arr_str):
	n = len(arr_str)

	if n == 1:
		return arr_str[0]

	if n == 2:
		return __common_prefix(arr_str[0], arr_str[1])

	lprefix = longest_common_prefix(arr_str[ : n//2])
	rprefix = longest_common_prefix(arr_str[n//2 : ])

	return __common_prefix(lprefix, rprefix)

if __name__ == "__main__":
	arr_str = ["geeksforgeeks", "geeks", "geek", "geeze"]
	print (longest_common_prefix(arr_str))

	arr_str = ["ravi malik", "ravish kumar", "ravit chauhan", "ravinder singh"]
	print (longest_common_prefix(arr_str))

	arr_str = ["apple", "ape", "april"]
	print (longest_common_prefix(arr_str))

	arr_str = ["ravi", "karan"]
	print (longest_common_prefix(arr_str))
