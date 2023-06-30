from draw_util import draw_line,draw_bar
from configs import default_data
from analysis_data import analysis_file,data_one_pic,reduce_and_times
# import numpy as np
import os
import sys

abs_path=os.path.abspath(r"..")+'/final_results_figure/exp_fig/'

def draw_DRC_diff_object_size(code_type):
    x = ["1KB", "4KB", "16KB", "256KB", "1MB", "4MB"]
    xlabel = 'Object Size'
    ylabel = 'Degraded Read Time (ms)'
    name = abs_path+'DRC_diff_object_size_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 5000, 10000, 15000, 20000, 25000],
        "azure_lrc":[0, 10, 20, 30],
        "azure_lrc_1":[0, 10, 20, 30],
        "optimal":[0, 5000, 10000, 15000, 20000, 25000]
    }
    yticks = yticks_all[code_type]
    y_all, _ = data_one_pic(default_data[code_type]['data_size_option'], "data_size", "DRC", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw_line(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


def draw_NRR_diff_object_size(code_type):
    x = ["1KB", "4KB", "16KB", "256KB", "1MB", "4MB"]
    xlabel = 'Object Size'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = abs_path+'NRR_diff_object_size_'+code_type+'.pdf'
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
    draw_line(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


def draw_DRC_diff_parameter_1M(code_type,if_sub=False):
    default_data[code_type]["data_size"] = 1024
    x = [str(item) for item in default_data[code_type]["parameter_option"]]
    xlabel = 'Coding Parameter'
    ylabel = 'Degraded Read Time (ms)'
    if if_sub:
        name = abs_path+'DRC_diff_Parameter_1MB_'+code_type+'_Sub.pdf'
    else:
        name = abs_path+'DRC_diff_Parameter_1MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 2000, 4000, 6000, 8000, 10000, 12000],
        "azure_lrc":[0, 5, 10, 15, 20],
        "azure_lrc_1":[0, 4, 8, 12, 16],
        "optimal":[0, 2000, 4000, 6000, 8000, 10000, 12000]
    }
    yticks = yticks_all[code_type]
    y_all, error_bar = data_one_pic(default_data[code_type]['parameter_option'], "parameter", "DRC", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    if not if_sub:
        reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
        draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])
    else:
        yticks = [0,2,4,6,8]
        reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
        draw_bar(x, None, None, y_all["Best_Placement"], \
            xlabel, ylabel, yticks, name, None, None, \
                error_bar["Best_Placement"],y4=y_all["Sub_Optimal"],
                yerr4=error_bar["Sub_Optimal"],legend_type=1,column=2)        


def draw_NRR_diff_parameter_1M(code_type,if_sub=False):
    default_data[code_type]["data_size"] = 1024
    x = [str(item) for item in default_data[code_type]["parameter_option"]]
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Rate (MiB/s)'
    if if_sub:
        name = abs_path+'NRR_diff_Parameter_1MB_'+code_type+'_Sub.pdf'
    else:
        name = abs_path+ 'NRR_diff_Parameter_1MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 20, 40, 60, 80, 100],
        "azure_lrc":[0, 40, 80, 120],
        "azure_lrc_1":[0, 40, 80, 120],
        "optimal":[0, 20, 40, 60, 80, 100]
    }
    yticks = yticks_all[code_type]
    y_all, error_bar = data_one_pic(default_data[code_type]['parameter_option'], "parameter", "NRR", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    if not if_sub:
        reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
        draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])
    else:
        reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
        draw_bar(x, None, None, y_all["Best_Placement"], 
                 xlabel, ylabel, yticks, name, None,
                 None, error_bar["Best_Placement"],
                 y4=y_all["Sub_Optimal"],yerr4=error_bar["Sub_Optimal"],legend_type=1,column=2)           


def draw_DRC_diff_parameter_4M(code_type,if_sub=False):
    default_data[code_type]["data_size"] = 4096
    x = [str(item) for item in default_data[code_type]["parameter_option"]]
    xlabel = 'Coding Parameter'
    ylabel = 'Degraded Read Time (ms)'
    if if_sub:
        name = abs_path+'DRC_diff_Parameter_4MB_'+code_type+'_Sub.pdf'
    else:
        name = abs_path+ 'DRC_diff_Parameter_4MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000],
        "azure_lrc":[0, 20, 40,60,80],
        "azure_lrc_1":[0, 10, 20, 30, 40, 50],
        "optimal":[0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    }
    yticks = yticks_all[code_type]
    y_all, error_bar = data_one_pic(default_data[code_type]['parameter_option'], "parameter", "DRC", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    if not if_sub:  
        reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
        draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])
    else:
        yticks = [0,5,10,15,20]
        reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
        draw_bar(x, None, None, y_all["Best_Placement"], 
                 xlabel, ylabel, yticks, name, None,
                 None, error_bar["Best_Placement"],
                 y4=y_all["Sub_Optimal"],yerr4=error_bar["Sub_Optimal"],legend_type=1,column=2)       


