#!/usr/bin/env bash
#rm -rf CppUTest-master
#conan source . --source-folder=./
mv CppUTest-master/CppUTest-master/* CppUTest-master
rm -rf cmake-build-debug
#conan install . --install-folder cmake-build-debug
conan install . --install-folder cmake-build-debug --profile ./.conan-profile/gcc-cortexm4
conan build . --build-folder cmake-build-debug
exit
#exit
#conan create . user/testing --profile gcc-cortexm4 -
#conan create . user/testing --profile ./.conan-profile/gcc-cortexm4
conan create . user/testing
#conan create . user/testing --profile ./.conan-profile/gcc-cortexm4