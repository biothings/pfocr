import os
import json

def load_data(data_folder):
    file_path = os.path.join(data_folder, "pfocr_biothings.ndjson?dl=0")
    with open(file_path) as f:
        for l in f.readlines():
            doc = json.loads(l)
            yield doc

