import os


# import openpyxl

def avg(l):
    return sum(l) / len(l)

def max_search(v):
    k = avg(v['maximum'])
    v = abs(avg(v['minimum']))
    return max(k, v)

#def avg_list(p):
#    return sum(p) / len(p)
total_average_dict = {}

directory = "CW1/"
data = os.listdir(directory)
# f = open("C:/Users/WIN/Desktop/sparta/myproject/CW1/EQ1.txt", 'r')

for dataname in data:
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

    process_list = []
    for (h, v) in height_group_dict.items():
        #    m.reverse()
        #        max_search.reverse()
        #    print(m[::-1])
        # print(h, max_search(v))
        process_list.append((h, max_search(v)))

        max_search_value = max_search(v)
        if h in total_average_dict:
            total_average_dict[h].append(max_search_value)
        else:
            total_average_dict[h] = []
            total_average_dict[h].append(max_search_value)
#        def avg_list(h):
#            return sum(total_average_dict(h))/len(h)

#    print(process_list)
    process_list.sort(reverse=True)
    print(process_list)
#    print("===========")
#    print(avg_list)



