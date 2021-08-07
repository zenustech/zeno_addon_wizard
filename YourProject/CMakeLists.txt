cmake_minimum_required(VERSION 3.10)

# SHARED is required for ZENO libraries
add_library(YourProjectLib SHARED CustomNumber.cpp MyPrimitiveOps.cpp)

# Link the libzeno.so to invoke ZENO API
target_link_libraries(YourProjectLib PRIVATE zeno)

# To make ZENO automatic load your node library,
# we need to output the .dll file to external/zeno/zenqt/lib
set(OUTPUT_DIR external/zeno/zenqt/lib)
set_target_properties(YourProjectLib PROPERTIES
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
