#include <sysexits.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "../../common_tools.h"

void get_all_coords(int x1, int x2, int y1, int y2, int ** p_coord_x, int ** p_coord_y, int * p_length)
{
    int length;
    int reverse = 0;
    int x, y, i, j;

    if (x1 == x2)
    {
        length = abs(y2 - y1) + 1;
        if (y1 > y2)
        {
            reverse = 1;
        }
    }
    else
    {
        length = abs(x2 - x1) + 1;
        if (x1 > x2)
        {
            reverse = 1;
        }
    }

    int * coord_x = (int *) calloc(length, sizeof(int));
    int * coord_y = (int *) calloc(length, sizeof(int));

    for (i = 0, y = (reverse ? y2 : y1); y <= (reverse ? y1 : y2); y++, i++)
    {
        for (j = 0, x = (reverse ? x2 : x1); x <= (reverse ? x1 : x2); x++, j++)
        {
            coord_x[j] = x;
            coord_y[i] = y;
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
    int x1, x2, y1, y2, x, y;

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
        sscanf(token, "%d,%d -> %d,%d", &x1, &y1, &x2, &y2);
        if ((x1 == x2) || (y1 == y2))
        {
            int * coord_x, * coord_y;
            int i, j = 0, length = 0;
            get_all_coords(x1, x2, y1, y2, &coord_x, &coord_y, &length);

            free(coord_x);
            free(coord_y);
        }
        token = strtok(NULL, "\n");
    } while (token != NULL);
}
