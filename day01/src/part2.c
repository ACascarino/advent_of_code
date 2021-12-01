#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <sysexits.h>
#include "../../common_tools.h"

#define WINDOW_SIZE 3

int sum_array(int * arr, int n)
{
    int result = 0;
    for (int i = 0; i < n; i++)
    {
        result += arr[i];
    }
    return result;
}

void main()
{
    FileError f_err;
    size_t f_size;
    char * token;
    int a_sum, b_sum, result = 0;
    int a[WINDOW_SIZE], b[WINDOW_SIZE];

    // Read file
    char * input = c_read_file("input.txt", &f_err, &f_size);

    // Report issues
    if (f_err != File_OK)
    {
        exit(f_err + EX__BASE);
    }

    token = strtok(input, "\n");
    // Get first set
    for (int i = 0; (i < WINDOW_SIZE) && (token != NULL); i++)
    {
        a[i] = atoi(token);
        a_sum += a[i];
        token = strtok(NULL, "\n");
    }

    // Start loop
    do
    {
        for (int i = 0; i < WINDOW_SIZE - 1; i++)
        {
            b[i] = a[i + 1];
        }
        
        b[WINDOW_SIZE - 1] = atoi(token);

        a_sum = sum_array(a, WINDOW_SIZE);
        b_sum = sum_array(b, WINDOW_SIZE);

        printf("%d, %d, %d\n", a[0], a[1], a[2]);

        result += (b_sum > a_sum) ? 1 : 0;

        for (int i = 0; i < WINDOW_SIZE; i++)
        {
            a[i] = b[i];
        }

        token = strtok(NULL, "\n");
    } while (token != NULL);

    printf("%d\n", result);
 }