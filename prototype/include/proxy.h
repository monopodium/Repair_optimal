#ifndef PROXY_H
#define PROXY_H
#include "devcommon.h"
#include <libmemcached/memcached.h>

namespace REPAIR
{
    class Proxy
    {
    public:
        Proxy(std::string config_path) : config_path(config_path)
        {
            init_memcached();
        }
        ~Proxy() { memcached_free(m_memcached); };
    private:
        std::string config_path;
        bool init_memcached();
        memcached_st *m_memcached;
    };

}
#endif
