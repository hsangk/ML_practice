import pandas as pd

data_path = "./data/231024-label.xlsx"

def label_dict(data_path):
    data = pd.read_excel(data_path, usecols="B:H")

    labels = dict()

    for _, data in data.iterrows():
        if data[1] == 'HC':
            cls = 0
        elif data[1] == 'CHR':
            cls = 1
        else:
            cls = 2
        labels[str(data[0])] = cls

    return labels
