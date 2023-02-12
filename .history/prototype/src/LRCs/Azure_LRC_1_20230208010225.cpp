#include "General.h"
namespace REPAIR
{
    bool Azure_LRC_1_Class::check_parameter()
    {
        if (k + l > n)
        {
            return false;
        }
        return true;
    };
    int Azure_LRC_1_Class::calculate_distance()
    {
        d = g + 2;
        return d;
    };
    void Azure_LRC_1_Class::generate_best_placement()
    {
        Cluster new_cluster = Cluster(m_best_placement_raw.size(), d - 1);
        m_best_placement_raw.push_back(new_cluster);
        for (std::vector<std::string> each_group : m_stripe_information)
        {
            if (each_group.size() <= d - 1)
            {
                Cluster last_cluster = m_best_placement_raw[m_best_placement_raw.size() - 1];
                if (last_cluster.remaind() < each_group.size())
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
    void Azure_LRC_1_Class::nkr_to_klgr(int n, int k, int r, int &l, int &g)
    {
        l = ceil(k, r) + 1;
        g = n - k - l;
    };
    void Azure_LRC_1_Class::klgr_to_nkr(int k, int l, int g, int r, int &n)
    {
        n = k + l + g;
    };
    void Azure_LRC_1_Class::generate_stripe_information()
    {
        for (int i = 0; i < l - 1; i++)
        {
            std::vector<std::string> group;
            m_stripe_information.push_back(group);
            for (int j = i * r; j < std::min(k, (i + 1) * r); j++)
            {
                group.push_back(index_to_str("D", i));
                m_block_to_groupnumber[index_to_str("D", i)] = i;
            }
        }
        std::vector<std::string> group;
        m_stripe_information.push_back(group);
        for (int i = 0; i < g; i++)
        {
            group.push_back(index_to_str("G", i));
            m_block_to_groupnumber[index_to_str("G", i)] = l;
        }
        for (int i = 0; i < l; i++)
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
        std::vector<int> new_matrix((g + l - 1) * k, 0);
        azure_lrc_make_matrix(k, g, l - 1, new_matrix.data());
        jerasure_matrix_encode(k, g + l - 1, w, new_matrix.data(), data_ptrs, coding_ptrs, blocksize);

        // 生成全局校验块的局部校验块
        std::vector<int> last_matrix(g, 1);
        jerasure_matrix_encode(g, 1, w, last_matrix.data(), coding_ptrs, &coding_ptrs[g + l - 1], blocksize);
    }
        bool Azure_LRC_Class::decode(char **data_ptrs, char **coding_ptrs, int *erasures, int blocksize){

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