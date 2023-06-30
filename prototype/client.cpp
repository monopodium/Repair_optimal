#include "proxy.h"
#include "ToolBox.h"

int main(int argc, char **argv)
{
    if (argc != 10)
    {
        std::cout << "./client partial_decoding encode_type placement_type n k r value_size_kbytes run_times result_file_abs" << std::endl;
        std::cout << "./client false Xorbas Random 16 10 5 1 10 filename" << std::endl;
        exit(-1);
    }
    std::ofstream outfile;

    std::string result_path =argv[9];// "/home/msms/codes/Repair_optimal/result_azure_lrc.txt";
    //std::cout<<"result_path"<<result_path<<std::endl;
    bool partial_decoding;
    REPAIR::EncodeType encode_type;
    REPAIR::PlacementType placement_type;
    int n, k, r;
    int value_size_kbytes;
    int run_times = 1;
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
    else if (std::string(argv[3]) == "Sub_Optimal")
    {
        placement_type = REPAIR::Sub_Optimal;
    }
    else
    {
        std::cout << "error: unknown placement_type" << std::endl;
        exit(-1);
    }
    n = std::stoi(std::string(argv[4]));
    k = std::stoi(std::string(argv[5]));
    r = std::stoi(std::string(argv[6]));
    value_size_kbytes = std::stoi(std::string(argv[7]));
    run_times = std::stoi(std::string(argv[8]));
    int totalvalue_size_kbytes = value_size_kbytes * 100;//value_size_kbytes * 100;
    int value_number = totalvalue_size_kbytes / value_size_kbytes;
    // std::cout << "test!" << std::endl;
    std::string config_path = "/home/msms/codes/Repair_optimal/prototype/config/ClusterInformation.xml";
    std::string networkcore_ip_port = "10.0.0.61:12222";
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
    std::string traces_path = "/home/msms/codes/Repair_optimal/prototype/traces/file_size_" + std::to_string(value_size_kbytes) + "K" + ".data";
    //std::cout<<"traces_path:"<<traces_path<<std::endl;
    std::ifstream infile(traces_path);
    if (infile.is_open())
    {
        getline(infile, value1);
        if (value1.size()!=value_size_kbytes*1024)
        {
            std::cout<<"read traces fail! value1.size()"<<value1.size()<<std::endl;
            REPAIR::random_generate_kv(key1, value1, 6, value_size_kbytes * 1024);
        }
    }
    else
    {
        std::cout<<"read traces fail!"<<std::endl;
        REPAIR::random_generate_kv(key1, value1, 6, value_size_kbytes * 1024);
    }
    // std::cout << "value_number:" << value_number << std::endl;
    // outfile << "./client partial_decoding encode_type placement_type n k r value_size_kbytes run_times" << std::endl;
    outfile.open(result_path, std::ios::app);

    outfile << "partial_decoding:" << partial_decoding << " encode_type: " << encode_type
            << " placement_type: " << placement_type << " n: " << n << " k: " << k << " r: " << r
            << " value_size_kbytes: " << value_size_kbytes << " run_times: " << run_times << std::endl;
    outfile.close();
    for (int i = 0; i < value_number; i++)
    {
        std::string key;
        std::string value00000;
        REPAIR::random_generate_kv(key, value00000, 6, 1);
        // std::cout << key.size() << std::endl;
        // std::cout <<i<<"    "<< key << std::endl;
        // std::cout << value1.size() << std::endl;

        proxy.Set(key, value1);
        key_list.push_back(key);
    }

    std::cout << "start repair!" << std::endl;
    auto start = std::chrono::system_clock::now();
    double min_drc_duration = -1.0;
    double max_drc_duration = 0.0;
    for (int j = 0; j < run_times; j++)
    {
        auto start_each = std::chrono::system_clock::now();
        for (auto key : key_list)
        {
            for (int i = 0; i < k; i++)
            {
                proxy.RepairByKeyIndex(key, i);
            }
        }
        auto end_each = std::chrono::system_clock::now();
        auto duration_each = std::chrono::duration_cast<std::chrono::microseconds>(end_each - start_each);
        if (j == 0)
        {
            min_drc_duration = double(duration_each.count());
            max_drc_duration = double(duration_each.count());
        }
        max_drc_duration = std::max(max_drc_duration, double(duration_each.count()));
        min_drc_duration = std::min(min_drc_duration, double(duration_each.count()));
    }
    auto end = std::chrono::system_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    double drc = double(duration.count()) / (k * key_list.size() * run_times);
    double drc_min = min_drc_duration / (k * key_list.size());
    double drc_max = max_drc_duration / (k * key_list.size());
    outfile.open(result_path, std::ios::app);
    outfile << "DRC(micro second): " << drc << std::endl;
    outfile << "DRC_min(micro second): " << drc_min << std::endl;
    outfile << "DRC_max(micro second): " << drc_max << std::endl;
    outfile.close();

    double min_rate_duration = -1.0;
    double max_rate_duration = -1.0;
    auto start1 = std::chrono::system_clock::now();
    for (int j = 0; j < run_times; j++)
    {
        auto start_each = std::chrono::system_clock::now();
        for (auto key : key_list)
        {
            // std::cout << key << std::endl;
            for (int i = 0; i < n; i++)
            {
                proxy.RepairByKeyIndex(key, i);
            }
        }
        auto end_each = std::chrono::system_clock::now();
        auto duration_each = std::chrono::duration_cast<std::chrono::milliseconds>(end_each - start_each);
        if (j == 0)
        {
            min_rate_duration = double(duration_each.count());
            max_rate_duration = double(duration_each.count());
        }
        // std::cout << "double(duration_each.count()):" << double(duration_each.count()) << std::endl;
        min_rate_duration = std::min(min_rate_duration, double(duration_each.count()));
        max_rate_duration = std::max(max_rate_duration, double(duration_each.count()));
    }
    auto end1 = std::chrono::system_clock::now();
    auto duration1 = std::chrono::duration_cast<std::chrono::milliseconds>(end1 - start1);
    double repair_rate_miB = (key_list.size() * value_size_kbytes * run_times * n * 1000) / (k * 1024 * double(duration1.count()));
    double repair_rate_min = (key_list.size() * value_size_kbytes * n * 1000) / (k * 1024 * max_rate_duration);
    double repair_rate_max = (key_list.size() * value_size_kbytes * n * 1000) / (k * 1024 * min_rate_duration);

    outfile.open(result_path, std::ios::app);
    outfile << "repair_Rate_MiB/(second): " << repair_rate_miB << std::endl;
    outfile << "repair_Rate_MiB_min/(second): " << repair_rate_min << std::endl;
    outfile << "repair_Rate_MiB_max/(second): " << repair_rate_max << std::endl;
    outfile << std::endl;
    outfile.close();
    int MiB = 1048576;
    for (auto key : key_list)
    {
        std::string get_value;
        if (proxy.Get(key, get_value))
        {
            if (value1 == get_value)
            {
                // std::cout << "repair kv successfully" << std::endl;
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
