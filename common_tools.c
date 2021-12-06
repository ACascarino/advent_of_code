#include <stdio.h>
#include <stdlib.h>
#include "common_tools.h"

// From https://stackoverflow.com/a/54057690/3791827

char * c_read_file(const char * f_name, FileError * err, size_t * f_size) 
{
    char * buffer;
    size_t length;
    FILE * f = fopen(f_name, "rb");
    size_t read_length;
    char * retval = NULL;

    if (f) 
    {
        fseek(f, 0, SEEK_END);
        length = ftell(f);
        fseek(f, 0, SEEK_SET);
        
        // 1 GiB; best not to load a whole large file in one string
        if (length > 1073741824) 
        {
            *err = File_Too_Large;
        }
        
        buffer = (char *)malloc(length + 1);
        
        if (length) 
        {
            read_length = fread(buffer, 1, length, f);
            
            if (length != read_length) 
            {
                 free(buffer);
                 *err = File_Read_Error;
            }
        }
        
        fclose(f);
        
        *err = File_OK;
        buffer[length] = '\0';
        *f_size = length;
    }
    else 
    {
        *err = File_Not_Exist;
    }
    retval = buffer;

    return retval;
}

void print_array(int * array, int length)
{
    while (length--)
    {
        printf("%d", *array);
        *array++;
    }
    printf("\n");
}

int max(int * array, int length)
{
    int max = 0;

    for (int i = 0; i < length; i++)
    {
        if (array[i] > max)
        {
            max = array[i];
        }
    }

    return max;
}