import matplotlib.pyplot as plt
import numpy as np


def mult_list(y1, n, k):
    y2 = []
    for item in y1:
        y2.append((item * k) / n)
    return y2


def time_to_MiBs(y1, size_MB, k):
    true_size = size_MB / k
    y2 = []
    for item in y1:
        y2.append((true_size * 64) / item)
    return y2


# def draw(x,y1,y2,y3,xlabel,ylabel,yticks,name):
#     fig,ax=plt.subplots(figsize=(1.7*2,1.3*2), dpi=300,constrained_layout=True)
#     #设置自变量的范围和个数

#     #画图
#     ax.plot(x,y1, label='Flat', linestyle=':', marker='s',  markersize='3.2',markerfacecolor="none",color="#C82423")
#     ax.plot(x,y2, label='Random', linestyle='--', marker='o', markersize='3',markerfacecolor="none",color="#FF8884")
#     ax.plot(x,y3, label='R-Opt', linestyle='-', marker='^', markersize='3',markerfacecolor="none",color="#2878B5")
#     #设置坐标轴
#     #ax.set_xlim(0, 9.5)
#     #ax.set_ylim(0, 1.4)
#     ax.set_yticks(yticks)
#     ax.set_xlabel(xlabel, fontsize=5,labelpad = 2)
#     ax.set_ylabel(ylabel, fontsize=5,labelpad = 2)
#     #设置刻度
#     ax.tick_params(axis='x', labelsize=5,rotation=45,pad=1,which='major',width=0.5,length=1)
#     ax.tick_params(axis='y', labelsize=5,pad = 1,which='major',width=0.5,length=1)
#     #显示网格
#     #ax.grid(True, linestyle='-.')
#     #ax.yaxis.grid(True, linestyle='-.')
#     #添加图例
#     legend = ax.legend(loc='best',frameon=False,fontsize = 4)


#     plt.show()
#     fig.savefig(name)
def draw(x, y1, y2, y3, xlabel, ylabel, yticks, name):
    fig, ax = plt.subplots(figsize=(1.7 * 2, 1.1 * 2), dpi=300, constrained_layout=True)
    #设置自变量的范围和个数
    
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    #画图
    #009db2 - 024b51 - 0780cf
    #  #C82423   #FF8884  #2878B5
    ax.plot(x, y1, label='Flat', linestyle=':', marker='s', markersize='6.4', markerfacecolor="none", color="#C82423", linewidth=2.5)
    ax.plot(x, y2, label='Random', linestyle='--', marker='o', markersize='6', markerfacecolor="none", color="#FF8884", linewidth=2.5)
    ax.plot(x, y3, label='R-Opt', linestyle='-', marker='^', markersize='6', markerfacecolor="none", color="#2878B5", linewidth=2.5)
    #设置坐标轴
    #ax.set_xlim(0, 9.5)
    #ax.set_ylim(0, 1.4)
    ax.set_yticks(yticks)
    ax.set_xlabel(xlabel, fontsize=10, labelpad=4)
    ax.set_ylabel(ylabel, fontsize=9, labelpad=4)
    #设置刻度
    ax.tick_params(axis='x', labelsize=10, rotation=45, pad=2, which='major', width=1, length=2)
    ax.tick_params(axis='y', labelsize=10, pad=2, which='major', width=1, length=2)
    #显示网格
    #ax.grid(True, linestyle='-.')
    #ax.yaxis.grid(True, linestyle='-.')
    #添加图例
    legend = ax.legend(loc='best', frameon=False, fontsize=10)

    plt.show()
    fig.savefig(name)


# def draw_bar(x,y1,y2,y3,xlabel,ylabel,yticks,name,yerr1,yerr2,yerr3):
#     fig,ax=plt.subplots(figsize=(1.7,1.1), dpi=300,constrained_layout=True)
#     #设置自变量的范围和个数
#     index = np.array([1,3,5])#np.arange(1,len(x)+1,0.7)
#     print(index)
#     bar_width = 1
#     #画图
#     ax.set_xticks(index)
#     error_attri={"elinewidth":1,"ecolor":"black","capsize":1.5}
#     ax.bar(index-bar_width/2,y1,bar_width/2, label='Flat',yerr=yerr1,error_kw=error_attri,color="#C82423",edgecolor="black")
#     ax.bar(index,y2, bar_width/2,label='Random',yerr=yerr2,error_kw=error_attri,color="#FF8884",edgecolor="black")
#     ax.bar(index+bar_width/2,y3,bar_width/2, label='R-Opt',yerr=yerr3,error_kw=error_attri,color="#2878B5",edgecolor="black")
#     #设置坐标轴
#     #ax.set_xlim(0, 9.5)
#     #ax.set_ylim(0, 1.4)
#     ax.set_yticks(yticks)
#     ax.set_xticklabels(x)
#     ax.set_xlabel(xlabel, fontsize=5,labelpad=2)
#     ax.set_ylabel(ylabel, fontsize=5,labelpad=2)
#     #设置刻度
#     ax.tick_params(axis='x', labelsize=5,pad=1,which='major',width=0.5,length=1)
#     ax.tick_params(axis='y', labelsize=5,pad = 1,which='major',width=0.5,length=1)
#     #显示网格
#     #ax.grid(True, linestyle='-.')
#     #ax.yaxis.grid(True, linestyle='-.')
#     #添加图例
#     legend = ax.legend(loc='best',frameon=False,fontsize = 4)

#     plt.show()
#     fig.savefig(name)


def draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3):
    fig, ax = plt.subplots(figsize=(1.7 * 2, 1.1 * 2), dpi=300, constrained_layout=True)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    #设置自变量的范围和个数
    index = np.array([1, 3, 5, 7, 9])  #np.arange(1,len(x)+1,0.7)
    print(index)
    bar_width = 1
    #画图
    ax.set_xticks(index)
    #009db2 - 024b51 - 0780cf
    #  #C82423   #FF8884  #2878B5
    error_attri = {"elinewidth": 1, "ecolor": "black", "capsize": 1.5}
    ax.bar(index - bar_width / 2, y1, bar_width / 2, label='Flat', yerr=yerr1, error_kw=error_attri, color="#C82423", edgecolor="black")
    ax.bar(index, y2, bar_width / 2, label='Random', yerr=yerr2, error_kw=error_attri, color="#FF8884", edgecolor="black")
    ax.bar(index + bar_width / 2, y3, bar_width / 2, label='R-Opt', yerr=yerr3, error_kw=error_attri, color="#2878B5", edgecolor="black")
    #设置坐标轴
    #ax.set_xlim(0, 9.5)
    #ax.set_ylim(0, 1.4)
    ax.set_yticks(yticks)
    ax.set_xticklabels(x)
    ax.set_xlabel(xlabel, fontsize=10, labelpad=4)
    ax.set_ylabel(ylabel, fontsize=8, labelpad=4)
    #设置刻度
    ax.tick_params(rotation=45, axis='x', labelsize=10, pad=1, which='major', width=1, length=1.5)
    ax.tick_params(axis='y', labelsize=10, pad=1, which='major', width=1, length=1.5)
    #显示网格
    #ax.grid(True, linestyle='-.')
    #ax.yaxis.grid(True, linestyle='-.')
    #添加图例
    legend = ax.legend(loc='best', frameon=False, fontsize=9)

    plt.show()
    fig.savefig(name)


def draw_DRC_diff_bandwidth():
    x = ["0.5", "0.7", "1", "2", "10"]
    y1 = [11013, 20481, 29778, 39364, 48503]
    y1.reverse()
    y2 = [8573, 11450, 14221, 17993, 22906]
    y2.reverse()
    y3 = [6103, 6826, 6873, 6912, 7051]
    y3.reverse()
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_bandwidth_4M.pdf'
    yticks = [0, 10000, 20000, 30000, 40000, 50000]
    for i in range(len(x)):
        print(x[i])
        print("Flat", (y1[i] - y3[i]) / y1[i])
        print("Random", (y2[i] - y3[i]) / y2[i])
    draw(x, y1, y2, y3, xlabel, ylabel, yticks, name)


def draw_1block_NRC_diff_bandwidth():
    x = ["0.5", "0.7", "1", "2", "10"]
    y1 = [22151, 40813, 65818, 78728, 98651]
    y1.reverse()
    y2 = [22002, 35643, 51718, 64026, 77904]
    y2.reverse()
    y3 = [12877, 13338, 12278, 13906, 14318]
    y3.reverse()
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Node Repair Cost (us)'
    name = 'NRC_diff_bandwidth.pdf'
    yticks = [20000, 40000, 60000, 80000, 100000]
    for i in range(len(x)):
        print(x[i])
        print("Flat", (y1[i] - y3[i]) / y1[i])
        print("Random", (y2[i] - y3[i]) / y2[i])
    draw(x, y1, y2, y3, xlabel, ylabel, yticks, name)


def draw_64blocks_NRC_diff_bandwidth_1M():
    x = ["0.5", "0.7", "1", "2", "10"]
    y1 = [0.575073, 0.789185, 1.105053, 1.385028, 1.689053]
    y1.reverse()
    y2 = [0.504670, 0.673898, 0.824261, 1.183238, 1.419028]
    y2.reverse()
    y3 = [0.244530, 0.243649, 0.242420, 0.247230, 0.252838]
    y3.reverse()
    y1 = mult_list(y1, 12, 6)
    y2 = mult_list(y2, 12, 6)
    y3 = mult_list(y3, 12, 6)
    y1 = time_to_MiBs(y1, 1, 6)
    y2 = time_to_MiBs(y2, 1, 6)
    y3 = time_to_MiBs(y3, 1, 6)
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Node Repair Rate (MiB/s)'  #Node Repair Cost (s)'
    name = 'NRC_diff_bandwidth_1M.pdf'
    #yticks = [0.2,0.4,0.6,0.8,1]
    yticks = [0, 30, 60, 90, 120, 150, 180]
    for i in range(len(x)):
        print(x[i])
        print("Flat", y3[i] / y1[i])
        print("Random", y3[i] / y2[i])
    draw(x, y1, y2, y3, xlabel, ylabel, yticks, name)


def draw_64blocks_NRC_diff_bandwidth_4M():
    x = ["0.5", "0.7", "1", "2", "10"]
    y1 = [1.411070, 2.462203, 3.784595, 5.032706, 6.265415]
    y1.reverse()
    #y2 = [1.319308,2.243632,2.920577,4.244291,5.194672]
    y2 = [1.319308, 2.056638, 2.920577, 3.624811, 4.530040]
    y2.reverse()
    y3 = [0.745904, 0.779247, 0.774496, 0.780601, 0.816040]
    y3.reverse()
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    y1 = mult_list(y1, 12, 6)
    y2 = mult_list(y2, 12, 6)
    y3 = mult_list(y3, 12, 6)
    y1 = time_to_MiBs(y1, 4, 6)
    y2 = time_to_MiBs(y2, 4, 6)
    y3 = time_to_MiBs(y3, 4, 6)
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Node Repair Rate (MiB/s)'  #Node Repair Cost (s)'
    name = 'NRC_diff_bandwidth_4M.pdf'
    yticks = [0, 30, 60, 90, 120, 150, 180, 210]
    for i in range(len(x)):
        print(x[i])
        print("Flat", y3[i] / y1[i])
        print("Random", y3[i] / y2[i])
    draw(x, y1, y2, y3, xlabel, ylabel, yticks, name)


