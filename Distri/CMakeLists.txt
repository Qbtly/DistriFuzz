cmake_minimum_required(VERSION 3.27)
project(DistriFuzz C)

set(CMAKE_C_STANDARD 11)

add_executable(DistriFuzz main.c
        fuzz2.c
        temp.c
        tt.c)
