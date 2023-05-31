import matplotlib.pyplot as plt
import numpy as np

placement_option = ["Flat", "Random", "Best_Placement"]
parameter_option = [(7, 4, 2), (10, 6, 3), (12, 8, 4), (15, 10, 5), (16, 10, 5)]
data_size_option = [1, 4, 16, 256, 1024, 4096]
bindwith_option = [493355, 657806, 986710, 1973420, 9867100]
all_result = {}
default_data = {"placement": "Random", "parameter": (12, 8, 4), "data_size": 1024, "bindwith": 986710, "DRC": 1, "NRR": 1, "maxDRC": 1, "minDRC": 1, "maxNRR": 1, "minNRR": 1}


def draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3):
    fig, ax = plt.subplots(figsize=(1.7 * 2, 1.1 * 2), dpi=300, constrained_layout=True)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # 设置自变量的范围和个数
    index = np.array([1, 3, 5, 7, 9])  # np.arange(1,len(x)+1,0.7)
    print(index)
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

    plt.show()
    fig.savefig(name)


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

    plt.show()
    fig.savefig(name)


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
                print(bindwith)
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


def data_one_pic(x_axis, x_axis_type, y_axis_type, column_options):
    all_data = {}
    all_data_error = {}
    for column in column_options:
        y_array = []
        y_array_error = [[], []]
        for x in x_axis:
            placement = column
            parameter = default_data["parameter"]
            data_size = default_data["data_size"]
            bindwith = default_data["bindwith"]
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


def draw_DRC_diff_object_size():
    x = ["1KB", "4KB", "16KB", "256KB", "1MB", "4MB"]
    xlabel = 'Object Size'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_object_size_xorbas.pdf'
    yticks = [5000, 10000, 15000, 20000, 25000]
    y_all, _ = data_one_pic(data_size_option, "data_size", "DRC", placement_option)
    draw(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


def draw_NRR_diff_object_size():
    x = ["1KB", "4KB", "16KB", "256KB", "1MB", "4MB"]
    xlabel = 'Object Size'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = 'NRC_diff_object_size_xorbas.pdf'
    yticks = [0, 10, 20, 30, 40, 50]
    y_all, _ = data_one_pic(data_size_option, "data_size", "NRR", placement_option)
    draw(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


def draw_DRC_diff_parameter_1M():
    default_data["data_size"] = 1024
    x = ["(7, 4, 2)", "(10, 6, 3)", "(12, 8, 4)", "(15, 10, 5)", "(16,10,5)"]
    xlabel = 'Coding Parameter'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_Parameter_1MB_xorbas.pdf'
    yticks = [0, 2000, 4000, 6000, 8000, 10000, 12000]
    y_all, error_bar = data_one_pic(parameter_option, "parameter", "DRC", placement_option)
    draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])


def draw_NRR_diff_parameter_1M():
    default_data["data_size"] = 1024
    x = ["(7, 4, 2)", "(10, 6, 3)", "(12, 8, 4)", "(15, 10, 5)", "(16,10,5)"]
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = 'NRR_diff_Parameter_1MB_xorbas.pdf'
    yticks = [0, 20, 40, 60, 80, 100]
    y_all, error_bar = data_one_pic(parameter_option, "parameter", "NRR", placement_option)
    draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])


def draw_DRC_diff_parameter_4M():
    default_data["data_size"] = 4096
    x = ["(7, 4, 2)", "(10, 6, 3)", "(12, 8, 4)", "(15, 10, 5)", "(16,10,5)"]
    xlabel = 'Coding Parameter'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_Parameter_4MB_xorbas.pdf'
    yticks = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    y_all, error_bar = data_one_pic(parameter_option, "parameter", "DRC", placement_option)
    draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])


def draw_NRR_diff_parameter_4M():
    default_data["data_size"] = 4096
    x = ["(7, 4, 2)", "(10, 6, 3)", "(12, 8, 4)", "(15, 10, 5)", "(16,10,5)"]
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = 'NRR_diff_Parameter_4MB_xorbas.pdf'
    yticks = [0, 20, 40, 60, 80]
    y_all, error_bar = data_one_pic(parameter_option, "parameter", "NRR", placement_option)
    draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])


def draw_DRC_diff_bandwidth_4M():
    default_data["data_size"] = 4096
    x = ["0.5", "0.7", "1", "2", "10"]
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_bandwidth_4M_xorbas.pdf'
    yticks = [0, 10000, 20000, 30000, 40000]
    y_all, _ = data_one_pic(bindwith_option, "bindwith", "DRC", placement_option)
    draw(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


def draw_NRR_diff_bandwidth_4M():
    default_data["data_size"] = 4096
    x = ["0.5", "0.7", "1", "2", "10"]
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = 'NRR_diff_bandwidth_4M_xorbas.pdf'
    yticks = [0, 30, 60, 90, 120]
    y_all, _ = data_one_pic(bindwith_option, "bindwith", "NRR", placement_option)
    draw(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


if __name__ == '__main__':
    analysis_file('./result_azure_lrc.txt')
    # draw_DRC_diff_object_size()
    # draw_NRR_diff_object_size()

    # draw_DRC_diff_parameter_1M()
    # draw_NRR_diff_parameter_1M()
    # draw_DRC_diff_parameter_4M()
    # draw_NRR_diff_parameter_4M()

    draw_DRC_diff_bandwidth_4M()
    draw_NRR_diff_bandwidth_4M()