# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2018.2.1\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2018.2.1\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\belee\Desktop\study\review\c++things\builders

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\belee\Desktop\study\review\c++things\builders\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/builders.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/builders.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/builders.dir/flags.make

CMakeFiles/builders.dir/main.cpp.obj: CMakeFiles/builders.dir/flags.make
CMakeFiles/builders.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\belee\Desktop\study\review\c++things\builders\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/builders.dir/main.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\builders.dir\main.cpp.obj -c C:\Users\belee\Desktop\study\review\c++things\builders\main.cpp

CMakeFiles/builders.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/builders.dir/main.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\belee\Desktop\study\review\c++things\builders\main.cpp > CMakeFiles\builders.dir\main.cpp.i

CMakeFiles/builders.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/builders.dir/main.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\belee\Desktop\study\review\c++things\builders\main.cpp -o CMakeFiles\builders.dir\main.cpp.s

CMakeFiles/builders.dir/PersonBuilder.cpp.obj: CMakeFiles/builders.dir/flags.make
CMakeFiles/builders.dir/PersonBuilder.cpp.obj: ../PersonBuilder.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\belee\Desktop\study\review\c++things\builders\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/builders.dir/PersonBuilder.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\builders.dir\PersonBuilder.cpp.obj -c C:\Users\belee\Desktop\study\review\c++things\builders\PersonBuilder.cpp

CMakeFiles/builders.dir/PersonBuilder.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/builders.dir/PersonBuilder.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\belee\Desktop\study\review\c++things\builders\PersonBuilder.cpp > CMakeFiles\builders.dir\PersonBuilder.cpp.i

CMakeFiles/builders.dir/PersonBuilder.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/builders.dir/PersonBuilder.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\belee\Desktop\study\review\c++things\builders\PersonBuilder.cpp -o CMakeFiles\builders.dir\PersonBuilder.cpp.s

# Object files for target builders
builders_OBJECTS = \
"CMakeFiles/builders.dir/main.cpp.obj" \
"CMakeFiles/builders.dir/PersonBuilder.cpp.obj"

# External object files for target builders
builders_EXTERNAL_OBJECTS =

builders.exe: CMakeFiles/builders.dir/main.cpp.obj
builders.exe: CMakeFiles/builders.dir/PersonBuilder.cpp.obj
builders.exe: CMakeFiles/builders.dir/build.make
builders.exe: CMakeFiles/builders.dir/linklibs.rsp
builders.exe: CMakeFiles/builders.dir/objects1.rsp
builders.exe: CMakeFiles/builders.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\belee\Desktop\study\review\c++things\builders\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable builders.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\builders.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/builders.dir/build: builders.exe

.PHONY : CMakeFiles/builders.dir/build

CMakeFiles/builders.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\builders.dir\cmake_clean.cmake
.PHONY : CMakeFiles/builders.dir/clean

CMakeFiles/builders.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\belee\Desktop\study\review\c++things\builders C:\Users\belee\Desktop\study\review\c++things\builders C:\Users\belee\Desktop\study\review\c++things\builders\cmake-build-debug C:\Users\belee\Desktop\study\review\c++things\builders\cmake-build-debug C:\Users\belee\Desktop\study\review\c++things\builders\cmake-build-debug\CMakeFiles\builders.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/builders.dir/depend
