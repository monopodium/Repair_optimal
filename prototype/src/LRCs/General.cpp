#include "General.h"

namespace REPAIR
{
    int Cluster::return_id()
    {
        return m_cluster_id;
    };
    int Cluster::return_block_number()
    {
        return m_blocks.size();
    }
    void Cluster::set_upperbound(int upperbound)
    {
        m_upperbound = upperbound;
    };
    int Cluster::form_group_number()
    {
        return m_from_groups.size();
    }
    bool Cluster::is_from_new_group(int group_number)
    {
        if (m_from_groups.find(group_number) == m_from_groups.end())
        {
            return true;
        }
        else
        {
            return false;
        }
    };
    bool Cluster::isfull()
    {
        if (int(m_blocks.size()) < m_upperbound)
        {
            return false;
        }
        return true;
    };
    void Cluster::add_new_block(std::string new_block, int group_number)
    {
        m_blocks.push_back(new_block);
        m_from_groups.insert(group_number);
    };
    int Cluster::remaind()
    {
        return m_upperbound - m_blocks.size();
    };
    std::vector<std::string> Cluster::return_all_blocks()
    {
        return m_blocks;
    };
    void Code_Placement::set_debug(bool if_debug)
    {
        m_if_debug = if_debug;
    };
    void Code_Placement::print_information()
    {
        std::cout << "-------------debug_information-------------" << std::endl;
        std::cout << "m_n k r" << std::endl;
        std::cout << m_n << " " << m_k << " " << m_r << std::endl;
    };
    std::string Code_Placement::s_index_to_string(int index)
    {
        std::string block;
        if (index < m_k)
        {
            block = index_to_str("D", index);
        }
        if (m_k <= index && index < m_k + m_g)
        {
            block = index_to_str("G", index - m_k);
        }
        if (m_k + m_g <= index)
        {
            block = index_to_str("L", index - m_k - m_g);
        }
        return block;
    }
    void Code_Placement::repair_request(int index, std::vector<int> &vec)
    {
        std::string block = s_index_to_string(index);
        for (auto each_block : m_block_repair_request[block])
        {
            vec.push_back(block_to_index(each_block));
        }
    };
    void Code_Placement::set_parameter(int n_in, int k_in, int r_in, int w)
    {
        m_n = n_in;
        m_k = k_in;
        m_r = r_in;
        nkr_to_klgr(m_n, m_k, m_r);
        check_parameter();
        m_raw_stripe.clear();
        m_stripe_information.clear();
        m_block_repair_request.clear();

        m_random_placement_raw.clear();
        m_random_placement_map.clear();
        m_flat_placement_raw.clear();
        m_flat_placement_map.clear();
        m_best_placement_raw.clear();
        m_best_placement_map.clear();
        m_block_repair_cost.clear();
        m_block_to_groupnumber.clear();
        m_first = true;
        // klgr_to_nkr(k, , g, r, m_n);
    };
    int Code_Placement::k_data_block_num()
    {
        return m_k;
    };
    int Code_Placement::g_global_block_num()
    {
        return m_g;
    };
    int Code_Placement::l_local_block_num()
    {
        return m_l;
    };
    int Code_Placement::n_all_block_num()
    {
        return m_n;
    };
    int Code_Placement::r_group_block_num()
    {
        return m_r;
    };
    REPAIR::Placement Code_Placement::generate_placement(REPAIR::PlacementType placement_type, int random_seed)
    {

        if (m_first)
        {
            generate_raw_information();
            generate_stripe_information();
            generate_block_repair_request();
            calculate_distance();
            generate_flat_placement();
            generate_best_placement();
            m_first = false;
        }
        Placement placement_return;
        std::map<std::string, int> placement_map;
        if(!check_parameter()){
            return placement_return;
        }
        if (placement_type == REPAIR::Random)
        {
            generate_random_placement(random_seed);
            placement_map = m_random_placement_map;
        }
        else if (placement_type == REPAIR::Flat)
        {
            placement_map = m_flat_placement_map;
        }
        else if (placement_type == REPAIR::Best_Placement)
        {
            placement_map = m_best_placement_map;
        }
        else
        {
            std::cout << "wrong type" << std::endl;
        }
        // 这三个循环的顺序是重要的
        for (int i = 0; i < m_n; i++)
        {
            int cluster_id;
            std::string block;
            if (i < m_k)
            {
                block = index_to_str("D", i);
            }
            if (m_k <= i && i < m_k + m_g)
            {
                block = index_to_str("G", i - m_k);
            }
            if (m_k + m_g <= i)
            {
                block = index_to_str("L", i - m_k - m_g);
            }
            cluster_id = placement_map[block];
            placement_return.push_back(cluster_id);
        }
        return placement_return;
    }
    std::pair<double, double> Code_Placement::return_DRC_NRC(REPAIR::PlacementType placement_type,int seed)
    {
        if(!check_parameter()){
            return std::make_pair(-1.0, -1.0);
        }
        generate_placement(placement_type, seed);
        if (placement_type == REPAIR::Random)
        {

            generate_repair_cost(m_random_placement_map);
        }
        else if (placement_type == REPAIR::Flat)
        {
            generate_repair_cost(m_flat_placement_map);
        }
        else if (placement_type == REPAIR::Best_Placement)
        {
            generate_repair_cost(m_best_placement_map);
        }
        else
        {
            std::cout << "wrong type" << std::endl;
        }
        if(m_if_debug){
            print_information();
        }
        return std::make_pair(return_DRC(), return_NRC());
    };

