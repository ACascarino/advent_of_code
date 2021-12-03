#include <sysexits.h>
#include "../../common_tools.h"
#include <stdlib.h>
#include <stdio.h>

#define BIT_LENGTH 12

void main()
{
    FileError f_err;
    size_t f_size;
    char * token;
    int gamma = 0, epsilon = 0;
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

    for (int c = BIT_LENGTH - 1; c >= 0; c--)
    {
        int count_0 = 0, count_1 = 0;
        for (int r = 0; r < num_rows; r++)
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
        gamma += (count_0 > count_1) ? 0 : (1 << (BIT_LENGTH - c - 1));
        epsilon += (count_0 < count_1) ? 0 : (1 << (BIT_LENGTH - c - 1));
    }

    result = gamma * epsilon;

    printf("%ld\n", result);
}