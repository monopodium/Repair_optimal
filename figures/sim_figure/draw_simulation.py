import sys

sys.path.append("draw_pic")
sys.path.append("/home/ms/Repair_optimal/prototype/cmake/build")
import Code_parameters
from parameter import PARAMETERS_OPT,NEW_AZURE_LRC_1,NEW_AZURE_LRC,ALL_LRC


if __name__ == '__main__':
    #print(Code_parameters.PlacementType)
    encoder = Code_parameters.CodePyInterface()
    encoder.CreateEncoder(Code_parameters.EncodeType.Azure_LRC)
    seed = 999
    
    
    for each_nkr in ALL_LRC:
        print("=====Best_Placement====")
        
        placement_type = Code_parameters.PlacementType.Best_Placement
        n = int(each_nkr[0])
        k = int(each_nkr[1])
        r = int(each_nkr[2])

        encoder.set_parameter(n, k, r, 8)
        encoder.set_debug(True)
        seed = seed + 1
        pppp = encoder.generate_placement(placement_type, seed)
        print(n,k,r)
        print("d - 1:")
        print(encoder.calculate_distance() - 1)
        print(encoder.return_DRC_NRC(placement_type, seed))
        # for i in range(n):
        #     vec = []
        #     encoder.repair_request(i, vec)
        # encoder.print_placement_raw(placement_type)
    # for each_nkr in PARAMETERS_OPT:
    #     print("=====flat====")
    #     placement_type = Code_parameters.PlacementType.Flat
    #     n = int(each_nkr[0])
    #     k = int(each_nkr[1])
    #     r = int(each_nkr[2])
    #     print(n,k,r)
    #     encoder.set_parameter(16, 10, 5,8)
    #     encoder.set_debug(True)
    #     seed = seed + 1
    #     pppp = encoder.generate_placement(placement_type, seed)
    #     print(pppp)
    #     for i in range(n):
    #         vec = []
    #         encoder.repair_request(i, vec)
    #     encoder.print_placement_raw(placement_type)
    # for each_nkr in PARAMETERS_OPT:
    #     print("=====random====")
    #     placement_type = Code_parameters.PlacementType.Best_Placement
    #     n = int(each_nkr[0])
    #     k = int(each_nkr[1])
    #     r = int(each_nkr[2])
    #     print(n,k,r)
    #     encoder.set_parameter(16, 10, 5,8)
    #     encoder.set_debug(True)
    #     seed = seed + 1
    #     pppp = encoder.generate_placement(placement_type, seed)
    #     print(pppp)
    #     for i in range(n):
    #         vec = []
    #         encoder.repair_request(i, vec)
    #     encoder.print_placement_raw(placement_type)