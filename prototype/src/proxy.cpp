#include<proxy.h>
namespace REPAIR
{
    bool Proxy::init_memcached()
    {
        /*这里原本是写死的datanode的ip和port，需要改成从.xml文件中读取*/
        memcached_return rc;
        memcached_server_st *servers;
        m_memcached = memcached_create(NULL);

        bool init = false;
        tinyxml2::XMLDocument xml;
        xml.LoadFile(config_path.c_str());
        tinyxml2::XMLElement *root = xml.RootElement();
        for (tinyxml2::XMLElement *az = root->FirstChildElement(); az != nullptr; az = az->NextSiblingElement())
        {
            for (tinyxml2::XMLElement *node = az->FirstChildElement()->FirstChildElement(); node != nullptr; node = node->NextSiblingElement())
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
    }
}