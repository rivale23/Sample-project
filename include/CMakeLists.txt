add_library(edr_header_lib
  main.h
)
# We first state that anybody linking to THIS_LIBRARY needs to include the current source
# directory, while THIS_LIBRARY itself doesn’t. So this can become an INTERFACE usage requirement.
# Hence you do NOT need to link this directory anymore, linking the library is enough.
target_include_directories(edr_header_lib
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
  PUBLIC ${PROJECT_SOURCE_DIR}            # Need to be public for datatypes/ to find headers in this folder
  # PUBLIC ${PROJECT_SOURCE_DIR}/datatypes
)

# target_link_libraries(edr_header_lib
#   extern_lib
#   rte_stubs_lib
#   edr_generated_lib
# )



# Sometimes properties like the language need to be defined, thsi can occur if you only have
# headers, since CMake can not figure it if the language is C or C++
set_target_properties(edr_header_lib PROPERTIES LINKER_LANGUAGE C)
