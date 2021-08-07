cmake_minimum_required(VERSION 3.10)

# SHARED is required for ZENO libraries
add_library(YourProject SHARED CustomNumber.cpp MyPrimitiveOps.cpp)

# Link the libzeno.so to invoke ZENO API
target_link_libraries(YourProject PUBLIC zeno)

if (WIN32)
    # On Windows, due to that fact that it doesn't support RPATH,
    # we need to output the .dll file to external/zeno/zenqt/lib
    set(OUTPUT_DIR external/zeno/zenqt/lib)
    set_target_properties(YourProject PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${OUTPUT_DIR}
        RUNTIME_OUTPUT_DIRECTORY ${OUTPUT_DIR}
        ARCHIVE_OUTPUT_DIRECTORY ${OUTPUT_DIR}
        LIBRARY_OUTPUT_DIRECTORY_DEBUG ${OUTPUT_DIR}
        RUNTIME_OUTPUT_DIRECTORY_DEBUG ${OUTPUT_DIR}
        ARCHIVE_OUTPUT_DIRECTORY_DEBUG ${OUTPUT_DIR}
        LIBRARY_OUTPUT_DIRECTORY_RELEASE ${OUTPUT_DIR}
        RUNTIME_OUTPUT_DIRECTORY_RELEASE ${OUTPUT_DIR}
        ARCHIVE_OUTPUT_DIRECTORY_RELEASE ${OUTPUT_DIR}
    )
endif()
