from conans import ConanFile, CMake, tools


class DlibConan(ConanFile):
    name = "dlib"
    version = "19.8.0"
    license = "GPLv3"
    url = "https://github.com/omaralvarez/conan_dlib"
    description = "Dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real world problems. See http://dlib.net for the main project documentation and API reference."
    settings = "os", "compiler", "build_type", "arch", "os_build", "arch_build"
    options = {"iso_cpp_only" : [True, False], "shared": [True, False]}
    default_options = "iso_cpp_only=False, shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/omaralvarez/conan_dlib")
        self.run("pwd")
        tools.replace_in_file("dlib/dlib/CMakeLists.txt", 'project(dlib)', '''project(dlib)
include(../../conanbuildinfo.cmake)
conan_basic_setup()
''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="dlib")
        lib_opt = ""
        if self.options.iso_cpp_only: # will override all other options
            lib_opt = " -DDLIB_ISO_CPP_ONLY=TRUE"
        cmake.build(lib_opt)

    def package(self):
        self.copy("*.h", dst="include/dlib", src="dlib/dlib")
        self.copy("config.h", dst="include/dlib", src="build/dlib")
        self.copy("revision.h", dst="include/dlib", src="build/dlib")
        self.copy("*.lib", dst="lib", src="build/dlib/Release")
        self.copy("*.lib", dst="lib", src="build/dlib/Debug")
        self.copy("*.lib", dst="lib", src="build/dlib/lib")
        self.copy("*.so", dst="lib", src="build/dlib")
        self.copy("*.a", dst="lib", src="build/dlib")

    def package_info(self):
        print("Compiler: %s %s" % (self.settings.compiler, self.settings.compiler.version))
        print("Arch: %s" % self.settings.arch)      
        print("Build_type: %s" % self.settings.build_type)     
        if self.settings.compiler == "Visual Studio":
            print("Runtime: %s" % self.settings.compiler.runtime)
        self.cpp_info.libs = ["dlib"]
