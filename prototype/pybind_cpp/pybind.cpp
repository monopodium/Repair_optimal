#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "interface.h"
#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)
using namespace REPAIR;
// int add(int i, int j)
// {
//     return i + j;
// }

PYBIND11_MODULE(Code_parameters, m)
{
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------

        .. currentmodule:: cmake_example

        .. autosummary::
           :toctree: _generate

           add
           subtract
    )pbdoc";

    pybind11::class_<std::vector<int>>(m, "IntVector")
    .def(pybind11::init<>())
    .def("clear", &std::vector<int>::clear)
    .def("pop_back", &std::vector<int>::pop_back)
    .def("__len__", [](const std::vector<int> &v) { return v.size(); })
    .def("__iter__", [](std::vector<int> &v) {
       return pybind11::make_iterator(v.begin(), v.end());
    }, pybind11::keep_alive<0, 1>()) ;/* Keep vector alive while iterator is used */
    // ....
    // PYBIND11_MAKE_OPAQUE(std::vector<int>);
    // pybind11::bind_vector<std::vector<int>>(m, "VectorInt");
    pybind11::enum_<EncodeType>(m, "EncodeType", pybind11::arithmetic())
        .value("Xorbas", EncodeType::Xorbas)
        .value("Azure_LRC", EncodeType::Azure_LRC)
        .value("Azure_LRC_1", EncodeType::Azure_LRC_1)
        .value("Optimal_LRC", EncodeType::Optimal_LRC);

    pybind11::enum_<PlacementType>(m, "PlacementType", pybind11::arithmetic())
        .value("Random", PlacementType::Random)
        .value("Flat", PlacementType::Flat)
        .value("Best_Placement", PlacementType::Best_Placement);

    pybind11::class_<CodePyInterface>(m, "CodePyInterface")
        .def(pybind11::init<>())
        .def("CreateEncoder", &CodePyInterface::CreateEncoder)
        .def("set_debug", &CodePyInterface::set_debug)
        .def("calculate_distance", &CodePyInterface::calculate_distance)
        .def("print_information", &CodePyInterface::print_information)
        .def("set_parameter", &CodePyInterface::set_parameter)
        .def("return_DRC_NRC", &CodePyInterface::return_DRC_NRC)
        .def("generate_placement", &CodePyInterface::generate_placement, pybind11::return_value_policy::copy)
        .def("calculate_distance", &CodePyInterface::calculate_distance)
        .def("nkr_to_klgr", &CodePyInterface::nkr_to_klgr)
        .def("klgr_to_nkr", &CodePyInterface::klgr_to_nkr)
        .def("check_parameter", &CodePyInterface::check_parameter)
        .def("print_placement_raw", &CodePyInterface::print_placement_raw)
        .def("repair_request", &CodePyInterface::repair_request, pybind11::return_value_policy::copy)
        .def("k_data_block_num", &CodePyInterface::k_data_block_num)
        .def("repair_request", &CodePyInterface::print_placement_raw)
        .def("g_global_block_num", &CodePyInterface::g_global_block_num)
        .def("l_local_block_num", &CodePyInterface::l_local_block_num)
        .def("n_all_block_num", &CodePyInterface::n_all_block_num)
        .def("r_group_block_num", &CodePyInterface::r_group_block_num);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
