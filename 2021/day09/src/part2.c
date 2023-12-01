#include "../../common_tools.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <sysexits.h>

#define MIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define MAX(X, Y) ((X) > (Y) ? (X) : (Y))

typedef enum Direction 
{
    Up,
    Down,
    Left,
    Right
} Direction_t;

int get_neighbour(Direction_t dir, int x, int x_max, int y, int y_max, int board[y_max][x_max])
{
    switch (dir)
    {
        case Up:
            return board[y-1][x];
        case Left:
            return board[y][x-1];
        case Down:
            return board[y+1][x];
        case Right:
            return board[y][x+1];
    }
}

int replace(int from, int to, int x_max, int y_max, int board[y_max][x_max])
{
    for (int y = 0; y < y_max; y++)
    {
        for (int x = 0; x < x_max; x++)
        {
            if (board[y][x] == from)
            {
                board[y][x] = to;
            }
        }
    }
}  

int get_largest_neighbour_not_int_max(int x, int x_max, int y, int y_max, int board[y_max][x_max])
{
    int up = (y == 0) ? 0 : get_neighbour(Up, x, x_max, y, y_max, board);
    int down = (y == y_max - 1) ? 0 : get_neighbour(Down, x, x_max, y, y_max, board);
    int left = (x == 0) ? 0 : get_neighbour(Left, x, x_max, y, y_max, board);
    int right = (x == x_max - 1) ? 0 : get_neighbour(Right, x, x_max, y, y_max, board);

    up = (up == INT_MAX) ? 0 : up;
    down = (down == INT_MAX) ? 0 : down;
    left = (left == INT_MAX) ? 0 : left;
    right = (right == INT_MAX) ? 0 : right;

    int max_neighbour = MAX(MAX(left, right), MAX(up, down));
    return (max_neighbour == 0) ? INT_MAX : max_neighbour;
}

int get_smallest_neighbour(int x, int x_max, int y, int y_max, int board[y_max][x_max])
{
    int up = (y == 0) ? INT_MAX : get_neighbour(Up, x, x_max, y, y_max, board);
    int down = (y == y_max - 1) ? INT_MAX : get_neighbour(Down, x, x_max, y, y_max, board);
    int left = (x == 0) ? INT_MAX : get_neighbour(Left, x, x_max, y, y_max, board);
    int right = (x == x_max - 1) ? INT_MAX : get_neighbour(Right, x, x_max, y, y_max, board);

    int min_neighbour = MIN(MIN(left, right), MIN(up, down));
    return min_neighbour;
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

    int number_of_nines = count_char(input, f_size, '9');
    int number_of_lines = count_char(input, f_size, '\n');
    int number_of_cols = strcspn(input, "\n");
    int number_of_elems = number_of_lines * number_of_cols;
    int board[number_of_lines][number_of_cols];
    int basin_board[number_of_lines][number_of_cols];
    int basin_tracker = 1;
    long result = 0;

    for (int i = 0, k = 0; i < number_of_lines; i++)
    {
        for (int j = 0; j < number_of_cols; j++)
        {
            board[i][j] = ctoi(input[k++]);
            basin_board[i][j] = INT_MAX;
            k += (input[k] == '\n');
        }
    }

    for (int i = 0; i < number_of_lines; i++)
    {
        for (int j = 0; j < number_of_cols; j++)
        {
            if (board[i][j] != 9)
            {
                int smallest_neighbour = get_smallest_neighbour(j, number_of_cols, i, number_of_lines, basin_board);
                int largest_neighbour = get_largest_neighbour_not_int_max(j, number_of_cols, i, number_of_lines, basin_board);

                if (smallest_neighbour == largest_neighbour)
                {
                    if (smallest_neighbour == INT_MAX)
                    {
                        basin_board[i][j] = basin_tracker++;
                    }
                    else
                    {
                        basin_board[i][j] = smallest_neighbour;
                    }
                }
                else
                {
                    basin_board[i][j] = smallest_neighbour;
                    replace(largest_neighbour, smallest_neighbour, number_of_cols, number_of_lines, basin_board);
                    basin_tracker--;
                    for (int k = largest_neighbour; k < basin_tracker; k++)
                    {
                        replace(k+1, k, number_of_cols, number_of_lines, basin_board);
                    }
                }
            }
        }
    }
    basin_tracker--;
    replace(INT_MAX, 0, number_of_cols, number_of_lines, basin_board);

    int * basin_sizes = (int *) calloc(basin_tracker + 1, sizeof(int));
    int max_size = 0;
    for (int i = 0; i < number_of_lines; i++)
    {
        for (int j = 0; j < number_of_cols; j++)
        {
            int target = basin_board[i][j];

            if (target != 0)
            {
                int new_size = basin_sizes[target] + 1;
                basin_sizes[target] = new_size;
                max_size = MAX(max_size, new_size);
            }
        }
    }
    int * basin_sizes_counts = (int *) calloc(max_size + 1, sizeof(int));
    for (int i = 1; i < basin_tracker+1; i++)
    {
        basin_sizes_counts[basin_sizes[i]]++;
    }

    int counted = basin_sizes_counts[max_size];
    if (counted < 3)
    {
        int next_size = max_size;
        do
        {
            next_size--;
        } 
        while (!basin_sizes_counts[next_size]);

        int next_count = basin_sizes_counts[next_size];
        if (counted + next_count < 3)
        {
            int final_size = next_size;
            do
            {
                final_size--;
            } 
            while (!basin_sizes_counts[final_size]);

            result = max_size * next_size * final_size;
        }
        else
        {
            result = (counted == 2) ? (max_size * max_size * next_size) : (max_size * next_size * next_size);
        }
    }
    else
    {
        result = max_size * max_size * max_size;
    }
    

    printf("%ld\n", result);
}