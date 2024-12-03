#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <sysexits.h>
#include "../../common_tools.h"

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
    // Get first token
    token = strtok(input, "\n");
    a = atoi(token);

    token = strtok(NULL, "\n");

    // Start loop
    do
    {
        b = atoi(token);
        result += (b > a) ? 1 : 0;
        a = b;
        token = strtok(NULL, "\n");
    } while (token != NULL);

    printf("%d\n", result);
}