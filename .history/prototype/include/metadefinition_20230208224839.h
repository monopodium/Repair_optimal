#ifndef META_DEFINITION
#define META_DEFINITION
#include "devcommon.h"
namespace REPAIR
{
    template <typename T>
    inline T ceil(T const &A, T const &B)
    {
        return T((A + B - 1) / B);
    };
    enum EncodeType
    {
        Xorbas,
        Azure_LRC,
        Azure_LRC_1,
        Optimal_LRC
    };
    enum PlacementType
    {
        Random,
        Flat,
        Best_Placement
    };
    typedef struct ECSchema
    {
        ECSchema() = default;

        ECSchema(bool partial_decoding, EncodeType encodetype, PlacementType placementtype, int n_block,
                 int k_datablock, int r_datapergroup)
            : partial_decoding(partial_decoding), encodetype(encodetype), placementtype(placementtype),
              n_block(n_block), k_datablock(k_datablock),
              r_datapergroup(r_datapergroup) {}
        bool partial_decoding;
        EncodeType encodetype;
        PlacementType placementtype;
        int n_block;
        int k_datablock;
        int r_datapergroup;
    } ECSchema;
    typedef struct Clusteritem
    {
        unsigned int Cluster_id;
        std::string proxy_ip;
        int proxy_port;
        std::vector<unsigned int> nodes;
    } Clusteritem;
    typedef struct Nodeitem
    {
        unsigned int Node_id;
        std::string Node_ip;
        int Node_port;
        int Cluster_id;
    } Nodeitem;
    // namespace REPAIR
    // data globle local
    //[cluster id, cluster id]
    typedef std::vector<int> Placement;
    typedef struct{
        std::vector<int> node_ids;
        }
}
#endif