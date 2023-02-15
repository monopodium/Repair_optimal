import math

from utils import Code_Placement, cluster


class Azure_LRC_1(Code_Placement):
    def generate_stripe_information(self):
        group_ptr = 0
        self.stripe_information.append([])
        for i in range(self.k):
            if i == self.r * (group_ptr + 1):
                group_ptr += 1
                self.stripe_information.append([])
            block = self.index_to_str('D', i)
            self.stripe_information[group_ptr].append(block)
            self.block_to_groupnumber[block] = group_ptr
        group_ptr += 1
        self.stripe_information.append([])
        for i in range(self.g):
            block = self.index_to_str('G', i)
            self.stripe_information[group_ptr].append(block)
            self.block_to_groupnumber[block] = group_ptr
        for i in range(self.l):
            block = self.index_to_str('L', i)
            self.stripe_information[i].append(block)
            self.block_to_groupnumber[block] = i

    def generate_block_repair_request(self):
        for group in self.stripe_information:
            for item in group:
                repair_request = [i for i in group if not i == item]
                self.block_repair_request[item] = repair_request

    def return_group_number(self):
        pass

    def generate_best_placement(self):
        cluster_id = 0
        self.b = self.d - 1
        remain_tails = []
        for group in self.stripe_information:
            cur_group_len = len(group)
            if self.b >= cur_group_len:
                if len(self.best_placement['raw_information']) > 0:
                    last_cluster_blk_num = len(
                        self.best_placement['raw_information'][cluster_id - 1].return_all_blocks())
                    if self.b - last_cluster_blk_num >= cur_group_len:
                        for block in group:
                            self.best_placement['raw_information'][cluster_id - 1].add_new_block(block,
                                                                                                 self.block_to_groupnumber[
                                                                                                     block])
                            self.best_placement['block_map_clusternumber'][block] = cluster_id - 1
                    else:
                        new_cluster = cluster(cluster_id, self.b)
                        for block in group:
                            new_cluster.add_new_block(block, self.block_to_groupnumber[block])
                            self.best_placement['block_map_clusternumber'][block] = cluster_id
                        self.best_placement['raw_information'].append(new_cluster)
                        cluster_id += 1
                else:
                    new_cluster = cluster(cluster_id, self.b)
                    for block in group:
                        new_cluster.add_new_block(block, self.block_to_groupnumber[block])
                        self.best_placement['block_map_clusternumber'][block] = cluster_id
                    self.best_placement['raw_information'].append(new_cluster)
                    cluster_id += 1
            else:
                for block_id in range(0, len(group), self.b):
                    if block_id + self.b >= len(group):
                        remain_tails.append(group[block_id:])
                    else:
                        new_cluster = cluster(cluster_id, self.b)
                        for block in group[block_id:block_id + self.b]:
                            new_cluster.add_new_block(block, self.block_to_groupnumber[block])
                            self.best_placement['block_map_clusternumber'][block] = cluster_id
                        self.best_placement['raw_information'].append(new_cluster)
                        cluster_id += 1
        # for Azure-LRC+1, merging tail or not meets the same repair cost, but to meet the least clusters, we can try
        if len(remain_tails) > 0:
            for tail in remain_tails:
                cur_tail_len = len(tail)
                last_cluster_blk_num = len(self.best_placement['raw_information'][cluster_id - 1].return_all_blocks())
                # merge tails into the least clusters if possible, but do not split any tail
                if self.b - last_cluster_blk_num >= cur_tail_len:
                    for block in tail:
                        self.best_placement['raw_information'][cluster_id - 1].add_new_block(block,
                                                                                             self.block_to_groupnumber[
                                                                                                 block])
                        self.best_placement['block_map_clusternumber'][block] = cluster_id - 1
                else:
                    new_cluster = cluster(cluster_id, self.b)
                    for block in tail:
                        new_cluster.add_new_block(block, self.block_to_groupnumber[block])
                        self.best_placement['block_map_clusternumber'][block] = cluster_id
                    self.best_placement['raw_information'].append(new_cluster)
                    cluster_id += 1
        assert self.check_cluster_information(self.best_placement)

    def calculate_distance(self):
        self.d = self.g + 2
        return self.d

    def nkr_to_klgr(self, n, k, r):
        l = math.ceil(k / r) + 1
        g = n - k - l
        return k, l, g, r

    def klgr_to_nkr(self, k, l, g, r):
        n = k + l + g
        return n, k, r

    def check_parameter(self):
        
        if self.n > self.k + self.l:
            return True
        else:
            print('Azure_LRC_1:Parameters do not meet requirements!')
            return False
        #assert self.n > self.k + self.l, 'Parameters do not meet requirements!'


if __name__ == '__main__':
    azure_lrc_1 = Azure_LRC_1()
    n = 18
    k = 12
    r = 5
    k, l, g, r = azure_lrc_1.nkr_to_klgr(n, k, r)
    print('Azure-LRC(k,l,g,r)', k, l, g, r)
    print(azure_lrc_1.return_DRC_NRC(k, l, g, r, "flat", 10, True))
    print(azure_lrc_1.return_DRC_NRC(k, l, g, r, "random", 10, True))
    print(azure_lrc_1.return_DRC_NRC(k, l, g, r, "best", 10, True))