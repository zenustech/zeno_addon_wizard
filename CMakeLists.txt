cmake_minimum_required(VERSION 3.10)
# Enable C++17 support first
set(CMAKE_CXX_STANDARD 17)
project(zeno_addon_wizard LANGUAGES C CXX)

# Use RelWithDebInfo mode by default
if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE RelWithDebInfo)
endif()

# Set output to the same folder with zeno.dll to prevent link failure
set(OUTPUT_DIR ${PROJECT_SOURCE_DIR}/external/zeno/zenqt/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${OUTPUT_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG ${OUTPUT_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${OUTPUT_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG ${OUTPUT_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE ${OUTPUT_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${OUTPUT_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE ${OUTPUT_DIR})
if (MSVC)
    set(CMAKE_DEBUG_POSTFIX "")
endif()

# Import ZENO
add_subdirectory(external/zeno)

# Add your ZENO node library
add_subdirectory(YourProject)