def draw_DRC_diff_Parameter_1MB():
    x = ["(8,3,3)", "(12,6,3)", "(15,10,5)", "(18,12,5)", "(24,15,5)"]
    y1 = [11795, 8657, 8437, 8085, 7249]
    y2 = [7263, 4721, 4644, 5447, 3892]
    y3 = [3274, 2193, 3134, 3171, 1211]
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Coding Parameter'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_Parameter_1MB.pdf'
    yticks = [0, 2500, 5000, 7500, 10000, 12500, 15000, 17500]
    yerr1 = [[12094-11795,8840-8657,8725-8437,8403-8085,7504-7249],\
            [11795-11073,8657-8475,8437-8149,8085-7933,7249-7101]]
    yerr2 = [[7593-7263,4778-4721,4794-4644,5807-5447,3967-3892],\
            [7263-7009,4721-4674,4644-4268,5447-5123,3892-3793 ]]
    yerr3 = [[3394-3274,2295-2193,3319-3134,3234-3171,1302-1211],\
            [3274-3001,2193-2061,3134-2902,3171-3095,1211-1194]]
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(len(x)):
        print(x[i])
        print("Flat", (y1[i] - y3[i]) / y1[i])
        print("Random", (y2[i] - y3[i]) / y2[i])
    draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3)


def draw_1block_NRC_diff_Parameter_1MB():
    x = ["(8,3,3)", "(12,6,3)", "(15,10,5)", "(18,12,5)", "(24,15,5)"]
    y1 = [23353, 17467, 11740]
    y2 = [16054, 14865, 6603]
    y3 = [5779, 4686, 4403]
    y1[0], y1[1], y1[2], y1[3], y1[4] = (y1[0] * 3) / 8, (y1[1] * 6) / 12, (y1[2] * 10) / 15, (y1[3] * 12) / 18, (y1[4] * 15) / 24
    y2[0], y2[1], y2[2], y2[3], y2[4] = (y2[0] * 3) / 8, (y2[1] * 6) / 12, (y2[2] * 10) / 15, (y2[3] * 12) / 18, (y2[4] * 15) / 24
    y3[0], y3[1], y3[2], y3[3], y3[4] = (y3[0] * 3) / 8, (y3[1] * 6) / 12, (y3[2] * 10) / 15, (y3[3] * 12) / 18, (y3[4] * 15) / 24
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Cost (us)'
    name = 'NRC_diff_Parameter_1MB.pdf'
    yticks = [5000, 10000, 15000, 20000, 25000]
    yerr1 = [[23353-22769,17467-16655,11740-10269],\
            [25059-23353,19004-17467,12789-11740]]
    yerr2 = [[16054-15171,14865-13881,6603-6419],\
            [18109-16054,16623-14865,6753-6603]]
    yerr3 = [[5779-5219,4686-4177,4403-4089],\
            [6004-5779,6150-4686,4683-4403]]
    for i in range(len(x)):
        print(x[i])
        print("Flat", (y1[i] - y3[i]) / y1[i])
        print("Random", (y2[i] - y3[i]) / y2[i])

    draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3)


