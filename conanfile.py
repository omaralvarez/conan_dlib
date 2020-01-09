from conans import ConanFile, CMake, tools


class DlibConan(ConanFile):
    name = "dlib"
    version = "19.19"
    license = "GPLv3"
    url = "https://github.com/a-alaa/conan_dlib"
    description = "Dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real world problems. See http://dlib.net for the main project documentation and API reference."
    settings = "os", "compiler", "build_type", "arch"
    options = {"iso_cpp_only" : [True, False], "enable_gif" : [True, False], "enable_png" : [True, False], "enable_jpeg" : [True, False], "no_gui_support" : [True, False], "enable_stack_trace" : [True, False], "link_with_sqlite" : [True, False], "enable_asserts" : [True, False], "enable_cuda" : [True, False], "enable_blas" : [True, False], "enable_lapack" : [True, False], "enable_sse2" : [True, False], "enable_sse4" : [True, False], "enable_avx" : [True, False], "enable_mkl_fft": [True, False], "shared": [True, False]}
    default_options = "iso_cpp_only=False", "enable_gif=True", "enable_png=True", "enable_jpeg=True", "no_gui_support=True", "enable_stack_trace=False", "link_with_sqlite=True", "enable_asserts=False", "enable_cuda=False", "enable_blas=False", "enable_lapack=False", "enable_avx=False", "enable_sse4=False", "enable_sse2=True", "enable_mkl_fft=False", "shared=False"
    generators = "cmake"
    
    def source(self):
        self.run("git clone --branch v" + self.version + " --depth 1 https://github.com/davisking/dlib.git")
        tools.replace_in_file("dlib/dlib/CMakeLists.txt", 'project(dlib)', '''project(dlib)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
''')

    def requirements(self):
        if not self.options.iso_cpp_only:
            if self.options.enable_gif:
                self.requires("giflib/5.1.4@bincrafters/stable")

            if self.options.enable_png:
                self.requires("libpng/1.6.34@bincrafters/stable")

            if self.options.enable_jpeg:
                self.requires("libjpeg-turbo/1.5.2@bincrafters/stable")

            if self.options.link_with_sqlite:
                self.requires("sqlite3/3.21.0@bincrafters/stable")

            if self.options.enable_lapack:
                self.requires("lapack/3.7.1@conan/stable")

            if self.options.enable_blas:
                self.requires("openblas/0.2.20@conan/stable")

    def build(self):
        cmake = CMake(self)
        defs = {
            "DLIB_ISO_CPP_ONLY": self.options.iso_cpp_only,
            "DLIB_GIF_SUPPORT": self.options.enable_gif,
            "DLIB_PNG_SUPPORT": self.options.enable_png,
            "DLIB_JPEG_SUPPORT": self.options.enable_jpeg,
            "DLIB_LINK_WITH_SQLITE3": self.options.link_with_sqlite,
            "DLIB_NO_GUI_SUPPORT": self.options.no_gui_support,
            "DLIB_ENABLE_STACK_TRACE": self.options.enable_stack_trace,
            "DLIB_ENABLE_ASSERTS": self.options.enable_asserts,
            "DLIB_USE_CUDA": self.options.enable_cuda,
            "DLIB_USE_BLAS": self.options.enable_blas,
            "DLIB_USE_LAPACK": self.options.enable_lapack,
            "DLIB_USE_MKL_FFT": self.options.enable_mkl_fft,
            "USE_SSE2_INSTRUCTIONS": self.options.enable_sse2,
            "USE_SSE4_INSTRUCTIONS": self.options.enable_sse4,
            "USE_AVX_INSTRUCTIONS": self.options.enable_avx,
            "BUILD_SHARED_LIBS": self.options.shared
        }
        cmake.configure(source_folder="dlib", defs=defs)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include/dlib", src="dlib/dlib")
        self.copy("config.h", dst="include/dlib", src="dlib")
        self.copy("revision.h", dst="include/dlib", src="dlib")
        self.copy("*.lib", dst="lib", src="dlib/lib")
        self.copy("*.so*", dst="lib", src="dlib/lib")
        self.copy("*.a", dst="lib", src="dlib/lib")

    def package_info(self):
        self.output.info("Compiler: %s %s" % (self.settings.compiler, self.settings.compiler.version))
        self.output.info("Arch: %s" % self.settings.arch)      
        self.output.info("Build_type: %s" % self.settings.build_type)     
        if self.settings.compiler == "Visual Studio":
            self.output.info("Runtime: %s" % self.settings.compiler.runtime)
        self.cpp_info.libs = ["dlib"]
