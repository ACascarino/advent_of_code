#include "../../common_tools.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <sysexits.h>

int get_error(int * array, int length, int target)
{
    int error = 0;
    for (int i = 0; i < length; i++)
    {
        int pos_error = abs(array[i] - target);
        error += ((pos_error * (pos_error + 1))/2);
    }
    return error;
}

void main()
{
    FileError f_err;
    size_t f_size;

    // Read file
    char * input = c_read_file("input.txt", &f_err, &f_size);

    // Report issues
    if (f_err != File_OK)
    {
        exit(f_err + EX__BASE);
    }

    int crab_count = count_char(input, f_size, ',') + 1;

    int starting_array[crab_count];
    int i = 0;
    char * token = strtok(input, ",");
    do
    {
        starting_array[i] = atoi(token);
        token = strtok(NULL, ",");
        i++;
    } while (token != NULL);
    
    int max_pos = max(starting_array, crab_count);
    int minimum_error = INT_MAX;

    for (i = 0; i <= max_pos; i++)
    {
        int target_error = get_error(starting_array, crab_count, i);
        if (target_error < minimum_error)
        {
            minimum_error = target_error;
        }
    }

    printf("%d\n", minimum_error);
}