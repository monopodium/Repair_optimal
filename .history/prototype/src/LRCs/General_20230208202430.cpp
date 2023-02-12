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
        if (m_from_groups.size() == 0)
        {
            m_from_groups.insert(group_number);
        }
    };
    int Cluster::remaind()
    {
        return m_upperbound - m_cluster_id;
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
        std::cout << "n k r" << std::endl;
        std::cout << n << " " << k << " " << r << std::endl;
    };
    void Code_Placement::set_parameter(int n_in, int k_in, int r_in,int w)
    {
        n = n_in;
        k = k_in;
        r = r_in;
        nkr_to_klgr(n, k, r, l, g);
        check_parameter();
        // klgr_to_nkr(k, l, g, r, n);
    };
    REPAIR::Placement Code_Placement::generate_placement(REPAIR::PlacementType placement_type, int random_seed)
    {

        generate_raw_information();
        generate_stripe_information();
        generate_block_repair_request();
        Placement placement_return;
        std::map<std::string, int> placement_map;

        if (placement_type == REPAIR::Random)
        {
            generate_random_placement(random_seed);
            placement_map = m_random_placement_map;
        }
        else if (placement_type == REPAIR::Flat)
        {
            generate_flat_placement();
            placement_map = m_flat_placement_map;
        }
        else if (placement_type == REPAIR::Best_Placement)
        {
            generate_best_placement();
            placement_map = m_best_placement_map;
        }
        else
        {
            std::cout << "wrong type" << std::endl;
        }
        // 这三个循环的顺序是重要的
        for (int i = 0; i < n; i++)
        {
            if (i < k)
            {
                placement_return.push_back(placement_map[index_to_str("D", i)]);
            }
            if (k <= i && i < k + g)
            {
                placement_return.push_back(placement_map[index_to_str("G", i - k)]);
            }
            if (k + g <= i)
            {
                placement_return.push_back(placement_map[index_to_str("L", i - k - g)]);
            }
        }
        return placement_return;
    }
    std::pair<double, double> Code_Placement::return_DRC_NRC(REPAIR::PlacementType placement_type, int random_seed)
    {
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

        print_information();
    };

    double Code_Placement::return_NRC()
    {
        int cost_sum = 0;
        for (int i = 0; i < n; i++)
        {
            std::string block = m_raw_stripe[i];
            cost_sum = cost_sum + m_block_repair_cost[block];
        }
        return cost_sum / k;
    };
    double Code_Placement::return_DRC()
    {
        int cost_sum = 0;
        for (int i = 0; i < k; i++)
        {
            std::string block = index_to_str("D", i);
            cost_sum = cost_sum + m_block_repair_cost[block];
        }
        return cost_sum / k;
    };
    int Code_Placement::generate_repair_cost(std::map<std::string, int> m_placement_map)
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
        for (int i = 0; i < k; i++)
        {
            m_raw_stripe.push_back(index_to_str("D", i));
        }
        for (int i = 0; i < l; i++)
        {
            m_raw_stripe.push_back(index_to_str("L", i));
        }
        for (int i = 0; i < g; i++)
        {
            m_raw_stripe.push_back(index_to_str("G", i));
        }
    };
    void Code_Placement::generate_random_placement(int random_seed)
    {
        std::default_random_engine eng{static_cast<long unsigned int>(random_seed)};
        std::vector<std::string> raw_stripe(m_raw_stripe);
        std::random_shuffle(raw_stripe.begin(), raw_stripe.end());
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            
            // float a = 1.0;
            // std::uniform_real_distribution<int> urd(&a, d);
            int blocks_in_cluster = 3;//urd(eng);
            int cluster_id = m_random_placement_raw.size();
            Cluster new_cluster = Cluster(cluster_id, d);
            if (count + blocks_in_cluster > n)
            {
                blocks_in_cluster = n - count;
            }
            for (int j = 0; j < blocks_in_cluster; j++)
            {
                if (new_cluster.isfull())
                {
                    std::cout << "random new_cluster.isfull()!!" << std::endl;
                }
                srand(unsigned(random_seed));
                std::string selected_block = raw_stripe[count + j];
                int group_number = m_block_to_groupnumber[selected_block];
                new_cluster.add_new_block(selected_block, group_number);
                m_flat_placement_map[selected_block] = cluster_id;
            }
            count = count + blocks_in_cluster;
            m_random_placement_raw.push_back(new_cluster);
            if (count == n)
            {
                break;
            }
        }
        if (!check_cluster_information(m_random_placement_raw, m_flat_placement_map))
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
        if (int(blocks_in_cluster.size())!= n)
        {
            return false;
        }
        return true;
    };

    void Code_Placement::generate_flat_placement()
    {
        for (int i = 0; i < n; i++)
        {
            std::string block = m_raw_stripe[i];
            Cluster new_cluster = Cluster(i, d - 1);
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
    bool Code_Placement::decode_in_group_xor(int group_data_number, char **data_ptrs, char **coding_ptrs, int *erasures, int blocksize)
    {
        std::vector<int> last_matrix(group_data_number, 1);
        jerasure_matrix_decode(group_data_number, 1, w, last_matrix.data(), 0, erasures, data_ptrs, coding_ptrs, blocksize);
        return true;
    }
}