#include <stdio.h>
#include <stdlib.h>

void mergesort(int arr[], int l, int r)
{
    int mid = (l -r)/2;
    if (l-r <= 0)
    {
        return;
    }
    else if (r-l > 1)
    {
        mergesort(arr, l, mid);
        mergesort(arr, mid+1, r);
    }
    merge(arr, l, mid, r);
}

void merge(int arr[], int l, int mid, int r)
{
    int a = mid- l + 1;
    int b = r - mid;

    int L[a];   //copying left side of array
    for (int i = 0; i < a; i++)
    {
        L[i] = arr[i];
    }

    int R[b];   //copying right side of array
    for (int j = 0; j < b; j++)
    {
        R[j] = arr[mid + 1 + j];
    }

    int left_counter = 0, right_counter = 0, arr_counter = l;
    while (left_counter < a && right_counter < b) //comparing elements from each array progressively
    {
        if (L[left_counter] < R[right_counter])
        {
            arr[arr_counter] = L[left_counter];
            left_counter++;
        }
        else if (L[left_counter] > R[right_counter])
        {
            arr[arr_counter] = R[right_counter];
            right_counter++;
        }
        arr_counter++;
    }
    
    while (left_counter < a)    //copying leftovers from left array
    {
        arr[arr_counter] = L[left_counter];
        arr_counter++;
        left_counter++;
    }
    while (right_counter < b)    //copying leftovers from right array
    {
        arr[arr_counter] = R[right_counter];
        arr_counter++;
        right_counter++;
    }
}
