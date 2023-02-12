#include "proxy.h"

namespace REPAIR
{
    bool Proxy::init_one_memcached(memcached_st * memcached, std::string ip, int port){
        memcached_return rc;
        memcached = memcached_create(NULL);
        memcached_server_st *servers;
        servers = memcached_server_list_append(NULL, ip.c_str(), port, &rc);
        rc = memcached_server_push(m_memcached, servers);
        memcached_server_free(servers);
        memcached_behavior_set(m_memcached, MEMCACHED_BEHAVIOR_DISTRIBUTION, MEMCACHED_DISTRIBUTION_CONSISTENT);
        memcached_behavior_set(m_memcached, MEMCACHED_BEHAVIOR_RETRY_TIMEOUT, 20);
        memcached_behavior_set(m_memcached, MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT, 5);
        memcached_behavior_set(m_memcached, MEMCACHED_BEHAVIOR_AUTO_EJECT_HOSTS, true);
    }
    bool Proxy::init_memcached()
    {
        memcached_return rc;
        memcached_server_st *servers;
        m_memcached = memcached_create(NULL);

        bool init = false;
        tinyxml2::XMLDocument xml;
        xml.LoadFile(m_config_path.c_str());
        tinyxml2::XMLElement *root = xml.RootElement();
        for (tinyxml2::XMLElement *cluster = root->FirstChildElement(); cluster != nullptr; cluster = cluster->NextSiblingElement())
        {
            for (tinyxml2::XMLElement *node = cluster->FirstChildElement()->FirstChildElement(); node != nullptr; node = node->NextSiblingElement())
            {
                std::string node_uri(node->Attribute("uri"));
                auto pos = node_uri.find(':');
                std::string Node_ip = node_uri.substr(0, pos);
                int Node_port = std::stoi(node_uri.substr(pos + 1, node_uri.size()));
                std::cout << Node_ip << ":" << Node_port << std::endl;
                if (!init)
                {
                    servers = memcached_server_list_append(NULL, Node_ip.c_str(), Node_port, &rc);
                    init = true;
                }
                else
                {
                    servers = memcached_server_list_append(servers, Node_ip.c_str(), Node_port, &rc);
                }
            }
        }

        rc = memcached_server_push(m_memcached, servers);
        memcached_server_free(servers);

        memcached_behavior_set(m_memcached, MEMCACHED_BEHAVIOR_DISTRIBUTION,
                               MEMCACHED_DISTRIBUTION_CONSISTENT);
        memcached_behavior_set(m_memcached, MEMCACHED_BEHAVIOR_RETRY_TIMEOUT, 20);
        //  memcached_behavior_set(m_memcached,
        //  MEMCACHED_BEHAVIOR_REMOVE_FAILED_SERVERS, 1) ;  //
        //  同时设置MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT 和
        //  MEMCACHED_BEHAVIOR_AUTO_EJECT_HOSTS
        memcached_behavior_set(m_memcached, MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT,
                               5);
        memcached_behavior_set(m_memcached, MEMCACHED_BEHAVIOR_AUTO_EJECT_HOSTS,
                               true);
        return true;
    };
    bool Proxy::SetParameter(ECSchema input_ecschema)
    {
        m_encode_parameter = input_ecschema;
        std::cout << "m_encode_parameter.partial_decoding" << m_encode_parameter.partial_decoding << std::endl;
        std::cout << "m_encode_parameter.encodetype" << m_encode_parameter.encodetype << std::endl;
        std::cout << "m_encode_parameter.placementtype" << m_encode_parameter.placementtype << std::endl;
        std::cout << "m_encode_parameter.n_block" << m_encode_parameter.n_block << std::endl;
        std::cout << "m_encode_parameter.k_datablock" << m_encode_parameter.k_datablock << std::endl;
        std::cout << "m_encode_parameter.r_datapergroup" << m_encode_parameter.r_datapergroup << std::endl;
        m_Optimal_LRC_encoder.set_parameter(m_encode_parameter.n_block, m_encode_parameter.k_datablock, m_encode_parameter.r_datapergroup);
        return true;
    }
    bool Proxy::init_cluster_meta()
    {

        std::cout << "m_config_path:" << m_config_path << std::endl;
        tinyxml2::XMLDocument xml;
        xml.LoadFile(m_config_path.c_str());
        tinyxml2::XMLElement *root = xml.RootElement();
        int node_id = 0;
        for (tinyxml2::XMLElement *cluster = root->FirstChildElement(); cluster != nullptr; cluster = cluster->NextSiblingElement())
        {
            std::string cluster_id(cluster->Attribute("id"));
            std::string proxy(cluster->Attribute("proxy"));
            std::cout << "cluster_id: " << cluster_id << " , proxy: " << proxy << std::endl;
            m_Cluster_info[std::stoi(cluster_id)].Cluster_id = std::stoi(cluster_id);
            auto pos = proxy.find(':');
            m_Cluster_info[std::stoi(cluster_id)].proxy_ip = proxy.substr(0, pos);
            m_Cluster_info[std::stoi(cluster_id)].proxy_port = std::stoi(proxy.substr(pos + 1, proxy.size()));
            for (tinyxml2::XMLElement *node = cluster->FirstChildElement()->FirstChildElement(); node != nullptr; node = node->NextSiblingElement())
            {
                memcached_st * memcached;
                init_one_memcached
                std::string node_uri(node->Attribute("uri"));
                std::cout << "____node: " << node_uri << std::endl;
                m_Cluster_info[std::stoi(cluster_id)].nodes.push_back(node_id);
                m_Node_info[node_id].Node_id = node_id;
                auto pos = node_uri.find(':');
                m_Node_info[node_id].Node_ip = node_uri.substr(0, pos);
                m_Node_info[node_id].Node_port = std::stoi(node_uri.substr(pos + 1, node_uri.size()));
                m_Node_info[node_id].Cluster_id = std::stoi(cluster_id);
                node_id++;
            }
        }

        for (auto it : m_Cluster_info)
        {
            std::cout << "it.first:" << it.first << " " << std::endl;
            std::cout << "cluster_id" << it.second.Cluster_id << std::endl;
            std::cout << "proxy_ip" << it.second.proxy_ip << std::endl;
            std::cout << "proxy_port" << it.second.proxy_port << std::endl;
            for (auto item : it.second.nodes)
            {
                std::cout << " nodes " << item;
            }
            std::cout << std::endl;
        }
    }
    

