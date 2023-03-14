
import os
# 目前的port/生成规则和之前的sh脚本一致
current_path = os.getcwd()
parent_path = os.path.dirname(current_path)
datanode_number_per_Cluster = 10
memcached_port_start = 8000
datanode_port_start = memcached_port_start
Clusterid_start = 0
networkcore = 12222
in_cluster_method = True
if_test = False
# 考虑到最后要到集群，而proxy的ip大概可能与它Cluster内的ip一致
# 所以这样写proxy_ip_lis
# proxy_ip_list = [
#     ["0.0.0.0", 50005],
#     ["0.0.0.0", 50015],
#     ["0.0.0.0", 50025],
#     ["0.0.0.0", 50035],
#     ["0.0.0.0", 50045],
#     ["0.0.0.0", 50055],
#     ["0.0.0.0", 50065],
#     ["0.0.0.0", 50075],
#     ["0.0.0.0", 50085],
#     ["0.0.0.0", 50095],
#     ["0.0.0.0", 50105],
#     ["0.0.0.0", 50115],
#     ["0.0.0.0", 50125],
#     ["0.0.0.0", 50135],
#     ["0.0.0.0", 50145],
#     ["0.0.0.0", 50155],
#     ["0.0.0.0", 50165],
#     ["0.0.0.0", 50175],
#     ["0.0.0.0", 50185],
#     ["0.0.0.0", 50195]
# ]

proxy_ip_list = [
    ["10.0.0.51", 50005],
    ["10.0.0.52", 50005],
    ["10.0.0.53", 50005],
    ["10.0.0.54", 50005],
    ["10.0.0.55", 50005],
    ["10.0.0.56", 50005],
    ["10.0.0.58", 50005],
]
proxy_num = len(proxy_ip_list)

# 目前期待的数据结构为Cluster_informtion = {Cluster_id:{“proxy”:0.0.0.0:50005,“datanode”:[[ip,port],...]},},酱紫的
# 另外生成一个数据结构为memcached_ip_port = {Cluster_id:[[ip,port],...]}
Cluster_informtion = {}
memcached_ip_port = {}


def generate_Cluster_info_dict():
    for i in range(proxy_num):
        new_Cluster = {}

        new_Cluster["proxy"] = proxy_ip_list[i][0]+":"+str(proxy_ip_list[i][1])
        datanode_list = []
        for j in range(datanode_number_per_Cluster):
            if in_cluster_method:
                port = datanode_port_start + j
            else:
                port = datanode_port_start + i*100 + j
            datanode_list.append(
                [proxy_ip_list[i][0], port])
        new_Cluster["datanode"] = datanode_list
        Cluster_informtion[i] = new_Cluster

    for i in range(proxy_num):
        memcached_list = []
        for j in range(datanode_number_per_Cluster):
            if in_cluster_method:
                port = memcached_port_start + j
            else:
                port = memcached_port_start + i*100 + j
            memcached_list.append(
                [proxy_ip_list[i][0], port])
        memcached_ip_port[i] = memcached_list


def generate_run_memcached_file():
    file_name = parent_path + "/prototype/run_memcached/run_memcached.sh"
    with open(file_name, 'w') as f:
        f.write("kill -9 $(pidof memcached)\n")
        f.write("\n")
        for Cluster_id in memcached_ip_port.keys():
            print("Cluster_id", Cluster_id)
            for each_datanode in memcached_ip_port[Cluster_id]:
                print(each_datanode)
                f.write("./memcached/bin/memcached -m 128 -p " +
                        str(each_datanode[1])+" --max-item-size=5242880 -vv -d\n")
            f.write("\n")
        f.write("./memcached/bin/memcached -m 128 -p " +
                str(networkcore)+" --max-item-size=5242880 -vv -d\n")
        f.write("\n")


def generate_run_proxy_datanode_file():
    file_name = parent_path + '/run_proxy_datanode.sh'
    with open(file_name, 'w') as f:
        f.write("kill -9 $(pidof run_datanode)\n")
        f.write("kill -9 $(pidof run_proxy)\n")
        f.write("\n")
        for Cluster_id in Cluster_informtion.keys():
            print("Cluster_id", Cluster_id)
            for each_datanode in Cluster_informtion[Cluster_id]["datanode"]:
                f.write("./prototype/cmake/build/run_datanode " +
                        str(each_datanode[0])+":"+str(each_datanode[1])+"\n")
            f.write("\n")
        for proxy_ip_port in proxy_ip_list:
            f.write("./prototype/cmake/build/run_proxy " +
                    str(proxy_ip_port[0])+":"+str(proxy_ip_port[1])+"\n")
        f.write("\n")


def generater_Cluster_information_xml():
    file_name = parent_path + '/prototype/config/ClusterInformation.xml'
    import xml.etree.ElementTree as ET
    root = ET.Element('Clusters')
    root.text = "\n\t"
    for Cluster_id in Cluster_informtion.keys():
        Cluster = ET.SubElement(root, 'Cluster', {'id': str(
            Cluster_id), 'proxy': Cluster_informtion[Cluster_id]["proxy"]})
        Cluster.text = "\n\t\t"
        datanodes = ET.SubElement(Cluster, 'datanodes')
        datanodes.text = "\n\t\t\t"
        for index, each_datanode in enumerate(Cluster_informtion[Cluster_id]["datanode"]):
            datanode = ET.SubElement(datanodes, 'datanode', {'uri': str(
                each_datanode[0])+":"+str(each_datanode[1])})
            # datanode.text = '\n\t\t\t'
            if index == len(Cluster_informtion[Cluster_id]["datanode"]) - 1:
                datanode.tail = '\n\t\t'
            else:
                datanode.tail = '\n\t\t\t'
        datanodes.tail = '\n\t'
        if Cluster_id == len(Cluster_informtion)-1:
            Cluster.tail = '\n'
        else:
            Cluster.tail = '\n\t'
    # root.tail = '\n'
    tree = ET.ElementTree(root)
    tree.write(file_name, encoding="utf-8", xml_declaration=True)

def generate_run_memcached_file_cluster():
    file_name = parent_path + "/prototype/run_memcached/cluster_run_memcached.sh"
    with open(file_name, 'w') as f:
        f.write("kill -9 $(pidof memcached)\n")
        f.write("\n")
        if not if_test:
            f.write("{\n")            
        # for Cluster_id in memcached_ip_port.keys():
        #     print("Cluster_id", Cluster_id)
        for each_datanode in memcached_ip_port[0]:
            print(each_datanode)
            f.write("./memcached/bin/memcached -m 128 -p " +
                    str(each_datanode[1])+" --max-item-size=5242880 -vv -d\n")
        if not if_test:
            f.write("} &> /dev/null")  
        f.write("\n")
        # f.write("./memcached/bin/memcached -m 128 -p " +
        #         str(networkcore)+" --max-item-size=5242880 -vv -d\n")
        # f.write("\n")

if __name__ == "__main__":
    generate_Cluster_info_dict()
    generate_run_memcached_file()
    generate_run_memcached_file_cluster()
    # generate_run_proxy_datanode_file()
    generater_Cluster_information_xml()
    # test_chat_gpt()
