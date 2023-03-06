cmake_minimum_required(VERSION 3.15)
project(prototype)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "-g -Wall -std=c++11 -DASIO_STANDALONE")
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include/LRCs)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/libmemcached/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/asio/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/gf-complete/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/jerasure/include/jerasure)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/jerasure/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/tinyxml2/include)


link_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/libmemcached/lib)
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/jerasure/lib)
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/gf-complete/lib)
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/third_party/tinyxml2/lib)


aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/src/   PROJECT_SRC)
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/src/LRCs/   PROJECT_SRC)

foreach (_target
        client test_tools)
    add_executable(${_target}            
            ${CMAKE_CURRENT_SOURCE_DIR}/src/proxy.cpp
            ${CMAKE_CURRENT_SOURCE_DIR}/src/ToolBox.cpp
            ${CMAKE_CURRENT_SOURCE_DIR}/${_target}.cpp
            ${CMAKE_CURRENT_SOURCE_DIR}/src/LRCs/Azure_LRC_1.cpp
            ${CMAKE_CURRENT_SOURCE_DIR}/src/LRCs/Azure_LRC.cpp
            ${CMAKE_CURRENT_SOURCE_DIR}/src/LRCs/General.cpp
            ${CMAKE_CURRENT_SOURCE_DIR}/src/LRCs/Optimal_LRC.cpp
            ${CMAKE_CURRENT_SOURCE_DIR}/src/LRCs/Xorbas.cpp
            )
    target_link_libraries(${_target}
            #${_REFLECTION}
            -lmemcached
            -lpthread
            -lJerasure -lgf_complete libtinyxml2.a
            )
endforeach ()