#include "General.h"
namespace REPAIR
{
    bool Xorbas_Class::check_parameter()
    {

        return true;
    };
    int Xorbas_Class::calculate_distance()
    {
        d = g + 1;
        return d;
    };
    void Xorbas_Class::generate_best_placement(){

    };
    void Xorbas_Class::nkr_to_klgr(int n, int k, int r, int &l, int &g)
    {
        l = ceil(k, r);
        g = n - k - l;
    };
    void Xorbas_Class::klgr_to_nkr(int k, int l, int g, int r, int &n)
    {
        n = k + l + g;
    };
    void Xorbas_Class::generate_stripe_information()
    {
        int group_ptr = -1;
        for (int i = 0; i < k; i++)
        {
            if (i % r == 0)
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
        m_stripe_information.push_back(group);
        for (int i = 0; i < g; i++)
        {
            std::string block = index_to_str("G", i);
            group.push_back(block);
            m_block_to_groupnumber[block] = -1;
        }
        for (int i = 0; i < l; i++)
        {
            std::string block = index_to_str("L", i);
            m_stripe_information[i].push_back(block);
            m_block_to_groupnumber[block] = i;
        }
        if (m_stripe_information.size() != l + 1)
        {
            std::cout << "Xorbas, error" << std::endl;
        }
    };
    void Xorbas_Class::generate_block_repair_request()
    {
        for (int i = 0; i < l; i++)
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

        for (std::string block : m_stripe_information[l])
        {
            for (std::string other_block : m_stripe_information[l])
            {
                std::vector<std::string> repair_request;
                if (block != other_block)
                {
                    repair_request.push_back(other_block);
                }
                for (int i = 0; i < l; i++)
                {
                    repair_request.push_back(index_to_str("L", i));
                }
                m_block_repair_request[block] = repair_request;
            }
        }
    };
    void Xorbas_Class::return_group_number(){};
        bool Xorbas_Class::encode(char **data_ptrs, char **coding_ptrs, int blocksize)
    {

    };
    bool Xorbas_Class::decode(char **data_ptrs, char **coding_ptrs, int *erasures, int blocksize)
    {

    }
}