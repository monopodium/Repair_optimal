import math
import random

from parameter import PARAMETERS_OPT
from utils import Code_Placement, cluster


class Optimal_LRC(Code_Placement):
    '''
    
    '''
    def generate_stripe_information(self):
        group_ptr = 0
        self.stripe_information.append([])
        for i in range(self.g + self.k):
            if i == self.r*(group_ptr + 1):
                group_ptr = group_ptr + 1
                self.stripe_information.append([])
            if i < self.k:
                block = self.index_to_str('D', i)
            else:
                block = self.index_to_str('G', i - self.k)
            self.stripe_information[group_ptr].append(block)
            self.block_to_groupnumber[block] = group_ptr
        for i in range(self.l):
            block = self.index_to_str('L', i)
            self.stripe_information[i].append(block)
            self.block_to_groupnumber[block] = i
        # print(self.stripe_information)
        assert len(self.stripe_information) == self.l, "optimal_lrc, error"

        
    def generate_block_repair_request(self):
        for group in self.stripe_information:
            for item in group:
                repair_request = [i for i in group if not i == item]
                self.block_repair_request[item] = repair_request

    def generate_best_placement(self):
        new_cluster = cluster(len(self.best_placement["raw_information"]), self.d - 1)
        self.best_placement["raw_information"].append(new_cluster)
        for each_group in self.stripe_information:
            if len(each_group) <= self.d - 1:
                last_cluster = self.best_placement["raw_information"][-1]
                if last_cluster.remaind() < len(each_group):
                    self.best_placement["raw_information"].append(cluster(len(self.best_placement["raw_information"]), self.d - 1))
                last_cluster = self.best_placement["raw_information"][-1]
                for block in each_group:
                    last_cluster.add_new_block(block, self.block_to_groupnumber[block])
                    self.best_placement["block_map_clusternumber"][block] = last_cluster.return_id()
            else:
                for each_group in self.stripe_information:
                    for each_c in range(0, len(each_group), self.d - 1):
                        for block in each_group[each_c:each_c + self.d -1]:
                            last_cluster = self.best_placement["raw_information"][-1]
                            last_cluster.add_new_block(block, self.block_to_groupnumber[block])
                            self.best_placement["block_map_clusternumber"][block] = last_cluster.return_id()
                        self.best_placement["raw_information"].append(cluster(len(self.best_placement["raw_information"]), self.d - 1))

    def calculate_distance(self):
        gl = math.ceil(self.n/(self.r+1))-self.l

        if math.ceil((self.g+1)/self.r) > gl:
            self.d = self.g + gl + 2
        else:
            self.d = self.g + gl + 1
        return self.d

    def nkr_to_klgr(self, n, k, r):
        k = k
        l = math.ceil(n/(r+1))
        g = n - k - l
        return k, l, g, r

    def klgr_to_nkr(self, k, l, g, r):
        n = k + l + g
        return n, k, r

    def check_parameter(self):
        #print(self.n, self.l, self.k, self.g, self.r)
        print('Parameters do not meet requirements!')
        #assert self.n % (self.r+1) != 1, 'Parameters do not meet requirements!'
        if self.n % (self.r+1) == 1:
            return False
        return True


if __name__ == '__main__':
    #
    optimal_lrc = Optimal_LRC()
    for item in PARAMETERS_OPT:
        n = item[0]
        k = item[1]
        r = item[2]
        k, l , g, r = optimal_lrc.nkr_to_klgr(n, k, r)
        print("n, k ,r")
        print(n, k, r)
        print(optimal_lrc.return_DRC_NRC(k, l , g, r, "flat", 10, False))
        print(optimal_lrc.return_DRC_NRC(k, l , g, r, "random", 10, False))
        print(optimal_lrc.return_DRC_NRC(k, l , g, r, "best", 10, False))

