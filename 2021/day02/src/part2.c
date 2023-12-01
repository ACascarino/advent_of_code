#include <string.h>
#include <sysexits.h>
#include <stdio.h>
#include <stdlib.h>
#include "../../common_tools.h"

typedef enum 
{
    Forward = 1,
    Down = 1,
    Up = -1
} DirectionEnum;

void main()
{
    FileError f_err;
    size_t f_size;
    char * token;
    long horz_pos = 0, depth_pos = 0, aim = 0;
    long result = 0;

    // Read file
    char * input = c_read_file("input.txt", &f_err, &f_size);
    // Report issues
    if (f_err != File_OK)
    {
        exit(f_err + EX__BASE);
    }

    // Loop over lines 
    token = strtok(input, "\n");
    while (token != NULL)
    {
        char * dir_string;
        int distance;
        DirectionEnum direction;
        int depth = 1;
        
        // Get direction and distance
        sscanf(token, "%s %d", dir_string, &distance);

        if (dir_string[0] == 'f')
        {
            direction = Forward;
            depth = 0;
        }
        else if (dir_string[0] == 'd')
        {
            direction = Down;
        }
        else
        {
            direction = Up;
        }

        // Add to the relevant variable
        if (depth)
        {
            aim += (direction * distance);
        }
        else
        {
            horz_pos += (direction * distance);
            depth_pos += (direction * distance * aim);
        }

        // Continue
        token = strtok(NULL, "\n");
    }

    result = horz_pos * depth_pos;

    printf("%ld\n", result);
}