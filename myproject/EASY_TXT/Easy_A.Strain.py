import os
from datetime import datetime

import openpyxl

def max_search(v):
    k = max(v['maximum'])
    return k

def min_search(v):
    a = min(v['minimum'])
    return a

def max_avg(l):
    return sum(k) / 14

def min_avg(l):
   return sum(a) / 14

xls_column_code = {
    'HEIGHT': 'C',
    'EQ1.txt': 'D',
    'EQ2.txt': 'E',
    'EQ3.txt': 'F',
    'EQ4.txt': 'G',
    'EQ5.txt': 'H',
    'EQ6.txt': 'I',
    'EQ7.txt': 'J',
    'EQ8.txt': 'K',
    'EQ9.txt': 'L',
    'EQ10.txt': 'M',
    'EQ11.txt': 'N',
    'EQ12.txt': 'O',
    'EQ13.txt': 'P',
    'EQ14.txt': 'Q',
    'AVG1': 'R',
    'EQ1.txt': 'S',
    'EQ2.txt': 'T',
    'EQ3.txt': 'U',
    'EQ4.txt': 'V',
    'EQ5.txt': 'W',
    'EQ6.txt': 'X',
    'EQ7.txt': 'Y',
    'EQ8.txt': 'Z',
    'EQ9.txt': 'AA',
    'EQ10.txt': 'AB',
    'EQ11.txt': 'AC',
    'EQ12.txt': 'AD',
    'EQ13.txt': 'AE',
    'EQ14.txt': 'AF',
    'AVG2': 'AG'
}

xls_input_file = './data/Axial Strain.xlsx'
xls_output_file = 'Axial Strain_output.xlsx'
xls_column_start_row = 3

xls_workbook = openpyxl.load_workbook(filename=xls_input_file, read_only=False, data_only=False)

root_directory = 'data/'
root_directory_list = os.listdir(root_directory)
root_list = []
for rd in root_directory_list:
    if rd.find('xls') < 0:
        root_list.append(rd)

for root in root_list:
    directory = root_directory + root + "/"
    data = os.listdir(directory)

    data.sort()
    file_list = []
    for d in data:
        file_list.append((int(d[2:-4]), d))

    file_list.sort()
    print(" ### > ", root)
    total_dict = {}
    for sorted_file in file_list:
        # dataname = EQ1. EQ2 ...
        dataname = sorted_file[1]
        if ".txt" not in dataname:
            continue
        f = open(directory + dataname)

        height_list = []
        max_list = []
        min_list = []

        print(dataname)

        while True:
            line = f.readline()
            if not line:
                break
            split_list = line.split(',')
            if len(split_list) == 10 and split_list[0].startswith('Column'):
                height_list.append(split_list)
            elif len(split_list) != 0 and split_list[0].startswith('Maximum'):
                max_list.append(split_list)
            elif len(split_list) != 0 and split_list[0].startswith('Minimum'):
                min_list.append(split_list)
            else:
                continue

        f.close()

        max_list = max_list[0][1:]
        min_list = min_list[0][1:]

        target_height_list = []
        for h in height_list:
            target_height_list.append(h[9].strip())

        v_target_height_list = []
        v_max_list = []
        v_min_list = []

        for h in target_height_list:
            v_target_height_list.append(float(h.strip()))
        for h in max_list:
            v_max_list.append(float(h.strip()))
        for h in min_list:
            v_min_list.append(float(h.strip()))

        zipped_list = list(zip(v_target_height_list, v_max_list, v_min_list))

        height_group_dict = {}
        for h in v_target_height_list:
            if h not in height_group_dict:
                height_group_dict[h] = {
                    'maximum': [],
                    'minimum': []
                }

        for zipped in zipped_list:
            height_score = zipped[0]
            maximum = zipped[1]
            minimum = zipped[2]

            height_group_dict[height_score]['maximum'].append(maximum)
            height_group_dict[height_score]['minimum'].append(minimum)
#    print(zipped_list)
        process_list = []
        for (h, v) in height_group_dict.items():
            process_list.append((h,  max_search(v), min_search(v)))

            max_search_value = max_search(v)
            if h in total_dict:
                total_dict[h].append(max_search_value)
            else:
                total_dict[h] = []
                total_dict[h].append(max_search_value)
            min_search_value = min_search(v)
            if h in total_dict:
                total_dict[h].append(min_search_value)
            else:
                total_dict[h] = []
            total_dict[h].append(min_search_value)

        process_list.sort(reverse=True)
        print(process_list)
        print("===========")

        xls_sheet = xls_workbook[root]
        ## eq[x]
        start_row = xls_column_start_row
        for process in process_list:
            cell = xls_column_code[dataname] + str(start_row)
            xls_workbook[root][cell] = process[1]
            start_row = start_row + 1

    floor_average_list = []
    for (k, l) in total_dict.items():
        floor_average_list.append((k, max_avg(l), min_avg(l)))
    floor_average_list.sort(reverse=True)

    print(floor_average_list)
    xls_sheet = xls_workbook[root]
    start_row = xls_column_start_row
    for floor in floor_average_list:
        h = floor[0]
        # write height
        height_cell = xls_column_code['HEIGHT'] + str(start_row)
        xls_workbook[root][height_cell] = h
        # write average
        avg1_cell = xls_column_code['AVG1'] + str(start_row)
        xls_workbook[root][avg1_cell] = floor[1]
        avg2_cell = xls_column_code['AVG2'] + str(start_row)
        xls_workbook[root][avg2_cell] = floor[2]

        start_row = start_row + 1

output_file_name = './data/' + datetime.now().strftime('%Y%m%d %H%M') + '_' + xls_output_file

xls_workbook.save(filename=output_file_name)
