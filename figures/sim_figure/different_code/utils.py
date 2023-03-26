import random


class cluster(object):
    def __init__(self, cluster_id, upperbound):
        self.__upperbound = upperbound
        self.__cluster_id = cluster_id
        self.__blocks = []
        self.__from_groups = set()

    def return_id(self):
        return self.__cluster_id

    def set_upperbound(self, upperbound):
        self.__upperbound = upperbound

    def is_from_new_group(self, group_number):
        if group_number not in self.__from_groups:
            return True
        else:
            return False

    def isfull(self):
        if len(self.__blocks) < self.__upperbound:
            return False
        return True

    def add_new_block(self, new_block, group_number):
        if len(self.__blocks) < self.__upperbound:
            self.__blocks.append(new_block)
            if group_number is not None:
                self.__from_groups.add(group_number)
            return True
        return False

    def remaind(self):
        return self.__upperbound - len(self.__blocks)

    def return_all_blocks(self):
        return self.__blocks

    def return_upper(self):
        return self.__upperbound


class Code_Placement(object):

    '''
    类型有三：数据块，局部校验块，全局校验块
    [[data_block1,data_block2...][],[global_parity1,global_parity1..]]
    数据块映射到组别
    {"data_block":{"group:number":,"repair_request":}}
    '''
    def __init__(self):
        self.init()

    def init(self):
        self.raw_stripe = []
        self.stripe_information = []
        self.block_repair_request = {}
        self.random_placement = {"raw_information": [],
                                 "block_map_clusternumber": {}}
        self.flat_placement = {"raw_information": [],
                               "block_map_clusternumber": {}}
        self.best_placement = {"raw_information": [],
                               "block_map_clusternumber": {}}
        self.block_repair_cost = {}
        self.block_to_groupnumber = {}

    def set_debug(self, if_debug):
        self.if_debug = if_debug

    def print_information(self):
        if self.if_debug:
            print("-------------debug_information-------------")
            print("n k r")
            print(self.n, self.k, self.r)
            print("self.raw_stripe")
            print(self.raw_stripe)
            print("self.stripe_information")
            print(self.stripe_information)
            print("block_repair_request")
            print(self.block_repair_request)
            print("cluster_information")
            if len(self.random_placement["raw_information"]) > 0:
                for cluster in self.random_placement["raw_information"]:
                    print(cluster.return_all_blocks())
                print("block_map_clusternumber")
                print(self.random_placement["block_map_clusternumber"])
            if len(self.flat_placement["raw_information"]) > 0:
                for cluster in self.flat_placement["raw_information"]:
                    print(cluster.return_all_blocks())
                print("block_map_clusternumber")
                print(self.flat_placement["block_map_clusternumber"])
            if len(self.best_placement["raw_information"]) > 0:
                for cluster in self.best_placement["raw_information"]:
                    print(cluster.return_all_blocks())
                print("block_map_clusternumber")
                print(self.best_placement["block_map_clusternumber"])
            print("block_repair_cost")
            print(self.block_repair_cost)
            
            print("-------------END_information-------------")

    def set_parameter(self, k_data_blocks: int, l_parity_blocks: int,
                      g_global_blocks: int, r_data_blocks_each_group: int):
        self.k = k_data_blocks
        self.l = l_parity_blocks
        self.g = g_global_blocks
        self.r = r_data_blocks_each_group
        self.n = self.k + self.l + self.g

    def return_DRC_NRC(self, k_data_blocks: int, l_parity_blocks: int,
                       g_global_blocks: int, r_data_blocks_each_group: int,
                       placement_type: str, random_seed=10, if_debug=False):
        
        '''
        通过继承的方式来写不同编码, 父类为Code_Placement
        以 n = 12, k = 6, r = 3的Optimal-LRC为例,简述各个函数和数据结构的作用

        self.init():
        初始化各种数据结构

        self.set_debug():
        如果是debug = True,则会输出各种数据结构的信息

        self.set_parameter():
        设置类的参数self.k(数据块的数量),self.l(局部组的数量),self.g(全局校验块的数量)
        self.r(每个组的块的数量，其中不包括局部校验块)

        self.check_parameter():
        检查不同编码的参数合法性,参数要满足一定的规则,不同的编码规则不同,需要重写
        可以利用断言,例如Optimal-LRC的合法性检查 assert self.n % (self.r+1) != 1, 'Parameters do not meet requirements!'

        self.calculate_distance():
        计算最小距离self.d,不同编码计算方式不同，需要重写

        self.generate_raw_information():
        通过参数生成数据块和校验块,保存在self.raw_stripe中,以n = 12, k = 6, r = 3的Optimal-LRC为例
        ['D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'L0', 'L1', 'L2', 'G0', 'G1', 'G2']
        也即:k个数据块,编号为0到(k-1),L个数据块,编号为0到(l-1)...
        所有编码方式是一样的，不需要重写

        self.generate_stripe_information():
        需要重写,生成保存了组信息的self.stripe_information:
        [['D0', 'D1', 'D2', 'L0'], ['D3', 'D4', 'D5', 'L1'], ['G0', 'G1', 'G2', 'L2']]
        对于全局校验块没有局部组的情况,可以自行定义,
        因为任何操作self.stripe_information的函数都要重写

        self.generate_block_repair_request():
        需要重写,以字典的形式保存了每单个数据块修复需要的幸存块
        例如：
        {'D0': ['D1', 'D2', 'L0'], 'D1': ['D0', 'D2', 'L0'], 
        'D2': ['D0', 'D1', 'L0'], 'L0': ['D0', 'D1', 'D2'], 
        'D3': ['D4', 'D5', 'L1'], 'D4': ['D3', 'D5', 'L1'], 
        'D5': ['D3', 'D4', 'L1'], 'L1': ['D3', 'D4', 'D5'], 
        'G0': ['G1', 'G2', 'L2'], 'G1': ['G0', 'G2', 'L2'], 
        'G2': ['G0', 'G1', 'L2'], 'L2': ['G0', 'G1', 'G2']}

        self.generate_random_placement(random_seed)
        无需重写
        随机生成放置,每个cluster里面的块数量不超过self.d - 1
        存在数据结构self.random_placement中:
        self.random_placement = {"raw_information": [],
                                 "block_map_clusternumber": {}}
        其中self.random_placement["raw_information"][i]是id为i的cluster
        为一个cluster对象的实例。
        "block_map_clusternumber"将存储的是块对应的集群id,例如对于如下的随机放置：
        
        集群0:['L0']
        集群1:['G1', 'D0', 'D4', 'G2']
        集群2:['G0', 'D3', 'D2', 'D1']
        集群3:['L1', 'D5', 'L2']
        block_map_clusternumber
        {'L0': 0, 'G1': 1, 'D0': 1, 'D4': 1, 'G2': 1,
        'G0': 2, 'D3': 2, 'D2': 2, 'D1': 2, 'L1': 3, 'D5': 3, 'L2': 3}
        
        self.generate_repair_cost(self.random_placement):
        生成每个块的修复代价,无需重写
        self.block_repair_cost {块:代价}
        {'D0': 2, 'D1': 2, 'D2': 2, 'D3': 2, 'D4': 2, 'D5': 2,
        'L0': 2, 'L1': 2, 'L2': 2, 'G0': 2, 'G1': 2, 'G2': 2}

        self.return_DRC(), self.return_NRC()
        根据self.block_repair_cost和公式计算DRC和NRC,无需重写
        '''
        self.init()
        self.set_debug(if_debug)
        self.set_parameter(k_data_blocks, l_parity_blocks, g_global_blocks,
                           r_data_blocks_each_group)

        if not self.check_parameter():
            return None, None

        self.calculate_distance()
        self.generate_raw_information()
        self.generate_stripe_information()
        self.generate_block_repair_request()

        if placement_type == "random":
            self.generate_random_placement(random_seed)
            self.generate_repair_cost(self.random_placement)
        if placement_type == "flat":
            self.generate_flat_placement()
            self.generate_repair_cost(self.flat_placement)
        if placement_type == "best":
            self.generate_best_placement()
            self.generate_repair_cost(self.best_placement)
        self.print_information()
        return round(self.return_DRC(), 1), round(self.return_NRC(), 1)
        #return self.return_DRC(), 1), round(self.return_NRC(), 1)

    def return_NRC(self):
        cost_sum = 0
        for i in range(self.n):
            block = self.raw_stripe[i]
            cost_sum = cost_sum + self.block_repair_cost[block]
        return cost_sum/self.k

    def return_DRC(self):
        cost_sum = 0
        for i in range(self.k):
            block = self.index_to_str('D', i)
            cost_sum = cost_sum + self.block_repair_cost[block]
        return cost_sum/self.k

    def generate_repair_cost(self, placement):
        for item in self.raw_stripe:
            repair_set = set()
            repair_set.add(placement["block_map_clusternumber"][item])
            for block in self.block_repair_request[item]:
                cluster_number = placement["block_map_clusternumber"][block]
                repair_set.add(cluster_number)
            print(repair_set)
            self.block_repair_cost[item] = len(repair_set) - 1

    def str_to_index(self):
        pass

    def index_to_str(self, block_type: str, index: int):
        return block_type + str(index)

    def generate_raw_information(self):
        for i in range(self.k):
            self.raw_stripe.append(self.index_to_str('D', i))
        for i in range(self.l):
            self.raw_stripe.append(self.index_to_str('L', i))
        for i in range(self.g):
            self.raw_stripe.append(self.index_to_str('G', i))

    def generate_stripe_information(self):
        pass

    def generate_block_repair_request(self):
        pass

    def return_group_number(self):
        pass

    def generate_random_placement(self, random_seed=10):
        random.seed(random_seed)
        count = 0
        raw_stripe = self.raw_stripe.copy()
        for i in range(self.n):
            blocks_in_cluster = random.randint(1, self.d - 1)
            cluster_id = len(self.random_placement['raw_information'])
            new_cluster = cluster(cluster_id, self.d)
            if (count + blocks_in_cluster) > self.n:
                blocks_in_cluster = self.n - count
            #print(self.d-1, new_cluster.return_all_blocks())
            for j in range(blocks_in_cluster):
                #print(new_cluster.return_id(), new_cluster.return_all_blocks())
                assert not new_cluster.isfull(), "new_cluster.isfull()"
                selected_block = random.choice(raw_stripe)
                group_number = self.block_to_groupnumber[selected_block]
                new_cluster.add_new_block(selected_block,
                                                    group_number)
                cluster_id = len(self.random_placement['raw_information'])
                self.random_placement['block_map_clusternumber'][
                    selected_block] = cluster_id
                raw_stripe.remove(selected_block)
            count = count + blocks_in_cluster
            self.random_placement['raw_information'].append(new_cluster)
            if count == self.n:
                break

        assert self.check_cluster_information(self.random_placement)

    def check_cluster_information(self, cluster_information):
        #print("check_cluster_information")
        blocks_in_cluster = []
        for block in self.raw_stripe:
            cluster_id = cluster_information['block_map_clusternumber'][block]
            this_cluster = cluster_information['raw_information'][cluster_id]
            block_list = this_cluster.return_all_blocks()
            #print(block_list)
            if block not in block_list:
                return False
        for cluster in cluster_information['raw_information']:
            blocks_in_cluster = blocks_in_cluster + cluster.return_all_blocks()
        #print(blocks_in_cluster)
        if not len(blocks_in_cluster) == self.n:
            return False
        if not set(blocks_in_cluster) == set(self.raw_stripe):
            return False
        return True

    def generate_flat_placement(self):
        for block_id in range(self.n):
            block = self.raw_stripe[block_id]
            cluster_id = block_id
            new_cluster = cluster(cluster_id, self.d-1)
            group_number = self.block_to_groupnumber[block]
            new_cluster.add_new_block(block, group_number)
            self.flat_placement["raw_information"].append(new_cluster)
            self.flat_placement["block_map_clusternumber"][block] = block_id
            # print(new_cluster.return_all_blocks())
            # print(new_cluster.return_id())
        # print(self.flat_placement["raw_information"])
        # print("self.print_information()")

        assert self.check_cluster_information(self.flat_placement)

    def generate_best_placement(self):
        pass

    def calculate_distance(self):
        pass

    def nkr_to_klgr(self, n, k, r):
        pass

    def klgr_to_nkr(self, k, l, g, r):
        pass

    def check_parameter(self):
        pass


if __name__ == '__main__':
    pass