def draw_64blocks_NRC_diff_Parameter_1MB():
    x = ["(8,3,3)", "(12,6,3)", "(15,10,5)", "(18,12,5)", "(24,15,5)"]
    y1 = [1.530155, 1.105053, 0.805892, 0.788984, 0.751027]
    y2 = [0.966644, 0.824261, 0.460064, 0.510249, 0.339853]
    y3 = [0.341029, 0.242420, 0.337872, 0.327082, 0.126371]
    y1[0], y1[1], y1[2], y1[3], y1[4] = (y1[0] * 3) / 8, (y1[1] * 6) / 12, (y1[2] * 10) / 15, (y1[3] * 12) / 18, (y1[4] * 15) / 24
    y2[0], y2[1], y2[2], y2[3], y2[4] = (y2[0] * 3) / 8, (y2[1] * 6) / 12, (y2[2] * 10) / 15, (y2[3] * 12) / 18, (y2[4] * 15) / 24
    y3[0], y3[1], y3[2], y3[3], y3[4] = (y3[0] * 3) / 8, (y3[1] * 6) / 12, (y3[2] * 10) / 15, (y3[3] * 12) / 18, (y3[4] * 15) / 24
    print(y1, y2, y3)
    y1[0], y1[1], y1[2], y1[3], y1[4] = (1 * 64) / (y1[0] * 3), (1 * 64) / (y1[1] * 6), (1 * 64) / (y1[2] * 10), (1 * 64) / (y1[3] * 12), (1 * 64) / (y1[4] * 15)
    y2[0], y2[1], y2[2], y2[3], y2[4] = (1 * 64) / (y2[0] * 3), (1 * 64) / (y2[1] * 6), (1 * 64) / (y2[2] * 10), (1 * 64) / (y2[3] * 12), (1 * 64) / (y2[4] * 15)
    y3[0], y3[1], y3[2], y3[3], y3[4] = (1 * 64) / (y3[0] * 3), (1 * 64) / (y3[1] * 6), (1 * 64) / (y3[2] * 10), (1 * 64) / (y3[3] * 12), (1 * 64) / (y3[4] * 15)
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Rate (MiB/s)'  #Node Repair Cost (s)'
    name = 'NRC_diff_Parameter_1MB.pdf'
    print(y1, y2, y3)
    yticks = [0, 40, 80, 120, 160, 200, 240]

    yerr1 = [[(1*64*8)/(1.530155*3*3)-(1*64*8)/(1.515182*3*3), (1*64*12)/(1.105053*6*6)-(1*64*12)/(1.100065*6*6), (1*64*15)/(0.805892*10*10)-(1*64*15)/(0.800367*10*10),  (1*18*64)/(0.788984*12*12)-(1*18*64)/(0.78082*12*12), (1*24*64)/(0.751027*15*15)-(1*24*64)/(0.735515*15*15)],\
            [(1*64*8)/(1.541491*3*3)-(1*64*8)/(1.530155*3*3), (1*64*12)/(1.129550*6*6)-(1*64*12)/(1.105053*6*6), (1*64*15)/(0.807234*10*10)-(1*64*15)/(0.805892*10*10),   (1*18*64)/(0.795515*12*12)-(1*18*64)/(0.788984*12*12), (1*24*64)/(0.761056*15*15)-(1*24*64)/(0.751027*15*15)]]
    yerr2 = [[(1*64*8)/(0.966644*3*3)-(1*64*8)/(0.947678*3*3), (1*64*12)/(0.824261*6*6)-(1*64*12)/(0.792793*6*6), (1*64*15)/(0.460064*10*10)-(1*64*15)/(0.454640*10*10),  (1*18*64)/(0.510249*12*12)-(1*18*64)/(0.507032*12*12), (1*24*64)/(0.339853*15*15)-(1*24*64)/(0.329260*15*15)],\
        [(1*64*8)/(0.999919*3*3)-(1*64*8)/(0.966644*3*3), (1*64*12)/(0.844320*6*6)-(1*64*12)/(0.824261*6*6), (1*64*15)/(0.487717*10*10)-(1*64*15)/(0.470064*10*10),       (1*18*64)/(0.513133*12*12)-(1*18*64)/(0.510249*12*12), (1*24*64)/(0.348884*15*15)-(1*24*64)/(0.339853*15*15)]]
    yerr3 = [[(1*64*8)/(0.341029*3*3)-(1*64*8)/(0.321817*3*3), (1*64*12)/(0.242420*6*6)-(1*64*12)/(0.231884*6*6), (1*64*15)/(0.307872*10*10)-(1*64*15)/(0.294297*10*10),  (1*18*64)/(0.327082*12*12)-(1*18*64)/(0.310901*12*12), (1*24*64)/(0.126371*15*15)-(1*24*64)/(0.120191*15*15)],\
            [(1*64*8)/(0.361474*3*3)-(1*64*8)/(0.341029*3*3), (1*64*12)/(0.253953*6*6)-(1*64*12)/(0.242420*6*6), (1*64*15)/(0.407709*10*10)-(1*64*15)/(0.397872*10*10),   (1*18*64)/(0.351632*12*12)-(1*18*64)/(0.337082*12*12), (1*24*64)/(0.129955*15*15)-(1*24*64)/(0.126371*15*15)]]
    # yerr1[0][0],yerr1[0][1],yerr1[0][2],yerr1[0][3],yerr1[0][4] = (yerr1[0][0]*3)/8,(yerr1[0][1]*6)/12,(yerr1[0][2]*10)/15,(yerr1[0][3]*12)/18,(yerr1[0][4]*15)/24
    # yerr1[1][0],yerr1[1][1],yerr1[1][2],yerr1[1][3],yerr1[1][4] = (yerr1[1][0]*3)/8,(yerr1[1][1]*6)/12,(yerr1[1][2]*10)/15,(yerr1[1][3]*12)/18,(yerr1[1][4]*15)/24

    # yerr2[0][0],yerr2[0][1],yerr2[0][2],yerr2[0][3],yerr2[0][4] = (yerr2[0][0]*3)/8,(yerr2[0][1]*6)/12,(yerr2[0][2]*10)/15,(yerr2[0][3]*12)/18,(yerr2[0][4]*15)/24
    # yerr2[1][0],yerr2[1][1],yerr2[1][2],yerr2[1][3],yerr2[1][4] = (yerr2[1][0]*3)/8,(yerr2[1][1]*6)/12,(yerr2[1][2]*10)/15,(yerr2[1][3]*12)/18,(yerr2[1][4]*15)/24

    # yerr3[0][0],yerr3[0][1],yerr3[0][2],yerr3[0][3],yerr3[0][4] = (yerr3[0][0]*3)/8,(yerr3[0][1]*6)/12,(yerr3[0][2]*10)/15,(yerr3[0][3]*12)/18,(yerr3[0][4]*15)/24
    # yerr3[1][0],yerr3[1][1],yerr3[1][2],yerr3[1][3],yerr3[1][4] = (yerr3[1][0]*3)/8,(yerr3[1][1]*6)/12,(yerr3[1][2]*10)/15,(yerr3[1][3]*12)/18,(yerr3[1][4]*15)/24

    # print(yerr1)
    # print(yerr2)
    # print(yerr3)

    # yerr1[0][0],yerr1[0][1],yerr1[0][2],yerr1[0][3],yerr1[0][4] = (1*64)/(yerr1[0][0]*3),(1*64)/(yerr1[0][1]*6),(1*64)/(yerr1[0][2]*10),(1*64)/(yerr1[0][3]*12),(1*64)/(yerr1[0][4]*15)
    # yerr1[1][0],yerr1[1][1],yerr1[1][2],yerr1[1][3],yerr1[1][4] = (1*64)/(yerr1[1][0]*3),(1*64)/(yerr1[1][1]*6),(1*64)/(yerr1[1][2]*10),(1*64)/(yerr1[1][3]*12),(1*64)/(yerr1[1][4]*15)

    # yerr2[0][0],yerr2[0][1],yerr2[0][2],yerr2[0][3],yerr2[0][4] = (1*64)/(yerr2[0][0]*3),(1*64)/(yerr2[0][1]*6),(1*64)/(yerr2[0][2]*10),(1*64)/(yerr2[0][3]*12),(1*64)/(yerr2[0][4]*15)
    # yerr2[1][0],yerr2[1][1],yerr2[1][2],yerr2[1][3],yerr2[1][4] = (1*64)/(yerr2[1][0]*3),(1*64)/(yerr2[1][1]*6),(1*64)/(yerr2[1][2]*10),(1*64)/(yerr2[1][3]*12),(1*64)/(yerr2[1][4]*15)

    # yerr3[0][0],yerr3[0][1],yerr3[0][2],yerr3[0][3],yerr3[0][4] = (1*64)/(yerr3[0][0]*3),(1*64)/(yerr3[0][1]*6),(1*64)/(yerr3[0][2]*10),(1*64)/(yerr3[0][3]*12),(1*64)/(yerr3[0][4]*15)
    # yerr3[1][0],yerr3[1][1],yerr3[1][2],yerr3[1][3],yerr3[1][4] = (1*64)/(yerr3[1][0]*3),(1*64)/(yerr3[1][1]*6),(1*64)/(yerr3[1][2]*10),(1*64)/(yerr3[1][3]*12),(1*64)/(yerr3[1][4]*15)
    # print(yerr1)
    # print(yerr2)
    # print(yerr3)
    # y1 = mult_list(y1,12,6)
    # y2 = mult_list(y2,12,6)
    # y3 = mult_list(y3,12,6)
    for i in range(len(x)):
        print(x[i])
        print("Flat", y3[i] / y1[i])
        print("Random", y3[i] / y2[i])

    draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3)


