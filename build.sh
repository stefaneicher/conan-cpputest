#!/usr/bin/env bash


cd "$(dirname "$0")" || exit

#see https://docs.conan.io/en/latest/developing_packages/package_dev_flow.html#
rm -rf tmp
conan source . --source-folder=tmp/source
conan install . --install-folder=tmp/build --profile ./.conan-profile/gcc-cortexm4 --build=missing
conan build . --source-folder=tmp/source --build-folder=tmp/build
conan package . --source-folder=tmp/source --build-folder=tmp/build --package-folder=tmp/package
#
#
#
##rm -rf CppUTest-master
##conan source . --source-folder=./
#mv CppUTest-master/CppUTest-master/* CppUTest-master
#rm -rf cmake-build-debug
##conan install . --install-folder cmake-build-debug
#conan install . --install-folder cmake-build-debug --profile ./.conan-profile/gcc-cortexm4
#conan build . --build-folder cmake-build-debug
#exit
#exit
#conan create . user/testing --profile gcc-cortexm4 -
#conan create . user/testing --profile ./.conan-profile/gcc-cortexm4
conan create . user/testing
#conan create . user/testing --profile ./.conan-profile/gcc-cortexm4