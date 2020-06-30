cmake_minimum_required (VERSION 3.5)

add_executable(Coding2SortingTest Test.cpp)

target_link_libraries(Coding2SortingTest PRIVATE
            header_lib
            libgtest
            source_lib
         )

add_test(
    NAME Coding2SortingTest
    COMMAND Coding2SortingTest
)