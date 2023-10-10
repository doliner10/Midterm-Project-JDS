import CSV
import os
from SJ import load_SJ_Parking and cut_data and tranform_data and SJ_data

BASE_DIR = "artifacts"
CSV_PATH = os.path.join(BASE_DIR, "results.csv")


combined_data = list()

SJ_data = load_SJ_parking()
cut_data = remove_data(SJ_data)
transform_data = transform_data(cut_data)
SJ_data = rename_data(transform_data)

#Need to add lists of dicts to add them together 

def sort_data(combined_data)
    """Sorts data by cities"""
    city_sort = sorted(data, key=lambda x: x["City"])
    final_data = city_sort
    return final data

def write_data_to_CSV(final_data, path)
    """Writes data to a CSV"""
    fieldname = ["City", "Street Address", "Rate"]
    with open(path, 'w+') as file:
        dict_writer = csv.DictWriter(f = file, fieldnames = fieldname)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    return
