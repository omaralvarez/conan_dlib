[![Download](https://api.bintray.com/packages/omaralvarez/public-conan/dlib%3Aomaralvarez/images/download.svg)](https://bintray.com/omaralvarez/public-conan/dlib%3Aomaralvarez/_latestVersion) [![Build Status](https://travis-ci.org/omaralvarez/conan_dlib.svg?branch=master)](https://travis-ci.org/omaralvarez/conan_dlib)

# conan_dlib

[Conan.io](https://conan.io) package for [dlib](https://github.com/davisking/dlib) library

## Build packages

    $ pip install conan_package_tools
    $ python build.py
    
## Reuse the packages

### Basic setup

    $ conan install dlib/19.19@omaralvarez/stable

### Package basic test
    $ conan test_package
    
## Example usage in a CMake-based project

### Conan and CMake files

* A sample from `conanfile.txt` in the root directory:
```
[requires]
dlib/19.19@omaralvarez/stable
...

[generators]
cmake
...

[options]
dlib:enable_blas=False
dlib:enable_lapack=False
...
```

* The `CMakeLists.txt` at the root directory:
```cmake
cmake_minimum_required(VERSION 3.8)
project(project_name C CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)
...
```
* The `CMakeLists.txt` of a dependent target:
```cmake
...
add_executable(example example.cpp)
target_link_libraries(example CONAN_PKG::dlib)
...
```

### Running Conan and CMake 

* First, add new remote pointing to the repository: 
```
conan remote add omaralvarez https://api.bintray.com/conan/omaralvarez/public-conan
```
* Change directory to the build location and run Conan installation:
```shell
conan install .. -s build_type=Release --build=missing
```
where the `..` points to the project root at the parent directory.
* Run CMake:
```shell
cmake ..
```