def draw_NRR_diff_parameter_4M(code_type,if_sub=False):
    default_data[code_type]["data_size"] = 4096
    x = [str(item) for item in default_data[code_type]["parameter_option"]]
    xlabel = 'Coding Parameter'
    ylabel = 'Node Repair Rate (MiB/s)'
    if if_sub:
        name = abs_path+'NRR_diff_Parameter_4MB_'+code_type+'_Sub.pdf'
    else:
        name = abs_path+'NRR_diff_Parameter_4MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas": [0, 20, 40, 60, 80],
        "azure_lrc":[0, 40, 80, 120, 160],
        "azure_lrc_1":[0, 40, 80, 120, 160],
        "optimal":[0, 20, 40, 60, 80]
    }
    yticks = yticks_all[code_type]
    y_all, error_bar = data_one_pic(default_data[code_type]['parameter_option'], "parameter", "NRR", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    if not if_sub:
        reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
        draw_bar(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name, error_bar["Flat"], error_bar["Random"], error_bar["Best_Placement"])
    else:
        yticks = [0, 40, 80, 120]
        reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
        draw_bar(x, None, None, y_all["Best_Placement"], 
                 xlabel, ylabel, yticks, name, None,
                 None, error_bar["Best_Placement"],
                 y4=y_all["Sub_Optimal"],yerr4=error_bar["Sub_Optimal"],legend_type=1,column=2)        

def draw_DRC_diff_bandwidth_4M(code_type):
    default_data[code_type]["data_size"] = 4096
    x = ["0.5", "0.7", "1", "2", "10"]
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Degraded Read Time (ms)'
    name = abs_path+'DRC_diff_bandwidth_4MB_'+code_type+'.pdf'
    yticks_all = {
        "xorbas":[0, 10000, 20000, 30000, 40000],
        "azure_lrc":[0, 20, 40, 60],
        "azure_lrc_1":[0, 20, 40, 60],
        "optimal":[0, 10000, 20000, 30000, 40000]
    }
    yticks = yticks_all[code_type]
    y_all, _ = data_one_pic(default_data[code_type]['bindwith_option'], "bindwith", "DRC", default_data[code_type]['placement_option'],default_data[code_type])
    print(sys._getframe().f_code.co_name)
    reduce_and_times(y_all["Flat"],y_all["Random"],y_all["Best_Placement"])
    draw_line(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


def draw_NRR_diff_bandwidth_4M(code_type):
    default_data[code_type]["data_size"] = 4096
    x = ["0.5", "0.7", "1", "2", "10"]
    xlabel = 'Bandwidth (Gbps)'
    ylabel = 'Node Repair Rate (MiB/s)'
    name = abs_path+'NRR_diff_bandwidth_4MB_'+code_type+'.pdf'
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
    draw_line(x, y_all["Flat"], y_all["Random"], y_all["Best_Placement"], xlabel, ylabel, yticks, name)


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
    
    analysis_file('../final_results_figure/results/result_azure_lrc.txt')
    

    draw_DRC_diff_parameter_1M("azure_lrc",if_sub=True)
    draw_NRR_diff_parameter_1M("azure_lrc",if_sub=True)
    draw_DRC_diff_parameter_4M("azure_lrc",if_sub=True)
    draw_NRR_diff_parameter_4M("azure_lrc",if_sub=True)
    
    # draw_DRC_diff_object_size("azure_lrc")
    # draw_NRR_diff_object_size("azure_lrc")
    # draw_DRC_diff_parameter_1M("azure_lrc")
    # draw_NRR_diff_parameter_1M("azure_lrc")
    # draw_DRC_diff_parameter_4M("azure_lrc")
    # draw_NRR_diff_parameter_4M("azure_lrc")
    # draw_DRC_diff_bandwidth_4M("azure_lrc")
    # draw_NRR_diff_bandwidth_4M("azure_lrc")
    
    # analysis_file('../final_results_figure/results/result_azure_lrc_1.txt')
    # draw_DRC_diff_object_size("azure_lrc_1")
    # draw_NRR_diff_object_size("azure_lrc_1")

    # draw_DRC_diff_parameter_1M("azure_lrc_1")
    # draw_NRR_diff_parameter_1M("azure_lrc_1")
    # draw_DRC_diff_parameter_4M("azure_lrc_1")
    # draw_NRR_diff_parameter_4M("azure_lrc_1")

    # draw_DRC_diff_bandwidth_4M("azure_lrc_1")
    # draw_NRR_diff_bandwidth_4M("azure_lrc_1")