
rmdir build
mkdir build
cd build
cmake -G "MinGW Makefiles" .. -DUNIT_TESTS=ON -DCMAKE_BUILD_TYPE=Debug -DCOVERAGE=ON
mingw32-make -j5
cd ..