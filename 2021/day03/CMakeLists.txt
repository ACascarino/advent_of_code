cmake_minimum_required(VERSION 3.22)
project(AOC21   VERSION 1.0
                LANGUAGES C)

set(CMAKE_BUILD_TYPE Debug)

add_executable(part1 c/part1.c ../common_tools.c)
add_executable(part2 c/part2.c ../common_tools.c)