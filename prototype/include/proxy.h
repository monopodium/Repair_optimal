#ifndef PROXY_H
#define PROXY_H
#include "metadefinition.h"
#include "General.h"


namespace REPAIR
{
    class Proxy
    {
    public:
        Proxy(std::string config_path, std::string networkcore) : m_config_path(config_path)
        {
            std::cout << "m_config_path:" << m_config_path << std::endl;
            auto pos = networkcore.find(':');
            networkcore_port_ip.first = networkcore.substr(0, pos);
            networkcore_port_ip.second = std::stoi(networkcore.substr(pos + 1, networkcore.size()));
            init_cluster_meta();
        };
        ~Proxy()
        {
            for (auto memcached_point : memcached_list)
            {
                memcached_free(memcached_point.second);
            }
        };
        bool Set(std::string key, std::string value);
        bool Get(std::string key, std::string &value);
        bool Delete(std::string key);
        bool Repair(std::string key, int blockid);
        bool SetParameter(ECSchema input_ecschema);
        bool RepairByKeyIndex(std::string key, int index);
        //bool Proxy::cross_network_core(std::string key, const char *value, int value_size);
    private:
        std::string config_path;
        bool init_memcached();
        bool init_cluster_meta();
        ECSchema m_encode_parameter;
        std::string m_config_path;
        std::map<std::string, StripeItem> m_Stripe_info;
        // vector中装的是数据块的nodeid,全局校验块的node_id,局部校验块node_id
        std::map<unsigned int, Clusteritem> m_Cluster_info;
        std::map<unsigned int, Nodeitem> m_Node_info;
        Optimal_LRC_Class m_Optimal_LRC_encoder;
        Azure_LRC_Class m_Azure_LRC_encoder;
        Azure_LRC_1_Class m_Azure_LRC_1_encoder;
        Xorbas_Class m_Xorbas_encoder;
        Code_Placement *m_encoder;
        std::map<int, memcached_st *> memcached_list;
        
        std::pair<std::string, int> networkcore_port_ip;
        bool init_one_memcached(memcached_st *memcached, std::string ip, int port);
        CrossNetworkCore m_networkcore;
    };

}
#endif
