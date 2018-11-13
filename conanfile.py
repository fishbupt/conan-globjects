#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class GlObjectsConan(ConanFile):
    name = "globjects"
    version = "2.0.0"
    description = "Cross platform C++ wrapper for OpenGL API objects"
    url = ""
    homepage = "https://github.com/cginternals/globjects"
    author = "fishbupt <fishbupt@gmail.com>"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    extracted_dir = "globjects"
    no_copy_source = True
    generators = "cmake"
    requires = ("glfw/[^3.2.1]@fishbupt/latest",
                "glbinding/[^3.0.2]@fishbupt/latest",
                "glm/0.9.9.3@fishbupt/latest")

    def source(self):
        self.run("git clone https://github.com/cginternals/globjects.git")
 
        tools.replace_in_file("{}/CMakeLists.txt".format(self.extracted_dir), "project(${META_PROJECT_NAME} C CXX)",
                              '''project(${META_PROJECT_NAME} C CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["OPTION_BUILD_TESTS"]="OFF"
        cmake.configure(source_folder=self.extracted_dir)
        cmake.build()
        cmake.install()

    def package(self):   
        # Copying static and dynamic libs
        self.copy(pattern="*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src=".", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", src=".", keep_path=False)

    def package_info(self):
        if self.settings.build_type == "Debug":
            self.cpp_info.libs = ["globjectsd"]
        else:
            self.cpp_info.libs = ["globjects"]
