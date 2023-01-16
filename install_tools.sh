CRT_DIR=$(pwd)
set -e

GCC_INSTALL_PATH=$CRT_DIR"/gcc_9.4.0"
CMAKE_INSTALL_PATH=$CRT_DIR"/cmake_3.22.0"

GCC_PATH=$CRT_DIR"/gcc-9.4.0"
CMAKE_PATH=$CRT_DIR"/cmake-3.22.0"

#gcc install
wget https://mirrors.tuna.tsinghua.edu.cn/gnu/gcc/gcc-9.4.0/gcc-9.4.0.tar.gz
tar -zxvf gcc-9.4.0.tar.gz
cd $GCC_PATH
./contrib/download_prerequisites
mkdir objdir
cd objdir
../configure --disable-checking --enable-languages=c,c++ --disable-multilib --prefix=$GCC_INSTALL_PATH
make -j8
mkdir -p $GCC_INSTALL_PATH
make install
echo "export PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin">>~/.bashrc
source ~/.bashrc
echo "export PATH=${GCC_INSTALL_PATH}/bin:${GCC_INSTALL_PATH}/lib64:$PATH">>~/.bashrc
echo "LD_LIBRARY_PATH=${GCC_INSTALL_PATH}/lib:$LD_LIBRARY_PATH">>~/.bashrc
echo "CC=${GCC_INSTALL_PATH}/bin/gcc">>~/.bashrc
echo "CXX=${GCC_INSTALL_PATH}/bin/g++">>~/.bashrc
source ~/.bashrc

wget https://cmake.org/files/v3.22/cmake-3.22.0.tar.gz
tar -zxvf cmake-3.22.0.tar.gz
cd $CMAKE_PATH
./bootstrap
./configure --prefix=$CMAKE_INSTALL_PATH
make -j8
mkdir -p $CMAKE_INSTALL_PATH
echo "export PATH=$CMAKE_INSTALL_PATH:$PATH">>~/.bashrc
make install

#wget https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
