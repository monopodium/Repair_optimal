from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
from matplotlib import pyplot as plt
def find_DRC0():
    k_nonoverlapping = np.arange(6, 30, 1)
    y_nonoverlapping = np.array([])
    r_nonoverlapping = np.array([])
    for k_each in k_nonoverlapping:
        y_i = 9999
        r_i = 0
        for r_each in range(2,k_each):
            y_now = 1 + r_each/k_each + math.ceil(k_each/r_each)/k_each + 1/k_each
            if y_now <= y_i:
                r_i = r_each
            y_i = min(y_i, y_now)

        y_nonoverlapping = np.append(y_nonoverlapping,y_i)
        r_nonoverlapping = np.append(r_nonoverlapping,r_i)
    print(k_nonoverlapping)
    print(r_nonoverlapping)
    plt.xlabel('k')
    plt.xlabel('k')
    plt.xticks(k_nonoverlapping)
    plt.ylabel('redundancy: n/k')
    plt.title("redundancy: n/k")
    plt.plot(k_nonoverlapping, y_nonoverlapping,label='Non-Overlapping')
    #plt.fill_between(k_nonoverlapping,y_nonoverlapping ,2, color='g', alpha=0.2)
    #plt.plot(k_nonoverlapping, r_nonoverlapping,label='Non-Overlapping')

    k_overlapping = np.arange(6, 30, 1)
    y_overlapping = np.array([])
    r_overlapping = np.array([])
    for k_each in k_overlapping:
        y_i = 9999
        r_i = 0
        for r_each in range(2,k_each):
            y_now = 1 + r_each/k_each + math.ceil(k_each/r_each)/k_each
            y_i = min(y_i,y_now)
            if y_now <= y_i:
                r_i = r_each
        y_overlapping = np.append(y_overlapping,y_i)
        r_overlapping = np.append(r_overlapping,r_i)
    plt.plot(k_overlapping, y_overlapping,label='Overlapping')
    #plt.fill_between(k_overlapping,y_overlapping ,2, color='r', alpha=0.3)
    #plt.plot(k_overlapping, r_overlapping,label='Overlapping')
    plt.legend(loc='best', frameon=False, fontsize=9)
    plt.grid(axis='x',color = '#27202b', linestyle = '-.', linewidth = 0.5,alpha=0.5)
    plt.grid(axis='y',color = '#27202b', linestyle = '-.', linewidth = 0.5,alpha=0.5)

    plt.savefig("a.png")
    
def find_DRC_NRC():
    k_nonoverlapping = np.arange(6, 30, 1)
    y_nonoverlapping = np.array([])
    r_nonoverlapping = np.array([])
    nrc_nonoverlapping = np.array([])
    for k_each in k_nonoverlapping:
        y_i = 9999
        r_i = 0
        for r_each in range(2,k_each):
            y_now = 1 + r_each/k_each + math.ceil(k_each/r_each)/k_each + 1/k_each
            if y_now <= y_i:
                r_i = r_each
            y_i = min(y_i, y_now)
        nrc_nonoverlapping = np.append(nrc_nonoverlapping,0)
        y_nonoverlapping = np.append(y_nonoverlapping,y_i)
        r_nonoverlapping = np.append(r_nonoverlapping,r_i)
    print(k_nonoverlapping)
    print(r_nonoverlapping)
    plt.xlabel('k')
    plt.xlabel('k')
    plt.xticks(k_nonoverlapping)
    plt.ylabel('NRC')
    plt.title("NRC")
    plt.plot(k_nonoverlapping, nrc_nonoverlapping,label='Non-Overlapping')
    #plt.fill_between(k_nonoverlapping,y_nonoverlapping ,2, color='g', alpha=0.2)
    #plt.plot(k_nonoverlapping, r_nonoverlapping,label='Non-Overlapping')

    k_overlapping = np.arange(6, 30, 1)
    y_overlapping = np.array([])
    r_overlapping = np.array([])
    nrc_overlapping = np.array([])
    for k_each in k_overlapping:
        y_i = 9999
        r_i = 0
        for r_each in range(2,k_each):
            y_now = 1 + r_each/k_each + math.ceil(k_each/r_each)/k_each
            y_i = min(y_i,y_now)
            if y_now <= y_i:
                r_i = r_each
        l = math.ceil(k_each/r_i)
        nrc_overlapping = np.append(nrc_overlapping,((l*r_i - k_each)*(l-1)+(r_i-(l*r_i - k_each))*l)/k_each)
        y_overlapping = np.append(y_overlapping,y_i)
        r_overlapping = np.append(r_overlapping,r_i)
    plt.plot(k_overlapping, nrc_overlapping,label='Overlapping')
    #plt.fill_between(k_overlapping,y_overlapping ,2, color='r', alpha=0.3)
    #plt.plot(k_overlapping, r_overlapping,label='Overlapping')
    plt.legend(loc='best', frameon=False, fontsize=9)
    plt.grid(axis='x',color = '#27202b', linestyle = '-.', linewidth = 0.5,alpha=0.5)
    plt.grid(axis='y',color = '#27202b', linestyle = '-.', linewidth = 0.5,alpha=0.5)

    plt.savefig("b.png")
#find_DRC0()    
find_DRC_NRC()