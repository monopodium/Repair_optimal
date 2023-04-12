CRT_DIR=$(pwd)
set -e

cd $CRT_DIR
mkdir -p cmake/build
cd cmake/build
cmake ../..
make -j