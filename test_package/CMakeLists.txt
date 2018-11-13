project(PackageTest CXX)

cmake_minimum_required(VERSION 2.8.12)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_compile_options(
    "$<$<CXX_COMPILER_ID:MSVC>:/wd4251>"
)

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})