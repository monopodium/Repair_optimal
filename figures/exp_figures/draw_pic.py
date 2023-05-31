import matplotlib.pyplot as plt
import numpy as np
import os
import sys

placement_option_default = ["Flat", "Random", "Best_Placement"]
parameter_option_default = [(7, 4, 2), (10, 6, 3), (12, 8, 4), (15, 10, 5), (16, 10, 5)]
data_size_option_default = [1, 4, 16, 256, 1024, 4096]
bindwith_option_default = [493355, 657806, 986710, 1973420, 9867100]


data_all_xorbas = {
    'placement_option' : placement_option_default,
    'parameter_option': parameter_option_default,
    'data_size_option':data_size_option_default,
    'bindwith_option':bindwith_option_default,
    "placement": "Random",
    "parameter": (12, 8, 4), 
    "data_size": 1024, 
    "bindwith": 986710, 
    "DRC": 1, 
    "NRR": 1, 
    "maxDRC": 1, 
    "minDRC": 1, 
    "maxNRR": 1, 
    "minNRR": 1
}

data_all_azure_lrc = {
    'placement_option' : placement_option_default,
    'parameter_option': [(12,6,3),(16,10,5),(16,12,6),(18,12,5),(24,15,5)],
    'data_size_option':data_size_option_default,
    'bindwith_option':bindwith_option_default,
    "placement": "Random",
    "parameter": (16,12,6), 
    "data_size": 1024, 
    "bindwith": 986710, 
    "DRC": 1, 
    "NRR": 1, 
    "maxDRC": 1, 
    "minDRC": 1, 
    "maxNRR": 1, 
    "minNRR": 1
}
data_all_azure_lrc_1 = {
    'placement_option' : placement_option_default,
    'parameter_option': [(12,6,3),(15,10,5),(17,12,6),(18,12,5),(24,15,5)],
    'data_size_option':data_size_option_default,
    'bindwith_option':bindwith_option_default,
    "placement": "Random",
    "parameter": (17,12,6), 
    "data_size": 1024, 
    "bindwith": 986710, 
    "DRC": 1, 
    "NRR": 1, 
    "maxDRC": 1, 
    "minDRC": 1, 
    "maxNRR": 1, 
    "minNRR": 1
}
data_all_optimal = {
    'placement_option' : placement_option_default,
    'parameter_option': parameter_option_default,
    'data_size_option':data_size_option_default,
    'bindwith_option':bindwith_option_default,
    "placement": "Random",
    "parameter": (12, 8, 4), 
    "data_size": 1024, 
    "bindwith": 986710, 
    "DRC": 1, 
    "NRR": 1, 
    "maxDRC": 1, 
    "minDRC": 1, 
    "maxNRR": 1, 
    "minNRR": 1
}

default_data = {
    "xorbas":data_all_xorbas,
    "azure_lrc":data_all_azure_lrc,
    "azure_lrc_1":data_all_azure_lrc_1,
    "optimal":data_all_optimal
}
all_result = {}

abs_path=os.path.abspath(r"..")+'/final_figure/exp_fig/'

def reduce_and_times(data_flat,data_random,data_best):
    print("compare with flat random")
    for index in range(len(data_flat)):
        print("reduce: ",'{:.1%}'.format((data_flat[index]-data_best[index])/data_flat[index]),
              "   ",'{:.1%}'.format((data_random[index]-data_best[index])/data_random[index]))
    for index in range(len(data_flat)):
        print("times: ",'{:.1f}'.format(data_best[index]/data_flat[index]),
              "   ",'{:.1f}'.format(data_best[index]/data_random[index])) 
    for index in range(len(data_flat)):
        print('{:.1f}\%'.format(100*(data_flat[index]-data_best[index])/data_flat[index]),"and"
              ,'{:.1f}\%'.format(100*(data_random[index]-data_best[index])/data_random[index]),end=', ')        
    print()
    for index in range(len(data_flat)):
        print('{:.1f}$\\times$'.format(data_best[index]/data_flat[index]),
              "and",'{:.1f}$\\times$'.format(data_best[index]/data_random[index]),end=', ')
    print()
def draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3):
    fig, ax = plt.subplots(figsize=(1.7 * 2, 1.1 * 2), dpi=300, constrained_layout=True)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # 设置自变量的范围和个数
    index = np.array([1, 3, 5, 7, 9])  # np.arange(1,len(x)+1,0.7)
   #print(index)
    bar_width = 1
    # 画图
    ax.set_xticks(index)
    # 009db2 - 024b51 - 0780cf
    #  #C82423   #FF8884  #2878B5
    error_attri = {"elinewidth": 1, "ecolor": "black", "capsize": 1.5}
    ax.bar(index - bar_width / 2, y1, bar_width / 2, label='Flat', yerr=yerr1, error_kw=error_attri, color="#C82423", edgecolor="black")
    ax.bar(index, y2, bar_width / 2, label='Random', yerr=yerr2, error_kw=error_attri, color="#FF8884", edgecolor="black")
    ax.bar(index + bar_width / 2, y3, bar_width / 2, label='R-Opt', yerr=yerr3, error_kw=error_attri, color="#2878B5", edgecolor="black")
    # 设置坐标轴
    # ax.set_xlim(0, 9.5)
    # ax.set_ylim(0, 1.4)
    ax.set_yticks(yticks)
    ax.set_xticklabels(x)
    ax.set_xlabel(xlabel, fontsize=10, labelpad=4)
    ax.set_ylabel(ylabel, fontsize=8, labelpad=4)
    # 设置刻度
    ax.tick_params(rotation=45, axis='x', labelsize=10, pad=1, which='major', width=1, length=1.5)
    ax.tick_params(axis='y', labelsize=10, pad=1, which='major', width=1, length=1.5)
    # 显示网格
    # ax.grid(True, linestyle='-.')
    # ax.yaxis.grid(True, linestyle='-.')
    # 添加图例
    # legend = ax.legend(loc='best', frameon=False, fontsize=9)
    ax.legend(loc='best', frameon=False, fontsize=9)

    #plt.show()
    fig.savefig(abs_path+name)


def draw(x, y1, y2, y3, xlabel, ylabel, yticks, name):
    fig, ax = plt.subplots(figsize=(1.7 * 2, 1.1 * 2), dpi=300, constrained_layout=True)
    # 设置自变量的范围和个数
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # 画图
    # 009db2 - 024b51 - 0780cf
    #  #C82423   #FF8884  #2878B5
    ax.plot(x, y1, label='Flat', linestyle=':', marker='s', markersize='6.4', markerfacecolor="none", color="#C82423", linewidth=2.5)
    ax.plot(x, y2, label='Random', linestyle='--', marker='o', markersize='6', markerfacecolor="none", color="#FF8884", linewidth=2.5)
    ax.plot(x, y3, label='R-Opt', linestyle='-', marker='^', markersize='6', markerfacecolor="none", color="#2878B5", linewidth=2.5)
    # 设置坐标轴
    # ax.set_xlim(0, 9.5)
    # ax.set_ylim(0, 1.4)
    ax.set_yticks(yticks)
    ax.set_xlabel(xlabel, fontsize=10, labelpad=4)
    ax.set_ylabel(ylabel, fontsize=9, labelpad=4)
    # 设置刻度
    ax.tick_params(axis='x', labelsize=10, rotation=45, pad=2, which='major', width=1, length=2)
    ax.tick_params(axis='y', labelsize=10, pad=2, which='major', width=1, length=2)
    # 显示网格
    # ax.grid(True, linestyle='-.')
    # ax.yaxis.grid(True, linestyle='-.')
    # 添加图例
    # legend = ax.legend(loc='best', frameon=False, fontsize=10)
    ax.legend(loc='best', frameon=False, fontsize=10)

    #plt.show()
    fig.savefig(abs_path+name)


def analysis_file(filename):
    import re
    bindwith = 986710
    placement = "Flat"
    data_size = 1
    DRC = 1
    NRR = 1
    parameter = (12, 8, 4)

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line0 = lines[i]
            line0 = line0.strip('\n')
            match_bindwith = re.match(r"ssh (\S+) sudo ./wondershaper/wondershaper -a (\w+) -d (\d+)", line0)
            match_run = re.match(r"\./prototype/cmake/build/client (\w+) (\w+) (\w+) (\d+) (\d+) (\d+) (\d+)", line0)
            if match_bindwith:
                bindwith = int(match_bindwith.group(3))
                #print(bindwith)
            if match_run:
                placement = match_run.group(3)
                n = int(match_run.group(4))
                k = int(match_run.group(5))
                r = int(match_run.group(6))
                data_size = match_run.group(7)
                parameter = (n, k, r)
                DRC = float(lines[i + 2].strip('\n').split(':')[-1])
                minDRC = float(lines[i + 3].strip('\n').split(':')[-1])
                maxDRC = float(lines[i + 4].strip('\n').split(':')[-1])
                NRR = float(lines[i + 5].strip('\n').split(':')[-1])
                minNRR = float(lines[i + 6].strip('\n').split(':')[-1])
                maxNRR = float(lines[i + 7].strip('\n').split(':')[-1])
                i = i + 8
                this_data = {"placement": placement, "parameter": (n, k, r), "data_size": data_size, "bindwith": bindwith, "DRC": DRC, "NRR": NRR, "maxDRC": maxDRC, "minDRC": minDRC, "maxNRR": maxNRR, "minNRR": minNRR}
                all_result[str(placement) + str(parameter) + str(data_size) + str(bindwith)] = this_data


