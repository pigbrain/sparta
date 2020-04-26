import os
#import openpyxl

directory = "CW1/"
data = os.listdir(directory)
#f = open("C:/Users/WIN/Desktop/sparta/myproject/CW1/EQ1.txt", 'r')

for dataname in data:
    if ".txt" not in dataname:
       continue
    f = open(directory + dataname)
    print(dataname)

height_list = []
max_list = []
min_list = []
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

#if len(max_list) == 0 or len(min_list) == 0:
#        print("max_list or min_list size is invalid");
#exit(-1)

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

#print("====== height list ==== ")
#print(len(v_target_height_list))
#print(v_target_height_list)

#print("====== maximum list ==== ")
#print(len(v_max_list))
#print(v_max_list)

#print("====== minimum list ==== ")
#print(len(v_min_list))
#print(v_min_list)

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

def avg(l):
    return sum(l) / len(l)
def max_search():
    k = avg(n['maximum'])
    v = abs(avg(n['minimum']))
    return max(k, v)
for (m, n) in height_group_dict.items():
#    m.reverse()
#        max_search.reverse()
#    print(m[::-1])
    print(m,max_search())

#    rb = load_workbook("C:/Users/WIN/Desktop/sparta/myproject/Wall Shear Force.xlsx")
#    print(CW1['C4'].value)