

add_library(sorter_lib
  include/Sorter.h
  Sorter.cpp
)


# include directories exported by this library
target_include_directories(sorter_lib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

set_target_properties(sorter_lib PROPERTIES LINKER_LANGUAGE CXX)