def data_one_pic(x_axis, x_axis_type, y_axis_type, column_options,default_data_this):
    all_data = {}
    all_data_error = {}
    for column in column_options:
        y_array = []
        y_array_error = [[], []]
        for x in x_axis:
            placement = column
            parameter = default_data_this["parameter"]
            data_size = default_data_this["data_size"]
            bindwith = default_data_this["bindwith"]
            if x_axis_type == "parameter":
                parameter = x
            if x_axis_type == "data_size":
                data_size = x
            if x_axis_type == "bindwith":
                bindwith = x
            result_mean = all_result[str(placement) + str(parameter) + str(data_size) + str(bindwith)][y_axis_type]
            result_max = all_result[str(placement) + str(parameter) + str(data_size) + str(bindwith)]['max' + y_axis_type]
            result_min = all_result[str(placement) + str(parameter) + str(data_size) + str(bindwith)]['min' + y_axis_type]
            y_array.append(result_mean)
            y_array_error[0].append(result_max - result_mean)
            y_array_error[1].append(result_mean - result_min)
        all_data[column] = y_array
        all_data_error[column] = y_array_error
    return all_data, all_data_error


def draw_DRC_diff_object_size(code_type):
    x = ["1KB", "4KB", "16KB", "256KB", "1MB", "4MB"]
    xlabel = 'Object Size'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_object_size_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 5000, 10000, 15000, 20000, 25000],
        "azure_lrc":[0, 10000, 20000, 30000],
        "azure_lrc_1":[0, 10000, 20000, 30000],
        "optimal":[0, 5000, 10000, 15000, 20000, 25000]
    }
    yticks = yticks_all[code_type]
    y_all, _ = data_one_pic(default_data[code_type]['data_size_option'], "data_size", "DRC", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


def draw_NRR_diff_object_size(code_type):
    x = ["1KB", "4KB", "16KB", "256KB", "1MB", "4MB"]
    xlabel = 'Object Size'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = 'NRR_diff_object_size_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 10, 20, 30, 40, 50],
        "azure_lrc":[0, 10, 20, 30, 40],
        "azure_lrc_1":[0, 10, 20, 30, 40, 50],
        "optimal":[0, 10, 20, 30, 40, 50]
    }
    yticks = yticks_all[code_type]
    y_all, _ = data_one_pic(default_data[code_type]['data_size_option'], "data_size", "NRR", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


def draw_DRC_diff_parameter_1M(code_type):
    default_data[code_type]["data_size"] = 1024
    x = [str(item) for item in default_data[code_type]["parameter_option"]]
    xlabel = 'Coding Parameter'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_Parameter_1MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 2000, 4000, 6000, 8000, 10000, 12000],
        "azure_lrc":[0, 4000, 8000, 12000, 16000],
        "azure_lrc_1":[0, 4000, 8000, 12000, 16000],
        "optimal":[0, 2000, 4000, 6000, 8000, 10000, 12000]
    }
    yticks = yticks_all[code_type]
    y_all, error_bar = data_one_pic(default_data[code_type]['parameter_option'], "parameter", "DRC", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])


def draw_NRR_diff_parameter_1M(code_type):
    default_data[code_type]["data_size"] = 1024
    x = [str(item) for item in default_data[code_type]["parameter_option"]]
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = 'NRR_diff_Parameter_1MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 20, 40, 60, 80, 100],
        "azure_lrc":[0, 20, 40, 60, 80, 100],
        "azure_lrc_1":[0, 40, 80, 120],
        "optimal":[0, 20, 40, 60, 80, 100]
    }
    yticks = yticks_all[code_type]
    y_all, error_bar = data_one_pic(default_data[code_type]['parameter_option'], "parameter", "NRR", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])


