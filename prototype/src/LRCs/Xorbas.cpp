#include "General.h"
namespace REPAIR
{
    bool Xorbas_Class::check_parameter()
    {

        return true;
    };
    int Xorbas_Class::calculate_distance()
    {
        m_d = m_g + 1;
        return m_d;
    };
    void Xorbas_Class::generate_best_placement()
    {
        if (m_d - 1 >= m_r)
        {
            Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
            for (size_t i = 0; i < m_stripe_information.size() - 1; i++)
            {
                std::vector<std::string> group = m_stripe_information[i];
                if (new_cluster.remaind() < group.size() - 1)
                {
                    new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
                }
                for (size_t j = 0; j < group.size() - 1; j++)
                {
                    std::string block = group[j];
                    int group_number = m_block_to_groupnumber[block];
                    int cluster_id = new_cluster.return_id();
                    new_cluster.add_new_block(block, group_number);
                    m_best_placement_map[block] = cluster_id;
                }
                if (new_cluster.return_id() == m_best_placement_raw.size())
                {
                    m_best_placement_raw.push_back(new_cluster);
                }
            }
        }
        else
        {
            std::vector<std::vector<std::string>> remain_list;
            for (size_t i = 0; i < m_stripe_information.size() - 1; i++)
            {
                std::vector<std::string> group = m_stripe_information[i];
                int remain = group.size() - 1;
                while (remain >= m_d - 1)
                {
                    Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
                    for (int j = 0; j < m_d - 1; j++)
                    {
                        std::string block = group[group.size() - 1 - remain + j];
                        int group_number = m_block_to_groupnumber[block];
                        int cluster_id = new_cluster.return_id();
                        new_cluster.add_new_block(block, group_number);
                        m_best_placement_map[block] = cluster_id;
                    }
                    m_best_placement_raw.push_back(new_cluster);
                    remain = remain - (m_d - 1);
                }
                if (remain > 0)
                {
                    int begin = group.size() - 1 - remain;
                    int end = group.size() - 1;
                    std::vector<std::string> Arrs2(group.begin() + begin, group.begin() + end);
                    remain_list.push_back(Arrs2);
                }
            }
            for (size_t j = 0; j < remain_list.size(); j++)
            {
                Cluster *last_cluster = &m_best_placement_raw[m_best_placement_raw.size() - 1];
                if (last_cluster->remaind() < remain_list[j].size())
                {
                    Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
                    m_best_placement_raw.push_back(new_cluster);
                    last_cluster = &m_best_placement_raw[m_best_placement_raw.size() - 1];
                }
                for (auto block : remain_list[j])
                {
                    int group_number = m_block_to_groupnumber[block];
                    int cluster_id = last_cluster->return_id();
                    last_cluster->add_new_block(block, group_number);
                    m_best_placement_map[block] = cluster_id;
                }
                if (last_cluster->return_id() == m_best_placement_raw.size())
                {
                    m_best_placement_raw.push_back(*last_cluster);
                }
            }
        }
        std::vector<std::string> global_parity = m_stripe_information[m_stripe_information.size() - 1];
        int remain = global_parity.size();
        int global_ptr = 0;
        for (size_t i = 0; i < m_best_placement_raw.size(); i++)
        {
            Cluster *each_cluster = &m_best_placement_raw[i];
            if (each_cluster->remaind() > 0)
            {
                while (!each_cluster->isfull())
                {
                    std::string block = global_parity[global_ptr];
                    int group_number = m_block_to_groupnumber[block];
                    int cluster_id = each_cluster->return_id();
                    each_cluster->add_new_block(block, group_number);
                    m_best_placement_map[block] = cluster_id;
                    global_ptr = global_ptr + 1;
                    if (global_ptr == remain)
                    {
                        break;
                    }
                }
                if (global_ptr == remain)
                {
                    break;
                }
            }
        }
        if (global_ptr < remain)
        {
            Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
            for (size_t j = global_ptr; j < global_parity.size(); j++)
            {
                std::string block = global_parity[j];
                int group_number = m_block_to_groupnumber[block];
                int cluster_id = new_cluster.return_id();
                new_cluster.add_new_block(block, group_number);
                m_best_placement_map[block] = cluster_id;
            }
            m_best_placement_raw.push_back(new_cluster);
        }
        for (int i = 0; i < m_stripe_information.size() - 1; i++)
        {
            std::string last_data = m_stripe_information[i][m_stripe_information[i].size() - 2];
            std::string local_block = m_stripe_information[i][m_stripe_information[i].size() - 1];
            int cluster_number = m_best_placement_map[last_data];
            int group_number = m_block_to_groupnumber[last_data];
            m_best_placement_raw[cluster_number].add_new_block(local_block, group_number);
            m_best_placement_map[local_block] = cluster_number;
        }
        if (!check_cluster_information(m_best_placement_raw, m_best_placement_map))
        {
            std::cout << "!!!best Xorbas check_cluster_information()" << std::endl;
        }
    };
    void Xorbas_Class::nkr_to_klgr(int n, int k, int r)
    {
        m_l = ceil(k, r);
        m_g = n - k - m_l;
    };
    void Xorbas_Class::klgr_to_nkr(int k, int l, int g, int r)
    {
        m_n = k + l + g;
    };
    void Xorbas_Class::generate_stripe_information()
    {
        int group_ptr = -1;
        for (int i = 0; i < m_k; i++)
        {
            if (i % m_r == 0)
            {
                group_ptr = group_ptr + 1;
                std::vector<std::string> group;
                m_stripe_information.push_back(group);
            }
            std::string block = index_to_str("D", i);
            m_stripe_information[group_ptr].push_back(block);
            m_block_to_groupnumber[block] = group_ptr;
        }
        std::vector<std::string> group;

        for (int i = 0; i < m_g; i++)
        {
            std::string block = index_to_str("G", i);
            group.push_back(block);
            m_block_to_groupnumber[block] = -1;
        }
        m_stripe_information.push_back(group);
        for (int i = 0; i < m_l; i++)
        {
            std::string block = index_to_str("L", i);
            m_stripe_information[i].push_back(block);
            m_block_to_groupnumber[block] = i;
        }
        if (int(m_stripe_information.size()) != m_l + 1)
        {
            std::cout << "Xorbas, error" << std::endl;
        }
    };
    void Xorbas_Class::generate_block_repair_request()
    {
        for (int i = 0; i < m_l; i++)
        {
            std::vector<std::string> group = m_stripe_information[i];
            for (std::string block : group)
            {
                std::vector<std::string> repair_request;
                for (std::string other_block : group)
                {
                    if (block != other_block)
                    {
                        repair_request.push_back(other_block);
                    }
                }
                m_block_repair_request[block] = repair_request;
            }
        }

        for (std::string block : m_stripe_information[m_l])
        {
            std::vector<std::string> repair_request;
            for (std::string other_block : m_stripe_information[m_l])
            {
                if (block != other_block)
                {
                    repair_request.push_back(other_block);
                }
            }
            for (int i = 0; i < m_l; i++)
            {
                repair_request.push_back(index_to_str("L", i));
            }
            m_block_repair_request[block] = repair_request;
        }
    };
    void Xorbas_Class::return_group_number(){};
    bool Xorbas_Class::encode(char **data_ptrs, char **coding_ptrs, int blocksize)
    {
        std::vector<int> new_matrix((m_g + m_l) * m_k, 0);
        xorbas_make_matrix(m_k, m_g, m_l, new_matrix.data());
        jerasure_matrix_encode(m_k, m_g + m_l, 8, new_matrix.data(), data_ptrs, coding_ptrs, blocksize);
        return true;
        return true;
    };
    bool Xorbas_Class::xorbas_make_matrix(int k, int g, int l, int *final_matrix)
    {
        int r = (k + l - 1) / l;
        int *matrix = NULL;

        matrix = reed_sol_vandermonde_coding_matrix(k, g, 8);
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
                final_matrix[i * k + j] = matrix[i * k + j];
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
    };
    bool Xorbas_Class::decode(char **data_ptrs, char **coding_ptrs, int *erasures, int blocksize)
    {
        std::vector<int> new_matrix((m_g + m_l) * m_k, 0);
        xorbas_make_matrix(m_k, m_g, m_l, new_matrix.data());
        jerasure_matrix_encode(m_k, m_g + m_l, 8, new_matrix.data(), data_ptrs, coding_ptrs, blocksize);
        return true;
    };
}