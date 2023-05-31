import matplotlib.pyplot as plt
import numpy as np

FIGSIZE_GLOBAL = (21,5)
Y_LABEL_FRONT_SIZE = 20
X_LABEL_FRONT_SIZE = 20
X_TICKS_FRONT_SIZE = 14
Y_TICKS_FRONT_SIZE = 14
SUBPLOTS_ADJUST_TOP = 0.95
SUBPLOTS_ADJUST_BOTTOM = 0.255
SUBPLOTS_ADJUST_RIGHT = 0.995
SUBPLOTS_ADJUST_LEFT = 0.04

def draw_bars_diff_placement_shared_x(y_labels,x_labels, Y_NRC_shared_x, Y_DRC_shared_x, legends, all_yticks,
                                        colors=["#2878B5", "#9AC9DB", "#C82423"],
                                        tick_step=2, group_gap=0.4, bar_gap=0,
                                        file_name="pic1.pdf"):
    number_subpic = len(y_labels)
    figure, ax_all = plt.subplots(number_subpic,1,figsize=(21,13),dpi=300,sharex=False)
    x_labels = [str(item) for item in x_labels]
    
    for index_i in range(number_subpic):
        ytick = all_yticks[index_i]
        ax = ax_all[index_i]
        y_NRC = Y_NRC_shared_x[index_i]
        y_DRC = Y_DRC_shared_x[index_i]
        ax_all[index_i]
            
        check_flag = True
        for i in range(len(y_NRC)-1):
            if len(y_NRC[i]) != len(y_NRC[i + 1]):
                check_flag = False
        if len(legends) - 1 != len(y_NRC):
            check_flag = False
        assert check_flag, "Check False"
        
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
            tmp_bar = ax.bar(x_index, y_new, bar_width, color=colors[index],
                            edgecolor="black", linewidth=1, zorder=0,label=legends[index])
            plt_list.append(tmp_bar)
            for a, b in zip(x_index, y):
                if b is not None:
                    ax.text(a, b + 0.05, np.round(b, decimals=1),
                            ha='center', va='bottom', fontsize=8)

        x_index = baseline_x - bar_span
        tmp_scatter = ax.scatter(x_index, y_DRC[0], s=80, marker='_', c='k', zorder=1,label=legends[-1])
        plt_list.append(tmp_scatter)
        x_index = baseline_x
        ax.scatter(x_index, y_DRC[1], s=80, marker='_', c='k', zorder=1)
        x_index = baseline_x + bar_span
        ax.scatter(x_index, y_DRC[2], s=80, marker='_', c='k', zorder=1)

        # ax.ylabel('Repair Cost (#Blocks)', fontsize=Y_LABEL_FRONT_SIZE)
        # ax.xlabel('Coding Parameter', fontsize=X_LABEL_FRONT_SIZE)
        # ax.gca()

        xlinm_position_left = xticks[0] - 4 * bar_width
        xlinm_position_right = xticks[-1] + 4 * bar_width
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xlim([xlinm_position_left, xlinm_position_right])
        ax.spines['left'].set_position(('data', xlinm_position_left))
        ax.spines['right'].set_position(('data', xlinm_position_right))

        #print(ytick)
        ax.tick_params(axis='x', labelsize= X_TICKS_FRONT_SIZE)
        ax.tick_params(axis='y', labelsize= Y_TICKS_FRONT_SIZE)
        ax.set_yticks(ytick)#, 
        #ax.set_yticks(fontsize=Y_TICKS_FRONT_SIZE)
        ax.set_xticks(xticks, x_labels, rotation=45, fontsize=X_TICKS_FRONT_SIZE)
        # ax.legend(handles=plt_list, labels=legends, loc='upper left', fontsize=14,
        #         frameon=False)
        #plt.show()
    lines, labels = ax_all[-1].get_legend_handles_labels()
    figure.legend(lines, labels, loc='upper center' , fontsize=24,frameon=False,ncol=4, labelspacing=0.5, columnspacing=1, handletextpad=0.5)
    #plt.xticks(xticks, x_labels, rotation=45, fontsize=X_TICKS_FRONT_SIZE)
    figure.subplots_adjust(hspace=0.1, top=SUBPLOTS_ADJUST_TOP, bottom=SUBPLOTS_ADJUST_BOTTOM, right=SUBPLOTS_ADJUST_RIGHT, left=SUBPLOTS_ADJUST_LEFT)
    plt.xlabel('Coding Parameter', fontsize=X_LABEL_FRONT_SIZE)
    figure.savefig(file_name,dpi=300, transparent=True)
    
    
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
    dpi_p = 300
    x_labels = [str(item) for item in x_labels]
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
    plt.figure(dpi=dpi_p,figsize=FIGSIZE_GLOBAL)
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
                plt.text(a, b + 0.05, np.round(b, decimals=1),
                         ha='center', va='bottom', fontsize=8)

    x_index = baseline_x - bar_span
    tmp_scatter = plt.scatter(x_index, y_DRC[0], s=80, marker='_', c='k', zorder=1)
    plt_list.append(tmp_scatter)
    x_index = baseline_x
    plt.scatter(x_index, y_DRC[1], s=80, marker='_', c='k', zorder=1)
    x_index = baseline_x + bar_span
    plt.scatter(x_index, y_DRC[2], s=80, marker='_', c='k', zorder=1)

    plt.ylabel('Repair Cost (#Blocks)', fontsize=Y_LABEL_FRONT_SIZE)
    plt.xlabel('Coding Parameter', fontsize=X_LABEL_FRONT_SIZE)
    ax = plt.gca()

    xlinm_position_left = xticks[0] - 4 * bar_width
    xlinm_position_right = xticks[-1] + 4 * bar_width
    plt.xlim([xlinm_position_left, xlinm_position_right])
    ax.spines['left'].set_position(('data', xlinm_position_left))
    ax.spines['right'].set_position(('data', xlinm_position_right))

    ax.set_yticks(yticks)
    plt.xticks(xticks, x_labels, fontsize=X_TICKS_FRONT_SIZE)
    plt.xticks(rotation=45, fontsize=X_TICKS_FRONT_SIZE)
    plt.yticks(fontsize=Y_TICKS_FRONT_SIZE)
    plt.legend(handles=plt_list, labels=legends, loc='upper left', fontsize=14,
               frameon=False)
    #plt.show()
    plt.subplots_adjust(top=SUBPLOTS_ADJUST_TOP, bottom=SUBPLOTS_ADJUST_BOTTOM, right=SUBPLOTS_ADJUST_RIGHT, left=SUBPLOTS_ADJUST_LEFT)
    plt.savefig(file_name,dpi=dpi_p)#, bbox_inches='tight'


