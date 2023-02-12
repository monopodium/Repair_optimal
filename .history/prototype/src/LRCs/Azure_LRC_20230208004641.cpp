#include "General.h"
namespace REPAIR
{
    bool Azure_LRC_Class::check_parameter()
    {
        if (n <= k + l)
        {
            std::cout << "Parameters do not meet requirements!" << std::endl;
        }
    };
    int Azure_LRC_Class::calculate_distance()
    {
        d = g + 2;
        return d;
    };
    void Azure_LRC_Class::generate_best_placement()
    {
        int b = d - 1;
        for (int i = 0; i < n; i++)
        {
            m_best_placement_raw.push_back(Cluster(i, b));
        }
        for (int i = 0; i < l; i++)
        {
            std::vector<std::string> group = m_stripe_information[i];
            int cur_group_len = group.size();
            if (b >= cur_group_len)
            {
                for (Cluster each_cluster : m_best_placement_raw)
                {
                    if (int(each_cluster.is_from_new_group(i)) + each_cluster.form_group_number() + g >= each_cluster.return_block_number() + cur_group_len)
                    {
                        for (std::string block : group)
                        {
                            each_cluster.add_new_block(block, i);
                            m_best_placement_map[block] = each_cluster.return_id();
                        }
                        break;
                    }
                }
            }
            else
            {
                int cluster_number = ceil(cur_group_len, b);
                for (int j = 0; j < cluster_number; j++)
                {
                    int number_in_group = std::min(b, cur_group_len - j * b);
                    for (Cluster each_cluster : m_best_placement_raw)
                    {
                        if (int(each_cluster.is_from_new_group(i)) + each_cluster.form_group_number() + g >=
                            each_cluster.return_block_number() + number_in_group)
                        {
                            for (int ii = 0; ii < number_in_group; ii++)
                            {
                                each_cluster.add_new_block(group[j + ii], i);
                                m_best_placement_map[block] = each_cluster.return_id();
                            }
                            break;
                        }
                    }
                }
            }
        }
        for (Cluster each_cluster : m_best_placement_raw)
        {
            if (each_cluster.return_block_number() == 0)
            {
                for (std::string block : m_stripe_information[m_stripe_information.size() - 1])
                {
                    each_cluster.add_new_block(block, m_stripe_information.size() - 1);
                    m_best_placement_map[block] = each_cluster.return_id();
                }
                break;
            }
        }
        for (int i = 0; i < n; i++)
        {
            if (m_best_placement_raw[i].return_block_number() == 0)
            {
                m_best_placement_raw.erase(m_best_placement_raw.begin() + i);
            }
        }
    };
    void Azure_LRC_Class::nkr_to_klgr(int n, int k, int r, int &l, int &g)
    {
        l = ceil(k, r);
        g = n - k - l;
    };
    void Azure_LRC_Class::klgr_to_nkr(int k, int l, int g, int r, int &n)
    {
        n = k + l + g;
    };
    void Azure_LRC_Class::generate_stripe_information()
    {
        int group_ptr = -1;
        for (int i = 0; i < k; i++)
        {
            std::string block = index_to_str("D", i);
            if (i % r == 0)
            {
                std::vector<std::string> group;
                m_stripe_information.push_back(group);
                group_ptr++;
            }
            m_stripe_information[int(i / r)].push_back(block);
            m_block_to_groupnumber[block] = group_ptr;
        }
        std::vector<std::string> group;
        m_stripe_information.push_back(group);
        group_ptr++;
        for (int i = 0; i < g; i++)
        {
            std::string block = index_to_str("G", i);
            m_stripe_information[group_ptr].push_back(block);
            m_block_to_groupnumber[block] = group_ptr;
        }
        for (int i = 0; i < l; i++)
        {
            std::string block = index_to_str("L", i);
            m_stripe_information[i].push_back(block);
            m_block_to_groupnumber[block] = i;
        }
    };
    void Azure_LRC_Class::generate_block_repair_request()
    {
        for (int i = 0; i < l; i++)
        {
            for (std::string item : m_stripe_information[i])
            {
                std::vector<std::string> repair_request;
                for (std::string other_item : m_stripe_information[i])
                {
                    if (other_item != item)
                    {
                        repair_request.push_back(other_item);
                    }
                }
                m_block_repair_request[item] = repair_request;
            }
        }
        for (std::string item : m_stripe_information[m_stripe_information.size() - 1])
        {
            std::vector<std::string> repair_request;
            for (std::string other_item : m_stripe_information[i])
            {
                if (other_item != item)
                {
                    repair_request.push_back(other_item);
                }
            }
            m_block_repair_request[item] = repair_request;
        }
    };
    void Azure_LRC_Class::return_group_number(){};
    bool Azure_LRC_Class::encode(char **data_ptrs, char **coding_ptrs, int blocksize)
    {
        std::vector<int> new_matrix((g + l) * k, 0);
        azure_lrc_make_matrix(k, g, l, new_matrix.data());
        jerasure_matrix_encode(k, g + l, 8, new_matrix.data(), data_ptrs, coding_ptrs, blocksize);
    };
    bool Azure_LRC_Class::azure_lrc_make_matrix(int k, int g, int l, int *final_matrix)
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