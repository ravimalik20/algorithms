/*
* Program to count inversions in an array.
* Use case: to find the degree of similarity between 2 ranked lists.
* 
* Solution is done by implementing merge sort, because merge sort is inherently
* good at finding array inversions.
*/

#include<stdio.h>

#define arr_len(arr) ((sizeof(arr)) / sizeof(arr[0]) )

int count_inversions(int *arr, int len);

static int __merge_count(int *arr, int beg, int end);

void main()
{
	int arr[] = {1, 3, 5, 2, 4 , 6};
	printf("Number of inversions: %d\n", count_inversions(arr, arr_len(arr)));

	int arr2[] = {2, 4, 1, 3, 5};
	printf("Number of inversions: %d\n", count_inversions(arr2, arr_len(arr2)));

	int arr3[] = {1, 5, 4, 8, 10, 2, 6, 9, 3, 7};
	printf("Number of inversions: %d\n", count_inversions(arr3, arr_len(arr3)));
}

int count_inversions(int *arr, int len)
{
	return __merge_count(arr, 0, len-1);
}

static int __merge_count(int *arr, int beg, int end)
{
	if (beg >= end)
		return 0;

	int count = 0;
	int mid = (beg + end) / 2;

	count += __merge_count(arr, beg, mid);
	count += __merge_count(arr, mid+1, end);

	int i = beg, j = mid+1, k = 0, len = (end-beg)+1, temp[len];

	for (k = 0; k < len && i <= mid && j <= end ; k++) {
		if (arr[i] < arr[j])
			temp[k] = arr[i++];
		else {
			temp[k] = arr[j++];
			count += (mid - i) + 1;
		}
	}

	while (i <= mid)
		temp[k++] = arr[i++];

	while (j <= end)
		temp[k++] = arr[j++];

	k = 0;
	while (beg <= end)
		arr[beg++] = temp[k++];

	return count;
}
