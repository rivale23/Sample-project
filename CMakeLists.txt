# Define the minimum CMake version, there are significant changes from version 3.15 on.
cmake_minimum_required(VERSION 3.15.0)

#Name of the project, version and language is specified
project(SAMPLE_PROJECT VERSION 1.0.0 )

if(UNIX)
    message(STATUS "COMPILING FOR UNIX : ${UNIX}")
    #defines pragma for cmocka testing lib not defined by default on linux
    add_definitions(-DHAVE_SIGNAL_H)  
endif(UNIX)


# Unit tests should be normally enabled
if(UNIT_TESTS)
    message("Unit tests are enabled!")
    enable_testing()
    add_subdirectory(test)
    
    #Code coverage is tied to unit tests. To Enable coverage
    # configure cmake with (in addition to testing flag) -DCOVERAGE=ON
    if(COVERAGE)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-arcs -ftest-coverage")
        message("Code coverage enabled!")
        set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/CMakeModules)
        include(CodeCoverage)
        setup_target_for_coverage_gcovr_html(NAME coverage EXECUTABLE ctest -VV
                                            # tests and main executables are excluded from the report
                                             EXCLUDE    "${PROJECT_SOURCE_DIR}/test/*" 
                                            )
    endif()
else()
    message("Unit tests are disabled!")
endif()

# If you set any CMAKE_ variables, that can go here.
# 
# Find packages go here.
add_subdirectory(include)
add_subdirectory(src)

# Adding some executable - Output name matches target name
add_executable (${PROJECT_NAME} main.c)
target_link_libraries(${PROJECT_NAME} PUBLIC
    header_lib
    )


# List of some (not all) compiler ID's [CMAKE_<LANG>_COMPILER_ID]:
# Clang = LLVM Clang (clang.llvm.org)
# GNU = GNU Compiler Collection (gcc.gnu.org)
# Intel = Intel Compiler (intel.com)
# MSVC = Microsoft Visual Studio (microsoft.com)
set(gcc_like_c "$<$<COMPILE_LANG_AND_ID:C,Clang,GNU,MSVC")

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

# Looking at this we see that the warning flags are encapsulated inside a 
# BUILD_INTERFACE condition. This is done so that consumers of our installed
# project will not inherit our warning flags.
target_compile_options(${PROJECT_NAME} INTERFACE 
    $<${gcc_like_c}:${BUILD_INTERFACE}:${gcc_options}>
)

# Printing compile options to see if they were set correctly
get_property(compile_flags TARGET ${PROJECT_NAME} PROPERTY INTERFACE_COMPILE_OPTIONS)
message("${PROJECT_NAME} compile options: \t\t${compile_flags}")

#sets the path for the executable 
set(EXECUTABLE_OUTPUT_PATH "bin")
