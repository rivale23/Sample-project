# We need thread support
find_package(Threads REQUIRED)
set(CMAKE_CXX_FLAGS "-Wno-deprecated-declarations")
# Enable ExternalProject CMake module
include(ExternalProject)

# Download and install GoogleTest
ExternalProject_Add(
    gtest
    URL https://github.com/google/googletest/archive/master.zip
    PREFIX ${CMAKE_CURRENT_BINARY_DIR}/gtest
    # Disable install step
    INSTALL_COMMAND ""
)

# Get GTest source and binary directories from CMake project
ExternalProject_Get_Property(gtest source_dir binary_dir)

set(GTEST_INCLUDE_DIR ${source_dir}/googletest/include)
set(GTEST_LIBRARY_PATH ${binary_dir}/lib/libgtest.a)

file(MAKE_DIRECTORY ${GTEST_INCLUDE_DIR})
# Create a libgtest target to be used as a dependency by test programs
add_library(libgtest IMPORTED STATIC GLOBAL)

set_property(TARGET libgtest PROPERTY IMPORTED_LOCATION  ${GTEST_LIBRARY_PATH})
set_property(TARGET libgtest APPEND PROPERTY INTERFACE_INCLUDE_DIRECTORIES ${GTEST_INCLUDE_DIR})

add_dependencies(libgtest gtest)
# Create a libgmock target to be used as a dependency by test programs


enable_testing()
add_subdirectory(Sorter_test)