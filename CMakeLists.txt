cmake_minimum_required(VERSION 3.10)
project(zeno_private LANGUAGES C CXX)

set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake ${PROJECT_SOURCE_DIR}/external/zeno/zeno/cmake ${CMAKE_MODULE_PATH})

add_subdirectory(external/zeno)

set(EXTENSIONS_LIST YourProject)
set(EXTENSIONS_ENABLE_LIST YourProject)

foreach (name IN ITEMS ${EXTENSIONS_LIST})
    if (${name} IN_LIST EXTENSIONS_ENABLE_LIST)
        set(val ON)
    else()
        set(val OFF)
    endif()
    option(EXTENSION_${name} "Build ZENO_Private with extension: ${name}" ${val})
endforeach()

foreach (name IN ITEMS ${EXTENSIONS_LIST})
    if (${EXTENSION_${name}})
        message("*** Building ZENO_Private with extension: ${name}")
        add_subdirectory(${name})
    endif()
endforeach()
