import sys

sys.path.append("draw_pic")
sys.path.append("/home/ms/Repair_optimal/prototype/cmake/build")
import Code_parameters
from parameter import PARAMETERS_OPT, NEW_AZURE_LRC_1, NEW_AZURE_LRC, ALL_LRC
from draw import draw_bars_diff_placement, draw_bars_diff_code
Placement_types = [
    Code_parameters.PlacementType.Flat,
    Code_parameters.PlacementType.Random,
    Code_parameters.PlacementType.Best_Placement
]
Code_types = {
    "Optimal_LRC":Code_parameters.EncodeType.Optimal_LRC,
    "Azure LRC":Code_parameters.EncodeType.Azure_LRC,
    "Azure+1 LRC":Code_parameters.EncodeType.Azure_LRC_1,
    "Xorbas":Code_parameters.EncodeType.Xorbas
}
def draw_diff_code_best_placement():
    placement_type = Code_parameters.PlacementType.Best_Placement
    x_labels = ALL_LRC
    y_NRC = []
    y_DRC = []
    for key in Code_types.keys():
        y_NRC.append([])
        y_DRC.append([])
    legends = list(Code_types.keys())+["DRC"]
    yticks = [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5]
    encoder = []
    for each_key in Code_types.keys():
        this_encoder = Code_parameters.CodePyInterface()
        this_encoder.CreateEncoder(Code_types[each_key])
        encoder.append(this_encoder)
    
    for each_nkr in ALL_LRC:
        print("=====Best_Placement====")
        n = int(each_nkr[0])
        k = int(each_nkr[1])
        r = int(each_nkr[2])        
        for i in range(len(encoder)):
            each_encoder = encoder[i]
            each_encoder.set_parameter(n, k, r, 8)
            DRC_NRC = each_encoder.return_DRC_NRC(placement_type, seed)
            print(DRC_NRC)
            if int(DRC_NRC[0])==-1:
                DRC_NRC = (None,None)
            y_DRC[i].append(DRC_NRC[0])
            y_NRC[i].append(DRC_NRC[1])
    draw_bars_diff_code(x_labels, y_NRC, y_DRC, legends, yticks)
if __name__ == '__main__':
    seed = 999
    draw_diff_code_best_placement()
