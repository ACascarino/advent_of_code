#include <stdio.h>
#include <sysexits.h>
#include <stdlib.h>
#include <string.h>
#include "../../common_tools.h"

#define BOARD_SIZE 5

typedef struct Board
{
    int * rows[BOARD_SIZE];
    int * marked[BOARD_SIZE];
    int has_won;
} Board;

void init_Board(Board * board, char * board_string, int board_length)
{
    board->has_won = 0;
    
    for (int i = 0; i < BOARD_SIZE; i++)
    {
        board->rows[i] = (int *) calloc(BOARD_SIZE, sizeof(int));
        board->marked[i] = (int *) calloc(BOARD_SIZE, sizeof(int));
    }
    
    int i = 0, j = 0;

    for (int k = 0; k < board_length; k++)
    {
        char target_1 = board_string[k];
        if ((target_1 != ' ') && (target_1 != '\n'))
        {
            char target_2 = board_string[k+1];
            if ((target_2 != ' ') && (target_2 != '\n'))
            {
                char target_str[3] = {target_1, target_2, '\0'};
                board->rows[j][i] = atoi(target_str);
                i++;
                k++;
            }
            else
            {
                char target_str[2] = {target_1, '\0'};
                board->rows[j][i] = atoi(target_str);
                i++;
            }
        }
        else if (target_1 == ' ')
        {
            continue;
        }
        else
        {
            i = 0;
            j++;
        }
    }
}

void destroy_Board(Board * board)
{
    for (int i = 0; i < BOARD_SIZE; i++)
    {
        free(board->rows[i]);
        free(board->marked[i]);
    }
}

int check_row_Board(Board * board, int index)
{
    int * target_row = board->marked[index];
    for (int i = 0; i < BOARD_SIZE; i++)
    {
        if (target_row[i] != 1)
        {
            return 0;
        }
    }
    return 1;
}

int check_column_Board(Board * board, int index)
{
    for (int row = 0; row < BOARD_SIZE; row++)
    {
        if (board->marked[row][index] != 1)
        {
            return 0;
        }
    }
    return 1;
}

int check_Board(Board * board)
{
    for (int i = 0; i < BOARD_SIZE; i++)
    {
        if (check_row_Board(board, i) || check_column_Board(board, i))
        {
            return 1;
        }
    }
    return 0;
}

int do_move_Board(Board * board, int move)
{
    for (int j = 0; j < BOARD_SIZE; j++)
    {
        for (int i = 0; i < BOARD_SIZE; i++)
        {
            if (board->rows[j][i] == move)
            {
                board->marked[j][i] = 1;
            }
        }
    }
}

long int score_Board(Board * board, int winning_no)
{
    long int result = 0;
    for (int j = 0; j < BOARD_SIZE; j++)
    {
        for (int i = 0; i < BOARD_SIZE; i++)
        {
            if (board->marked[j][i])
            {
                continue;
            }
            else
            {
                result += board->rows[j][i];
            }
        }
    }

    return result * winning_no; 
}

int all_boards_won_Board_Array(Board * board_array, int board_count)
{
    int result = 0;
    
    for (int i = 0; i < board_count; i++)
    {
        result += board_array[i].has_won;
    }

    return (result == board_count);
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

    char * rest = strstr(input, "\n\n") + 2; // \n\n before first board
    char * inst = strtok(input, "\n");       // Instruction line
    char * new_rest = strstr(rest, "\n\n");  // \n\n before second board
    int board_len = (int) (new_rest - rest);
    int board_count = (strlen(rest)+1)/(board_len+2);
    Board boardArray[board_count];

    for (int i = 0; i < board_count; i++)
    {
        new_rest = strstr(rest, "\n\n");
        init_Board(&boardArray[i], rest, board_len);
        rest = new_rest + 2;
    }

    char * move_str = strtok(inst, ",");
    int board_wins, board_idx, move;
    int all_boards_won = 0;
    do
    {
        move = atoi(move_str);
        for (board_idx = 0; board_idx < board_count; board_idx++)
        {
            Board * target_board = &boardArray[board_idx];
            do_move_Board(target_board, move);
            board_wins = check_Board(target_board);
            if (board_wins)
            {
                target_board->has_won = 1;
            }
            all_boards_won = all_boards_won_Board_Array(boardArray, board_count);
            if (all_boards_won)
            {
                break;
            }
        }
        move_str = strtok(NULL, ",");
    } 
    while (move_str != NULL && !all_boards_won);
    
    result = score_Board(&boardArray[board_idx], move);

    printf("%ld\n", result);

    for (int i = 0; i < board_count; i++)
    {
        destroy_Board(&boardArray[i]);
    }
}