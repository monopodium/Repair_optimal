#include "proxy.h"
#include "ToolBox.h"

int main(int argc, char **argv)
{
    if (argc != 7)
    {
        std::cout << "./run_client partial_decoding encode_type placement_type n k r" << std::endl;
        std::cout << "./run_client false RS Flat 12 6 3" << std::endl;
        exit(-1);
    }
    bool partial_decoding;
    REPAIR::EncodeType encode_type;
    REPAIR::PlacementType placement_type;
    int n, k, r;

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
    std::string config_path = "/home/msms/codes/Repair_optimal/prototype/config/cluster.xml";
    REPAIR::Proxy proxy(config_path);
    if (proxy.SetParameter({partial_decoding, encode_type, placement_type, n, k, r}))
    {
        std::cout << "set parameter successfully!" << std::endl;
    }
    else
    {
        std::cout << "Failed to set parameter!" << std::endl;
    }

    for (int i = 0; i < 10000; i++)
    {
        std::string key;
        std::string value;
        REPAIR::random_generate_kv(key, value, 6, 16070);
        std::cout << key.size() << std::endl;
        std::cout << key << std::endl;
        std::cout << value.size() << std::endl;

        proxy.Set(key, value);

        // std::string get_value;
        // proxy.Get(key, get_value);
        // std::cout << value << std::endl;
        // std::cout << get_value << std::endl;
        // if (value == get_value)
        // {
        //     std::cout << "set kv successfully" << std::endl;
        // }
        // else
        // {
        //     std::cout << "wrong!" << std::endl;
        //     break;
        // }
    }

    return 0;
}
