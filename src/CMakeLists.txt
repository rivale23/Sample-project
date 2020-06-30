# Library definition
add_library(source_lib
  sorter.cpp
)
# target_link_libraries(source_lib 
#           header_lib
#           )

if(UNIT_TESTS)
target_compile_definitions(source_lib PUBLIC TESTING_INTERFACE)
endif()

# INTERFACE: We first state that anybody linking to THIS_LIBRARY needs to include the current source
# directory, while THIS_LIBRARY itself doesn’t. So this can become an INTERFACE usage requirement.
# Hence you do NOT need to link this directory anymore, linking the library is enough.
# PRIVATE: Include project source dir to path so we can include files like:
# dir/example.h
target_include_directories(source_lib
    # INTERFACE header_lib
    PRIVATE ${PROJECT_SOURCE_DIR}
)

