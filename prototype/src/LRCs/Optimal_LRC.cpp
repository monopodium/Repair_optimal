#include "General.h"
namespace REPAIR
{
    bool Optimal_LRC_Class::check_parameter()
    {
        if (m_n % (m_r + 1) == 1)
        {
            std::cout << "Parameters do not meet requirements!" << std::endl;
            return false;
        }
        return true;
    };
    int Optimal_LRC_Class::calculate_distance()
    {
        nkr_to_klgr(m_n, m_k, m_r);
        m_d = m_g + ceil(m_g + 1, m_r) + 1;
        return m_d;
    };
    void Optimal_LRC_Class::generate_best_placement()
    {
        
        
        for (std::vector<std::string> each_group : m_stripe_information)
        {
            if (int(each_group.size()) <= m_d - 1)
            {
                Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
                for (std::string block : each_group)
                {
                    new_cluster.add_new_block(block, m_block_to_groupnumber[block]);
                    m_best_placement_map[block] = new_cluster.return_id();
                }
                m_best_placement_raw.push_back(new_cluster);
            }
            else
            {   
                Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
                m_best_placement_raw.push_back(new_cluster);
                for (int i = 0; i < ceil(int(each_group.size()), m_d - 1); i++)
                {

                    int each_c = std::min(int(each_group.size() - i * (m_d - 1)), m_d - 1);

                    if (m_best_placement_raw[m_best_placement_raw.size() - 1].remaind() < each_c)
                    {
                        m_best_placement_raw.push_back(Cluster(m_best_placement_raw.size(), m_d - 1));
                    }
                    Cluster* last_cluster = &m_best_placement_raw[m_best_placement_raw.size() - 1];
                    for (int j = i * (m_d - 1); j < each_c + i * (m_d - 1); j++)
                    {
                        std::string block = each_group[j];
                        last_cluster->add_new_block(block, m_block_to_groupnumber[block]);
                        m_best_placement_map[block] = last_cluster->return_id();
                    }
                }
            }
        }
    };
    void Optimal_LRC_Class::nkr_to_klgr(int n, int k, int r)
    {
        m_l = ceil(n, (r + 1));
        m_g = n - k - m_l;
    };
    void Optimal_LRC_Class::klgr_to_nkr(int k, int l, int g, int r)
    {
        m_n = k + l + g;
    };
    void Optimal_LRC_Class::generate_stripe_information()
    {
        int group_ptr = 0;
        std::vector<std::string> group;
        m_stripe_information.push_back(group);
        for (int i = 0; i < m_g + m_k; i++)
        {
            std::string block;
            if (i == m_r * (group_ptr + 1))
            {
                group_ptr = group_ptr + 1;
                std::vector<std::string> group;
                m_stripe_information.push_back(group);
            }
            if (i < m_k)
            {
                block = index_to_str("D", i);
            }
            else
            {
                block = index_to_str("G", i - m_k);
            }
            m_stripe_information[group_ptr].push_back(block);
            m_block_to_groupnumber[block] = group_ptr;
        }

        for (int i = 0; i < m_l; i++)
        {
            std::string block = index_to_str("L", i);
            m_stripe_information[i].push_back(block);
            m_block_to_groupnumber[block] = i;
        }
        for(auto group:m_stripe_information){
            for(auto block:group){
                std::cout<<"block"<<block;
            }
            std::cout<<std::endl;
        }
        if (int(m_stripe_information.size()) != m_l)
        {
            std::cout << "Optimal_LRC_Class, error" << std::endl;
        }
    };
    void Optimal_LRC_Class::generate_block_repair_request()
    {
        for (std::vector<std::string> group : m_stripe_information)
        {
            for (std::string item : group)
            {
                std::vector<std::string> repair_request;
                for (std::string other_item : group)
                {
                    if (other_item != item)
                    {
                        repair_request.push_back(other_item);
                    }
                }
                m_block_repair_request[item] = repair_request;
            }
        }
    };
    void Optimal_LRC_Class::return_group_number(){};

    bool Optimal_LRC_Class::encode(char **data_ptrs, char **coding_ptrs, int blocksize)
    {
        // 全局校验块，局部校验块；
        int *matrix = NULL;
        matrix = reed_sol_vandermonde_coding_matrix(m_k, m_g, m_w);
        if (matrix == NULL)
        {
            std::cout << "matrix == NULL" << std::endl;
        }
        jerasure_matrix_encode(m_k, m_g, m_w, matrix, data_ptrs, coding_ptrs, blocksize);
        free(matrix);
        std::vector<int> group_number(m_l, 0);
        for (int i = 0; i < m_l; i++)
        {
            int group_size = std::min(m_r, m_k + m_g - i * m_r);
            std::vector<char *> vecotr_number(group_size);
            char **new_data = (char **)vecotr_number.data();
            for (int j = 0; j < group_size; j++)
            {
                if (i * m_r + j < m_k)
                {
                    new_data[j] = data_ptrs[i * m_r + j];
                }
                else
                {
                    new_data[j] = coding_ptrs[i * m_r + j - m_k];
                }
            }
            std::vector<int> last_matrix(group_size, 1);
            jerasure_matrix_encode(group_size, 1, 8, last_matrix.data(), new_data, &coding_ptrs[m_g + i], blocksize);
        }
        return true;
    };
    bool Optimal_LRC_Class::decode(char **data_ptrs, char **coding_ptrs, int *erasures, int blocksize)
    {
        // std::vector<int> matrix(g * k, 0);
        int *rs_matrix = reed_sol_vandermonde_coding_matrix(m_k, m_g, m_w);
        // memcpy(matrix.data(), rs_matrix, g * k * sizeof(int));
        jerasure_matrix_decode(m_k, m_g, m_w, rs_matrix, 0, erasures, data_ptrs, coding_ptrs, blocksize);
        free(rs_matrix);
        return true;
    }
}