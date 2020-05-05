import os
from datetime import datetime

import openpyxl

#def avg(l):
#    return sum(l) / len(l)

def max_search(v):
    k = avg(v['maximum'])
    a = abs(avg(v['minimum']))
    return max(k, a)

xls_column_code = {
    'STORY': 'B',
    'EQ1.txt': 'C',
    'EQ2.txt': 'D',
    'EQ3.txt': 'E',
    'EQ4.txt': 'F',
    'EQ5.txt': 'G',
    'EQ6.txt': 'H',
    'EQ7.txt': 'I',
    'EQ8.txt': 'J',
    'EQ9.txt': 'K',
    'EQ10.txt': 'L',
    'EQ11.txt': 'M',
    'EQ12.txt': 'N',
    'EQ13.txt': 'O',
    'EQ14.txt': 'P',
    'AVG': 'Q'
}

xls_input_file = './data/Story Shear Force.xlsx'
xls_output_file = 'Story Shear Force_output.xlsx'
xls_column_start_row = 2

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
    total_average_dict = {}
    for sorted_file in file_list:
        # dataname = EQ1. EQ2 ...
        dataname = sorted_file[1]
        if ".txt" not in dataname:
            continue
        f = open(directory + dataname)

        story_list = []
        max_list = []
        min_list = []

        print(dataname)

        while True:
            line = f.readline()
            if not line:
                break
            split_list = line.split(',')
            if len(split_list) == 6 and split_list[0].startswith('Column'):
                story_list.append(split_list)
            elif len(split_list) != 0 and split_list[0].startswith('Maximum'):
                max_list.append(split_list)
            elif len(split_list) != 0 and split_list[0].startswith('Minimum'):
                min_list.append(split_list)
            else:
                continue

        f.close()

        max_list = max_list[0][1:]
        min_list = min_list[0][1:]

        target_story_list = []
        for h in story_list:
            target_story_list.append(h[5].strip())

        v_target_story_list = []
        v_max_list = []
        v_min_list = []

        for h in target_story_list:
            v_target_story_list.append(float(h.strip()))
        for h in max_list:
            v_max_list.append(float(h.strip()))
        for h in min_list:
            v_min_list.append(float(h.strip()))

        zipped_list = list(zip(v_target_story_list, v_max_list, v_min_list))
    print(zipped_list)
#        story_group_dict = {}
#        for h in v_target_story_list:
#            if h not in story_group_dict:
#                story_group_dict[h] = {
#                    'maximum': [],
#                    'minimum': []
#                }

 #       for zipped in zipped_list:
 #           story_score = zipped[0]
 #           maximum = zipped[1]
 #           minimum = zipped[2]

 #           story_group_dict[story_score]['maximum'].append(maximum)
 #           story_group_dict[story_score]['minimum'].append(minimum)

 #      process_list = []
 #       for (h, v) in story_group_dict.items():
 #           process_list.append((h, max_search(v)))

 #           max_search_value = max_search(v)
 #           if h in total_average_dict:
 #               total_average_dict[h].append(max_search_value)
 #           else:
 #               total_average_dict[h] = []
 #               total_average_dict[h].append(max_search_value)

 #       process_list.sort(reverse=True)
 #       print(process_list)
 #       print("===========")

 #       xls_sheet = xls_workbook[root]
        ## eq[x]
 #       start_row = xls_column_start_row
 #       for process in process_list:
 #           cell = xls_column_code[dataname] + str(start_row)
 #           xls_workbook[root][cell] = process[1]
 #           start_row = start_row + 1

 #   floor_average_list = []
 #   for (k, v) in total_average_dict.items():
 #       floor_average_list.append((k, avg(v)))
 #   floor_average_list.sort(reverse=True)

 #   print(floor_average_list)
 #   xls_sheet = xls_workbook[root]
 #   start_row = xls_column_start_row
 #   for floor in floor_average_list:
 #       h = floor[0]
 #       # write height
 #       story_cell = xls_column_code['STORY'] + str(start_row)
 #       xls_workbook[root][story_cell] = h
        # write average
 #       avg_cell = xls_column_code['AVG'] + str(start_row)
 #       xls_workbook[root][avg_cell] = floor[1]

 #       start_row = start_row + 1

#output_file_name = './data/' + datetime.now().strftime('%Y%m%d %H%M') + '_' + xls_output_file

#xls_workbook.save(filename=output_file_name)
