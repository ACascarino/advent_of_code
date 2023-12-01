#include <sysexits.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "../../common_tools.h"

void get_all_coords(int x1, int x2, int y1, int y2, int ** p_coord_x, int ** p_coord_y, int * p_length)
{
    int length;
    int reverse = 0;
    int up_down = 0;
    int diagonal = 0;
    int x, y, i, j;

    if (x1 == x2)
    {
        length = abs(y2 - y1) + 1;
        if (y1 > y2)
        {
            reverse = 1;
        }
    }
    else if (y1 == y2)
    {
        length = abs(x2 - x1) + 1;
        if (x1 > x2)
        {
            reverse = 1;
        }
    }
    else
    {
        diagonal = 1;
        length = abs(x2 - x1) + 1;
    }

    int * coord_x = (int *) calloc(length, sizeof(int));
    int * coord_y = (int *) calloc(length, sizeof(int));

    if (diagonal)
    {
        if (y1 > y2)
        {
            // Diagonal upward
            if (x1 > x2)
            {
                // Diagonal up left
                for (int i = 0; i < length; i++)
                {
                    coord_x[i] = x1 - i; 
                    coord_y[i] = y1 - i;
                }
            }
            else
            {
                // Diagonal up right
                for (int i = 0; i < length; i++)
                {
                    coord_x[i] = x1 + i; 
                    coord_y[i] = y1 - i;
                }
            }
        }
        else
        {
            // Diagonal downward
            if (x1 > x2)
            {
                // Diagonal down left
                for (int i = 0; i < length; i++)
                {
                    coord_x[i] = x1 - i; 
                    coord_y[i] = y1 + i;
                }
            }
            else
            {
                // Diagonal down right
                for (int i = 0; i < length; i++)
                {
                    coord_x[i] = x1 + i; 
                    coord_y[i] = y1 + i;
                }
            }
        }
    }
    else
    {
        for (i = 0, y = (reverse ? y2 : y1); y <= (reverse ? y1 : y2); y++, i++)
        {
            for (j = 0, x = (reverse ? x2 : x1); x <= (reverse ? x1 : x2); x++, j++)
            {
                coord_x[i+j] = x;
                coord_y[i+j] = y;
            }
        }
    }
    

    *p_coord_x = coord_x;
    *p_coord_y = coord_y;
    *p_length = length;
}

void main()
{
    FileError f_err;
    size_t f_size;
    long result = 0;
    int x1, x2, y1, y2;
    int * x_set = NULL;
    int * y_set = NULL;
    int set_len = 0;

    // Read file
    char * input = c_read_file("input.txt", &f_err, &f_size);

    // Report issues
    if (f_err != File_OK)
    {
        exit(f_err + EX__BASE);
    }

    char * token = strtok(input, "\n");

    do
    {
        int * coord_x, * coord_y;
        int length;
        
        sscanf(token, "%d,%d -> %d,%d", &x1, &y1, &x2, &y2);
        get_all_coords(x1, x2, y1, y2, &coord_x, &coord_y, &length);

        int new_len = length + set_len;
        x_set = (int *) realloc(x_set, new_len * sizeof(int));
        y_set = (int *) realloc(y_set, new_len * sizeof(int));

        memcpy(x_set+set_len, coord_x, length * sizeof(int));
        memcpy(y_set+set_len, coord_y, length * sizeof(int));

        set_len = new_len;

        free(coord_x);
        free(coord_y);

        token = strtok(NULL, "\n");
    } while (token != NULL);

    int max_x = max(x_set, set_len);
    int max_y = max(y_set, set_len);

    int ** grid = (int **) calloc(max_y+1, sizeof(int *));
    for (int i = 0; i < max_y+1; i++)
    {
        grid[i] = (int *) calloc(max_x+1, sizeof(int));
    }

    for (int i = 0; i < set_len; i++)
    {
        int x = x_set[i];
        int y = y_set[i];
        grid[y][x]++;
    }

    for (int y = 0; y <= max_y; y++)
    {
        for (int x = 0; x <= max_x; x++)
        {
            if (grid[y][x] > 1)
            {
                result++;
            }
        }
    }

    for (int i = 0; i < max_y+1; i++)
    {
        free(grid[i]);
    }
    free(grid);
    free(x_set);
    free(y_set);

    printf("%ld\n", result);
}
