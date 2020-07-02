
# Adding some executable - Output name matches target name
add_executable (${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PUBLIC
sorter_lib
)

set_target_properties(${PROJECT_NAME} PROPERTIES LINKER_LANGUAGE CXX)
# if(UNIT_TESTS)
# target_compile_definitions(source_lib PUBLIC TESTING_INTERFACE)
# endif()

# INTERFACE: We first state that anybody linking to THIS_LIBRARY needs to include the current source
# directory, while THIS_LIBRARY itself doesn’t. So this can become an INTERFACE usage requirement.
# Hence you do NOT need to link this directory anymore, linking the library is enough.
# PRIVATE: Include project source dir to path so we can include files like:
# dir/example.h
# target_include_directories(source_lib
#     # INTERFACE header_lib
#     PRIVATE ${PROJECT_SOURCE_DIR}
# )

add_subdirectory(libs)
