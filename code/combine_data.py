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


def combine_data()
combined_data = SJ_data + SF_data + PHX_data + SD_data + Charlotte_data + NYC_data + Indianapolis_data + LA_data 



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

if __name__ == "__main__":
    combined_data = SJ_data + SF_data + PHX_data + SD_data + Charlotte_data + NYC_data + Indianapolis_data + LA_data
    final_data = sort_data(combined_data)
    write_data_to_CSV(fina_data, CSV_PATH)
