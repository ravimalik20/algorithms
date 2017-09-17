#include<stdio.h>

#define ARR_LEN 20

void array_print(int *arr, int len);
void merge_sort(int *arr, int len);

void __merge_sort(int *arr, int beg, int end);

int main()
{
	int arr[ARR_LEN] = {
		51, 9, 55, 76, 77,
		54, 36, 71, 34, 34,
		72, 62, 79, 15, 60,
		98, 99, 75, 82, 41
	};
	printf("Array before sorting.\n");
	array_print(arr, ARR_LEN);
	
	merge_sort(arr, ARR_LEN);

	printf("Array after sorting.\n");
	array_print(arr, ARR_LEN);

	return 0;
}

void merge_sort(int *arr, int len)
{
	__merge_sort(arr, 0, len-1);
}

void array_print(int *arr, int len)
{
	int i;

	for (i=0; i<len ; i++) {
		printf("%d ", arr[i]);
	}

	printf("\n");
}

void __merge_sort(int *arr, int beg, int end)
{
	if (beg >= end)
		return;

	int mid = (beg + end) / 2;

	__merge_sort(arr, beg, mid);
	__merge_sort(arr, mid+1, end);

	int i = beg, j = mid+1, k=0, len = (end-beg)+1, temp[len];

	/* Merge start */
	for (k = 0 ; k < len && i <= mid && j <= end ; k++) {
		if (arr[i] < arr[j]) {
			temp[k] = arr[i++];
		}
		else {
			temp[k] = arr[j++];
		}
	}

	/* Add leftover elements in the left and right sorted array */
	while (i <= mid) {
		temp[k++] = arr[i++];
	}

	while (j <= end) {
		temp[k++] = arr[j++];
	}

	/* Copy temp array to original array. */
	k = 0;
	while (beg <= end) {
		arr[beg++] = temp[k++];
	}
}
