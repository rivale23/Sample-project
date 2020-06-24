#cmocka header files
file(
        GLOB
        cmocka_header_files
        include/*.h
    )

#cmocka source files
file(
        GLOB 
        cmocka_source_files 
        src/*.c
        src/cmocka.def
    )

#compile cmocka as a static lib
add_library(
        cmocka_testing_lib 
        STATIC               
        ${cmocka_header_files}
        ${cmocka_source_files}
    )    

#PUBLIC : consumers of this lib must include it using `target_include_directories` 
    target_include_directories(
    cmocka_testing_lib
    PUBLIC
    "${CMAKE_CURRENT_SOURCE_DIR}/include"
)
    