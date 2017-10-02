/*
* Implementation of quick sort.
*/

#include<stdio.h>

void quick_sort(int *arr, int len);
void print_arr(int *arr, int len);

void __quick_sort(int *arr, int beg, int end);
int __partition(int *arr, int beg, int end);
void __swap(int *a, int *b);

int main(void)
{
	int arr[8] = {3, 8, 2, 5, 1, 4, 7, 6};

	print_arr(arr, 8);
	quick_sort(arr, 8);
	print_arr(arr, 8);

	int arr2[20] = {42, 90, 69, 31, 79, 75, 7, 5, 6, 93, 10, 24, 86, 56, 85,
		21, 90, 42, 24, 71};
	print_arr(arr2, 20);
	quick_sort(arr2, 20);
	print_arr(arr2, 20);

	return 0;
}

void quick_sort(int *arr, int len)
{
	__quick_sort(arr, 0, len-1);
}

void __quick_sort(int *arr, int beg, int end)
{
	if (beg >= end)
		return;

	int p;

	p = __partition(arr, beg, end);

	__quick_sort(arr, beg, p-1);
	__quick_sort(arr, p+1, end);
}

int __partition(int *arr, int beg, int end)
{
	int pivot = beg, i = beg+1, j = i+1;

	for (j = i ; j <= end ; j++) {
		if (arr[j] < arr[pivot])
			__swap(&arr[i++], &arr[j]);
	}

	__swap(&arr[pivot], &arr[i-1]);

	return i-1;
}

void __swap(int *a, int *b)
{
	int temp = *b;
	*b = *a;
	*a = temp;
}

void print_arr(int *arr, int len)
{
	int i=0;
	while (i < len)
		printf("%d ", arr[i++]);

	printf("\n");
}