def draw_draw_1blocks_DRC_diff_Parameter_4MB():
    x = ["(8,3,3)", "(12,6,3)", "(15,10,5)", "(18,12,5)", "(24,15,5)"]
    y1 = [44179, 29778, 29908, 28001, 26984]
    y2 = [22991, 14221, 17292, 19945, 8450]
    y3 = [11065, 6873, 8020, 10295, 3714]
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Coding Parameter'
    ylabel = 'Degraded Read Time (us)'
    name = 'DRC_diff_Parameter_4MB.pdf'
    yticks = [0, 10000, 20000, 30000, 40000, 50000, 60000]
    yerr1 = [[44179-41007,29778-27334,29908-27112,28001-27011,26984-24887],\
            [46215-44179,31040-29778,29908-28745,29033-28001,28584-26984]]
    yerr2 = [[22991-21728,14221-14054,17292-14710,19945-18002,8450-7935],\
            [24097-22991,14328-14221,19919-17292,21123-19945,8963-8450]]

    yerr3 = [[11065-10589,6873-6179,8020-7070,10295-9939,3714-3632],\
            [11199-11065,8355-6873,9904-8020,10651-10295,3902-3714]]
    for i in range(len(x)):
        print(x[i])
        print("Flat", (y1[i] - y3[i]) / y1[i])
        print("Random", (y2[i] - y3[i]) / y2[i])
    draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3)


def draw_draw_1blocks_NRC_diff_Parameter_4MB():
    x = ["(8,3,3)", "(12,6,3)", "(15,10,5)", "(18,12,5)", "(24,15,5)"]
    y1 = [88116, 65818, 40766]
    y2 = [55389, 51718, 20616]
    y3 = [20647, 12278, 11230]
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Cost (us)'
    name = 'NRC_diff_Parameter_4MB.pdf'
    yticks = [20000, 40000, 60000, 80000, 100000]
    yerr1 = [[88116-82992,65818-60288,40766-39167],\
            [90890-88116,70892-65818,45019-40766]]
    yerr2 = [[55389-53277,51718-50048,20616-19713],\
            [58910-55389,54161-51718,23196-20616]]
    yerr3 = [[20647-19497,12278-11527,11230-10291],\
            [23971-20647,15584-12278,13350-11230]]
    for i in range(len(x)):
        print(x[i])
        print("Flat", (y1[i] - y3[i]) / y1[i])
        print("Random", (y2[i] - y3[i]) / y2[i])
    draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3)