    double Code_Placement::return_NRC()
    {
        int cost_sum = 0;
        for (int i = 0; i < m_n; i++)
        {
            std::string block = m_raw_stripe[i];
            cost_sum = cost_sum + m_block_repair_cost[block];
        }
        // std::cout<<" cost_sum "<<cost_sum<<" m_k "<< m_k<<"double(cost_sum / m_k)"<<double(cost_sum / m_k)<<std::endl;
        return double(cost_sum) / double(m_k);
    };
    double Code_Placement::return_DRC()
    {
        int cost_sum = 0;
        for (int i = 0; i < m_k; i++)
        {
            std::string block = index_to_str("D", i);
            cost_sum = cost_sum + m_block_repair_cost[block];
        }
        // std::cout<<" cost_sum "<<cost_sum<<" m_k "<< m_k <<" double(cost_sum / m_k) "<<double(cost_sum / m_k)<<std::endl;
        return double(cost_sum)/double(m_k);
    };
    void Code_Placement::generate_repair_cost(std::map<std::string, int> m_placement_map)
    {
        for (int i = 0; i < int(m_raw_stripe.size()); i++)
        {
            std::string item = m_raw_stripe[i];
            std::set<int> repair_set;
            repair_set.insert(m_placement_map[item]);
            for (auto block : m_block_repair_request[item])
            {
                int cluster_number = m_placement_map[block];
                repair_set.insert(cluster_number);
            }
            m_block_repair_cost[item] = repair_set.size() - 1;
        }
    };
    std::string Code_Placement::index_to_str(std::string block_type, int index)
    {
        return block_type + std::to_string(index);
    };
    void Code_Placement::generate_raw_information()
    {
        for (int i = 0; i < m_k; i++)
        {
            m_raw_stripe.push_back(index_to_str("D", i));
        }
        for (int i = 0; i < m_l; i++)
        {
            m_raw_stripe.push_back(index_to_str("L", i));
        }
        for (int i = 0; i < m_g; i++)
        {
            m_raw_stripe.push_back(index_to_str("G", i));
        }
    };
    void Code_Placement::generate_random_placement(int random_seed)
    {
        m_random_placement_raw.clear();
        m_random_placement_map.clear();
        // std::default_random_engine eng{static_cast<long unsigned int>(random_seed)};
        std::vector<std::string> raw_stripe(m_raw_stripe);
        std::random_shuffle(raw_stripe.begin(), raw_stripe.end(), MyRand());
        int count = 0;
        for (int i = 0; i < m_n; i++)
        {

            // float a = 1.0;
            // std::uniform_real_distribution<int> urd(&a, d);
            std::random_device rd;
            std::mt19937 gen(rd());
            std::uniform_int_distribution<int> urd(1, m_d - 1);
            // std::default_random_engine eng(time(0));
            int blocks_in_cluster = urd(gen); // urd(eng);
            int cluster_id = m_random_placement_raw.size();
            Cluster new_cluster = Cluster(cluster_id, m_d - 1);
            if (count + blocks_in_cluster > m_n)
            {
                blocks_in_cluster = m_n - count;
            }
            for (int j = 0; j < blocks_in_cluster; j++)
            {
                if (new_cluster.isfull())
                {
                    std::cout << "n " << m_n << " k " << m_k << " r " << m_r << " g " << m_g << " d " << m_d << std::endl;
                    std::cout << "blocks_in_cluster" << blocks_in_cluster << std::endl;
                    std::cout << "random new_cluster.isfull()!!" << std::endl;
                }
                //  srand(unsigned(random_seed));
                std::string selected_block = raw_stripe[count + j];
                int group_number = m_block_to_groupnumber[selected_block];
                new_cluster.add_new_block(selected_block, group_number);
                m_random_placement_map[selected_block] = cluster_id;
            }
            count = count + blocks_in_cluster;
            m_random_placement_raw.push_back(new_cluster);
            if (count == m_n)
            {
                break;
            }
        }
        if (!check_cluster_information(m_random_placement_raw, m_random_placement_map))
        {
            std::cout << "random check_cluster_information(m_random_placement_raw)" << std::endl;
        }
    };
    bool Code_Placement::check_cluster_information(PlacementRaw placement,
                                                   std::map<std::string, int> placement_map)
    {
        std::set<std::string> blocks_in_cluster;
        for (std::string block : m_raw_stripe)
        {
            int cluster_id = placement_map[block];
            Cluster this_cluster = placement[cluster_id];
            std::vector<std::string> block_in_cluster = this_cluster.return_all_blocks();
            if (std::find(block_in_cluster.begin(), block_in_cluster.end(), block) == block_in_cluster.end())
            {
                return false;
            }
        }
        for (Cluster cluster : placement)
        {
            for (std::string block : cluster.return_all_blocks())
            {
                blocks_in_cluster.insert(block);
            }
        }
        if (int(blocks_in_cluster.size()) != m_n)
        {
            return false;
        }
        return true;
    };

