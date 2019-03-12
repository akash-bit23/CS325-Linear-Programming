import csv


def parse_data(file_path):
    data_list = []
    with open(file_path, mode='r', encoding="utf-8") as data:
        reader = csv.reader(
            data, delimiter=';', quotechar='|')
        for row in reader:
            data_list.append({
                temp: row[8],
                day: row[9]
            })
    return data_list
