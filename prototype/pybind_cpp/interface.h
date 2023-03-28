#pragma once
#include "General.h"

class CodePyInterface{
public:
    CodePyInterface(){};
    ~CodePyInterface(){};
    void CreateEncoder(REPAIR::EncodeType encodetype);
    void set_debug(bool if_debug);
    void print_information();
    void set_parameter(int n_in, int k_in, int r_in, int w = 8);
    std::pair<double, double> return_DRC_NRC(REPAIR::PlacementType placement_type, int random_seed = 10);
    REPAIR::Placement generate_placement(REPAIR::PlacementType placement_type, int random_seed = 10);
    int calculate_distance();
    void nkr_to_klgr(int n, int k, int r);
    void klgr_to_nkr(int k, int l, int g, int r);
    bool check_parameter();
    void print_placement_raw(REPAIR::PlacementType placement_type);
    void repair_request(int index,std::vector<int> &vec);
    int k_data_block_num();
    int g_global_block_num();
    int l_local_block_num();
    int n_all_block_num();
    int r_group_block_num();
private:
    std::shared_ptr<REPAIR::Code_Placement> m_encoder;
};