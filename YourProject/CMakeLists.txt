cmake_minimum_required(VERSION 3.10)

# SHARED is required for ZENO libraries
add_library(YourProject SHARED CustomNumber.cpp MyPrimitiveOps.cpp)

# Link the libzeno.so to invoke ZENO API
target_link_libraries(YourProject PUBLIC zeno)
