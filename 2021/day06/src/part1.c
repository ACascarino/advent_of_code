#include "../../common_tools.h"
#include <sysexits.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define AGES      9
#define MATURITY  (AGES-1)
#define CYCLE_LEN (MATURITY-2)
#define DAYS      80

void advance(int * population)
{
    int new_pop[AGES];
    for (int age = AGES-1; age >= 0; age--)
    {
        if (age == MATURITY)
        {
            new_pop[age] = population[0];
        }
        else
        {
            new_pop[age] = population[age+1];
        }

        if (age == CYCLE_LEN)
        {
            new_pop[age] += population[0];
        }
    }

    for (int age = AGES-1; age >= 0; age--)
    {
        population[age] = new_pop[age];
    }

}

void main()
{
    FileError f_err;
    size_t f_size;
    long result = 0;

    // Read file
    char * input = c_read_file("input.txt", &f_err, &f_size);

    // Report issues
    if (f_err != File_OK)
    {
        exit(f_err + EX__BASE);
    }

    int population[AGES] = {0};

    char * token = strtok(input, ",");

    do
    {
        int age = atoi(token);
        population[age]++;
        token = strtok(NULL, ",");
    } 
    while (token != NULL);

    for (int age = 0; age < AGES; age++)
    {
        printf("%d:%d\n", age, population[age]);
    }

    printf("-\n");

    for (int i = 0; i < DAYS; i++)
    {
        advance(population);
    }

    for (int age = 0; age < AGES; age++)
    {
        result += population[age];
        printf("%d:%d\n", age, population[age]);
    }

    printf("%ld\n", result);
}