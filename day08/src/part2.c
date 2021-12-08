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

    int result = 0;

    int number_lines = count_char(input, f_size, '\n');
    char ** left_sides = (char **) calloc(number_lines, sizeof(char *));
    char ** right_sides = (char **) calloc(number_lines, sizeof(char *));

    char * left_side = strtok(input, "|");
    char * right_side = strtok(NULL, "\n");

    int i = 0;
    do
    {
        left_sides[i] = left_side;
        right_sides[i] = right_side;

        left_side = strtok(NULL, "|");
        right_side = strtok(NULL, "\n");

        i++;
    } while (left_side != NULL && right_side != NULL);
    
    for (int i = 0; i < number_lines; i++)
    {
        char * target_side = left_sides[i];
        
        char * map[10] = {0};
        char * remaining_tokens[6] = {0};

        char * token = strtok(target_side, " ");
        int j = 0;
        do
        {
            int len = strlen(token);

            if (len == 2)
            {
                map[1] = token;
            }
            else if (len == 3)
            {
                map[7] = token;
            }
            else if (len == 4)
            {
                map[4] = token;
            }
            else if (len == 7)
            {
                map[8] = token;
            }
            else
            {
                remaining_tokens[j++] = token;
            }
            token = strtok(NULL, " ");
        } while (token != NULL); 

        int remaining = j;
        while(j)
        {    
            for (int k = 0; k < remaining; k++)
            {
                char * target = remaining_tokens[k];
                if (target == NULL)
                {
                    continue;
                }

                int len = strlen(target);

                if (len == 5)
                {
                    // Must be 2, 3, or 5

                    // If contains all in 1, must be 3
                    int is_three = 1;
                    for (int m = 0; m < 2; m++)
                    {
                        is_three &= (strchr(target, map[1][m]) != NULL);
                    }
                    if (is_three)
                    {
                        map[3] = target;
                        remaining_tokens[k] = NULL;
                        j--;
                        continue;
                    }

                    // If contains all parts of 4 that aren't present in 1, must be 5
                    int is_five = 1;
                    int four_not_one_array[3] = {0};
                    int n = 0;
                    for (int m = 0; m < 4; m++)
                    {
                        int is_not_in_one = (strchr(map[1], map[4][m]) == NULL);
                        if (is_not_in_one)
                        {
                            four_not_one_array[n++] = map[4][m];
                        }
                    }
                    for (int m = 0; m < 2; m++)
                    {
                        is_five &= (strchr(target, four_not_one_array[m]) != NULL);
                    }
                    if (is_five)
                    {
                        map[5] = target;
                        remaining_tokens[k] = NULL;
                        j--;
                        continue;
                    }


                    // Else, must be 2
                    map[2] = target;
                    remaining_tokens[k] = NULL;
                    j--;
                }
                else if (len == 6)
                {
                    // Must be 0, 6, or 9

                    // If doesn't contain all in 1, must be 6
                    int is_six = 0;
                    for (int m = 0; m < 2; m++)
                    {
                        is_six |= (strchr(target, map[1][m]) == NULL);
                    }
                    if (is_six)
                    {
                        map[6] = target;
                        remaining_tokens[k] = NULL;
                        j--;
                        continue;
                    }

                    // If it doesn't contain all in 4, must be 0
                    int is_zero = 0;
                    for (int m = 0; m < 4; m++)
                    {
                        is_zero |= (strchr(target, map[4][m]) == NULL);
                    }
                    if (is_zero)
                    {
                        map[0] = target;
                        remaining_tokens[k] = NULL;
                        j--;
                        continue;
                    }

                    // Otherwise, it must be 9
                    map[9] = target;
                    remaining_tokens[k] = NULL;
                    j--;
                }
            }
        }

        // Do other computation
        target_side = right_sides[i];
        char composite[5] = {0};
        token = strtok(target_side, " ");
        int k = 0;
        
        do
        {
            int len = strlen(token);
            for (int j = 0; j < 10; j++)
            {
                if ((len == strspn(map[j], token)) && (len == strlen(map[j])))
                {
                    composite[k++] = sd_itoa(j);
                    break;
                };
            }
            token = strtok(NULL, " ");
        } while (token != NULL);

        result += atoi(composite);
    }

    free(left_sides);
    free(right_sides);
    printf("%d\n", result);
}