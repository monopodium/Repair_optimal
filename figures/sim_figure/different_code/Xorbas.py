import math
import random

from .parameter import PARAMETER_XORBAS
from .utils import Code_Placement, cluster


class Xorbas(Code_Placement):
    '''
    
    '''
    def generate_stripe_information(self):
        group_ptr = 0
        self.stripe_information.append([])
        for i in range(self.k):
            if i == self.r * (group_ptr + 1):
                group_ptr = group_ptr + 1
                self.stripe_information.append([])
            block = self.index_to_str('D', i)
            self.stripe_information[group_ptr].append(block)
            self.block_to_groupnumber[block] = group_ptr
        self.stripe_information.append([])

        for i in range(self.g):
            block = self.index_to_str('G', i)
            self.stripe_information[-1].append(block)
            self.block_to_groupnumber[block] = 'g'

        for i in range(self.l):
            block = self.index_to_str('L', i)
            self.stripe_information[i].append(block)
            self.block_to_groupnumber[block] = i
        # print(self.stripe_information)
        assert len(self.stripe_information) == self.l + 1, "Xorbas, error"

    def generate_block_repair_request(self):
        for group in self.stripe_information[0:-1]:
            for item in group:
                repair_request = [i for i in group if not i == item]
                self.block_repair_request[item] = repair_request
        virtual_block = []
        for i in range(self.l):
            block = self.index_to_str('L', i)
            virtual_block.append(block)
        global_parity = self.stripe_information[-1]
        for item in global_parity:
            other_g = [i for i in global_parity if not i == item]
            repair_request = virtual_block + other_g
            self.block_repair_request[item] = repair_request

    def generate_best_placement(self):
        
        if self.d - 1 >= self.r:
            new_cluster = cluster(len(self.best_placement['raw_information']), self.d - 1)
            self.best_placement['raw_information'].append(new_cluster)
            for group in self.stripe_information[0:-1]:
                group = group[0:-1]
                last_cluster = self.best_placement['raw_information'][-1]
                if last_cluster.remaind() < len(group) - 1:
                    last_cluster = cluster(len(self.best_placement['raw_information']), self.d - 1)
                    self.best_placement['raw_information'].append(last_cluster)
                for item in group:
                    last_cluster.add_new_block(item, self.block_to_groupnumber[item])
                    self.best_placement['block_map_clusternumber'][item] = last_cluster.return_id()
        else:
            remain_list = []
            for group in self.stripe_information[0:-1]:
                group = group[0:-1]
                remain = len(group)
                while remain >= self.d - 1:
                    new_cluster = cluster(len(self.best_placement['raw_information']), self.d - 1)
                    self.best_placement['raw_information'].append(new_cluster)
                    for item in group[len(group)-remain:len(group) - remain + self.d - 1]:
                        new_cluster.add_new_block(item, self.block_to_groupnumber[item])
                        self.best_placement['block_map_clusternumber'][item] = new_cluster.return_id()
                    remain = remain - (self.d - 1)
                if remain > 0:
                    remain_list.append(group[-remain:])

            for remain in remain_list:
                last_cluster = self.best_placement['raw_information'][-1]
                if last_cluster.remaind() < len(remain):
                    last_cluster = cluster(len(self.best_placement['raw_information']), self.d - 1)
                    self.best_placement['raw_information'].append(last_cluster)
                for item in remain:
                    last_cluster.add_new_block(item, self.block_to_groupnumber[item])
                    self.best_placement['block_map_clusternumber'][item] = last_cluster.return_id()
        global_parity = self.stripe_information[-1]
        remain = len(global_parity)
        global_ptr = 0
        for each_cluster in self.best_placement['raw_information']:
            while not each_cluster.isfull():
                block = global_parity[global_ptr]
                each_cluster.add_new_block(block, self.block_to_groupnumber[block])
                self.best_placement['block_map_clusternumber'][block] = each_cluster.return_id()
                global_ptr = global_ptr + 1
                if global_ptr == remain:
                    break
            if global_ptr == remain:
                break

        if global_ptr < remain:
            new_cluster = cluster(len(self.best_placement['raw_information']), self.d - 1)
            self.best_placement['raw_information'].append(new_cluster)
            for item in global_parity[global_ptr:]:
                new_cluster.add_new_block(item, self.block_to_groupnumber[item])
                self.best_placement['block_map_clusternumber'][item] = new_cluster.return_id()

        for group in self.stripe_information[:-1]:
            last2 = group[-2]
            last1 = group[-1]
            cluster_number = self.best_placement['block_map_clusternumber'][last2]
            self.best_placement['raw_information'][cluster_number].add_new_block(last1, self.block_to_groupnumber[last1])
            self.best_placement['block_map_clusternumber'][last1] = cluster_number

    def calculate_distance(self):
        self.d = self.g + 1
        return self.d

    def nkr_to_klgr(self, n, k, r):
        k = k
        l = math.ceil(k/r)
        g = n - k - l
        return k, l, g, r

    def klgr_to_nkr(self, k, l, g, r):
        n = k + l + g
        return n, k, r

    def check_parameter(self):
        #print(self.n, self.l, self.k, self.g, self.r)
        if not (self.n, self.k, self.r) in PARAMETER_XORBAS:
            return False
        return True
        #assert self.n % (self.r+1) != 1, 'Parameters do not meet requirements!'


if __name__ == '__main__':
    #
    optimal_lrc = Xorbas()
    for item in PARAMETER_XORBAS:
        param_n = item[0]
        param_k = item[1]
        param_r = item[2]
        param_k, param_l, param_g, param_r = optimal_lrc.nkr_to_klgr(n, k, r)
        print("n, k ,r")
        print(n, k, r)
        print(optimal_lrc.return_DRC_NRC(param_k, param_l, param_g, param_r, "flat", 10, False))
        print(optimal_lrc.return_DRC_NRC(param_k, param_l, param_g, param_r, "random", 10, False))
        print(optimal_lrc.return_DRC_NRC(param_k, param_l, param_g, param_r, "best", 10, False))


