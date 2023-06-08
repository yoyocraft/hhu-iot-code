#include "quicksort.h"

int partition(int *arr, int left, int right)
{
    // 随机选择一个元素作为pivot
    int pivot_index = rand() % (right - left + 1) + left;
    int pivot = arr[pivot_index];
    // 将pivot交换到序列的最右端
    int tmp = arr[pivot_index];
    arr[pivot_index] = arr[right];
    arr[right] = tmp;
    int i = left, j = right - 1;
    while (i <= j)
    {
        while (arr[i] < pivot)
            i++;
        while (j >= left && arr[j] > pivot)
            j--;
        if (i < j)
        {
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
        else
            break;
    }
    // 将pivot交换到序列中间
    tmp = arr[i];
    arr[i] = arr[right];
    arr[right] = tmp;
    return i;
}

void quick_sort(int *arr, int left, int right)
{
    if (left < right)
    {
        int pivot_index = partition(arr, left, right);
        quick_sort(arr, left, pivot_index - 1);
        quick_sort(arr, pivot_index + 1, right);
    }
}

void random_array(int *arr, int len)
{
    srand(time(NULL));
    for (int i = 0; i < len; i++)
    {
        arr[i] = rand() % 100;
    }
}
