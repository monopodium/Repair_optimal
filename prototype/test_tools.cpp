#include "metadefinition.h"
#include "General.h"
int main()
{

    REPAIR::Xorbas_Class m_Xorbas_encoder;

    std::vector<std::vector<int>> xorbas_n_k_r = {
        {16, 10, 5},
        {15, 10, 5},
        {14, 10, 5},
        {13, 10, 5},
        {13, 8, 4},
        {12, 8, 4},
        {11, 8, 4},
        {10, 6, 3},
        {9, 6, 3},
        {7, 4, 2}};

    REPAIR::Placement pppp;
    int seed = 999;
    for (auto each_nkr : xorbas_n_k_r)
    {
        std::cout << "=====random====" << std::endl;

        int n = each_nkr[0];
        int k = each_nkr[1];
        int r = each_nkr[2];

        m_Xorbas_encoder.set_parameter(n, k, r);
        m_Xorbas_encoder.set_debug(true);
        int g = m_Xorbas_encoder.g_global_block_num();
        int l = m_Xorbas_encoder.l_local_block_num();
        // int *final_matrix;

        std::vector<int> final_matrix(k*(g+l), 0);
        m_Xorbas_encoder.xorbas_make_matrix(k, g, l, final_matrix.data());
        seed++;
        REPAIR::Placement pppp = m_Xorbas_encoder.generate_placement(REPAIR::Random, seed);
        std::cout << "n = " << each_nkr[0] << " "
                  << "k = " << each_nkr[1] << " "
                  << "r = " << each_nkr[2] << " d = " << m_Xorbas_encoder.calculate_distance() << std::endl;
        for (auto each_i : pppp)
        {
            std::cout << each_i << " ";
        }
        std::cout << std::endl;
        for (int i = 0; i < each_nkr[0]; i++)
        {
            std::vector<int> vec;
            m_Xorbas_encoder.repair_request(i, vec);
            std::cout << "i:" << i << std::endl;
            for (auto jjj : vec)
            {
                std::cout << jjj << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;

        m_Xorbas_encoder.print_placement_raw(REPAIR::Random);
    }
    for (auto each_nkr : xorbas_n_k_r)
    {
        std::cout << "=====flat====" << std::endl;
        m_Xorbas_encoder.set_parameter(each_nkr[0], each_nkr[1], each_nkr[2]);
        REPAIR::Placement pppp = m_Xorbas_encoder.generate_placement(REPAIR::Flat);
        std::cout << each_nkr[0] << " " << each_nkr[1] << " " << each_nkr[2] << " " << std::endl;
        for (auto each_i : pppp)
        {
            std::cout << each_i << " ";
        }
        std::cout << std::endl;
        m_Xorbas_encoder.print_placement_raw(REPAIR::Flat);
    }
    for (auto each_nkr : xorbas_n_k_r)
    {
        std::cout << "=====Best_Placement====" << std::endl;
        m_Xorbas_encoder.set_parameter(each_nkr[0], each_nkr[1], each_nkr[2]);
        REPAIR::Placement pppp = m_Xorbas_encoder.generate_placement(REPAIR::Best_Placement);
        std::cout << each_nkr[0] << " " << each_nkr[1] << " " << each_nkr[2] << " " << std::endl;
        for (auto each_i : pppp)
        {
            std::cout << each_i << " ";
        }
        std::cout << std::endl;
        m_Xorbas_encoder.print_placement_raw(REPAIR::Best_Placement);
    }
    return 0;
}
