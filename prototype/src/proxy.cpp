#include "proxy.h"

namespace REPAIR
{
    bool cross_network_core(CrossNetworkCore *network_core, std::string key, int key_size, const char *value, int value_size)
    {
        // vc std::cout<<"cross_network_core"<<std::endl;
        std::lock_guard<std::mutex> lock(network_core->mMutex);
        if (value == NULL)
        {
            return false;
        }
        memcached_return_t ret = memcached_set(network_core->networkcore, (const char *)key.data(), (size_t)key.size(), value, (size_t)value_size, (time_t)1000, (uint32_t)0);
        if (memcached_failed(ret))
        {
            std::cout << "cross_networkcore fail" << std::endl;
            return false;
        }
        memcached_return_t error;
        uint32_t flag;
        size_t value_size1;
        char *value_ptr = memcached_get(network_core->networkcore, (const char *)key.data(), (size_t)key.size(), &value_size1, &flag, &error);
        if (value_ptr == NULL)
        {
            std::cout << "cross_networkcore fail key:" << key << std::endl;
            return false;
        }

        return true;
    }
    std::function<bool(memcached_st *memcached, std::string key, int key_size, const char *value, int value_size)> send_to_datanode = [](memcached_st *memcached, std::string key, int key_size, const char *value, int value_size) mutable
    {
        if (value == NULL)
        {
            return false;
        }
        memcached_return_t ret = memcached_set(memcached, (const char *)key.data(), (size_t)key_size, value, (size_t)value_size, (time_t)0, (uint32_t)0);
        if (memcached_failed(ret))
        {
            std::cout << "memcached_set fail:" << ret << std::endl;
        }
        return true;
    };
    std::function<bool(memcached_st *memcached, std::string key, int key_size, char *value, CrossNetworkCore *network_core, bool if_cross)> get_from_datanode = [](memcached_st *memcached, std::string key, int key_size, char *value, CrossNetworkCore *network_core, bool if_cross) mutable
    {
        if (value == NULL)
        {
            std::cout << "get_from_datanode,value==NULL" << std::endl;
            return false;
        }
        memcached_return_t error;
        uint32_t flag;
        size_t value_size;
        char *value_ptr = memcached_get(memcached, (const char *)key.data(), key_size, &value_size, &flag, &error);
        memcpy(value, value_ptr, value_size);
        if (value_ptr == NULL)
        {
            std::cout << "memcached_get fail key:" << key << std::endl;
        }
        if (if_cross)
        {
            if (!cross_network_core(network_core, key, key_size, value_ptr, value_size))
            {
                return false;
            }
        }
        return true;
    };

    bool Proxy::init_one_memcached(memcached_st *memcached, std::string ip, int port)
    {
        memcached_return rc;

        memcached_server_st *servers;
        servers = memcached_server_list_append(NULL, ip.c_str(), port, &rc);
        rc = memcached_server_push(memcached, servers);
        memcached_server_free(servers);
        memcached_behavior_set(memcached, MEMCACHED_BEHAVIOR_DISTRIBUTION, MEMCACHED_DISTRIBUTION_CONSISTENT);
        memcached_behavior_set(memcached, MEMCACHED_BEHAVIOR_RETRY_TIMEOUT, 20);
        memcached_behavior_set(memcached, MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT, 5);
        memcached_behavior_set(memcached, MEMCACHED_BEHAVIOR_AUTO_EJECT_HOSTS, true);
        return true;
    }
    bool Proxy::SetParameter(ECSchema input_ecschema)
    {
        m_encode_parameter = input_ecschema;
        // std::cout << "m_encode_parameter.partial_decoding" << m_encode_parameter.partial_decoding << std::endl;
        // std::cout << "m_encode_parameter.encodetype" << m_encode_parameter.encodetype << std::endl;
        // std::cout << "m_encode_parameter.placementtype" << m_encode_parameter.placementtype << std::endl;
        // std::cout << "m_encode_parameter.n_block" << m_encode_parameter.n_block << std::endl;
        // std::cout << "m_encode_parameter.k_datablock" << m_encode_parameter.k_datablock << std::endl;
        // std::cout << "m_encode_parameter.r_datapergroup" << m_encode_parameter.r_datapergroup << std::endl;
        if (m_encode_parameter.encodetype == Xorbas)
        {
            m_encoder = std::make_shared<REPAIR::Xorbas_Class>();
        }
        else if (m_encode_parameter.encodetype == Optimal_LRC)
        {
            m_encoder = std::make_shared<REPAIR::Optimal_LRC_Class>();
        }
        else if (m_encode_parameter.encodetype == Azure_LRC_1)
        {
            m_encoder = std::make_shared<REPAIR::Azure_LRC_1_Class>();
        }
        else
        {
            m_encoder = std::make_shared<REPAIR::Azure_LRC_Class>();
        }
        m_encoder->set_parameter(m_encode_parameter.n_block, m_encode_parameter.k_datablock, m_encode_parameter.r_datapergroup);
        return true;
    }

