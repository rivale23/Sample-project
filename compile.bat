
rmdir build
mkdir build
cd build
cmake -G "MinGW Makefiles" .. -DUNIT_TESTS=ON
mingw32-make -j1