def draw_64blocks_NRC_diff_Parameter_4MB():
    x = ["(8,3,3)", "(12,6,3)", "(15,10,5)", "(18,12,5)", "(24,15,5)"]
    y1 = [5.610397, 3.784595, 2.663662, 2.543211, 2.382081]
    y2 = [3.475751, 2.920577, 1.426934, 1.895024, 0.914806]
    y3 = [1.080300, 0.774496, 0.947704, 1.072348, 0.375345]
    y1[0], y1[1], y1[2], y1[3], y1[4] = (y1[0] * 3) / 8, (y1[1] * 6) / 12, (y1[2] * 10) / 15, (y1[3] * 12) / 18, (y1[4] * 15) / 24
    y2[0], y2[1], y2[2], y2[3], y2[4] = (y2[0] * 3) / 8, (y2[1] * 6) / 12, (y2[2] * 10) / 15, (y2[3] * 12) / 18, (y2[4] * 15) / 24
    y3[0], y3[1], y3[2], y3[3], y3[4] = (y3[0] * 3) / 8, (y3[1] * 6) / 12, (y3[2] * 10) / 15, (y3[3] * 12) / 18, (y3[4] * 15) / 24
    y1[0], y1[1], y1[2], y1[3], y1[4] = (4 * 64) / (y1[0] * 3), (4 * 64) / (y1[1] * 6), (4 * 64) / (y1[2] * 10), (4 * 64) / (y1[3] * 12), (4 * 64) / (y1[4] * 15)
    y2[0], y2[1], y2[2], y2[3], y2[4] = (4 * 64) / (y2[0] * 3), (4 * 64) / (y2[1] * 6), (4 * 64) / (y2[2] * 10), (4 * 64) / (y2[3] * 12), (4 * 64) / (y2[4] * 15)
    y3[0], y3[1], y3[2], y3[3], y3[4] = (4 * 64) / (y3[0] * 3), (4 * 64) / (y3[1] * 6), (4 * 64) / (y3[2] * 10), (4 * 64) / (y3[3] * 12), (4 * 64) / (y3[4] * 15)
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Rate (MiB/s)'  #Node Repair Cost (s)'
    name = 'NRC_diff_Parameter_4MB.pdf'
    yticks = [0, 40, 80, 120, 160, 200, 240, 280]
    yerr1 = [[(4*64*8)/(5.610397*3*3)-(4*64*8)/(5.547993*3*3),  (4*64*12)/(3.7845958*6*6)-(4*64*12)/(3.714837*6*6),  (4*64*15)/(2.663662*10*10)-(4*64*15)/(2.609742*10*10),   (4*64*18)/(2.543211*12*12)-(4*64*18)/(2.489419*12*12),  (4*64*24)/(2.382081*15*15)-(4*64*24)/(2.313187*15*15),],\
            [(4*64*8)/(5.771332*3*3)-(4*64*8)/(5.610397*3*3),   (4*64*12)/(3.873669*6*6)-(4*64*12)/(3.784595*6*6),   (4*64*15)/(2.735906*10*10)-(4*64*15)/(2.663662*10*10),   (4*64*18)/(2.593051*12*12)-(4*64*18)/(2.543211*12*12),  (4*64*24)/(2.475105*15*15)-(4*64*24)/(2.382081*15*15),]]
    yerr2 = [[(4*64*8)/(3.475751*3*3)-(4*64*8)/(3.391519*3*3),  (4*64*12)/(2.920577*6*6)-(4*64*12)/(2.895699*6*6),   (4*64*15)/(1.426934*10*10)-(4*64*15)/(1.404525*10*10),   (4*64*18)/(1.895024*12*12)-(4*64*18)/(1.859207*12*12),  (4*64*24)/(0.914806*15*15)-(4*64*24)/(0.850277*15*15)],\
            [(4*64*8)/(3.558689*3*3)-(4*64*8)/(3.475751*3*3),   (4*64*12)/(2.945822*6*6)-(4*64*12)/(2.920577*6*6),   (4*64*15)/(1.503417*10*10)-(4*64*15)/(1.426934*10*10),   (4*64*18)/(1.916368*12*12)-(4*64*18)/(1.895024*12*12),  (4*64*24)/(0.952451*15*15)-(4*64*24)/(0.914806*15*15)] ]
    yerr3 = [[(4*64*8)/(1.080300*3*3)-(4*64*8)/(1.041069*3*3),  (4*64*12)/(0.774496*6*6)-(4*64*12)/(0.752889*6*6),   (4*64*15)/(0.947704*10*10)-(4*64*15)/(0.931452*10*10),   (4*64*18)/(1.072348*12*12)-(4*64*18)/(1.054289*12*12),  (4*64*24)/(0.375345*15*15)-(4*64*24)/(0.368995*15*15)],\
            [(4*64*8)/(1.150704*3*3)-(4*64*8)/(1.080300*3*3),   (4*64*12)/(0.795514*6*6)-(4*64*12)/(0.774496*6*6),   (4*64*15)/(0.985113*10*10)-(4*64*15)/(0.947704*10*10),   (4*64*18)/(1.098734*12*12)-(4*64*18)/(1.072348*12*12),  (4*64*24)/(0.382673*15*15)-(4*64*24)/(0.375345*15*15)]]
    # yerr1[0][0],yerr1[0][1],yerr1[0][2],yerr1[0][3],yerr1[0][4] = (yerr1[0][0]*3)/8,(yerr1[0][1]*6)/12,(yerr1[0][2]*10)/15,(yerr1[0][3]*12)/18,(yerr1[0][4]*15)/24
    # yerr1[1][0],yerr1[1][1],yerr1[1][2],yerr1[1][3],yerr1[1][4] = (yerr1[1][0]*3)/8,(yerr1[1][1]*6)/12,(yerr1[1][2]*10)/15,(yerr1[1][3]*12)/18,(yerr1[1][4]*15)/24

    # yerr2[0][0],yerr2[0][1],yerr2[0][2],yerr2[0][3],yerr2[0][4] = (yerr2[0][0]*3)/8,(yerr2[0][1]*6)/12,(yerr2[0][2]*10)/15,(yerr2[0][3]*12)/18,(yerr2[0][4]*15)/24
    # yerr2[1][0],yerr2[1][1],yerr2[1][2],yerr2[1][3],yerr2[1][4] = (yerr2[1][0]*3)/8,(yerr2[1][1]*6)/12,(yerr2[1][2]*10)/15,(yerr2[1][3]*12)/18,(yerr2[1][4]*15)/24

    # yerr3[0][0],yerr3[0][1],yerr3[0][2],yerr3[0][3],yerr3[0][4] = (yerr3[0][0]*3)/8,(yerr3[0][1]*6)/12,(yerr3[0][2]*10)/15,(yerr3[0][3]*12)/18,(yerr3[0][4]*15)/24
    # yerr3[1][0],yerr3[1][1],yerr3[1][2],yerr3[1][3],yerr3[1][4] = (yerr3[1][0]*3)/8,(yerr3[1][1]*6)/12,(yerr3[1][2]*10)/15,(yerr3[1][3]*12)/18,(yerr3[1][4]*15)/24

    # yerr1[0][0],yerr1[0][1],yerr1[0][2],yerr1[0][3],yerr1[0][4] = (4*64)/(yerr1[0][0]*3),(4*64)/(yerr1[0][1]*6),(4*64)/(yerr1[0][2]*10),(4*64)/(yerr1[0][3]*12),(4*64)/(yerr1[0][4]*15)
    # yerr1[1][0],yerr1[1][1],yerr1[1][2],yerr1[1][3],yerr1[1][4] = (4*64)/(yerr1[1][0]*3),(4*64)/(yerr1[1][1]*6),(4*64)/(yerr1[1][2]*10),(4*64)/(yerr1[1][3]*12),(4*64)/(yerr1[1][4]*15)

    # yerr2[0][0],yerr2[0][1],yerr2[0][2],yerr2[0][3],yerr2[0][4] = (4*64)/(yerr2[0][0]*3),(4*64)/(yerr2[0][1]*6),(4*64)/(yerr2[0][2]*10),(4*64)/(yerr2[0][3]*12),(4*64)/(yerr2[0][4]*15)
    # yerr2[1][0],yerr2[1][1],yerr2[1][2],yerr2[1][3],yerr2[1][4] = (4*64)/(yerr2[1][0]*3),(4*64)/(yerr2[1][1]*6),(4*64)/(yerr2[1][2]*10),(4*64)/(yerr2[1][3]*12),(4*64)/(yerr2[1][4]*15)

    # yerr3[0][0],yerr3[0][1],yerr3[0][2],yerr3[0][3],yerr3[0][4] = (4*64)/(yerr3[0][0]*3),(4*64)/(yerr3[0][1]*6),(4*64)/(yerr3[0][2]*10),(4*64)/(yerr3[0][3]*12),(4*64)/(yerr3[0][4]*15)
    # yerr3[1][0],yerr3[1][1],yerr3[1][2],yerr3[1][3],yerr3[1][4] = (4*64)/(yerr3[1][0]*3),(4*64)/(yerr3[1][1]*6),(4*64)/(yerr3[1][2]*10),(4*64)/(yerr3[1][3]*12),(4*64)/(yerr3[1][4]*15)
    for i in range(len(x)):
        print(x[i])
        print("Flat", y3[i] / y1[i])
        print("Random", y3[i] / y2[i])
    draw_bar(x, y1, y2, y3, xlabel, ylabel, yticks, name, yerr1, yerr2, yerr3)


