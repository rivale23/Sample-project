
rmdir build
mkdir build
cd build
cmake -G "MinGW Makefiles" ..  -DCMAKE_BUILD_TYPE=Debug 
mingw32-make -j5
cd ..