# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

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

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /cygdrive/c/Users/Bummy/.CLion2018.2/system/cygwin_cmake/bin/cmake.exe

# The command to remove a file.
RM = /cygdrive/c/Users/Bummy/.CLion2018.2/system/cygwin_cmake/bin/cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/command.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/command.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/command.dir/flags.make

CMakeFiles/command.dir/main.cpp.o: CMakeFiles/command.dir/flags.make
CMakeFiles/command.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/command.dir/main.cpp.o"
	/usr/bin/c++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/command.dir/main.cpp.o -c /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/main.cpp

CMakeFiles/command.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/command.dir/main.cpp.i"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/main.cpp > CMakeFiles/command.dir/main.cpp.i

CMakeFiles/command.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/command.dir/main.cpp.s"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/main.cpp -o CMakeFiles/command.dir/main.cpp.s

# Object files for target command
command_OBJECTS = \
"CMakeFiles/command.dir/main.cpp.o"

# External object files for target command
command_EXTERNAL_OBJECTS =

command.exe: CMakeFiles/command.dir/main.cpp.o
command.exe: CMakeFiles/command.dir/build.make
command.exe: CMakeFiles/command.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable command.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/command.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/command.dir/build: command.exe

.PHONY : CMakeFiles/command.dir/build

CMakeFiles/command.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/command.dir/cmake_clean.cmake
.PHONY : CMakeFiles/command.dir/clean

CMakeFiles/command.dir/depend:
	cd /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/cmake-build-debug /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/cmake-build-debug /cygdrive/c/Users/Bummy/Desktop/study/review/c++things/command/cmake-build-debug/CMakeFiles/command.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/command.dir/depend

