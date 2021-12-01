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

#endif // ifndef COMMON_TOOLS_H