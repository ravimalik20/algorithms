#include<stdio.h>

#define ARR_LEN 10

void array_print(int *arr, int len);
void merge_sort(int *arr, int len);

void __merge_sort(int *arr, int beg, int end);

int main()
{
	int arr[ARR_LEN] = {49, 64, 61, 58, 2, 2, 38, 4, 51, 31};
	merge_sort(arr, ARR_LEN);
	array_print(arr, ARR_LEN);

	int arr2[ARR_LEN] = {98, 1, 26, 30, 2, 29, 60, 70, 37, 66};
	merge_sort(arr2, ARR_LEN);
	array_print(arr2, ARR_LEN);

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

	int i = beg, j = mid+1, k=0, len=end-beg+1, temp[len];
	int limit_arr1 = mid;
	int limit_arr2 = end;

	/* Merge start */
	while (i <= limit_arr1 && j <= limit_arr2) {
		if (arr[i] <= arr[j]) {
			temp[k++] = arr[i++];
		}
		else {
			temp[k++] = arr[j++];
		}
	}

	/* Add leftover elements in the left and right sorted array */
	while (i <= limit_arr1) {
		temp[k++] = arr[i++];
	}

	while (j <= limit_arr2) {
		temp[k++] = arr[j++];
	}

	for (k = 0; k < len ; k++) {
		arr[beg+k] = temp[k];
	}
}
