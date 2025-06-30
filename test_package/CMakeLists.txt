cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(slang CONFIG REQUIRED)

add_executable(testPackageApp src/testPackageApp.cpp)
target_link_libraries(testPackageApp slang::slang)
