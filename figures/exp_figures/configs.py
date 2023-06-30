placement_option_default = ["Flat", "Random", "Best_Placement"]
parameter_option_default = [(7, 4, 2), (10, 6, 3), (12, 8, 4), (15, 10, 5), (16, 10, 5)]
data_size_option_default = [1, 4, 16, 256, 1024, 4096]
bindwith_option_default = [493355, 657806, 986710, 1973420, 9867100]


data_all_xorbas = {
    'code_type':"xorbas",
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
    'code_type':"azure_lrc",
    'placement_option' : ["Flat", "Random", "Best_Placement","Sub_Optimal"],
    #'parameter_option': [(12,6,3),(16,10,5),(16,12,6),(18,12,5),(24,15,5)],
    'parameter_option': [(8, 3, 3), (9, 4, 2), (12, 6, 3), (16,12,6), (20, 12, 3), (24, 15, 5)],
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
    'code_type':"azure_lrc_1",
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
    'code_type':"optimal",
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