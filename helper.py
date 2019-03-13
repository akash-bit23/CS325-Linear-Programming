import csv


def parse_data(file_path):
    data_list = []
    with open(file_path, mode='r', encoding="utf-8") as data:
        reader = csv.reader(
            data, delimiter=';', quotechar='|')
        for (index, row) in enumerate(reader):
            if(index != 0):
                data_list.append((float(row[7]), float(row[8])))
    return data_list
