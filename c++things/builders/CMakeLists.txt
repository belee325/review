cmake_minimum_required(VERSION 3.12)
project(builders)

set(CMAKE_CXX_STANDARD 17)

add_executable(builders main.cpp PersonBuilder.cpp PersonBuilder.h)