def draw_bars_diff_code(x_labels, y_NRC, y_DRC, legends, yticks,
                        colors=["#2878B5", "#9AC9DB", "#C82423", "#F8AC8C"],
                        tick_step=1.4, group_gap=0.35, bar_gap=0,
                        file_name="pic1.pdf",y_label="Repair Cost (#Blocks)",x_label="Coding Parameter",legend_loc='upper right',text_size=8):
    xticks = np.arange(len(x_labels)) * tick_step + 1
    group_num = len(y_NRC)
    group_width = tick_step - group_gap
    bar_span = group_width / group_num
    dpi_p = 300
    bar_width = bar_span - bar_gap
    baseline_x = xticks
    
    plt.figure(dpi=dpi_p,figsize=FIGSIZE_GLOBAL) #dpi=1000,
    #plt.grid(axis='y',color = '#27202b', linestyle = '-.', linewidth = 0.5,alpha=0.5)
    #plt.plot(whatever)
    #plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt_list = []
    for index, y in enumerate(y_NRC):
        x_index = baseline_x + (index-1)*bar_span
        y_new = len(y)*[0]
        for i in range(len(y)):
            if y[i] is None:
                y_new[i] = 0
            else:
                y_new[i] = y[i]
        tmp_bar = plt.bar(x_index, y_new, bar_width, color=colors[index],
                          edgecolor="black", linewidth=1, zorder=0)
        plt_list.append(tmp_bar)
        for a, b in zip(x_index, y):
            if b is not None:
                plt.text(a, b+0.05, np.round(b, decimals=1), ha='center',
                         va='bottom', fontsize=text_size)
        tmp_scatter = plt.scatter(x_index, y_DRC[index], s=1.2*bar_span*dpi_p, marker='_',#"_"bar_span*dpi_p
                                  c='k', zorder=1,linewidth=3)##007d23
    plt_list.append(tmp_scatter)
    plt.ylabel(y_label, fontsize=Y_LABEL_FRONT_SIZE)
    plt.xlabel(x_label, fontsize=X_LABEL_FRONT_SIZE)
    ax = plt.gca()
    xlinm_position_left = xticks[0] - 4 * bar_width
    xlinm_position_right = xticks[-1] + 4 * bar_width
    plt.xlim([xlinm_position_left, xlinm_position_right])
    ax.spines['left'].set_position(('data', xlinm_position_left))
    ax.spines['right'].set_position(('data', xlinm_position_right))
    #ax.set_yticks(yticks, fontsize=14)
    plt.xticks(xticks + 0*bar_width, x_labels,rotation=45, fontsize=X_TICKS_FRONT_SIZE)
    #plt.xticks(rotation=45, fontsize=14)
    plt.yticks(yticks, fontsize=Y_TICKS_FRONT_SIZE)
    plt.legend(handles=plt_list, labels=legends, loc=legend_loc,#loc='best'
               fontsize=13, frameon=True,edgecolor="w",framealpha=1,facecolor="w")
    #plt.show()
    plt.subplots_adjust(top=SUBPLOTS_ADJUST_TOP, bottom=SUBPLOTS_ADJUST_BOTTOM, right=SUBPLOTS_ADJUST_RIGHT, left=SUBPLOTS_ADJUST_LEFT)#,hspace=0.1,wspace=0.1
    #plt.margins(0, 0)
    plt.savefig(file_name, dpi=dpi_p)#,dpi=300 , bbox_inches='tight'

