#ifndef PROXY_H
#define PROXY_H
#include "devcommon.h"
#include "General.h"
#include <libmemcached/memcached.h>
#include <thread>

namespace REPAIR
{
    class Proxy
    {
    public:
        Proxy(std::string config_path) : m_config_path(config_path)
        {
            std::cout << "m_config_path:" << m_config_path << std::endl;
            init_memcached();
            init_cluster_meta();
        };
        ~Proxy() { memcached_free(m_memcached); };
        bool Set(std::string key, std::string value);
        bool Get(std::string key, std::string &value);
        bool Delete(std::string key);
        bool Repair(std::string key, int blockid);
        bool SetParameter(ECSchema input_ecschema);
        
    private:
        std::string config_path;
        bool init_memcached();
        bool init_cluster_meta();
        memcached_st *m_memcached;
        ECSchema m_encode_parameter;
        std::string m_config_path;
        std::map<unsigned int, Clusteritem> m_Cluster_info;
        std::map<unsigned int, Nodeitem> m_Node_info;
        Optimal_LRC_Class m_Optimal_LRC_encoder;
        std::map<int,memcached_st *> memcached_list;
        bool Proxy::init_one_memcached(memcached_st * memcached, std::string ip, int port);
    };

}
#endif
