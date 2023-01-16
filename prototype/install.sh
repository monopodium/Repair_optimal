CRT_DIR=$(pwd)
set -e

MEMCACHED_INSTALL_DIR=$CRT_DIR"/memcached"
JERASURE_INSTALL_DIR=$CRT_DIR"/third_party/jerasure"
GF_COMPLETE_INSTALL_DIR=$CRT_DIR"/third_party/gf-complete"
XML_INSTALL_DIR=$CRT_DIR"/third_party/tinyxml2"

MEMCACHED_PACKAGES_DIR=$CRT_DIR"/packages/memcached-1.6.18"
JERASURE_PACKAGES_DIR=$CRT_DIR"/packages/Jerasure"
GF_COMPLETE_PACKAGES_DIR=$CRT_DIR"/packages/gf-complete"

PACKAGES_DIR=$CRT_DIR"/packages" 
mkdir -p $PACKAGES_DIR

mkdir -p $MEMCACHED_INSTALL_DIR
mkdir -p $GF_COMPLETE_INSTALL_DIR
mkdir -p $JERASURE_INSTALL_DIR

cd $PACKAGES_DIR
git clone git@github.com:ceph/gf-complete.git
cd $GF_COMPLETE_PACKAGES_DIR
autoreconf --force --install
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
cd ./tinyxml2
make
make install DESTDIR=$XML_INSTALL_DIR prefix=''