def draw_DRC_diff_parameter_4M(code_type):
    default_data[code_type]["data_size"] = 4096
    x = [str(item) for item in default_data[code_type]["parameter_option"]]
    xlabel = 'Coding Parameter'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_Parameter_4MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000],
        "azure_lrc":[0, 15000, 30000, 45000],
        "azure_lrc_1":[0, 10000, 20000, 30000, 40000, 50000],
        "optimal":[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    }
    yticks = yticks_all[code_type]
    y_all, error_bar = data_one_pic(default_data[code_type]['parameter_option'], "parameter", "DRC", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])


def draw_NRR_diff_parameter_4M(code_type):
    default_data[code_type]["data_size"] = 4096
    x = [str(item) for item in default_data[code_type]["parameter_option"]]
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = 'NRR_diff_Parameter_4MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas": [0, 20, 40, 60, 80],
        "azure_lrc":[0, 40, 80, 120, 160],
        "azure_lrc_1":[0, 40, 80, 120, 160],
        "optimal":[0, 20, 40, 60, 80]
    }
    yticks = yticks_all[code_type]
    y_all, error_bar = data_one_pic(default_data[code_type]['parameter_option'], "parameter", "NRR", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])


def draw_DRC_diff_bandwidth_4M(code_type):
    default_data[code_type]["data_size"] = 4096
    x = ["0.5", "0.7", "1", "2", "10"]
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_bandwidth_4MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 10000, 20000, 30000, 40000],
        "azure_lrc":[0, 20000, 40000, 60000],
        "azure_lrc_1":[0, 20000, 40000, 60000],
        "optimal":[0, 10000, 20000, 30000, 40000]
    }
    yticks = yticks_all[code_type]
    y_all, _ = data_one_pic(default_data[code_type]['bindwith_option'], "bindwith", "DRC", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


def draw_NRR_diff_bandwidth_4M(code_type):
    default_data[code_type]["data_size"] = 4096
    x = ["0.5", "0.7", "1", "2", "10"]
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = 'NRR_diff_bandwidth_4MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 30, 60, 90, 120],
        "azure_lrc":[0, 20,40,60,80],
        "azure_lrc_1":[0, 30, 60, 90],
        "optimal":[0, 30, 60, 90, 120]
    }
    yticks = yticks_all[code_type]
    y_all, _ = data_one_pic(default_data[code_type]['bindwith_option'], "bindwith", "NRR", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


if __name__ == '__main__':
    # analysis_file('./result_xorbas.txt')
    # draw_DRC_diff_object_size("xorbas")
    # draw_NRR_diff_object_size("xorbas")

    # draw_DRC_diff_parameter_1M("xorbas")
    # draw_NRR_diff_parameter_1M("xorbas")
    # draw_DRC_diff_parameter_4M("xorbas")
    # draw_NRR_diff_parameter_4M("xorbas")

    # draw_DRC_diff_bandwidth_4M("xorbas")
    # draw_NRR_diff_bandwidth_4M("xorbas")
    
    analysis_file('./result_azure_lrc_copy.txt')
    draw_DRC_diff_object_size("azure_lrc")
    draw_NRR_diff_object_size("azure_lrc")

    draw_DRC_diff_parameter_1M("azure_lrc")
    draw_NRR_diff_parameter_1M("azure_lrc")
    draw_DRC_diff_parameter_4M("azure_lrc")
    draw_NRR_diff_parameter_4M("azure_lrc")

    draw_DRC_diff_bandwidth_4M("azure_lrc")
    draw_NRR_diff_bandwidth_4M("azure_lrc")
    
    # analysis_file('./result_azure_lrc_1.txt')
    # draw_DRC_diff_object_size("azure_lrc_1")
    # draw_NRR_diff_object_size("azure_lrc_1")

    # draw_DRC_diff_parameter_1M("azure_lrc_1")
    # draw_NRR_diff_parameter_1M("azure_lrc_1")
    # draw_DRC_diff_parameter_4M("azure_lrc_1")
    # draw_NRR_diff_parameter_4M("azure_lrc_1")

    # draw_DRC_diff_bandwidth_4M("azure_lrc_1")
    # draw_NRR_diff_bandwidth_4M("azure_lrc_1")