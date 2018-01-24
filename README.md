[![Build Status](https://travis-ci.org/omaralvarez/conan_dlib.svg?branch=master)](https://travis-ci.org/omaralvarez/conan_dlib) [![Build status](https://ci.appveyor.com/api/projects/status/wbi4x7t82a3cmhnc?svg=true)](https://ci.appveyor.com/project/omaralvarez/conan-dlib)
# conan_dlib

[Conan.io](https://conan.io) package for [dlib](https://github.com/davisking/dlib) library

## Build packages

    $ pip install conan_package_tools
    $ python build.py
    
## Reuse the packages

### Basic setup

    $ conan install dlib/19.8.0@omaralvarez/stable

### Package basic test
    $ conan test_package
    