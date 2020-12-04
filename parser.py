import os
import json


def load_data(data_folder):
    file_path = os.path.join(data_folder, "pfocr_biothings_65k_20201203.json")
    with open(file_path) as f:
        for l in f.readlines():
            doc = json.loads(l)
            yield doc
