#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include "common_tools.h"

// From https://stackoverflow.com/a/54057690/3791827

char * c_read_file(const char * f_name, FileError * err, size_t * f_size) 
{
    char * buffer;
    size_t length;
    FILE * f = fopen(f_name, "rb");
    size_t read_length;
    char * retval = NULL;

    if (f) 
    {
        fseek(f, 0, SEEK_END);
        length = ftell(f);
        fseek(f, 0, SEEK_SET);
        
        // 1 GiB; best not to load a whole large file in one string
        if (length > 1073741824) 
        {
            *err = File_Too_Large;
        }
        
        buffer = (char *)malloc(length + 1);
        
        if (length) 
        {
            read_length = fread(buffer, 1, length, f);
            
            if (length != read_length) 
            {
                 free(buffer);
                 *err = File_Read_Error;
            }
        }
        
        fclose(f);
        
        *err = File_OK;
        buffer[length] = '\0';
        *f_size = length;
    }
    else 
    {
        *err = File_Not_Exist;
    }
    retval = buffer;

    return retval;
}

void print_array(int * array, int length)
{
    while (length--)
    {
        printf("%d,", *array);
        *array++;
    }
    printf("\n");
}

int max(int * array, int length)
{
    int max = 0;

    for (int i = 0; i < length; i++)
    {
        max = (array[i] > max) ? array[i] : max;
    }

    return max;
}

int min(int * array, int length)
{
    int min = INT_MAX;

    for (int i = 0; i < length; i++)
    {
        min = (array[i] < min) ? array[i] : min;
    }

    return min;
}

long count_char(char * array, int length, char target)
{
    long result = 0;
    for (int i = 0; i < length; i++)
    {
        if (array[i] == target)
        {
            result++;
        }
    }
    return result;
}

char * strplace(char * array, char target, char replace)
{
    int i = 0;
    while (array[i] != 0)
    {
        char character = array[++i];
        array[i] = (array[i] == target) ? replace : target;
    }
    
    return array;
}

char sd_itoa(int input)
{
    return (char)(input + 48);
}

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
void alphabetise(char * arr, int n)
{
    int i, j, min_idx;
 
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n-1; i++)
    {
        // Find the minimum element in unsorted array
        min_idx = i;
        for (j = i+1; j < n; j++)
          if (arr[j] < arr[min_idx])
            min_idx = j;
 
        // Swap the found minimum element with the first element
        swap(&arr[min_idx], &arr[i]);
    }
}