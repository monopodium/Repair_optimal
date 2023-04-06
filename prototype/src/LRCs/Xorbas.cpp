#include "General.h"
namespace REPAIR
{
    bool Xorbas_Class::check_parameter()
    {
        if (m_n <= m_k + m_l)
        {
            return false;
        }
        return true;
    };
    int Xorbas_Class::calculate_distance()
    {
        m_d = m_g + 1;
        return m_d;
    };
    // void Xorbas_Class::generate_best_placement()
    // {
    //     if (m_d - 1 >= m_r)
    //     {
    //         Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
    //         for (size_t i = 0; i < m_stripe_information.size() - 1; i++)
    //         {
    //             std::vector<std::string> group = m_stripe_information[i];
    //             if (new_cluster.remaind() < group.size() - 1)
    //             {
    //                 new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
    //             }
    //             for (size_t j = 0; j < group.size() - 1; j++)
    //             {
    //                 std::string block = group[j];
    //                 int group_number = m_block_to_groupnumber[block];
    //                 int cluster_id = new_cluster.return_id();
    //                 new_cluster.add_new_block(block, group_number);
    //                 m_best_placement_map[block] = cluster_id;
    //             }
    //             if (new_cluster.return_id() == m_best_placement_raw.size())
    //             {
    //                 m_best_placement_raw.push_back(new_cluster);
    //             }
    //         }
    //     }
    //     else
    //     {
    //         std::vector<std::vector<std::string>> remain_list;
    //         for (size_t i = 0; i < m_stripe_information.size() - 1; i++)
    //         {
    //             std::vector<std::string> group = m_stripe_information[i];
    //             int remain = group.size() - 1;
    //             while (remain >= m_d - 1)
    //             {
    //                 Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
    //                 for (int j = 0; j < m_d - 1; j++)
    //                 {
    //                     std::string block = group[group.size() - 1 - remain + j];
    //                     int group_number = m_block_to_groupnumber[block];
    //                     int cluster_id = new_cluster.return_id();
    //                     new_cluster.add_new_block(block, group_number);
    //                     m_best_placement_map[block] = cluster_id;
    //                 }
    //                 m_best_placement_raw.push_back(new_cluster);
    //                 remain = remain - (m_d - 1);
    //             }
    //             if (remain > 0)
    //             {
    //                 int begin = group.size() - 1 - remain;
    //                 int end = group.size() - 1;
    //                 std::vector<std::string> Arrs2(group.begin() + begin, group.begin() + end);
    //                 remain_list.push_back(Arrs2);
    //             }
    //         }
    //         for (size_t j = 0; j < remain_list.size(); j++)
    //         {
    //             Cluster *last_cluster = &m_best_placement_raw[m_best_placement_raw.size() - 1];
    //             if (last_cluster->remaind() < remain_list[j].size())
    //             {
    //                 Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
    //                 m_best_placement_raw.push_back(new_cluster);
    //                 last_cluster = &m_best_placement_raw[m_best_placement_raw.size() - 1];
    //             }
    //             for (auto block : remain_list[j])
    //             {
    //                 int group_number = m_block_to_groupnumber[block];
    //                 int cluster_id = last_cluster->return_id();
    //                 last_cluster->add_new_block(block, group_number);
    //                 m_best_placement_map[block] = cluster_id;
    //             }
    //             if (last_cluster->return_id() == m_best_placement_raw.size())
    //             {
    //                 m_best_placement_raw.push_back(*last_cluster);
    //             }
    //         }
    //     }
    //     std::vector<std::string> global_parity = m_stripe_information[m_stripe_information.size() - 1];
    //     int remain = global_parity.size();
    //     int global_ptr = 0;
    //     for (size_t i = 0; i < m_best_placement_raw.size(); i++)
    //     {
    //         Cluster *each_cluster = &m_best_placement_raw[i];
    //         if (each_cluster->remaind() > 0)
    //         {
    //             while (!each_cluster->isfull())
    //             {
    //                 std::string block = global_parity[global_ptr];
    //                 int group_number = m_block_to_groupnumber[block];
    //                 int cluster_id = each_cluster->return_id();
    //                 each_cluster->add_new_block(block, group_number);
    //                 m_best_placement_map[block] = cluster_id;
    //                 global_ptr = global_ptr + 1;
    //                 if (global_ptr == remain)
    //                 {
    //                     break;
    //                 }
    //             }
    //             if (global_ptr == remain)
    //             {
    //                 break;
    //             }
    //         }
    //     }
    //     if (global_ptr < remain)
    //     {
    //         Cluster new_cluster = Cluster(m_best_placement_raw.size(), m_d - 1);
    //         for (size_t j = global_ptr; j < global_parity.size(); j++)
    //         {
    //             std::string block = global_parity[j];
    //             int group_number = m_block_to_groupnumber[block];
    //             int cluster_id = new_cluster.return_id();
    //             new_cluster.add_new_block(block, group_number);
    //             m_best_placement_map[block] = cluster_id;
    //         }
    //         m_best_placement_raw.push_back(new_cluster);
    //     }
    //     for (int i = 0; i < m_stripe_information.size() - 1; i++)
    //     {
    //         std::string last_data = m_stripe_information[i][m_stripe_information[i].size() - 2];
    //         std::string local_block = m_stripe_information[i][m_stripe_information[i].size() - 1];
    //         int cluster_number = m_best_placement_map[last_data];
    //         int group_number = m_block_to_groupnumber[last_data];
    //         m_best_placement_raw[cluster_number].add_new_block(local_block, group_number);
    //         m_best_placement_map[local_block] = cluster_number;
    //     }
    //     if (!check_cluster_information(m_best_placement_raw, m_best_placement_map))
    //     {
    //         std::cout << "!!!best Xorbas check_cluster_information()" << std::endl;
    //     }
    // };
    void Xorbas_Class::generate_best_placement()
    {
        for (int i = 0; i < m_n; i++)
        {
            m_best_placement_raw.push_back(Cluster(i, m_d - 1));
        }
        int p_cluster = 0;
        if (m_g >= m_r)
        {
            for (size_t i = 0; i < m_stripe_information.size() - 1; i++)
            {
                std::vector<std::string> group = m_stripe_information[i];
                if (m_best_placement_raw[p_cluster].return_nonparity_number()+group.size()-1> m_g)
                {
                    
                    p_cluster++;
                }
                for (size_t j = 0; j < group.size() - 1; j++)
                {
                    std::string block = group[j];
                    int group_number = m_block_to_groupnumber[block];
                    int cluster_id = m_best_placement_raw[p_cluster].return_id();
                    m_best_placement_raw[p_cluster].add_new_block(block, group_number);
                    m_best_placement_map[block] = cluster_id;
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
                    for (int j = 0; j < m_d - 1; j++)
                    {
                        std::string block = group[group.size() - 1 - remain + j];
                        int group_number = m_block_to_groupnumber[block];
                        int cluster_id = m_best_placement_raw[p_cluster].return_id();
                        m_best_placement_raw[p_cluster].add_new_block(block, group_number);
                        m_best_placement_map[block] = cluster_id;
                    }
                    remain = remain - (m_d - 1);
                    p_cluster++;
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
                if (m_best_placement_raw[p_cluster].return_nonparity_number() + remain_list[j].size() > m_g)
                {
                    std::cout<<"m_best_placement_raw[p_cluster].return_nonparity_number():"<<m_best_placement_raw[p_cluster].return_nonparity_number()<<std::endl;
                    p_cluster++;
                }
                for (auto block : remain_list[j])
                {
                    int group_number = m_block_to_groupnumber[block];
                    int cluster_id = m_best_placement_raw[p_cluster].return_id();
                    m_best_placement_raw[p_cluster].add_new_block(block, group_number);
                    m_best_placement_map[block] = cluster_id;
                }
            }
        }
        std::vector<std::string> global_parity = m_stripe_information[m_stripe_information.size() - 1];
        int remain = global_parity.size();
        int global_ptr = 0;
        for (size_t i = 0; i < m_best_placement_raw.size(); i++)
        {
            Cluster *each_cluster = &m_best_placement_raw[i];
            while (each_cluster->return_nonparity_number() < m_g)
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
        for(size_t i = 0; i < m_best_placement_raw.size(); i++){
            if(m_best_placement_raw[i].return_block_number()==0){
                p_cluster = i;
            }
        }
        for (int i = 0; i < m_stripe_information.size() - 1; i++)
        {
            std::string last_data = m_stripe_information[i][m_stripe_information[i].size() - 2];
            std::string local_block = m_stripe_information[i][m_stripe_information[i].size() - 1];
            int last_cluster_number = m_best_placement_map[last_data];
            int input_cluster_ptr = last_cluster_number;
            if(m_best_placement_raw[last_cluster_number].return_nonparity_number() > m_g){
                input_cluster_ptr = p_cluster;
            }
            int group_number = m_block_to_groupnumber[local_block];
            m_best_placement_raw[input_cluster_ptr].add_new_block(local_block, group_number);
            m_best_placement_map[local_block] = input_cluster_ptr;
        }

        for (int i = 0; i < m_n; i++)
        {
            if (m_best_placement_raw[i].return_block_number() == 0)
            {
                m_best_placement_raw.erase(m_best_placement_raw.begin() + i);
            }
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
            for (size_t j = 0; j < group.size(); j++)
            {
                if (j == group.size())
                {
                    if (group.size() > m_g + m_l)
                    {
                        std::vector<std::string> repair_request;
                        for (int lll = 0; lll < m_l; lll++)
                        {
                            if (i != lll)
                            {
                                repair_request.push_back(index_to_str("L", lll));
                            }
                        }
                        for (int lll = 0; lll < m_g; lll++)
                        {
                            repair_request.push_back(index_to_str("G", lll));
                        }
                        break;
                    }
                }
                else
                {
                    std::string block = group[j];
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
    };
    bool Xorbas_Class::xorbas_make_matrix(int k, int g, int l, int *final_matrix)
    {
        int r = ceil(k, l);
        int *matrix = NULL;
        int alpha = 2;
        std::vector<int> H_in_paper;
        if (final_matrix == NULL)
        {
            std::cout << "final_matrix == NULL" << std::endl;
        }
        bzero(final_matrix, sizeof(int) * k * (g + l));
        for (int i = 0; i < k + g; i++)
        {
            H_in_paper.push_back(1);
        }
        std::vector<int> one_line;
        one_line.push_back(1);
        for (int i = 0; i < k + g - 1; i++)
        {
            int alpha1 = galois_single_multiply(alpha, one_line[one_line.size() - 1], 8);
            one_line.push_back(alpha1);
        }

        std::vector<int> two_line(one_line);
        for (size_t i = 0; i < std::max(g - 1, 0); i++)
        {
            if (i == 0)
            {
                for (size_t i = 0; i < one_line.size(); i++)
                {
                    H_in_paper.push_back(one_line[i]);
                }
            }
            else
            {
                for (size_t j = 0; j < one_line.size(); j++)
                {
                    two_line[j] = galois_single_multiply(one_line[j], two_line[j], 8);
                }
                for (size_t j = 0; j < two_line.size(); j++)
                {
                    H_in_paper.push_back(two_line[j]);
                }
            }
        }
        std::vector<int> g_g_matrix;
        for (int i = 0; i < g; i++)
        {
            for (int j = 0; j < g; j++)
            {
                g_g_matrix.push_back(H_in_paper[i * (k + g) + k + j]);
            }
        }
        std::vector<int> invert(g_g_matrix.size());
        jerasure_invert_matrix(g_g_matrix.data(), invert.data(), g, 8);
        int *part_matrix = jerasure_matrix_multiply(invert.data(), H_in_paper.data(), g, g, g, g + k, 8);
        std::vector<int> G_g_k;

        for (size_t i = 0; i < g; i++)
        {
            for (size_t j = 0; j < k; j++)
            {
                G_g_k.push_back(part_matrix[i * (k + g) + j]);
            }
        }
        std::vector<int> G_g_k_T;
        for (size_t i = 0; i < k; i++)
        {
            for (size_t j = 0; j < g; j++)
            {
                G_g_k_T.push_back(G_g_k[j * k + i]);
            }
        }
        std::vector<int> G_in_paper;
        for (int i = 0; i < k; i++)
        {
            for (int j = 0; j < k; j++)
            {
                if (i == j)
                {
                    G_in_paper.push_back(1);
                }
                else
                {
                    G_in_paper.push_back(0);
                }
            }
            for (int j = k; j < k + g; j++)
            {
                G_in_paper.push_back(G_g_k_T[i * g + j - k]);
            }
        }
        for (size_t i = 0; i < g; i++)
        {
            for (size_t j = 0; j < k; j++)
            {
                final_matrix[i * k + j] = G_in_paper[j * (k + g) + i + k];
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
        if (m_if_debug)
        {
            for (int i = 0; i < g + l; i++)
            {
                for (int j = 0; j < k; j++)
                {
                    std::cout << " " << final_matrix[i * k + j];
                }
                std::cout << std::endl;
            }
        }
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