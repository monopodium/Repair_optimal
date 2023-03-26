import sys

sys.path.append("different_code")
sys.path.append("draw_pic")

from Azure_LRC import Azure_LRC
from Azure_LRC_1 import Azure_LRC_1
from draw import draw_bars_diff_code, draw_bars_diff_placement
from Optimal_LRC import Optimal_LRC
from parameter import (DIFF_CODE, PARAMETER_AZURE_LRC, PARAMETER_AZURE_LRC_1,
                       PARAMETER_XORBAS, PARAMETERS_OPT)
from Xorbas import Xorbas


def return_DRC_NRC(code_class, paramter_list, number_of_random):
    Flat_DRC = []
    Random_DRC = []
    Best_DRC = []
    Flat_NRC = []
    Random_NRC = []
    Best_NRC = []
    for each_parameter in paramter_list:
        n = each_parameter[0]
        k = each_parameter[1]
        r = each_parameter[2]
        k, l, g, r = code_class.nkr_to_klgr(n, k, r)
        DRC, NRC = code_class.return_DRC_NRC(k, l, g, r,
                                             "flat", 10, False)
        Flat_DRC.append(DRC)
        Flat_NRC.append(NRC)
        sum_DRC = 0
        sum_NRC = 0
        for i in range(number_of_random):
            DRC, NRC = code_class.return_DRC_NRC(k, l, g, r,  
                                                 "random", number_of_random, False)
            if DRC is None:
                break
            sum_DRC = sum_DRC + DRC
            sum_NRC = sum_NRC + NRC
        
        if DRC is None:
            Random_DRC.append(None)
            Random_NRC.append(None)
        else:
            Random_DRC.append(round(sum_DRC/number_of_random, 1))
            Random_NRC.append(round(sum_NRC/number_of_random, 1))

        DRC, NRC = code_class.return_DRC_NRC(k, l, g, r,
                                             "best", 10, False)
        Best_DRC.append(DRC)
        Best_NRC.append(NRC)

    return [Flat_DRC, Random_DRC, Best_DRC], [Flat_NRC, Random_NRC, Best_NRC]


# ["Opt-LRC NRC", "Azure NRC", "Azure+1 NRC", "Xorbas NRC", "DRC"]
def compare_diff_code(paramter_list):
    Opt_DRC = []
    Azure_DRC = []
    Azure_1_DRC = []
    Xorbas_DRC = []

    Opt_NRC = []
    Azure_NRC = []
    Azure_1_NRC = []
    Xorbas_NRC = []

    for item in paramter_list:
        n = item[0]
        k = item[1]
        r = item[2]
        optimal_lrc = Optimal_LRC()
        k, l, g, r = optimal_lrc.nkr_to_klgr(n, k, r)
        DRC, NRC = optimal_lrc.return_DRC_NRC(k, l, g, r,
                                              "best", 10, False)
        Opt_DRC.append(DRC)
        Opt_NRC.append(NRC)

        azure_lrc = Azure_LRC()
        k, l, g, r = azure_lrc.nkr_to_klgr(n, k, r)
        DRC, NRC = azure_lrc.return_DRC_NRC(k, l, g, r,
                                            "best", 10, False)
        Azure_DRC.append(DRC)
        Azure_NRC.append(NRC)

        azure_lrc_1 = Azure_LRC_1()
        k, l, g, r = azure_lrc_1.nkr_to_klgr(n, k, r)
        DRC, NRC = azure_lrc_1.return_DRC_NRC(k, l, g, r,
                                              "best", 10, False)

        Azure_1_DRC.append(DRC)
        Azure_1_NRC.append(NRC)

        xorbas = Xorbas()
        k, l, g, r = xorbas.nkr_to_klgr(n, k, r)
        DRC, NRC = xorbas.return_DRC_NRC(k, l, g, r,
                                         "best", 10, False)
        Xorbas_DRC.append(DRC)
        Xorbas_NRC.append(NRC)
    return [Opt_DRC, Azure_DRC, Azure_1_DRC, Xorbas_DRC],\
           [Opt_NRC, Azure_NRC, Azure_1_NRC, Xorbas_NRC]


