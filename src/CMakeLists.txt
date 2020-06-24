# Library definition
add_library(edr_source_lib
  main.c
)

if(UNIT_TESTS)
target_compile_definitions(edr_source_lib PUBLIC TESTING_INTERFACE)
endif()

# INTERFACE: We first state that anybody linking to THIS_LIBRARY needs to include the current source
# directory, while THIS_LIBRARY itself doesn’t. So this can become an INTERFACE usage requirement.
# Hence you do NOT need to link this directory anymore, linking the library is enough.
# PRIVATE: Include project source dir to path so we can include files like:
# dir/example.h
target_include_directories(edr_source_lib
    INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
    PRIVATE ${PROJECT_SOURCE_DIR}
)

