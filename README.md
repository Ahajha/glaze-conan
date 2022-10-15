# glaze-conan
A basic Conan recipe for the glaze json IO library

## How to install the package
```
git clone https://github.com/Ahajha/glaze-conan.git
conan create glaze-conan <version>@<desired-user>/<desired-channel>
# Example:
conan create glaze-conan 0.0.2@local/stable
```

(I may look into getting a remote for this in the future, or uploading to conan-center-index directly)

Using the package: (Basic CMake example)

conanfile.txt:
```
[requires]
glaze/0.0.2@local/stable

[generators]
CMakeDeps
CMakeToolchain
```

CMakeLists.txt:
```cmake
cmake_minimum_required(VERSION 3.15)

project(glaze-conan-test CXX)

find_package(glaze REQUIRED)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE glaze::glaze)
target_compile_features(main PRIVATE cxx_std_20)
```
