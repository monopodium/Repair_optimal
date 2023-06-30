import matplotlib.pyplot as plt
import numpy as np

Y_LABEL_FRONT_SIZE = 10
X_LABEL_FRONT_SIZE = 10
X_TICKS_FRONT_SIZE = 10
Y_TICKS_FRONT_SIZE = 10
LEGEND_FONT_SIZE=10

X_LABEL_PAD=2
Y_LABEL_PAD=3
SUBPLOTS_ADJUST_TOP = 0.95
SUBPLOTS_ADJUST_BOTTOM = 0.4
SUBPLOTS_ADJUST_RIGHT = 0.97
SUBPLOTS_ADJUST_LEFT = 0.2

def draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3,column=0,y4 = None,yerr4= None,legend_type=0):
    SUBPLOTS_ADJUST_TOP = 0.95
    SUBPLOTS_ADJUST_BOTTOM = 0.38
    SUBPLOTS_ADJUST_RIGHT = 0.97
    SUBPLOTS_ADJUST_LEFT = 0.15
    if yerr1:
        yerr1 = np.absolute(yerr1)
    if yerr2:
        yerr2 = np.absolute(yerr2)
    if yerr3:
        yerr3 = np.absolute(yerr3)
    fig, ax = plt.subplots(figsize=(1.7 * 2, 1.1 * 2), dpi=300)#, constrained_layout=True)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # 设置自变量的范围和个数
    #index = np.array([1, 3, 5, 7, 9])  # np.arange(1,len(x)+1,0.7)
    index = np.arange(1,len(x)*2,2)
   #print(index)
    bar_width = 1
    # 画图
    ax.set_xticks(index)
    # 009db2 - 024b51 - 0780cf
    #  #C82423   #FF8884  #2878B5
    error_attri = {"elinewidth": 1, "ecolor": "black", "capsize": 1.5}
    if column==2:
        ax.bar(index - bar_width / 3, y3, bar_width *2/ 3 , label='R-Opt', yerr=yerr3, error_kw=error_attri, color="#2878B5", edgecolor="black")
        ax.bar(index + bar_width / 3, y4, bar_width *2/ 3, label='Sub-Opt', yerr=yerr4, error_kw=error_attri, color="#C7F1F7", edgecolor="black")

    elif y4==None:
        ax.bar(index - bar_width / 2, y1, bar_width / 2, label='Flat', yerr=yerr1, error_kw=error_attri, color="#C82423", edgecolor="black")
        ax.bar(index, y2, bar_width / 2, label='Random', yerr=yerr2, error_kw=error_attri, color="#FF8884", edgecolor="black")
        ax.bar(index + bar_width / 2, y3, bar_width / 2, label='R-Opt', yerr=yerr3, error_kw=error_attri, color="#2878B5", edgecolor="black")
    else:
        bar_width = 1.3
        ax.bar(index - bar_width / 2, y1, bar_width / 3, label='Flat', yerr=yerr1, error_kw=error_attri, color="#C82423", edgecolor="black")
        ax.bar(index - bar_width / 6, y2, bar_width / 3, label='Random', yerr=yerr2, error_kw=error_attri, color="#FF8884", edgecolor="black")
        ax.bar(index + bar_width / 6, y3, bar_width / 3, label='R-Opt', yerr=yerr3, error_kw=error_attri, color="#2878B5", edgecolor="black")
        ax.bar(index + bar_width / 2, y4, bar_width / 3, label='Sub-Opt', yerr=yerr4, error_kw=error_attri, color="#C7F1F7", edgecolor="black")
    # 设置坐标轴
    # ax.set_xlim(0, 9.5)
    # ax.set_ylim(0, 1.4)
    ax.set_yticks(yticks)
    ax.set_xticklabels(x)
    ax.set_xlabel(xlabel, fontsize=X_LABEL_FRONT_SIZE, labelpad=X_LABEL_PAD)#, position=(10,20)
    ax.set_ylabel(ylabel, fontsize=Y_LABEL_FRONT_SIZE, labelpad=Y_LABEL_PAD, loc='top')
    # 设置刻度
    ax.tick_params(rotation=45, axis='x', labelsize=X_TICKS_FRONT_SIZE, pad=1, which='major', width=1, length=1.5)
    ax.tick_params(axis='y', labelsize=Y_TICKS_FRONT_SIZE, pad=1, which='major', width=1, length=1.5)
    # 显示网格 
    # ax.grid(True, linestyle='-.')
    # ax.yaxis.grid(True, linestyle='-.')
    # 添加图例
    # legend = ax.legend(loc='best', frameon=False, fontsize=9)
    if legend_type==0:
        ax.legend(loc='best', frameon=False, fontsize=LEGEND_FONT_SIZE)
    else:
        ax.legend(loc='best', frameon=False, fontsize=LEGEND_FONT_SIZE,ncol=2,borderpad=0,labelspacing=0.3,handlelength=2,columnspacing=1)

    #plt.show()
    plt.subplots_adjust(top=SUBPLOTS_ADJUST_TOP, bottom=SUBPLOTS_ADJUST_BOTTOM, right=SUBPLOTS_ADJUST_RIGHT, left=SUBPLOTS_ADJUST_LEFT)
    fig.savefig(name)


def draw_line(x, y1, y2, y3, xlabel, ylabel, yticks, name):
    SUBPLOTS_ADJUST_TOP = 0.95
    SUBPLOTS_ADJUST_BOTTOM = 0.29
    SUBPLOTS_ADJUST_RIGHT = 0.97
    SUBPLOTS_ADJUST_LEFT = 0.15
    fig, ax = plt.subplots(figsize=(1.7 * 2, 1.1 * 2), dpi=300)#, constrained_layout=True)
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
    ax.set_xlabel(xlabel, fontsize=X_LABEL_FRONT_SIZE, labelpad=X_LABEL_PAD)
    ax.set_ylabel(ylabel, fontsize=Y_LABEL_FRONT_SIZE, labelpad=Y_LABEL_PAD, loc='top')
    # 设置刻度
    ax.tick_params(axis='x', labelsize=X_TICKS_FRONT_SIZE, rotation=45, pad=1, which='major', width=1, length=2)
    ax.tick_params(axis='y', labelsize=Y_TICKS_FRONT_SIZE, pad=1, which='major', width=1, length=2)
    # 显示网格
    # ax.grid(True, linestyle='-.')
    # ax.yaxis.grid(True, linestyle='-.')
    # 添加图例
    # legend = ax.legend(loc='best', frameon=False, fontsize=10)
    ax.legend(loc='best', frameon=False, fontsize=LEGEND_FONT_SIZE)

    #plt.show()
    plt.subplots_adjust(top=SUBPLOTS_ADJUST_TOP, bottom=SUBPLOTS_ADJUST_BOTTOM, right=SUBPLOTS_ADJUST_RIGHT, left=SUBPLOTS_ADJUST_LEFT)
    fig.savefig(name)