def draw_Xorbas():
    y_DRC, y_NRC = return_DRC_NRC(Xorbas(), PARAMETER_XORBAS, 100)
    x_labels = []
    for item in PARAMETER_XORBAS:
        x_labels.append('(' + str(item[0]) + ',' + str(item[1]) + ','
                        + str(item[2]) + ')')
    legends = ["Flat NRC", "Random NRC", "R-Opt NRC", "DRC"]
    yticks = [2, 4, 6, 8, 10, 12]
    print(y_NRC)
    print(y_DRC)
    draw_bars_diff_placement(x_labels, y_NRC, y_DRC, legends, yticks,
                             colors=["#2878B5", "#9AC9DB", "#C82423", "#F8AC8C"],
                             tick_step=24, group_gap=4, bar_gap=0,
                             file_name="Xorbas.pdf")


def draw_Azure_LRC():
    y_DRC, y_NRC = return_DRC_NRC(Azure_LRC(), PARAMETER_AZURE_LRC, 100)
    x_labels = []
    for item in PARAMETER_AZURE_LRC:
        x_labels.append('(' + str(item[0]) + ',' + str(item[1]) + ','
                        + str(item[2]) + ')')
    legends = ["Flat NRC", "Random NRC", "R-Opt NRC", "DRC"]
    yticks = [2, 4, 6, 8, 10, 12]
    draw_bars_diff_placement(x_labels, y_NRC, y_DRC, legends, yticks,
                             colors=["#2878B5", "#9AC9DB", "#C82423", "#F8AC8C"],
                             tick_step=2, group_gap=0.4, bar_gap=0,
                             file_name="Xorbas.pdf")


def draw_Optimal_LRC():
    y_DRC, y_NRC = return_DRC_NRC(Optimal_LRC(), PARAMETERS_OPT, 100)
    x_labels = []
    for item in PARAMETERS_OPT:
        x_labels.append('(' + str(item[0]) + ',' + str(item[1]) + ','
                        + str(item[2]) + ')')
    legends = ["Flat NRC", "Random NRC", "R-Opt NRC", "DRC"]
    yticks = [2, 4, 6, 8, 10, 12]
    draw_bars_diff_placement(x_labels, y_NRC, y_DRC, legends, yticks,
                             colors=["#2878B5", "#9AC9DB", "#C82423", "#F8AC8C"],
                             tick_step=2, group_gap=0.4, bar_gap=0,
                             file_name="Xorbas.pdf")


def draw_Azure_LRC_1():
    y_DRC, y_NRC = return_DRC_NRC(Azure_LRC_1(), PARAMETER_AZURE_LRC_1, 100)
    x_labels = []
    for item in PARAMETER_AZURE_LRC_1:
        x_labels.append('(' + str(item[0]) + ',' + str(item[1]) + ','
                        + str(item[2]) + ')')
    legends = ["Flat NRC", "Random NRC", "R-Opt NRC", "DRC"]
    yticks = [2, 4, 6, 8, 10, 12]
    draw_bars_diff_placement(x_labels, y_NRC, y_DRC, legends, yticks,
                             colors=["#2878B5", "#9AC9DB", "#C82423", "#F8AC8C"],
                             tick_step=2, group_gap=0.4, bar_gap=0,
                             file_name="Xorbas.pdf")


def COMPARE_DIFF():
    x_labels = []
    for item in DIFF_CODE:
        x_labels.append('(' + str(item[0]) + ',' + str(item[1]) + ','
                        + str(item[2]) + ')')
    y_DRC, y_NRC = compare_diff_code(DIFF_CODE)
    yticks = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
    legends = ["Opt-LRC NRC", "Azure NRC", "Azure+1 NRC", "Xorbas NRC", "DRC"]
    draw_bars_diff_code(x_labels, y_NRC, y_DRC, legends, yticks,
                        colors=["#2878B5", "#9AC9DB", "#C82423", "#F8AC8C"],
                        tick_step=2, group_gap=0.4, bar_gap=0,
                        file_name="pic1.pdf")


if __name__ == '__main__':

    # draw_Xorbas()
    # draw_Azure_LRC()
    # draw_Optimal_LRC()
    # draw_Azure_LRC_1()
    COMPARE_DIFF()
    
    