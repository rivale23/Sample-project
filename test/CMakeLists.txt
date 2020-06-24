# Defining the minimum version
cmake_minimum_required(VERSION 3.15.0)

# Defining the language
project(edr_global LANGUAGES C)

# Defining some C flags
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fprofile-arcs -ftest-coverage")

# This cmake file is for testing, hence testing has to be enabled
enable_testing()

function(set_target_compile_options INPUT_TARGET)
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
    target_compile_options(${INPUT_TARGET} INTERFACE 
        $<${gcc_like_c}:${BUILD_INTERFACE}:${gcc_options}>
    )

    # Printing compile options to see if they were set correctly
    get_property(target_name TARGET ${INPUT_TARGET} PROPERTY NAME)
    get_property(compile_flags TARGET ${INPUT_TARGET} PROPERTY INTERFACE_COMPILE_OPTIONS)
    message("${target_name} compile flags via function: \t${compile_flags}")
endfunction()


# Adding the subdirectories to look for tests
add_subdirectory(cmocka)
add_subdirectory(unit_tests)