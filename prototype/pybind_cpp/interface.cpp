#include "interface.h"

void CodePyInterface::CreateEncoder(REPAIR::EncodeType encodetype)
{
    if (encodetype == REPAIR::Xorbas)
    {
        m_encoder = std::make_shared<REPAIR::Xorbas_Class>();
    }
    else if (encodetype == REPAIR::Optimal_LRC)
    {
        m_encoder = std::make_shared<REPAIR::Optimal_LRC_Class>();
    }
    else if (encodetype == REPAIR::Azure_LRC_1)
    {
        m_encoder = std::make_shared<REPAIR::Azure_LRC_1_Class>();
    }
    else
    {
        m_encoder = std::make_shared<REPAIR::Azure_LRC_Class>();
    }
};

    void CodePyInterface::set_debug(bool if_debug){
        m_encoder->set_debug(if_debug);
    };
    void CodePyInterface::print_information(){
        m_encoder->print_information();
    };
    void CodePyInterface::set_parameter(int n_in, int k_in, int r_in, int w){
        m_encoder->set_parameter(n_in, k_in, r_in, w);
    };
    std::pair<double, double> CodePyInterface::return_DRC_NRC(REPAIR::PlacementType placement_type, int random_seed){
        return m_encoder->return_DRC_NRC(placement_type, random_seed);
    };
    REPAIR::Placement CodePyInterface::generate_placement(REPAIR::PlacementType placement_type, int random_seed){
        return m_encoder->generate_placement(placement_type, random_seed);

    };
    int CodePyInterface::calculate_distance(){
        return m_encoder->calculate_distance();
    };
    void CodePyInterface::nkr_to_klgr(int n, int k, int r){
        m_encoder->nkr_to_klgr(n, k, r);
    };
    void CodePyInterface::klgr_to_nkr(int k, int l, int g, int r){
        m_encoder->klgr_to_nkr(k, l, g, r);
    };
    bool CodePyInterface::check_parameter(){
        return m_encoder->check_parameter();
    };
    void CodePyInterface::print_placement_raw(REPAIR::PlacementType placement_type){
        m_encoder->print_placement_raw(placement_type);
    };
    void CodePyInterface::repair_request(int index,std::vector<int> &vec){
        m_encoder->repair_request(index, vec);
        std::cout<<"repair request: "<<m_encoder->s_index_to_string(index)<<": "<<std::flush;
        for(auto each_index:vec){
            std::cout<<" "<<m_encoder->s_index_to_string(each_index)<<std::flush;
        }
        std::cout<<std::endl<<std::flush;
    };
    int CodePyInterface::k_data_block_num(){
        return m_encoder->k_data_block_num();
    };
    int CodePyInterface::g_global_block_num(){
        return m_encoder->g_global_block_num();
    };
    int CodePyInterface::l_local_block_num(){
        return m_encoder->l_local_block_num();
    };
    int CodePyInterface::n_all_block_num(){
        return m_encoder->n_all_block_num();
    };
    int CodePyInterface::r_group_block_num(){
        return m_encoder->r_group_block_num();
    };
 