#ifndef COMMON_TOOLS_H
#define COMMON_TOOLS_H

#include <stddef.h>

typedef enum 
{
    File_OK,
    File_Not_Exist,
    File_Too_Large,
    File_Read_Error
} FileError;

char * c_read_file(const char * f_name, FileError * err, size_t * f_size);
int max(int * array, int length);
int min(int * array, int length);
void print_array(int * array, int length);
long count_char(char * array, int length, char target);
char * strplace(char * array, char target, char replace);
char sd_itoa(int input);
int ctoi(char input);
void diff(int * input, int * output, int length);

#endif // ifndef COMMON_TOOLS_H