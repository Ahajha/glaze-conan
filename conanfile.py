from conan import ConanFile
from conan.tools.files import copy, get, replace_in_file
from conan.tools.layout import basic_layout
import os


required_conan_version = ">=1.52.0"


class GlazeConan(ConanFile):
    name = "glaze"
    description = "Extremely fast, in memory, JSON and interface library for modern C++ "
    author = "stephenberry"
    url = "https://github.com/stephenberry/glaze"
    topics = ("json", "serialize", "parser" "header-only")
    settings = "os", "arch", "compiler", "build_type"
    no_copy_source = True

    def layout(self):
        basic_layout(self, src_folder="src")

    def requirements(self):
        self.requires("fmt/9.0.0")
        self.requires("fast_float/3.4.0")
        self.requires("frozen/1.1.1")
        self.requires("nanorange/20200505")
    
    def configure(self):
        # Glaze is intended to be fully header-only, fmt included
        self.options["fmt"].header_only = True

    def package_id(self):
        self.info.clear()

    def source(self):
        get(self, **self.conan_data["sources"][self.version],
            destination=self.source_folder, strip_root=True)
        
        # Update all includes to Nanorange to remove the "NanoRange/" prefix
        for root, subdirs, files in os.walk(os.path.join(self.source_folder, "include")):
            for filename in files:
                replace_in_file(self, file_path=os.path.join(root, filename), search="NanoRange/", replace="", strict = False)


    def build(self):
        pass

    # copy all files to the package folder
    def package(self):
        copy(self, pattern="LICENSE", dst=os.path.join(self.package_folder, "licenses"), src=self.source_folder)
        copy(
            self,
            pattern="*.hpp",
            dst=os.path.join(self.package_folder, "include"),
            src=os.path.join(self.source_folder, "include"),
        )

    def package_info(self):
        # folders not used for header-only
        self.cpp_info.bindirs = []
        self.cpp_info.frameworkdirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.resdirs = []
