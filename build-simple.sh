rm -rf build
rm -rf CppUTest-master
conan install -pr gcc-cortex-m4-debug -if build .
conan source -if build .
conan build -bf build -o detect_mem_leaks=OFF .

conan create -pr gcc-cortex-m4-debug . ypsomed/development