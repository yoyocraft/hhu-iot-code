#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "quicksort.h"

#define TEST_TIMES 10
#define ARRAY_LEN 20

void print_array(int arr[], int len)
{
    printf("[ ");
    for (int i = 0; i < len; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("]\n");
}

int main(int argc, char const *argv[])
{
    srand(time(NULL));

    for (int i = 1; i <= TEST_TIMES; i++)
    {
        printf("Test %d:\n", i);

        int arr[ARRAY_LEN];
        for (int j = 0; j < ARRAY_LEN; j++)
        {
            arr[j] = rand() % 100;
        }

        printf("Original Array: ");
        print_array(arr, ARRAY_LEN);

        quick_sort(arr, 0, ARRAY_LEN - 1);

        printf("Sorted Array:   ");
        print_array(arr, ARRAY_LEN);

        printf("\n");
    }

    return 0;
}
