# Define the minimum CMake version, there are significant changes from version 3.15 on.
cmake_minimum_required(VERSION 3.15.0)

#Name of the project, version and language is specified
project(SAMPLE_PROJECT VERSION 1.0.0 )

# if(UNIX)
#     message(STATUS "COMPILING FOR UNIX : ${UNIX}")
#     #defines pragma for cmocka testing lib not defined by default on linux
#     add_definitions(-DHAVE_SIGNAL_H)  
# endif(UNIX)

add_subdirectory(src)

# Unit tests should be normally enabled
if(UNIT_TESTS)
message("Unit tests are enabled!")
enable_testing()
add_subdirectory(test)

    #Code coverage is tied to unit tests. To Enable coverage
    # configure cmake with (in addition to testing flag) -DCOVERAGE=ON
    if(COVERAGE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-arcs -ftest-coverage")
        message("Code coverage enabled!")
        set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/CMakeModules)
        include(CodeCoverage)
        SETUP_TARGET_FOR_COVERAGE(coverage ctest code_cov)
        # setup_target_for_coverage_gcovr_html(NAME coverage EXECUTABLE ctest -VV
        #                                     # tests and main executables are excluded from the report
        #                                      BASE_DIRECTORY "${PROJECT_SOURCE_DIR}/"
        #                                     #  EXCLUDE    "${PROJECT_SOURCE_DIR}/test/*" 
        #                                     )
    endif()
else()
    message("Unit tests are disabled!")
endif()


# Compiler flags:
### WARNINGS ###
# See https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html#Warning-Options:
# -Werror:      Turns all warnings into errors
# -pedantic:    Issue all the warnings demanded by strict ISO C
# -Wall:        This enables all warnings regarding constructions
# -Wextra:      This enables some extra warning flags
# -Wshadow:     Warn whenever a local variable or type declaration shadows 
#               another variable, parameter, type, ...
### Code Generation Conventions ###
# See https://gcc.gnu.org/onlinedocs/gcc/Code-Gen-Options.html#Code-Gen-Options:
# -ftrapv:      This option generates traps for signed overflow on addition, 
#               subtraction, multiplication
set(gcc_options 
    -Werror
    -pedantic
    -Wall
    -Wextra
    -Wshadow
    -ftrapv
)    

#sets the path for the executable 
set(EXECUTABLE_OUTPUT_PATH "bin")