def draw_DRC_diff_object_size():
    x = ["1KB", "4KB", "16KB", "256KB", "1MB", "4MB"]
    y1 = [1397, 1443, 1675, 3261, 8657, 29778]
    y2 = [771, 888, 944, 2038, 4721, 14221]
    y3 = [486, 477, 523, 868, 2193, 6873]
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Object Size'
    ylabel = 'Degraded Read Time (us)'
    yticks = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000]
    name = 'DRC_diff_object_size.pdf'
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(len(y1)):
        print(x[i])
        print("Flat")
        print((y1[i] - y3[i]) / y1[i])
        print("Random")
        print((y2[i] - y3[i]) / y2[i])
    # for item in y1:
    #     sum1 = sum1 + item
    # for item in y2:
    #     sum2 = sum2 + item
    # for item in y3:
    #     sum3 = sum3 + item
    # print(ylabel)
    # print("Flat")
    # print((sum1-sum3)/sum1)
    # print("Random")
    # print((sum2-sum3)/sum2)
    draw(x, y1, y2, y3, xlabel, ylabel, yticks, name)


def draw_1block_NRC_diff_object_size():
    x = ["1KB", "4KB", "16KB", "256KB", "1MB", "4MB"]
    y1 = [2822, 2905, 3257, 6492, 17467, 65818]
    y2 = [2562, 2348, 2637, 5561, 14865, 51718]
    y3 = [906, 918, 1020, 1612, 4686, 12278]
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Object Size'
    ylabel = 'Node Repair Cost (us)'
    name = 'NRC_diff_object_size.pdf'
    yticks = [10000, 20000, 30000, 40000, 50000, 60000, 70000]
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for item in y1:
        sum1 = sum1 + item
    for item in y2:
        sum2 = sum2 + item
    for item in y3:
        sum3 = sum3 + item
    print(ylabel)
    print("Flat")
    print((sum1 - sum3) / sum1)
    print("Random")
    print((sum2 - sum3) / sum2)
    draw(x, y1, y2, y3, xlabel, ylabel, yticks, name)


def draw_64blocks_NRC_diff_object_size():
    x = ["1KB", "4KB", "16KB", "256KB", "1MB", "4MB"]
    y1 = [0.197268, 0.226847, 0.226847, 0.426290, 1.105053, 3.784595]
    y2 = [0.131399, 0.145351, 0.165066, 0.321367, 0.824261, 2.920577]
    y3 = [0.080147, 0.088120, 0.091774, 0.125175, 0.242420, 0.774496]
    y1 = mult_list(y1, 12, 6)
    y2 = mult_list(y2, 12, 6)
    y3 = mult_list(y3, 12, 6)
    y1[0], y1[1], y1[2], y1[3], y1[4], y1[5] = (1 / 1024) * 64 / (y1[0] * 6), (4 / 1024) * 64 / (y1[1] * 6), (16 / 1024) * 64 / (y1[2] * 6), (256 / 1024) * 64 / (y1[3] * 6), (1 * 64) / (y1[4] * 6), (4 * 64) / (y1[5] * 6)
    y2[0], y2[1], y2[2], y2[3], y2[4], y2[5] = (1 / 1024) * 64 / (y2[0] * 6), (4 / 1024) * 64 / (y2[1] * 6), (16 / 1024) * 64 / (y2[2] * 6), (256 / 1024) * 64 / (y2[3] * 6), (1 * 64) / (y2[4] * 6), (4 * 64) / (y2[5] * 6)
    y3[0], y3[1], y3[2], y3[3], y3[4], y3[5] = (1 / 1024) * 64 / (y3[0] * 6), (4 / 1024) * 64 / (y3[1] * 6), (16 / 1024) * 64 / (y3[2] * 6), (256 / 1024) * 64 / (y3[3] * 6), (1 * 64) / (y3[4] * 6), (4 * 64) / (y3[5] * 6)
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Object Size'
    ylabel = 'Node Repair Rate (MiB/s)'  #Node Repair Cost (s)'
    name = 'NRC_diff_object_size.pdf'
    #yticks = [0.4,0.8,1.2,1.6,2]#[1,2,3,4,5]#
    yticks = [0, 20, 40, 60, 80, 100, 120, 140]
    # sum1=0
    # sum2=0
    # sum3=0
    print(y1, y2, y3)
    for i in range(len(y1)):
        print(x[i])
        print("Flat")
        print(y3[i] / y1[i])
        print("Random")
        print(y3[i] / y2[i])
        #if y2[i]<y1[i]:
        #print(y1[i],y2[i],y3[i])
    # for item in y1:
    #     sum1 = sum1 + item
    # for item in y2:
    #     sum2 = sum2 + item
    # for item in y3:
    #     sum3 = sum3 + item
    # print(ylabel)
    # print("Flat")
    # print((sum1-sum3)/sum1)
    # print("Random")
    # print((sum2-sum3)/sum2)
    # print(ylabel)
    # print("Flat")
    # print(sum3/sum1)
    # print("Random")
    # print(sum3/sum2)
    draw(x, y1, y2, y3, xlabel, ylabel, yticks, name)


def item_to_size_G(list_origin, size_of_one_block_M):
    y1 = []
    for item in list_origin:
        y1.append((item * size_of_one_block_M) / 1024)
    return y1


