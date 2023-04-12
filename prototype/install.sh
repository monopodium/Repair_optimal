CRT_DIR=$(pwd)
#set -e

MEMCACHED_INSTALL_DIR=$CRT_DIR"/run_memcached/memcached"
JERASURE_INSTALL_DIR=$CRT_DIR"/third_party/jerasure"
GF_COMPLETE_INSTALL_DIR=$CRT_DIR"/third_party/gf-complete"
XML_INSTALL_DIR=$CRT_DIR"/third_party/tinyxml2"
PYBIND_INSTALL_DIR=$CRT_DIR"/third_party/pybind11"
LIBMEMCACHED_INSTALL_DIR=$CRT_DIR"/third_party/libmemcached"

MEMCACHED_PACKAGES_DIR=$CRT_DIR"/packages/memcached-1.6.18"
JERASURE_PACKAGES_DIR=$CRT_DIR"/packages/Jerasure"
GF_COMPLETE_PACKAGES_DIR=$CRT_DIR"/packages/gf-complete"
XML_PACKAGES_DIR=$CRT_DIR"/packages/tinyxml2"
PYBIND_PACKAGES_DIR=$CRT_DIR"/packages/pybind11-2.10.4"
LIBMEMCACHED_PACKAGES_DIR=$CRT_DIR"/packages/libmemcached-1.0.18"

PACKAGES_DIR=$CRT_DIR"/packages" 
mkdir -p $PACKAGES_DIR

mkdir -p $MEMCACHED_INSTALL_DIR
mkdir -p $GF_COMPLETE_INSTALL_DIR
mkdir -p $JERASURE_INSTALL_DIR
mkdir -p $XML_INSTALL_DIR
mkdir -p $PYBIND_INSTALL_DIR
mkdir -p $LIBMEMCACHED_INSTALL_DIR

cd $PACKAGES_DIR
git clone git@github.com:ceph/gf-complete.git
cd $GF_COMPLETE_PACKAGES_DIR
#sleep 10s
autoreconf -if;autoreconf -if
#autoreconf --force --install
./configure --prefix=$GF_COMPLETE_INSTALL_DIR
make && make install

cd $PACKAGES_DIR
git clone git@github.com:tsuraan/Jerasure.git
cd $JERASURE_PACKAGES_DIR
autoreconf --force --install
./configure --prefix=$JERASURE_INSTALL_DIR LDFLAGS=-L$GF_COMPLETE_INSTALL_DIR/lib CPPFLAGS=-I$GF_COMPLETE_INSTALL_DIR/include
make && make install

cd $PACKAGES_DIR
wget http://www.memcached.org/files/memcached-1.6.18.tar.gz
tar -xvzf memcached-1.6.18.tar.gz
rm memcached-1.6.18.tar.gz
cd $MEMCACHED_PACKAGES_DIR
./configure --prefix=$MEMCACHED_INSTALL_DIR CFLAGS="-O0 -g"
make && make install

cd $PACKAGES_DIR
git clone git@github.com:leethomason/tinyxml2.git
cd $XML_PACKAGES_DIR
make
make install DESTDIR=$XML_INSTALL_DIR prefix=''

cd $PACKAGES_DIR
wget https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
tar -xvzf libmemcached-1.0.18.tar.gz
rm libmemcached-1.0.18.tar.gz
cd $LIBMEMCACHED_PACKAGES_DIR
autoreconf -i
./configure --prefix=$LIBMEMCACHED_INSTALL_DIR CFLAGS="-O0 -g"
sed -i 's/opt_servers == false/opt_servers == NULL/g' ./clients/memflush.cc
make -j6
make install

cd $PACKAGES_DIR
wget https://github.com/pybind/pybind11/archive/refs/tags/v2.10.4.tar.gz
tar -xvzf v2.10.4.tar.gz
mv $PYBIND_PACKAGES_DIR/pybind11 $PYBIND_INSTALL_DIR
mv $PYBIND_PACKAGES_DIR/include $PYBIND_INSTALL_DIR
mv $PYBIND_PACKAGES_DIR/tools $PYBIND_INSTALL_DIR
mv $PYBIND_PACKAGES_DIR/CMakeLists.txt $PYBIND_INSTALL_DIR

rm -r $MEMCACHED_PACKAGES_DIR
rm -r $JERASURE_PACKAGES_DIR
rm -r $GF_COMPLETE_PACKAGES_DIR
rm -r $XML_PACKAGES_DIR
rm -r $PYBIND_PACKAGES_DIR
rm -r $LIBMEMCACHED_PACKAGES_DIR