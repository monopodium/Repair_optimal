#include "General.h"
namespace REPAIR
{
    bool Azure_LRC_1_Class::check_parameter()
    {
        if (m_k + m_l >= m_n)
        {
            return false;
        }
        return true;
    };
    int Azure_LRC_1_Class::calculate_distance()
    {
        nkr_to_klgr(m_n, m_k, m_r);
        m_d = m_g + 2;
        return m_d;
    };
    void Azure_LRC_1_Class::generate_best_placement()
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
    void Azure_LRC_1_Class::generate_sub_optimal_placement(){};
    void Azure_LRC_1_Class::nkr_to_klgr(int n, int k, int r)
    {
        m_l = ceil(k, r) + 1;
        m_g = n - k - m_l;
    };
    void Azure_LRC_1_Class::klgr_to_nkr(int k, int l, int g, int r)
    {
        m_n = k + l + g;
    };
    void Azure_LRC_1_Class::generate_stripe_information()
    {
        for (int i = 0; i < m_l-1 ; i++)
        {
            std::vector<std::string> group;
            for (int j = i * m_r; j < std::min(m_k, (i + 1) * m_r); j++)
            {
                group.push_back(index_to_str("D", j));
                m_block_to_groupnumber[index_to_str("D", j)] = i;
            }
            m_stripe_information.push_back(group);
        }
        std::vector<std::string> group;   
        for (int i = 0; i < m_g; i++)
        {
            group.push_back(index_to_str("G", i));
            m_block_to_groupnumber[index_to_str("G", i)] = m_l;
        }
        m_stripe_information.push_back(group);

        for (int i = 0; i < m_l; i++)
        {
            m_stripe_information[i].push_back(index_to_str("L", i));
            m_block_to_groupnumber[index_to_str("L", i)] = i;
        }
    };
    void Azure_LRC_1_Class::generate_block_repair_request()
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
    void Azure_LRC_1_Class::return_group_number(){};
    bool Azure_LRC_1_Class::encode(char **data_ptrs, char **coding_ptrs, int blocksize)
    {
        std::vector<int> new_matrix((m_g + m_l - 1) * m_k, 0);
        azure_lrc_make_matrix(m_k, m_g, m_l - 1, new_matrix.data());
        jerasure_matrix_encode(m_k, m_g + m_l - 1, m_w, new_matrix.data(), data_ptrs, coding_ptrs, blocksize);

        // 生成全局校验块的局部校验块
        std::vector<int> last_matrix(m_g, 1);
        jerasure_matrix_encode(m_g, 1, m_w, last_matrix.data(), coding_ptrs, &coding_ptrs[m_g + m_l - 1], blocksize);
        return true;
    }
    bool Azure_LRC_1_Class::decode(char **data_ptrs, char **coding_ptrs, int *erasures, int blocksize){
        
    }
    bool Azure_LRC_1_Class::azure_lrc_make_matrix(int k, int g, int l, int *final_matrix)
    {
        int r = (k + l - 1) / l;
        int *matrix = NULL;

        matrix = reed_sol_vandermonde_coding_matrix(k, g + 1, 8);
        if (matrix == NULL)
        {
            std::cout << "matrix == NULL" << std::endl;
        }

        // final_matrix = (int *)malloc(sizeof(int) * k * (g + l));
        if (final_matrix == NULL)
        {
            std::cout << "final_matrix == NULL" << std::endl;
        }
        bzero(final_matrix, sizeof(int) * k * (g + l));

        for (int i = 0; i < g; i++)
        {
            for (int j = 0; j < k; j++)
            {
                final_matrix[i * k + j] = matrix[(i + 1) * k + j];
            }
        }

        for (int i = 0; i < l; i++)
        {
            for (int j = 0; j < k; j++)
            {
                if (i * r <= j && j < (i + 1) * r)
                {
                    final_matrix[(i + g) * k + j] = 1;
                }
            }
        }

        free(matrix);
        return true;
    }
}