def draw_7(x, y1, y2, y3, y4, y5, y6, xlabel, ylabel, yticks, name):
    fig, ax = plt.subplots(figsize=(1.7 * 4, 1.1 * 2), dpi=300, constrained_layout=True)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    #设置自变量的范围和个数
    index = np.array([1, 3.5, 6, 8.5, 11, 13.5, 16])  #np.arange(1,len(x)+1,0.7)#[1,4,7,10,13,16,19]
    print(index)
    bar_width = 2
    #画图
    ax.set_xticks(index)
    #009db2 - 024b51 - 0780cf
    #  #C82423   #FF8884  #2878B5
    error_attri = {"elinewidth": 1, "ecolor": "black", "capsize": 1.5}
    ax.bar(index - 5 * bar_width / 12, y1, bar_width / 6, error_kw=error_attri, color="#C82423", edgecolor="black", label='Node0')
    ax.bar(index - bar_width / 4, y2, bar_width / 6, error_kw=error_attri, color="#FF8884", edgecolor="black", label='Node1')
    ax.bar(index - bar_width / 12, y3, bar_width / 6, error_kw=error_attri, color="#2878B5", edgecolor="black", label='Node2')
    ax.bar(index + bar_width / 12, y4, bar_width / 6, error_kw=error_attri, color="#F8AC8C", edgecolor="black", label='Node3')
    ax.bar(index + bar_width / 4, y5, bar_width / 6, error_kw=error_attri, color="#00adb5", edgecolor="black", label='Node4')
    ax.bar(index + 5 * bar_width / 12, y6, bar_width / 6, error_kw=error_attri, color="#fce38a", edgecolor="black", label='Node5')
    #设置坐标轴
    #ax.set_xlim(0, 9.5)
    #ax.set_ylim(0, 1.4)
    ax.set_yticks(yticks)
    ax.set_xticklabels(x)
    ax.set_xlabel(xlabel, fontsize=10, labelpad=4)
    ax.set_ylabel(ylabel, fontsize=8, labelpad=4)
    #设置刻度
    ax.tick_params(axis='x', labelsize=10, pad=1, which='major', width=1, length=1.5)  #rotation=45,
    ax.tick_params(axis='y', labelsize=10, pad=1, which='major', width=1, length=1.5)
    #显示网格
    #ax.grid(True, linestyle='-.')
    #ax.yaxis.grid(True, linestyle='-.')
    #添加图例
    legend = ax.legend(loc='best', frameon=False, fontsize=9, ncol=3, labelspacing=0.1, columnspacing=0.1, handletextpad=0.1)

    plt.show()
    fig.savefig(name)


def load_balance_draw():
    x = ["0", "1", "2", "3", "4", "5", "6"]
    yy1 = item_to_size_G([511, 528, 526, 538, 567, 557], 2.67)
    yy2 = item_to_size_G([601, 523, 533, 596, 562, 508], 2.67)
    yy3 = item_to_size_G([507, 545, 543, 599, 550, 504], 2.67)
    yy4 = item_to_size_G([537, 581, 597, 564, 535, 559], 2.67)
    yy5 = item_to_size_G([562, 517, 532, 530, 518, 543], 2.67)
    yy6 = item_to_size_G([554, 528, 493, 507, 508, 539], 2.67)
    yy7 = item_to_size_G([530, 532, 512, 499, 539, 521], 2.67)
    y1 = item_to_size_G([511, 601, 507, 537, 562, 554, 530], 2.67)
    y2 = item_to_size_G([528, 523, 545, 581, 517, 528, 532], 2.67)
    y3 = item_to_size_G([526, 533, 543, 597, 532, 493, 512], 2.67)
    y4 = item_to_size_G([538, 596, 599, 564, 530, 507, 499], 2.67)
    y5 = item_to_size_G([567, 562, 550, 535, 518, 508, 539], 2.67)
    y6 = item_to_size_G([557, 508, 504, 559, 543, 539, 521], 2.67)

    all_list = y1 + y2 + y3 + y4 + y5 + y6
    all_cluster = [sum(yy1), sum(yy2), sum(yy3), sum(yy4), sum(yy5), sum(yy6), sum(yy7)]
    print("node_level_min:", min(all_list))
    print("node_level_max:", max(all_list))
    print("node_level_average:", sum(all_list) / len(all_list))
    print("cluster_level_min:", min(all_cluster))
    print("cluster_level_max:", max(all_cluster))
    print("cluster_level_average:", sum(all_cluster) / len(all_cluster))

    print(y1)
    print(y2)
    print(y3)
    print(y4)
    print(y5)
    print(y6)
    #assert y1.shape[0]==y2.shape[0], '两个因变量个数不相等！'
    xlabel = 'Cluster ID'
    ylabel = 'Data volume(GB)'
    name = 'Load_Balance_pic.pdf'
    yticks = [0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1]
    print(y1)

    max1 = max(y1 + y2 + y3 + y4 + y5 + y6)
    min1 = min(y1 + y2 + y3 + y4 + y5 + y6)
    print("max1/min1", max1 / min1)
    print("sum", sum(y1 + y2 + y3 + y4 + y5 + y6))
    draw_7(x, y1, y2, y3, y4, y5, y6, xlabel, ylabel, yticks, name)
    #draw(x,y1,y2,y3,xlabel,ylabel,yticks,name)


#load_balance_draw()
print("draw_64blocks_NRC_diff_object_size")
draw_64blocks_NRC_diff_object_size()
# print("draw_64blocks_NRC_diff_bandwidth_1M")
# draw_64blocks_NRC_diff_bandwidth_1M()
print("draw_64blocks_NRC_diff_bandwidth_4M")
draw_64blocks_NRC_diff_bandwidth_4M()
print("draw_64blocks_NRC_diff_Parameter_1MB")
draw_64blocks_NRC_diff_Parameter_1MB()
print("draw_64blocks_NRC_diff_Parameter_4MB")
draw_64blocks_NRC_diff_Parameter_4MB()

# print("draw_DRC_diff_bandwidth")
# draw_DRC_diff_bandwidth()
# print("draw_DRC_diff_object_size")
# draw_DRC_diff_object_size()
# print("draw_draw_1blocks_DRC_diff_Parameter_4MB")
# draw_draw_1blocks_DRC_diff_Parameter_4MB()
# print("draw_DRC_diff_Parameter_1MB")
# draw_DRC_diff_Parameter_1MB()
