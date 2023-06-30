#include "metadefinition.h"
#include "General.h"
#include <sstream>
#include "jerasure.h"
#include "reed_sol.h"
#include "cauchy.h"
int main()
{

    REPAIR::Azure_LRC_Class LRC_encoder;

    // std::vector<std::vector<int>> lrc_n_k_r = {
    //     {16, 10, 5},
    //     {15, 10, 5},
    //     {14, 10, 5},
    //     {13, 10, 5},
    //     {13, 8, 4},
    //     {12, 8, 4},
    //     {11, 8, 4},
    //     {10, 6, 3},
    //     {9, 6, 3},
    //     {7, 4, 2}};
    // std::vector<std::vector<int>> lrc_n_k_r = {
    // {6, 3, 2},
    // {7, 4, 3},
    // {8,  3, 3},
    // {9, 4, 2},
    // {10, 7, 4},
    // {11, 6, 3},
    // {12, 6, 3},
    // {14, 9, 4},
    // {14, 10, 6},
    // {15, 10, 5},
    // {16, 10, 5},
    // {16, 10, 6},
    // {16, 11, 7},
    // {16, 12, 5},
    // {16, 12, 6},
    // {17, 12, 4},
    // {17, 12, 5},
    // {17, 12, 6},
    // {18, 12, 3},
    // {18, 12, 4},
    // {18, 12, 5},
    // {19, 12, 4},
    // {20, 12, 3},
    // {21, 13, 5},
    // {24, 15, 5}
    // };
    std::vector<std::vector<int>> lrc_n_k_r = {
    {8, 3, 3},
    {9, 4, 2},
    {12, 6, 3},
    // {15, 10, 5},
    // {16, 10, 6},
    {16,12,6},
    {20, 12, 3},
    // {21, 13, 5},
    {24, 15, 5},

    // {12,6,3},
    // {16,10,5},
    
    // {18,12,5},
    // {24,15,5}
    };
    REPAIR::Placement pppp;
    int seed = 999;
    // for (auto each_nkr : lrc_n_k_r)
    // {
    //     std::cout << "=====random====" << std::endl;

    //     int n = each_nkr[0];
    //     int k = each_nkr[1];
    //     int r = each_nkr[2];

    //     LRC_encoder.set_parameter(n, k, r);
    //     LRC_encoder.set_debug(true);
    //     int g = LRC_encoder.g_global_block_num();
    //     int l = LRC_encoder.l_local_block_num();
    //     // int *final_matrix;

    //     std::vector<int> final_matrix(k*(g+l), 0);
    //     //LRC_encoder.xorbas_make_matrix(k, g, l, final_matrix.data());
    //     seed++;
    //     REPAIR::Placement pppp = LRC_encoder.generate_placement(REPAIR::Random, seed);
    //     std::cout << "n = " << each_nkr[0] << " "
    //               << "k = " << each_nkr[1] << " "
    //               << "r = " << each_nkr[2] << " d = " << LRC_encoder.calculate_distance() << std::endl;
    //     for (auto each_i : pppp)
    //     {
    //         std::cout << each_i << " ";
    //     }
    //     std::cout << std::endl;
    //     for (int i = 0; i < each_nkr[0]; i++)
    //     {
    //         std::vector<int> vec;
    //         LRC_encoder.repair_request(i, vec);
    //         std::cout << "i:" << i << std::endl;
    //         for (auto jjj : vec)
    //         {
    //             std::cout << jjj << " ";
    //         }
    //         std::cout << std::endl;
    //     }
    //     std::cout << std::endl;

    //     LRC_encoder.print_placement_raw(REPAIR::Random);
    // }
    // for (auto each_nkr : lrc_n_k_r)
    // {
    //     std::cout << "=====flat====" << std::endl;
    //     LRC_encoder.set_parameter(each_nkr[0], each_nkr[1], each_nkr[2]);
    //     REPAIR::Placement pppp = LRC_encoder.generate_placement(REPAIR::Flat);
    //     std::cout << each_nkr[0] << " " << each_nkr[1] << " " << each_nkr[2] << " " << std::endl;
    //     for (auto each_i : pppp)
    //     {
    //         std::cout << each_i << " ";
    //     }
    //     std::cout << std::endl;
    //     LRC_encoder.print_placement_raw(REPAIR::Flat);
    // }
    // for (auto each_nkr : lrc_n_k_r)
    // {
    //     std::cout << "=====Best_Placement====" << std::endl;
    //     LRC_encoder.set_parameter(each_nkr[0], each_nkr[1], each_nkr[2]);
    //     REPAIR::Placement pppp = LRC_encoder.generate_placement(REPAIR::Best_Placement);
    //     std::cout << each_nkr[0] << " " << each_nkr[1] << " " << each_nkr[2] << " " << std::endl;
    //     for (auto each_i : pppp)
    //     {
    //         std::cout << each_i << " ";
    //     }
    //     std::cout << std::endl;
    //     LRC_encoder.print_placement_raw(REPAIR::Best_Placement);
    //     LRC_encoder.return_DRC_NRC(REPAIR::Best_Placement);
    //     double optimal_nrc = LRC_encoder.return_DRC_NRC(REPAIR::Best_Placement).second;

    //     std::stringstream ss1;
    //     ss1 << std::fixed <<optimal_nrc;
    //     std::cout<<"NRC:"<<ss1.str()<<std::endl;


    //     std::cout << "=====Sub_Optimal_Placement====" << std::endl;
    //     LRC_encoder.set_parameter(each_nkr[0], each_nkr[1], each_nkr[2]);
    //     pppp = LRC_encoder.generate_placement(REPAIR::Sub_Optimal);
    //     std::cout << each_nkr[0] << " " << each_nkr[1] << " " << each_nkr[2] << " " << std::endl;
    //     for (auto each_i : pppp)
    //     {
    //         std::cout << each_i << " ";
    //     }
    //     std::cout << std::endl;
    //     LRC_encoder.print_placement_raw(REPAIR::Sub_Optimal);
    //     LRC_encoder.return_DRC_NRC(REPAIR::Sub_Optimal);
    //     double sub_optimal_nrc = LRC_encoder.return_DRC_NRC(REPAIR::Sub_Optimal).second;
    
    //     std::stringstream ss2;
    //     ss2 << std::fixed <<sub_optimal_nrc;
    //     std::cout<<"NRC:"<<ss2.str()<<std::endl;
    //     if(sub_optimal_nrc>optimal_nrc){
    //         std::cout<<"ratio: "<<float(sub_optimal_nrc/optimal_nrc)<<std::endl;
    //         std::cout<<"good parameter! "<<each_nkr[0]<<","<<each_nkr[1]<<","<<each_nkr[2]<<","<<std::endl;
    //     }
    // }
    int k, m,w;
    w = 8;
    k = 2;
    m = 2;
    std::cout<<"k: "<<k<<" m: "<<m<<std::endl;
    //int *matrix = new int[100];
    int *matrix = cauchy_good_general_coding_matrix(k, m, w);
    std::cout<<"cauchy matrix:"<<std::endl;
    for(int i = 0;i<m;i++)
    { 
        for(int j = 0;j<k;j++){
            std::cout<<" "<<matrix[i*m+j]<<" ";
        }
        std::cout<<std::endl;
    }
    
    k = 4;
    m = 2;
    std::cout<<"k: "<<k<<" m: "<<m<<std::endl;
    //int *matrix = new int[100];
    matrix = cauchy_good_general_coding_matrix(k, m, w);
    std::cout<<"cauchy matrix:"<<std::endl;
    for(int i = 0;i<m;i++)
    { 
        for(int j = 0;j<k;j++){
            std::cout<<" "<<matrix[i*m+j]<<" ";
        }
        std::cout<<std::endl;
    }


    k = 8;
    m = 2;
    std::cout<<"k: "<<k<<" m: "<<m<<std::endl;
    //int *matrix = new int[100];
    matrix = cauchy_good_general_coding_matrix(k, m, w);
    std::cout<<"cauchy matrix:"<<std::endl;
    for(int i = 0;i<m;i++)
    { 
        for(int j = 0;j<k;j++){
            std::cout<<" "<<matrix[i*m+j]<<" ";
        }
        std::cout<<std::endl;
    }

    k = 16;
    m = 2;
    std::cout<<"k: "<<k<<" m: "<<m<<std::endl;
    //int *matrix = new int[100];
    matrix = cauchy_good_general_coding_matrix(k, m, w);
    std::cout<<"cauchy matrix:"<<std::endl;
    for(int i = 0;i<m;i++)
    { 
        for(int j = 0;j<k;j++){
            std::cout<<" "<<matrix[i*m+j]<<" ";
        }
        std::cout<<std::endl;
    }

    k = 4;
    m = 4;
    std::cout<<"k: "<<k<<" m: "<<m<<std::endl;
    //int *matrix = new int[100];
    matrix = cauchy_good_general_coding_matrix(k, m, w);
    std::cout<<"cauchy matrix:"<<std::endl;
    for(int i = 0;i<m;i++)
    { 
        for(int j = 0;j<k;j++){
            std::cout<<" "<<matrix[i*m+j]<<" ";
        }
        std::cout<<std::endl;
    }

    k = 8;
    m = 4;
    std::cout<<"k: "<<k<<" m: "<<m<<std::endl;
    //int *matrix = new int[100];
    matrix = cauchy_good_general_coding_matrix(k, m, w);
    std::cout<<"cauchy matrix:"<<std::endl;
    for(int i = 0;i<m;i++)
    { 
        for(int j = 0;j<k;j++){
            std::cout<<" "<<matrix[i*m+j]<<" ";
        }
        std::cout<<std::endl;
    }
    
    k = 16;
    m = 4;
    std::cout<<"k: "<<k<<" m: "<<m<<std::endl;
    //int *matrix = new int[100];
    matrix = cauchy_good_general_coding_matrix(k, m, w);
    std::cout<<"cauchy matrix:"<<std::endl;
    for(int i = 0;i<m;i++)
    { 
        for(int j = 0;j<k;j++){
            std::cout<<" "<<matrix[i*m+j]<<" ";
        }
        std::cout<<std::endl;
    }

    k = 32;
    m = 4;
    std::cout<<"k: "<<k<<" m: "<<m<<std::endl;
    //int *matrix = new int[100];
    matrix = cauchy_good_general_coding_matrix(k, m, w);
    std::cout<<"cauchy matrix:"<<std::endl;
    for(int i = 0;i<m;i++)
    { 
        for(int j = 0;j<k;j++){
            std::cout<<" "<<matrix[i*m+j]<<" ";
        }
        std::cout<<std::endl;
    }
    return 0;
}
