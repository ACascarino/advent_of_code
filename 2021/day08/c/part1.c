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

    int number_lines = count_char(input, f_size, '\n');
    char ** left_sides = (char **) calloc(number_lines, sizeof(char *));
    char ** right_sides = (char **) calloc(number_lines, sizeof(char *));
    int i = 0;
    int result = 0;

    char * left_side = strtok(input, "|");
    char * right_side = strtok(NULL, "\n");

    do
    {
        left_sides[i] = left_side;
        right_sides[i] = right_side;

        left_side = strtok(NULL, "|");
        right_side = strtok(NULL, "\n");

        i++;
    } while (left_side != NULL && right_side != NULL);
    
    for (i = 0; i < number_lines; i++)
    {
        char * target_side = right_sides[i];
        char * token = strtok(target_side, " ");
        do
        {
            int len = strlen(token);
            if ((len == 2) || (len == 3) || (len == 4) || (len == 7))
            {
                result += 1;
            }
            token = strtok(NULL, " ");
        } while (token != NULL); 
    }
    printf("%d\n", result);
}