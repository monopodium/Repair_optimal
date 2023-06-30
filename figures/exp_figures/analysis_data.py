
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

all_result = {}

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
                code_type = match_run.group(2)
                placement = match_run.group(3)
                n = int(match_run.group(4))
                k = int(match_run.group(5))
                r = int(match_run.group(6))
                data_size = match_run.group(7)
                parameter = (n, k, r)
                DRC = float(lines[i + 2].strip('\n').split(':')[-1])/1000
                minDRC = float(lines[i + 3].strip('\n').split(':')[-1])/1000
                maxDRC = float(lines[i + 4].strip('\n').split(':')[-1])/1000
                NRR = float(lines[i + 5].strip('\n').split(':')[-1])
                minNRR = float(lines[i + 6].strip('\n').split(':')[-1])
                maxNRR = float(lines[i + 7].strip('\n').split(':')[-1])
                i = i + 8
                this_data = {"code_type":code_type,"placement": placement, "parameter": (n, k, r), "data_size": data_size, "bindwith": bindwith, "DRC": DRC, "NRR": NRR, "maxDRC": maxDRC, "minDRC": minDRC, "maxNRR": maxNRR, "minNRR": minNRR}
                all_result[str(code_type).lower()+str(placement) + str(parameter) + str(data_size) + str(bindwith)] = this_data


def data_one_pic(x_axis, x_axis_type, y_axis_type, column_options,default_data_this):
    all_data = {}
    all_data_error = {}
    for column in column_options:
        y_array = []
        y_array_error = [[], []]
        for x in x_axis:
            placement = column
            code_type = default_data_this["code_type"]
            parameter = default_data_this["parameter"]
            data_size = default_data_this["data_size"]
            bindwith = default_data_this["bindwith"]
            if x_axis_type == "parameter":
                parameter = x
            if x_axis_type == "data_size":
                data_size = x
            if x_axis_type == "bindwith":
                bindwith = x
            result_mean = all_result[str(code_type)+str(placement) + str(parameter) + str(data_size) + str(bindwith)][y_axis_type]
            result_max = all_result[str(code_type)+str(placement) + str(parameter) + str(data_size) + str(bindwith)]['max' + y_axis_type]
            result_min = all_result[str(code_type)+str(placement) + str(parameter) + str(data_size) + str(bindwith)]['min' + y_axis_type]
            y_array.append(result_mean)
            y_array_error[0].append(result_max - result_mean)
            y_array_error[1].append(result_mean - result_min)
        all_data[column] = y_array
        all_data_error[column] = y_array_error
    return all_data, all_data_error