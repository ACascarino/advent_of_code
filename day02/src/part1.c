#include <string.h>
#include <sysexits.h>
#include "../../common_tools.h"

typedef enum 
{
    Forward,
    Down,
    Up
} DirectionEnum;

void main()
{
    FileError f_err;
    size_t f_size;
    char * token;
    int a, b, result = 0;

    // Read file
    char * input = c_read_file("input.txt", &f_err, &f_size);
    // Report issues
    if (f_err != File_OK)
    {
        exit(f_err + EX__BASE);
    }

    
}