import os
from conans import ConanFile, CMake


class CppUTest(ConanFile):
    name = "CppUTest"
    version = "master" # "3.8"
    description = """C /C++ based unit xUnit test framework for unit testing and for test-driving your code"""
    license = "BSD 3-clause \"New\" or \"Revised\" License, https://github.com/cpputest/cpputest/blob/master/COPYING"
    url = "https://cpputest.github.io"
    settings = "os", "compiler", "arch", "build_type"
    source_dir = "{name}-{version}".format(name=name, version=version)
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "verbose": [True, False],
        "use_std_c_lib": ["ON", "OFF"],
        "use_std_cpp_lib": ["ON", "OFF"],
        "use_cpp11": ["ON", "OFF"],
        "detect_mem_leaks": ["ON", "OFF"],
        "extensions": ["ON", "OFF"],
        "longlong": ["ON", "OFF"],
        "coverage": ["ON", "OFF"],
        "tests": ["ON", "OFF"]
    }
    default_options = (
        "shared=False",
        "fPIC=False",
        "verbose=False",
        "use_std_c_lib=OFF",
        "use_std_cpp_lib=OFF",
        "use_cpp11=ON",
        "detect_mem_leaks=ON",
        "extensions=ON",
        "longlong=ON",
        "coverage=OFF",
        "tests=ON"
    )
    scm = {
        "type": "git",
        "subfolder": source_dir,
        "url": "https://github.com/cpputest/cpputest.git",
        "revision": "tags/v{version}".format(version=version)
    }
    if version == "master":
        scm["revision"] = "master"

    def _my_cmake(self):
        cmake = CMake(self, set_cmake_flags=True)
        cmake.verbose = self.options.verbose
        # Translate our options to CppUTest's cmake options
        cmake.definitions["STD_C"] = self.options.use_std_c_lib
        cmake.definitions["STD_CPP"] = self.options.use_std_cpp_lib
        cmake.definitions["C++11"] = self.options.use_cpp11
        cmake.definitions["MEMORY_LEAK_DETECTION"] = self.options.detect_mem_leaks
        cmake.definitions["EXTENSIONS"] = self.options.extensions
        cmake.definitions["LONGLONG"] = self.options.longlong
        cmake.definitions["COVERAGE"] = self.options.coverage
        cmake.definitions["TESTS"] = self.options.tests
        cmake.definitions["CMAKE_TRY_COMPILE_TARGET_TYPE"] = "STATIC_LIBRARY"
        #self.output.info("definitions={}".format(cmake.definitions))
        cmake.configure(source_dir=os.path.join(self.source_folder, self.source_dir))
        return cmake

    def source(self):
        # No need to do anything here, since our scm definition does the work
        pass

    def build(self):
        cmake = self._my_cmake()
        cmake.build()
        if self.options.tests:
            cmake.test()

    def package(self):
        cmake = self._my_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["CppUTest"]
        if self.options.extensions:
            self.cpp_info.libs.append("CppUTestExt")
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs.append("winmm.lib")
