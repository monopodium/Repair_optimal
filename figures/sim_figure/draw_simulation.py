import sys

sys.path.append("draw_pic")
sys.path.append("/home/ms/Repair_optimal/prototype/cmake/build")
import Code_parameters
from parameter import PARAMETERS_OPT, NEW_AZURE_LRC_1, NEW_AZURE_LRC, ALL_LRC,PARAMETERS_Azure_LRC_1
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
PARAMETERS_DIFF ={
    "Optimal_LRC":PARAMETERS_OPT,
    "Azure LRC":PARAMETERS_OPT,
    "Azure+1 LRC":PARAMETERS_Azure_LRC_1,
    "Xorbas":PARAMETERS_OPT
}

file_name = {
    "Optimal_LRC":"Optimal_LRC_diff_place.pdf",
    "Azure LRC":"Azure_LRC_diff_place.pdf",
    "Azure+1 LRC":"Azure_1_LRC_diff_place.pdf",
    "Xorbas":"Xorbas_diff_place.pdf"
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
        #print("=====Best_Placement====")
        n = int(each_nkr[0])
        k = int(each_nkr[1])
        r = int(each_nkr[2])        
        for i in range(len(encoder)):
            each_encoder = encoder[i]
            each_encoder.set_parameter(n, k, r, 8)
            DRC_NRC = each_encoder.return_DRC_NRC(placement_type, seed)
            if int(DRC_NRC[0])==-1:
                DRC_NRC = (None,None)
            y_DRC[i].append(DRC_NRC[0])
            y_NRC[i].append(DRC_NRC[1])
    draw_bars_diff_code(x_labels, y_NRC, y_DRC, legends, yticks)

def draw_diff_placement():
    for code_type in Code_types.keys():
        x_labels = PARAMETERS_DIFF[code_type]
        this_encoder = Code_parameters.CodePyInterface()
        this_encoder.CreateEncoder(Code_types[code_type])
        legends = ["Flat NRC","Random NRC","R-Opt NRC","DRC"]
        y_NRC = []
        y_DRC = []
        for each_key in Placement_types:
            y_NRC.append([])
            y_DRC.append([])
        for each_nkr in PARAMETERS_DIFF[code_type]:
            n = int(each_nkr[0])
            k = int(each_nkr[1])
            r = int(each_nkr[2]) 
            this_encoder.set_parameter(n, k, r, 8)
            for i in range(len(Placement_types)):
                DRC_arg = 0
                NRC_arg = 0
                number = 100
                for j in range(number):
                    DRC_NRC = this_encoder.return_DRC_NRC(Placement_types[i], 993+j)
                    DRC_arg = DRC_arg + DRC_NRC[0]
                    NRC_arg = NRC_arg + DRC_NRC[1]
                if int(NRC_arg/number)==-1:
                    y_NRC[i].append(None)
                    y_DRC[i].append(None)
                else:
                    y_NRC[i].append(NRC_arg/number)
                    y_DRC[i].append(DRC_arg/number)
        yticks = [2,4,6,8,10,12,14]
        draw_bars_diff_placement(x_labels, y_NRC, y_DRC, legends, yticks,file_name=file_name[code_type])
if __name__ == '__main__':
    seed = 999
    #draw_diff_code_best_placement()
    draw_diff_placement()