    void Code_Placement::generate_flat_placement()
    {
        for (int i = 0; i < m_n; i++)
        {
            std::string block = m_raw_stripe[i];
            Cluster new_cluster = Cluster(i, m_d - 1);
            int group_number = m_block_to_groupnumber[block];
            new_cluster.add_new_block(block, group_number);
            m_flat_placement_raw.push_back(new_cluster);
            m_flat_placement_map[block] = i;
        }
        if (!check_cluster_information(m_flat_placement_raw, m_flat_placement_map))
        {
            std::cout << "random check_cluster_information(m_random_placement_raw)" << std::endl;
        }
    };
    int Code_Placement::block_to_index(std::string block)
    {
        int index = 0;
        for (int i = 1; i < block.length(); i++)
        {
            index = index * 10 + block[i] - '0';
        }
        if (block[0] == 'G')
        {
            index = index + m_k;
        }
        if (block[0] == 'L')
        {
            index = index + m_k + m_g;
        }
        return index;
    }
    void Code_Placement::print_placement_raw(PlacementType placement_type)
    {
        PlacementRaw placment;
        if (placement_type == Random)
        {
            placment = m_random_placement_raw;
        }
        else if (placement_type == Best_Placement)
        {
            placment = m_best_placement_raw;
        }
        else
        {
            placment = m_flat_placement_raw;
        }
        for (auto group:m_stripe_information){
            std::cout<<"group "<< " | " << std::flush;
            for(auto each_block:group){
                std::cout << each_block <<" "<<std::flush; 
            }
            std::cout << " | " << std::endl
                      << std::flush;
        }
        for (auto cluster : placment)
        {
            std::cout << "cluster id " << cluster.return_id() << " | " << std::flush;
            for (auto block : cluster.return_all_blocks())
            {
                std::cout << block << " " << std::flush;
            }
            std::cout << " | " << std::endl
                      << std::flush;
        }
        std::cout << std::endl
                  << std::flush;
    }
    bool Code_Placement::decode_in_group_xor(int group_data_number, char **data_ptrs, char **coding_ptrs, int blocksize)
    {
        std::vector<int> last_matrix(group_data_number, 1);
        jerasure_matrix_encode(group_data_number, 1, 8, last_matrix.data(), data_ptrs, coding_ptrs, blocksize);
        return true;
    }
}