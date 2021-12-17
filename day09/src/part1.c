#include "../../common_tools.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <sysexits.h>

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

    int number_of_lines = count_char(input, f_size, '\n');
    int number_of_cols = strcspn(input, "\n");
    int board[number_of_lines][number_of_cols];
    int marked[number_of_lines][number_of_cols];
    int diff_board[number_of_lines][number_of_cols-1];
    int risk_level = 0;

    for (int i = 0, k = 0; i < number_of_lines; i++)
    {
        for (int j = 0; j < number_of_cols; j++)
        {
            board[i][j] = ctoi(input[k++]);
            marked[i][j] = 0;
            k += (input[k] == '\n');
        }
        diff(board[i], diff_board[i], number_of_cols);
    }

    for (int i = 0; i < number_of_lines; i++)
    {
        for (int j = 0; j < number_of_cols-1; j++)
        {
            if (diff_board[i][j] < 0)
            {
                if ((j == number_of_cols - 2) || (diff_board[i][j + 1] > 0))
                {
                    marked[i][j + 1] = 1;
                }
            }
            else if (j == 0)
            {
                marked[i][0] = 1;
            }
        }
    }

    for (int i = 0; i < number_of_lines; i++)
    {
        for (int j = 0; j < number_of_cols; j++)
        {
            if (marked[i][j])
            {
                int do_up = (i != 0);
                int do_down = (i != number_of_lines-1);
                int result = 1;

                if (do_up)
                {
                    result &= (board[i-1][j] > board[i][j]);
                }
                if (do_down)
                {
                    result &= (board[i+1][j] > board[i][j]);
                }

                marked[i][j] &= result;
            }
            if (marked[i][j])
            {
                risk_level += board[i][j] + 1;
            }
        }
    }
    printf("%d\n", risk_level);
}