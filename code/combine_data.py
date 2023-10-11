import CSV
import os
from SJ import load_SJ_Parking and cut_data and tranform_data and rename_data
from SD import load_SD_Parking and cut_data and tranform_data and rename_data
from SF import load_SF_Parking and cut_data and tranform_data and rename_data
from PHX import load_PHX_Parking and cut_data and tranform_data and rename_data
from nyc import load_NYC_parking and remove_data and calculate_average
from charlotte import load_charlotte_parking and remove_data

BASE_DIR = "artifacts"
CSV_PATH = os.path.join(BASE_DIR, "results.csv")




def load_SJ()
    """Loads in SJ data"""
    SJ_data = load_SJ_parking()
    cut_data = remove_data(SJ_data)
    transform_data = transform_data(cut_data)
    SJ_data = rename_data(transform_data)

def load_PHX()
    """Loads in PHX data"""
    PHX_data = load_SD_parking()
    cut_data = remove_data(SD_data)
    transform_data = transform_data(cut_data)
    PHX_data = rename_data(transform_data)

def load_SF()
    """Loads in SF data"""
    SF_data = load_SD_parking()
    cut_data = remove_data(SD_data)
    transform_data = transform_data(cut_data)
    SF_data = rename_data(transform_data)

def load_SD()
    """Loads in SD data"""
    SD_data = load_SD_parking()
    cut_data = remove_data(SD_data)
    transform_data = transform_data(cut_data)
    SD_data = rename_data(transform_data)
def load_nyc()
    """Loads NYC data"""
    NYC_data = load_NYC_parking()
    cut_data = remove_data(NYC_data)
    NYC_data = calculate_average(cut_data)
def load_Charlotte()
    """Loads Charlotte data"""
    Charlotte_data = load_charlotte_parking()
    Charlotee_data = remove_data(Charlotte_data)
def load_Indianapolis()
    """Loads Indianapolis data"""
    Indianapolis_data = 



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
