import matplotlib.pyplot as plt
import numpy as np


def draw_bars_diff_placement(x_labels, y_NRC, y_DRC, legends, yticks,
                             colors=["#2878B5", "#9AC9DB", "#C82423"],
                             tick_step=2, group_gap=0.4, bar_gap=0,
                             file_name="pic1.pdf"):
    '''
    yticks指的是y轴坐标的间隔
    yticks = [2,4,6,8,10,12]
    y_NRC的结构如下 = [[Flat_list]```````,[],[],[]]
    y_DRC的结构如下:[[],[],[],[]]
    legends的结构如下:[legend1, legend2, legend3]

    '''
    check_flag = True
    for i in range(len(y_NRC)-1):
        if len(y_NRC[i]) != len(y_NRC[i + 1]):
            check_flag = False

    if len(legends) - 1 != len(y_NRC):
        check_flag = False

    assert check_flag, "Check False"
    '''
    xticks为x轴刻度
    group_num为数据的组数,即每组柱子的柱子个数
    group_width为每组柱子的总宽度,group_gap 为柱子组与组之间的间隙
    bar_span为每组柱子之间在x轴上的距离,即柱子宽度和间隙的总和
    bar_width为每个柱子的实际宽度
    baseline_x为每组柱子第一个柱子的基准x轴位置,随后的柱子依次递增bar_span即可
    '''
    group_num = len(y_NRC)
    group_width = tick_step - group_gap
    bar_span = group_width / group_num
    bar_width = bar_span - bar_gap
    xticks = np.arange(len(x_labels)) * tick_step + bar_width
    baseline_x = xticks
    plt_list = []
    for index, y in enumerate(y_NRC):
        x_index = baseline_x + (index-1)*bar_span
        y_new = x_index * [0]
        for i in range(len(y)):
            if not y[i]:
                y_new[i] = 0
            else:
                y_new[i] = y[i]
        tmp_bar = plt.bar(x_index, y_new, bar_width, color=colors[index],
                          edgecolor="black", linewidth=1, zorder=0)
        plt_list.append(tmp_bar)
        for a, b in zip(x_index, y):
            if b is not None:
                plt.text(a + 0.3, b + 0.05, np.round(b, decimals=1),
                         ha='center', va='bottom', fontsize=10)

    x_index = baseline_x - bar_span
    tmp_scatter = plt.scatter(x_index, y_DRC[0], s=80, marker='_', c='k', zorder=1)
    plt_list.append(tmp_scatter)
    x_index = baseline_x
    plt.scatter(x_index, y_DRC[1], s=80, marker='_', c='k', zorder=1)
    x_index = baseline_x + bar_span
    plt.scatter(x_index, y_DRC[2], s=80, marker='_', c='k', zorder=1)

    plt.ylabel('Repair Cost (#Blocks)', fontsize=18)
    plt.xlabel('Coding Parameter', fontsize=18)
    ax = plt.gca()

    plt.xlim([xticks[0] - 2 * bar_width, xticks[-1] + 2 * bar_width])
    ax.spines['left'].set_position(('data', xticks[0] - 2 * bar_width))
    ax.spines['right'].set_position(('data', xticks[-1] + 2 * bar_width))

    ax.set_yticks(yticks)
    plt.xticks(xticks, x_labels, fontsize=14)
    plt.xticks(rotation=45, fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend(handles=plt_list, labels=legends, loc='best', fontsize=14,
               frameon=False)
    plt.show()
    plt.savefig(file_name)


def draw_bars_diff_code(x_labels, y_NRC, y_DRC, legends, yticks,
                        colors=["#2878B5", "#9AC9DB", "#C82423", "#F8AC8C"],
                        tick_step=2, group_gap=0.4, bar_gap=0,
                        file_name="pic1.pdf"):
    xticks = np.arange(len(x_labels)) * tick_step
    group_num = len(y_NRC)
    group_width = tick_step - group_gap
    bar_span = group_width / group_num
    bar_width = bar_span - bar_gap
    baseline_x = xticks

    plt_list = []
    for index, y in enumerate(y_NRC):
        x_index = baseline_x + (index-1)*bar_span
        y_new = len(y)*[0]
        for i in range(len(y)):
            if not y[i]:
                y_new[i] = 0
            else:
                y_new[i] = y[i]
        tmp_bar = plt.bar(x_index, y_new, bar_width, color=colors[index],
                          edgecolor="black", linewidth=1, zorder=0)
        plt_list.append(tmp_bar)
        for a, b in zip(x_index, y):
            if b is not None:
                plt.text(a, b+0.05, np.round(b, decimals=1), ha='center',
                         va='bottom', fontsize=8)

        tmp_scatter = plt.scatter(x_index, y_DRC[index], s=80, marker='_',
                                  c='k', zorder=1)

    plt_list.append(tmp_scatter)
    plt.ylabel('Repair Cost (#Blocks)', fontsize=18)
    plt.xlabel('Coding Parameter', fontsize=18)
    ax = plt.gca()
    plt.xlim([xticks[0] - 2 * bar_width, xticks[-1] + 2 * bar_width])
    ax.spines['left'].set_position(('data', xticks[0] - 2 * bar_width))
    ax.spines['right'].set_position(('data', xticks[-1] + 2 * bar_width))
    ax.set_yticks(yticks)

    plt.xticks(xticks, x_labels, fontsize=14)
    plt.xticks(rotation=45, fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend(handles=plt_list, labels=legends, loc='best',
               fontsize=11, frameon=False)
    plt.show()
    plt.savefig(file_name)

