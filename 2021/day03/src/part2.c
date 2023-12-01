#include <sysexits.h>
#include "../../common_tools.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define BIT_LENGTH 12

int get_target(char * system, int count_0, int count_1)
{
    if (strcmp(system, "o2"))
    {
        return (count_0 > count_1) ? 0 : 1;
    }
    else
    {
        return (count_0 <= count_1) ? 0 : 1;
    }
}

int find_value(int ** bit_array, int rows, int cols, char * system)
{
    int value = 0;
    int count_skipped = 0;

    // Set up the "skipped" array
    int skip_array[rows];
    memset(skip_array, 0, sizeof(skip_array));
    
    for (int c = 0; c < cols; c++)
    {
        int count_0 = 0, count_1 = 0; 
        for (int r = 0; r < rows; r++)
        {
            if (!skip_array[r])
            {
                if (bit_array[r][c] == 0)
                {
                    count_0++;
                }
                else
                {
                    count_1++;
                }
            }
        }

        int target = get_target(system, count_0, count_1);

        // Add this row to the skipped array if it doesn't meet the criteria
        for (int r = 0; r < rows; r++)
        {
            if ((bit_array[r][c] != target) && !skip_array[r])
            {
                skip_array[r] = 1;
                count_skipped++;
            }
        }
        // Return condition - we've got one row left. Parse and return.
        if (count_skipped == (rows - 1))
        {
            int * target_row;
            for (int r = 0; r < rows; r++)
            {
                if (skip_array[r] == 0)
                {
                    target_row = bit_array[r];
                    break;
                }
            }

            for (int i = cols - 1; i >= 0; i--)
            {
                value += (target_row[i] == 0) ? 0 : (1 << (cols - 1 - i));
            }
            return value;
        }
    }
}

void main()
{
    FileError f_err;
    size_t f_size;
    long result = 0;

    // Read file
    char * input = c_read_file("input.txt", &f_err, &f_size);

    // Report issues
    if (f_err != File_OK)
    {
        exit(f_err + EX__BASE);
    }

    // This assumes all the lines are the same size!
    const int num_rows = f_size / (BIT_LENGTH + 1);

    // Set up the array of bits - goal is "001\n101" -> [[0, 0, 1], [1, 0, 1]]
    int ** bit_array = (int **) malloc(f_size * sizeof(int));
    for (int i = 0; i < num_rows; i++)
    {
        bit_array[i] = (int *) malloc(BIT_LENGTH * sizeof(int));
    }

    // k is the index through the input string
    // i is the row
    // j is the column
    unsigned int i = 0, j = 0, k = 0;
    for (; k < f_size - 1; k++)
    {
        const char inchar = input[k];
        if (inchar == '0')
        {
            bit_array[i][j] = 0;
            j++;
        }
        else if (inchar == '1')
        {
            bit_array[i][j] = 1;
            j++;
        }
        else if (inchar == '\n')
        {
            j = 0;
            i++;
        }
        else break;
    }

    int oxygen = find_value(bit_array, num_rows, BIT_LENGTH, "o2");
    int co2 = find_value(bit_array, num_rows, BIT_LENGTH, "co2");

    result = oxygen * co2;

    printf("%ld\n", result);

    for (int i = 0; i < num_rows; i++)
    {
        free(bit_array[i]);
    }
    
    free(bit_array);
}