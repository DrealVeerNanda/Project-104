import csv
from collections import Counter
with open("SOCR-HeightWeight.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
#to remove the list of the titles using pop
file_data.pop(0)
#sorting the data for weight
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

#mode
data = Counter(new_data)
#creating range
mode_data_for_range = {"75-85": 0, "85-95": 0, "95-105": 0, "105-115":0, "115-125":0, "125-135": 0, "135-145":0, "145-155":0,"155-165":0,"165-175":0}

#if for each range
for weight, occurence in data.items():
    if 75 < weight < 85:
        mode_data_for_range["75-85"] += occurence #increasing occurrence by 1
    elif 85 < weight < 95:
        mode_data_for_range["85-95"] += occurence #increasing occurrence by 1
    elif 95 < weight < 105:
        mode_data_for_range["95-105"] += occurence #increasing occurrence by 1
    elif 105 < weight < 115:
        mode_data_for_range["105-115"] += occurence #increasing occurrence by 1
    elif 115 < weight < 125:
        mode_data_for_range["115-125"] += occurence #increasing occurrence by 1
    elif 125 < weight < 135:
        mode_data_for_range["125-135"] += occurence #increasing occurrence by 1
    elif 135 < weight < 145:
        mode_data_for_range["135-145"] += occurence #increasing occurrence by 1
    elif 145 < weight < 155:
        mode_data_for_range["145-155"] += occurence #increasing occurrence by 1
    elif 155 < weight < 165:
        mode_data_for_range["155-165"] += occurence #increasing occurrence by 1
    elif 165 < weight < 175:
        mode_data_for_range["165-175"] += occurence #increasing occurrence by 1

mode_range, mode_occurrence = 0,0
for range, occurrence in mode_data_for_range.items():
    if(occurrence > mode_occurrence): 
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence


mode = float((mode_range[0] + mode_range[1]) / 2) 
print(f"Mode is -> {mode:2f}")       