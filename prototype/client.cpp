#include "proxy.h"
#include "ToolBox.h"

int main(int argc, char **argv)
{
    if (argc != 7)
    {
        std::cout << "./client partial_decoding encode_type placement_type n k r value_size_kbytes" << std::endl;
        std::cout << "./client false Optimal_LRC Flat 12 6 3 1024" << std::endl;
        exit(-1);
    }
    bool partial_decoding;
    REPAIR::EncodeType encode_type;
    REPAIR::PlacementType placement_type;
    int n, k, r;
    int value_size_kbytes;
    partial_decoding = (std::string(argv[1]) == "true");
    if (std::string(argv[2]) == "Xorbas")
    {
        encode_type = REPAIR::Xorbas;
    }
    else if (std::string(argv[2]) == "Azure_LRC")
    {
        encode_type = REPAIR::Azure_LRC;
    }
    else if (std::string(argv[2]) == "Azure_LRC_1")
    {
        encode_type = REPAIR::Azure_LRC_1;
    }
    else if (std::string(argv[2]) == "Optimal_LRC")
    {
        encode_type = REPAIR::Optimal_LRC;
    }
    else
    {
        std::cout << "error: unknown encode_type" << std::endl;
        exit(-1);
    }

    if (std::string(argv[3]) == "Flat")
    {
        placement_type = REPAIR::Flat;
    }
    else if (std::string(argv[3]) == "Random")
    {
        placement_type = REPAIR::Random;
    }
    else if (std::string(argv[3]) == "Best_Placement")
    {
        placement_type = REPAIR::Best_Placement;
    }
    else
    {
        std::cout << "error: unknown placement_type" << std::endl;
        exit(-1);
    }
    n = std::stoi(std::string(argv[4]));
    k = std::stoi(std::string(argv[5]));
    r = std::stoi(std::string(argv[6]));
    // std::cout << "test!" << std::endl;
    std::string config_path = "/home/msms/codes/Repair_optimal/prototype/config/ClusterInformation.xml";
    std::string networkcore_ip_port = "0.0.0.0:11221";
    REPAIR::Proxy proxy(config_path, networkcore_ip_port);
    if (proxy.SetParameter({partial_decoding, encode_type, placement_type, n, k, r}))
    {
        std::cout << "set parameter successfully!" << std::endl;
    }
    else
    {
        std::cout << "Failed to set parameter!" << std::endl;
    }
    std::vector<std::string> key_list;
    std::string key1;
    std::string value1;
    REPAIR::random_generate_kv(key1, value1, 6, 16070);
    for (int i = 0; i < 1; i++)
    {
        std::string key;
        std::string value;
        REPAIR::random_generate_kv(key, value, 6, 16070);
        std::cout << key.size() << std::endl;
        std::cout << key << std::endl;
        std::cout << value.size() << std::endl;

        proxy.Set(key, value);
        key_list.push_back(key);
    }
    
    for (auto key : key_list)
    {
        for (int i = 0; i < n; i++)
        {
            proxy.RepairByKeyIndex(key, i);
        }
    }
    for (auto key : key_list)
    {
        std::string get_value;
        if (proxy.Get(key, get_value))
        {
            //std::cout << "value" << std::endl;
            // std::cout << value << std::endl;
            //std::cout << "get_value" << std::endl;
            // std::cout << get_value << std::endl;

            if (value1 == get_value)
            {
                std::cout << "repair kv successfully" << std::endl;
            }
            else
            {
                std::cout << "wrong!" << std::endl;
                break;
            }
        }
        else
        {
            std::cout << "not object!" << std::endl;
        }
    }
    return 0;
}