    bool Proxy::init_cluster_meta()
    {

        // std::cout << "m_config_path:" << m_config_path << std::endl;
        tinyxml2::XMLDocument xml;
        xml.LoadFile(m_config_path.c_str());
        tinyxml2::XMLElement *root = xml.RootElement();
        int node_id = 0;
        memcached_st *memcached;
        memcached = memcached_create(NULL);
        init_one_memcached(memcached, networkcore_port_ip.first, networkcore_port_ip.second);
        memcached_list[-1] = memcached;
        m_networkcore.networkcore = memcached_list[-1];

        for (tinyxml2::XMLElement *cluster = root->FirstChildElement(); cluster != nullptr; cluster = cluster->NextSiblingElement())
        {
            std::string cluster_id(cluster->Attribute("id"));
            std::string proxy(cluster->Attribute("proxy"));
            // std::cout << "cluster_id: " << cluster_id << " , proxy: " << proxy << std::endl;
            m_Cluster_info[std::stoi(cluster_id)].Cluster_id = std::stoi(cluster_id);
            m_cluster_ids.push_back(std::stoi(cluster_id));
            auto pos = proxy.find(':');
            m_Cluster_info[std::stoi(cluster_id)].proxy_ip = proxy.substr(0, pos);
            m_Cluster_info[std::stoi(cluster_id)].proxy_port = std::stoi(proxy.substr(pos + 1, proxy.size()));
            for (tinyxml2::XMLElement *node = cluster->FirstChildElement()->FirstChildElement(); node != nullptr; node = node->NextSiblingElement())
            {
                std::string node_uri(node->Attribute("uri"));
                // std::cout << "____node: " << node_uri << std::endl;
                m_Cluster_info[std::stoi(cluster_id)].nodes.push_back(node_id);
                m_Node_info[node_id].Node_id = node_id;
                auto pos = node_uri.find(':');
                m_Node_info[node_id].Node_ip = node_uri.substr(0, pos);
                m_Node_info[node_id].Node_port = std::stoi(node_uri.substr(pos + 1, node_uri.size()));
                m_Node_info[node_id].Cluster_id = std::stoi(cluster_id);

                memcached_st *memcached;
                memcached = memcached_create(NULL);
                init_one_memcached(memcached, m_Node_info[node_id].Node_ip, m_Node_info[node_id].Node_port);
                memcached_list[node_id] = memcached;
                node_id++;
            }
        }

        // for (auto it : m_Cluster_info)
        // {
        //     std::cout << "it.first:" << it.first << " " << std::endl;
        //     std::cout << "cluster_id" << it.second.Cluster_id << std::endl;
        //     std::cout << "proxy_ip" << it.second.proxy_ip << std::endl;
        //     std::cout << "proxy_port" << it.second.proxy_port << std::endl;
        //     for (auto item : it.second.nodes)
        //     {
        //         std::cout << " nodes " << item;
        //     }
        //     std::cout << std::endl;
        // }
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

        std::vector<std::pair<std::string, int>>
            nodes_ip_and_port;
        std::vector<int> nodes_id;

        // Optimal_LRC_Class new_Optimal_LRC = Optimal_LRC_Class(n, k, r);
        Placement placement_plan = m_encoder->generate_placement(placement_type);

        std::vector<int> cluster_ids_dis(m_cluster_ids);
        std::random_shuffle(cluster_ids_dis.begin(), cluster_ids_dis.end(), MyRand());
        std::vector<int> all_node_ids;

        m_encoder->encode(data, coding, block_size);

        std::vector<std::thread> senders;
        int send_num = n;
        StripeItem stripe_this;
        stripe_this.value_size_bytes = value_size_bytes;
        stripe_this.block_size_bytes = block_size;

        for (int j = 0; j < n; j++)
        {

            int cluster_id = cluster_ids_dis[placement_plan[j] % cluster_ids_dis.size()];
            std::random_device rd;
            std::mt19937 gen(rd());
            std::uniform_int_distribution<int> urd(0, m_Cluster_info[cluster_id].nodes.size() - 1);
            int random_number = urd(gen);
            int node_id = m_Cluster_info[cluster_id].nodes[random_number];
            while (std::find(all_node_ids.begin(), all_node_ids.end(), cluster_id * 100 + node_id) != all_node_ids.end())
            {
                random_number = (random_number + 1) % m_Cluster_info[cluster_id].nodes.size();
                node_id = m_Cluster_info[cluster_id].nodes[random_number];
            }
            all_node_ids.push_back(cluster_id * 100 + node_id);

            std::string shard_id = key + std::to_string(j);

            //node_id = j;
            stripe_this.node_ids.push_back(node_id);
            // std::cout << "==============" << std::endl;
            // std::cout << "shard_id " << shard_id << ", node_id " << node_id << std::endl;
            if (j < k)
            {
                senders.push_back(std::thread(send_to_datanode, memcached_list[node_id], shard_id,
                                              shard_id.size(), (const char *)data[j], block_size));
            }
            else
            {
                senders.push_back(std::thread(send_to_datanode, memcached_list[node_id], shard_id,
                                              shard_id.size(), (const char *)coding[j - k], block_size));
            }
        }

        for (int j = 0; j < senders.size(); j++)
        {
            senders[j].join();
        }
        m_Stripe_info[key] = stripe_this;
        return true;
    }
    bool Proxy::Get(std::string key, std::string &value)
    {
        if (m_Stripe_info.end() == m_Stripe_info.find(key))
        {
            return false;
        }
        int n = m_encode_parameter.n_block;
        int k = m_encode_parameter.k_datablock;
        int r = m_encode_parameter.r_datapergroup;
        int value_size_bytes = m_Stripe_info.at(key).value_size_bytes;
        int block_size = m_Stripe_info.at(key).block_size_bytes;
        REPAIR::EncodeType encode_type = m_encode_parameter.encodetype;
        REPAIR::PlacementType placement_type = m_encode_parameter.placementtype;

        std::vector<std::thread> receiver;
        std::vector<char> data(block_size * k);
        int data_ptr = 0;
        for (int i = 0; i < k; i++)
        {
            std::string shard_id = key + std::to_string(i);

            int node_id = m_Stripe_info.at(key).node_ids[i];
            memcached_st *memcached = memcached_list[node_id];
            receiver.push_back(std::thread(get_from_datanode, memcached_list[node_id], shard_id,
                                           shard_id.size(), data.data() + block_size * i, &m_networkcore, false));
        }
        for (int j = 0; j < receiver.size(); j++)
        {
            receiver[j].join();
        }
        value = std::string(data.data(), value_size_bytes);
    }
    bool Proxy::RepairByKeyIndex(std::string key, int index)
    {
        // 寻找新节点

        StripeItem *key_meta_data = &m_Stripe_info.at(key);
        int block_size_bytes = key_meta_data->block_size_bytes;
        int nodeid_of_fail_block = key_meta_data->node_ids[index];
        int clusterid_of_fail_block = m_Node_info.at(nodeid_of_fail_block).Cluster_id;
        int old_cluster_id = m_Node_info[clusterid_of_fail_block].Cluster_id;
        int new_node_id = nodeid_of_fail_block;
        std::vector<int> cluster_list;
        cluster_list.push_back(old_cluster_id);
        for (int each_node_id : m_Cluster_info.at(clusterid_of_fail_block).nodes)
        {
            if (key_meta_data->node_ids.end() == std::find(key_meta_data->node_ids.begin(), key_meta_data->node_ids.end(), each_node_id))
            {
                new_node_id = each_node_id;
            }
        }
        std::vector<int> repair_request;
        m_encoder->return_repair_request(index, repair_request);
        std::vector<char *> v_data(repair_request.size());
        std::vector<char *> v_coding(1);
        char **data = (char **)v_data.data();
        char **coding = (char **)v_coding.data();
        std::vector<std::vector<char>> v_data_area(repair_request.size(), std::vector<char>(key_meta_data->block_size_bytes));
        std::vector<std::vector<char>> v_coding_area(1, std::vector<char>(key_meta_data->block_size_bytes));
        std::vector<std::thread> receiver;
        for (int i = 0; i < repair_request.size(); i++)
        {
            data[i] = v_data_area[i].data();
        }
        coding[0] = v_coding_area[0].data();

        for (int i = 0; i < repair_request.size(); i++)
        {
            int request_index = repair_request[i];
            std::string shard_id = key + std::to_string(request_index);

            int node_id = m_Stripe_info.at(key).node_ids[request_index];
            int cluster_id = m_Node_info[node_id].Cluster_id;
            bool cross_cluster = false;
            if (m_encode_parameter.encodetype != Flat)
            {
                if (std::find(cluster_list.begin(), cluster_list.end(), cluster_id) == cluster_list.end())
                {
                    cluster_list.push_back(cluster_id);
                    cross_cluster = true;
                }
            }
            else
            {
                cross_cluster = true;
            }

            // std::cout << "++++++++++repair++++++++++" << std::endl;
            // std::cout << "  shard_id:  " << shard_id
            //           << "  node_id " << node_id << std::endl;
            memcached_st *memcached = memcached_list[node_id];
            // cross_cluster = true;
            receiver.push_back(std::thread(get_from_datanode, memcached_list[node_id], shard_id,
                                           shard_id.size(), data[i], &m_networkcore, cross_cluster));
        }
        for (int i = 0; i < receiver.size(); i++)
        {
            receiver[i].join();
        }

        // 修复
        if (!m_encoder->decode_in_group_xor(repair_request.size(), data, coding, block_size_bytes))
        {
            std::cout << "single repair failed while decoding!!" << std::endl;
            return false;
        }
        // std::cout<<"coding[i]"<<std::endl;
        // for (int i = 0; i < block_size_bytes; i++)
        // {
        //     std::cout<<coding[0][i];
        // }
        // std::cout<<std::endl;
        std::string shard_id = key + std::to_string(index);
        std::thread th(send_to_datanode, memcached_list[new_node_id], shard_id,
                       shard_id.size(), (const char *)coding[0], block_size_bytes);
        th.join();

        // 放置修复的数据
        key_meta_data->node_ids[index] = new_node_id;
        return true;
    }
}