#!/bin/bash
CRT_DIR=$(pwd)
set -e

TEMPORARY_SETTING=1
if [ $# -gt 1 ]; then
	TEMPORARY_SETTING=$1
fi

GCC_VERSION=9.4.0
CMAKE_VERSION=3.22.0
CMAKE_VERSION_PREFIX=3.22
INSTALL_DIR=$CRT_DIR/usr/local
GCC_INSTALL_DIR=$INSTALL_DIR/gcc-$GCC_VERSION
CMAKE_INSTALL_DIR=$INSTALL_DIR/cmake-$CMAKE_VERSION
# dependencies of gcc, latest version, 2023.4.19
GMP_INSTALL_DIR=$INSTALL_DIR/gmp-6.2.1
MPFR_INSTALL_DIR=$INSTALL_DIR/mpfr-4.2.0
MPC_INSTALL_DIR=$INSTALL_DIR/mpc-1.3.1

PACKAGE_DIR=$CRT_DIR/usr/package
GCC_DIR=$PACKAGE_DIR/gcc-$GCC_VERSION
CMAKE_DIR=$PACKAGE_DIR/cmake-$CMAKE_VERSION
GMP_DIR=$PACKAGE_DIR/gmp-6.2.1
MPFR_DIR=$PACKAGE_DIR/mpfr-4.2.0
MPC_DIR=$PACKAGE_DIR/mpc-1.3.1


mkdir -p $PACKAGE_DIR

# gmp
mkdir -p $GMP_INSTALL_DIR
cd $GMP_INSTALL_DIR
rm -rf *
cd $PACKAGE_DIR
rm -rf gmp-6.2.1
if [ ! -f "gmp-6.2.1.tar.xz" ]; then
	wget --no-check-certificate https://mirrors.tuna.tsinghua.edu.cn/gnu/gmp/gmp-6.2.1.tar.xz
fi
xz -d gmp-6.2.1.tar.xz
tar -xf gmp-6.2.1.tar
cd $GMP_DIR
./configure --prefix=$GMP_INSTALL_DIR
make -j6
make install

# mpfr
mkdir -p $MPFR_INSTALL_DIR
cd $MPFR_INSTALL_DIR
rm -rf *
cd $PACKAGE_DIR
rm -rf mpfr-4.2.0
if [ ! -f "mpfr-4.2.0.tar.gz" ]; then
	wget --no-check-certificate https://mirrors.tuna.tsinghua.edu.cn/gnu/mpfr/mpfr-4.2.0.tar.gz
fi
tar -xvzf mpfr-4.2.0.tar.gz
cd $MPFR_DIR
./configure --prefix=$MPFR_INSTALL_DIR --with-gmp=$GMP_INSTALL_DIR
make -j6
make install

# mpc
mkdir -p $MPC_INSTALL_DIR
cd $MPC_INSTALL_DIR
rm -rf *
cd $PACKAGE_DIR
rm -rf mpc-1.3.1
if [ ! -f "mpc-1.3.1.tar.gz" ]; then
	wget --no-check-certificate https://mirrors.tuna.tsinghua.edu.cn/gnu/mpc/mpc-1.3.1.tar.gz
fi
tar -xvzf mpc-1.3.1.tar.gz
cd $MPC_DIR
./configure --prefix=$MPC_INSTALL_DIR --with-gmp=$GMP_INSTALL_DIR --with-mpfr=$MPFR_INSTALL_DIR
make -j6
make install

# environment setting
if [ ${TEMPORARY_SETTING} -eq 1 ]; then
	export LD_LIBRARY_PATH=${GMP_INSTALL_DIR}/lib:${MPFR_INSTALL_DIR}/lib:${MPC_INSTALL_DIR}/lib:$LD_LIBRARY_PATH
else
	sudo echo "export LD_LIBRARY_PATH=${GMP_INSTALL_DIR}/lib:${MPFR_INSTALL_DIR}/lib:${MPC_INSTALL_DIR}/lib:\$LD_LIBRARY_PATH"  >> ~/.bashrc
	source ~/.bashrc
fi

# gcc
mkdir -p $GCC_INSTALL_DIR
cd $GCC_INSTALL_DIR
rm -rf *
cd $PACKAGE_DIR
rm -rf gcc-$GCC_VERSION
if [ ! -f "gcc-${GCC_VERSION}.tar.gz" ]; then
	wget --no-check-certificate https://mirrors.tuna.tsinghua.edu.cn/gnu/gcc/gcc-${GCC_VERSION}/gcc-${GCC_VERSION}.tar.gz
fi
tar -xvzf gcc-${GCC_VERSION}.tar.gz
cd $GCC_DIR
./configure --prefix=$GCC_INSTALL_DIR --with-gmp=$GMP_INSTALL_DIR --with-mpfr=$MPFR_INSTALL_DIR \
			--with-mpc=$MPC_INSTALL_DIR --disable-multilib 
make -j6
make install

# environment setting
if [ ${TEMPORARY_SETTING} -eq 1 ]; then
	export PATH=${GCC_INSTALL_DIR}/bin:\$PATH
	export CC=${GCC_INSTALL_DIR}/bin/gcc
	export CXX=${GCC_INSTALL_DIR}/bin/g++
	export LIBRARY_PATH=${GCC_INSTALL_DIR}/lib:$LIBRARY_PATH
	export LD_LIBRARY_PATH=${GCC_INSTALL_DIR}/lib64:$LD_LIBRARY_PATH
else
	sudo echo "" >> ~/.bashrc
	sudo echo "export PATH=${GCC_INSTALL_DIR}/bin:\$PATH" >> ~/.bashrc
	sudo echo "export CC=${GCC_INSTALL_DIR}/bin/gcc" >> ~/.bashrc
	sudo echo "export CXX=${GCC_INSTALL_DIR}/bin/g++" >> ~/.bashrc
	sudo echo "export LIBRARY_PATH=${GCC_INSTALL_DIR}/lib:$LIBRARY_PATH" >> ~/.bashrc
	sudo echo "export LD_LIBRARY_PATH=${GCC_INSTALL_DIR}/lib:${GCC_INSTALL_DIR}/lib64:\$LD_LIBRARY_PATH" >> ~/.bashrc
	source ~/.bashrc
fi


# cmake
mkdir -p $CMAKE_INSTALL_DIR
cd $CMAKE_INSTALL_DIR
rm -rf *
cd $PACKAGE_DIR
rm -rf cmake-$CMAKE_VERSION
if [ ! -f "cmake-${CMAKE_VERSION}-rc2.tar.gz" ]; then
	wget https://cmake.org/files/v${CMAKE_VERSION_PREFIX}/cmake-${CMAKE_VERSION}-rc2.tar.gz
fi
tar -xvzf cmake-${CMAKE_VERSION}-rc2.tar.gz
cd cmake-${CMAKE_VERSION}-rc2
./bootstrap --prefix=$CMAKE_INSTALL_DIR
make -j6
make install

# environment setting
if [ ${TEMPORARY_SETTING} -eq 1 ]; then
	export PATH=${CMAKE_INSTALL_DIR}/bin:\$PATH
else
	sudo echo "" >> ~/.bashrc
	sudo echo "export PATH=${CMAKE_INSTALL_DIR}/bin:\$PATH" >> ~/.bashrc
	source ~/.bashrc
fi

# delete source codes
cd $PACKAGE_DIR
rm -rf gmp-6.2.1
rm -rf mpfr-4.2.0
rm -rf mpc-1.3.1
rm -rf gcc-${GCC_VERSION}
rm -rf cmake-${CMAKE_VERSION}-rc2
