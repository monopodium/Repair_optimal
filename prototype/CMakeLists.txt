cmake_minimum_required(VERSION 3.15)
project(prototype)

add_subdirectory(third_party/pybind11)
set(simulator_source
        pybind_cpp/interface.cpp
        pybind_cpp/interface.h
        pybind_cpp/pybind.cpp)
pybind11_add_module(Code_parameters ${simulator_source})

set(CMAKE_CXX_STANDARD 11)
#set(CMAKE_CXX_FLAGS "-g -Wall -DASIO_STANDALONE")
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
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/include/   PROJECT_SRC)
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/include/LRCs/   PROJECT_SRC)
#echo PROJECT_SRC
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/src/LRCs/   PROJECT_SRC1)
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/include/LRCs/   PROJECT_SRC1)
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/include/metadefinition.h   PROJECT_SRC1)
# message(${PROJECT_SRC1}) 

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


add_library(utils SHARED ${PROJECT_SRC1})

set_target_properties(utils PROPERTIES output_name "utils")

target_compile_definitions(Code_parameters
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
set(Jerasurelib ${CMAKE_CURRENT_SOURCE_DIR}/third_party/jerasure/lib/libJerasure.so)
set(gf_completelib ${CMAKE_CURRENT_SOURCE_DIR}/third_party/gf-complete/lib/libgf_complete.so)

target_link_libraries(Code_parameters
PRIVATE
${Jerasurelib} ${gf_completelib} utils
)

# set(TEST_FILE "/home/ms/Repair_optimal/figures/sim_figure")
# set(TEST_FILE1 "/home/ms/Repair_optimal/prototype/cmake/build/Code_parameters.cpython-310-x86_64-linux-gnu.so")


# add_custom_command(
#         OUTPUT  ${TEST_FILE}
#         COMMAND copy 
#         ARGS ${CMAKE_CURRENT_LIST_FILE} ${TEST_FILE} )


# set(TEST_FILE "log.txt")
# add_custom_command(TARGET target POST_BUILD
#         OUTPUT  ${TEST_FILE}
#         COMMAND echo "Generating log.txt file..."
#         COMMAND ${CMAKE_COMMAND} -E copy ${TEST_FILE1} ${TEST_FILE}
#         COMMENT  "This is a test"
#         )
# add_custom_target(Test1 ALL DEPENDS ${TEST_FILE})
