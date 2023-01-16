CRT_DIR=$(pwd)
set -e
#libmemcached-1.0.18
LIBMEMCACHED_INSTALL_DIR=$CRT_DIR"/third_party/libmemcached"

LIBMEMCACHED_DIR=$CRT_DIR"/src/libmemcached-1.0.18"

mkdir -p $LIBMEMCACHED_INSTALL_DIR
cd $LIBMEMCACHED_DIR
./configure --prefix=$LIBMEMCACHED_INSTALL_DIR CFLAGS="-O0 -g"
make -j6
make install

cd $CRT_DIR
mkdir -p cmake/build
cd cmake/build
cmake ../..
make -j