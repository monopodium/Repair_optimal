## LRC Repair 
This is the code repository for the paper "Repair-Optimal Data Placement for Locally Repairable Codes". The code consists of two main parts: simulation and prototype.

We will introduce our repository in two parts.
### Part 1:environment and combination of code.
#### 1.1 Simulation:
The code for the simulation consists of two parts:
* python codes to anlysis.
* c++ codes to generate placement.
To call c++ code in python code, we use pybind to package the c++ codes as .so file.The codes of simulation are in folder \LRC the required runtime environment is as follows:
```shell
python == 3.10 (strictly required)
pybind == 2.10.4 (strictly required)
matplotlib == 3.7.1 (not usually strictly required)
numpy == 1.23.5 (not usually strictly required)
```
#### 1.2 Prototype:
We implement our prototype on top on Libmemcached (v1.0.18) , by adding about 3000 SLoC. We deploy the Libmemcached as the proxy. We also deploy multiple Memcached servers as storage servers. We leverage the Jerasure Library for erasure coding. To show the improvements of the optimal data placements over flat and random data placements, we also implement the flat and random data placement.

The codes of simulation are in folder \prototype the required runtime environment is as follows:
* Tools for compile:
    ```shell
    # best to meet or use a higher vision:
    gcc version 11.3.0 ()
    cmake version 3.22.1 ()
    GNU Make 4.3
    automake (GNU automake) 1.16.5
    aclocal (GNU automake) 1.16.5
    autoconf (GNU Autoconf) 2.71
    libevent 2.0.10 (required by memcached)
    ```

    Users can use apt-get to install the required libraries. It can also be installed by compiling the source codes while paying attention to the version of the various tools. (This part needs to be prepared by the user.)

* Dependency:

    The dependency of packages for the prototype codes are as follows:
    ```shell
    memcached-1.5.20
    libmemcached: v1.0.18
    gf-complete
    tinyxml2
    Jerasure
    ```
    The installation of these third-party libraries are organized in /prototype/install.sh. 

    Simply run the script. Then the third party libraries will be installed in the /prototype/third_party directory. (only requires the user to execute ./install.sh)


* Structure:
    * The prototype/third_party folder contains third-party libraries
    * The prototype/install.sh can be used to install third party dependency.
    * The prototype/test_tools.cpp can be used to test the small part of project. The prototype/client.cpp can be used to experiment.

#### 1.3 Small Tools:

### Part 2: Quit start and Run
* install third party dependency
```shell
cd prototype
bash compile.sh
```
* compile the prototype
```shell
cd prototype
bash compile.sh
```
* There are two ways to run our prototype:
    * run the prototype : simply test on one machine
    ```shell
    cd prototype
    bash ./run_memcached.sh
    cd cmake/build
    ./client false Xorbas Random 16 10 5 1 10
    ```
    * run the prototype : experiment on several machines

        To run the prototype, you should have several machines. In general, you should set the IP array in ./get_result.sh to the IP address of your machines.

    ```shell
    touch result_xorbas.txt
    cd REPAIR_OPTIMAL
    ./get_result.sh
    ```