    bool Proxy::Set(std::string key, std::string value)
    {
        int n = m_encode_parameter.n_block;
        int k = m_encode_parameter.k_datablock;
        int r = m_encode_parameter.r_datapergroup;
        REPAIR::EncodeType encode_type = m_encode_parameter.encodetype;
        REPAIR::PlacementType placement_type = m_encode_parameter.placementtype;
        int value_size_bytes = value.size();
        int block_size = ceil(value_size_bytes, k);
        block_size = 16 * ceil(block_size, 16);
        int extend_value_size_byte = block_size * k;

        for (int i = value_size_bytes; i < extend_value_size_byte; i++)
        {
            value = value + '0';
        }

        char *buf = (char *)value.data();

        std::vector<char *> v_data(k);
        std::vector<char *> v_coding(n - k);

        char **data = (char **)v_data.data();
        char **coding = (char **)v_coding.data();

        std::vector<std::vector<char>> v_coding_area(n - k, std::vector<char>(block_size));
        for (int j = 0; j < k; j++)
        {
            data[j] = &buf[j * block_size];
        }
        for (int j = 0; j < n - k; j++)
        {
            coding[j] = v_coding_area[j].data();
        }

        std::vector<std::pair<std::string, int>> nodes_ip_and_port;
        std::vector<int> nodes_id;

        //Optimal_LRC_Class new_Optimal_LRC = Optimal_LRC_Class(n, k, r);
        m_Optimal_LRC_encoder.generate_placement(placement_type);

        m_Optimal_LRC_encoder.encode(data, coding, block_size);

        std::vector<std::thread> senders;
        for (int j = 0; j < n; j++)
        {
            std::string shard_id = key + std::to_string(j);
            std::pair<std::string, int> &ip_and_port = nodes_ip_and_port[i * send_num + j];
            senders.push_back(std::thread(send_to_datanode, j, k, shard_id, data, coding, shard_size, ip_and_port));
        }
        for (int j = 0; j < senders.size(); j++)
        {
            senders[j].join();
        }
    }
    bool Proxy::Get(std::string key, std::string &value)
    {
    }

}