add_library(header_lib
  main.h
  Sorter.h
)
# We first state that anybody linking to THIS_LIBRARY needs to include the current source
# directory, while THIS_LIBRARY itself doesn’t. So this can become an INTERFACE usage requirement.
# Hence you do NOT need to link this directory anymore, linking the library is enough.
# target_include_directories(header_lib
#   INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
#   PUBLIC ${PROJECT_SOURCE_DIR}            # Need to be public for datatypes/ to find headers in this folder
# )


# Sometimes properties like the language need to be defined, thsi can occur if you only have
# headers, since CMake can not figure it if the language is C or C++
set_target_properties(header_lib PROPERTIES LINKER_LANGUAGE CXX)

target_include_directories(header_lib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}
)