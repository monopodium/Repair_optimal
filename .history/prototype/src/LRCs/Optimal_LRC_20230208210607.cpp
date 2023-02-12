#include "General.h"
namespace REPAIR
{
    bool Optimal_LRC_Class::check_parameter()
    {
        if (n % (r + 1) == 1)
        {
            std::cout << "Parameters do not meet requirements!" << std::endl;
            return false;
        }
        return true;
    };
    int Optimal_LRC_Class::calculate_distance()
    {
        int gl = ceil(n, r + 1) - l;
        if (ceil(g + 1, r) > gl)
        {
            d = g + gl + 2;
        }
        else
        {
            d = g + gl + 1;
        }
        return d;
    };
    void Optimal_LRC_Class::generate_best_placement()
    {
        Cluster new_cluster = Cluster(m_best_placement_raw.size(), d - 1);
        m_best_placement_raw.push_back(new_cluster);
        for (std::vector<std::string> each_group : m_stripe_information)
        {
            if (int(each_group.size()) <= d - 1)
            {
                Cluster last_cluster = m_best_placement_raw[m_best_placement_raw.size() - 1];
                if (last_cluster.remaind() < int(each_group.size()))
                {
                    m_best_placement_raw.push_back(Cluster(m_best_placement_raw.size(), d - 1));
                }
                last_cluster = m_best_placement_raw[m_best_placement_raw.size() - 1];
                for (std::string block : each_group)
                {
                    last_cluster.add_new_block(block, m_block_to_groupnumber[block]);
                    m_best_placement_map[block] = last_cluster.return_id();
                }
            }
            else
            {
                for (int i = 0; i < ceil(int(each_group.size()), d - 1); i++)
                {

                    int each_c = std::min(int(each_group.size() - i * (d - 1)), d - 1);

                    if (m_best_placement_raw[m_best_placement_raw.size() - 1].remaind() < each_c)
                    {
                        m_best_placement_raw.push_back(Cluster(m_best_placement_raw.size(), d - 1));
                    }
                    Cluster last_cluster = m_best_placement_raw[m_best_placement_raw.size() - 1];
                    for (int j = i * (d - 1); j < each_c + i * (d - 1); j++)
                    {
                        std::string block = each_group[j];
                        last_cluster.add_new_block(block, m_block_to_groupnumber[block]);
                        m_best_placement_map[block] = last_cluster.return_id();
                    }
                }
            }
        }
    };
    void Optimal_LRC_Class::nkr_to_klgr(int n, int k, int r, int &in_l, int &in_g)
    {
        l = ceil(n, (r + 1));
        g = n - k - l;
        in_l = l;
        in_g = g;
    };
    void Optimal_LRC_Class::klgr_to_nkr(int k, int l, int g, int r, int &in_n)
    {
        n = k + l + g;
        in_n = n;
    };
    void Optimal_LRC_Class::generate_stripe_information()
    {
        int group_ptr = 0;
        std::vector<std::string> group;
        m_stripe_information.push_back(group);
        for (int i = 0; i < g + k; i++)
        {
            std::string block;
            if (i == r * (group_ptr + 1))
            {
                group_ptr = group_ptr + 1;
                std::vector<std::string> group;
                m_stripe_information.push_back(group);
            }
            if (i < k)
            {
                block = index_to_str("D", i);
            }
            else
            {
                block = index_to_str("G", i - k);
            }
            m_stripe_information[group_ptr].push_back(block);
            m_block_to_groupnumber[block] = group_ptr;
        }

        for (int i = 0; i < l; i++)
        {
            std::string block = index_to_str("L", i);
            m_stripe_information[i].push_back(block);
            m_block_to_groupnumber[block] = i;
        }
        for(auto group:m_stripe_information){
            for(:group)
        }
        if (int(m_stripe_information.size()) != l)
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
        matrix = reed_sol_vandermonde_coding_matrix(k, g, w);
        if (matrix == NULL)
        {
            std::cout << "matrix == NULL" << std::endl;
        }
        jerasure_matrix_encode(k, g, w, matrix, data_ptrs, coding_ptrs, blocksize);
        free(matrix);
        std::vector<int> group_number(l, 0);
        for (int i = 0; i < l; i++)
        {
            int group_size = std::min(r, k + g - i * r);
            std::vector<char *> vecotr_number(group_size);
            char **new_data = (char **)vecotr_number.data();
            for (int j = 0; j < group_size; j++)
            {
                if (i * r + j < k)
                {
                    new_data[j] = data_ptrs[i * r + j];
                }
                else
                {
                    new_data[j] = coding_ptrs[i * r + j - k];
                }
            }
            std::vector<int> last_matrix(group_size, 1);
            jerasure_matrix_encode(group_size, 1, 8, last_matrix.data(), new_data, &coding_ptrs[g + i], blocksize);
        }
        return true;
    };
    bool Optimal_LRC_Class::decode(char **data_ptrs, char **coding_ptrs, int *erasures, int blocksize)
    {
        // std::vector<int> matrix(g * k, 0);
        int *rs_matrix = reed_sol_vandermonde_coding_matrix(k, g, w);
        // memcpy(matrix.data(), rs_matrix, g * k * sizeof(int));
        jerasure_matrix_decode(k, g, w, rs_matrix, 0, erasures, data_ptrs, coding_ptrs, blocksize);
        free(rs_matrix);
        return true;
    }
}