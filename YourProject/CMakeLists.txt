cmake_minimum_required(VERSION 3.19)

set(CMAKE_CXX_STANDARD 17)
project(your_first_zenode CXX)

add_subdirectory(YourRepoToImport) # add target: your_repo_to_import

add_library(your_first_zenode SHARED 	# SHARED is required for zenode target
	add.cpp)

#simd compiler flags
if (WIN32)
else()
target_compile_options(your_first_zenode PRIVATE "-march=native")
endif()

target_include_directories(your_first_zenode PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}")
target_link_directories(your_first_zenode PUBLIC /usr/lib/x86_64-linux-gnu:/usr/local/lib)

if (WIN32)
  target_compile_options(your_first_zenode PRIVATE -DNOMINMAX)
endif()

target_link_libraries(your_first_zenode PRIVATE your_repo_to_import)

# for automatic shared lib load
find_package(zeno REQUIRED)
target_link_libraries(your_first_zenode PRIVATE zeno)
set_target_properties(your_first_zenode PROPERTIES
	LIBRARY_OUTPUT_DIRECTORY ${zeno_AUTOLOAD_DIR}
	RUNTIME_OUTPUT_DIRECTORY ${zeno_AUTOLOAD_DIR}
	ARCHIVE_OUTPUT_DIRECTORY ${zeno_AUTOLOAD_DIR}
	LIBRARY_OUTPUT_DIRECTORY_DEBUG ${zeno_AUTOLOAD_DIR}
	RUNTIME_OUTPUT_DIRECTORY_DEBUG ${zeno_AUTOLOAD_DIR}
	ARCHIVE_OUTPUT_DIRECTORY_DEBUG ${zeno_AUTOLOAD_DIR}
	LIBRARY_OUTPUT_DIRECTORY_RELEASE ${zeno_AUTOLOAD_DIR}
	RUNTIME_OUTPUT_DIRECTORY_RELEASE ${zeno_AUTOLOAD_DIR}
	ARCHIVE_OUTPUT_DIRECTORY_RELEASE ${zeno_AUTOLOAD_DIR}
)
