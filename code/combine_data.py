<<<<<<< HEAD
import csv
import os
from SJ import load_SJ_parking, SJ_remove_data, SJ_transform_data, SJ_rename_data
from SD import load_SD_parking, SD_remove_data, SD_transform_data, SD_rename_data
from SF import load_SF_parking, SF_remove_data, SF_transform_data, SF_rename_data
from PHX import load_PHX_parking, PHX_remove_data, PHX_transform_data, PHX_rename_data
from nyc import load_NYC_parking, nyc_remove_data, nyc_calculate_average
from charlotte import load_Charlotte_parking, charlotte_remove_data
from indianapolis import indy_parking_data, indy_narrow_down_data, indy_transform_data, indy_proper_names
from la import LA_parking_data, la_narrow_down_data, la_transform_data, la_convert_average_rate_to_float, la_proper_names

BASE_DIR = "artifacts"
CSV_PATH = os.path.join(BASE_DIR, "results.csv")




def load_SJ():
    """Loads in SJ data"""
    SJ_data = load_SJ_parking()
    cut_data = SJ_remove_data(SJ_data)
    transform_data = SJ_transform_data(cut_data)
    

def load_PHX():
    """Loads in PHX data"""
    PHX_data = load_PHX_parking()
    cut_data = PHX_remove_data(PHX_data)
    transform_data = PHX_transform_data(cut_data)


def load_SF():
    """Loads in SF data"""
    SF_data = load_SF_parking()
    cut_data = SF_remove_data(SF_data)
    transform_data = SF_transform_data(cut_data)

def load_SD():
    """Loads in SD data"""
    SD_data = load_SD_parking()
    cut_data = SD_remove_data(SD_data)
    transform_data = SD_transform_data(cut_data)
def load_nyc():
    """Loads NYC data"""
    NYC_data = load_NYC_parking()
    cut_data = nyc_remove_data(NYC_data)
    
def load_Charlotte():
    """Loads Charlotte data"""
    Charlotte_data = load_Charlotte_parking()
    Charlotte_data = charlotte_remove_data(Charlotte_data)
def load_Indianapolis():
    """Loads Indianapolis data"""
    parking_data = indy_parking_data()
    narrowed_data = indy_narrow_down_data(parking_data)
    transformed_data = indy_transform_data(narrowed_data)
    
def load_LA():
    """Loads in LA data"""
    parking_data = LA_parking_data()
    narrowed_data = la_narrow_down_data(parking_data)
    transformed_data = la_transform_data(narrowed_data)
    converted_data = la_convert_average_rate_to_float(transformed_data)
    


def sort_data(combined_data):
    """Sorts data by cities"""
    city_sort = sorted(combined_data, key=lambda x: x["City"])
    final_data = city_sort
    return final_data

def write_data_to_CSV(final_data, path):
    """Writes data to a CSV"""
    fieldname = ["City", "Street Address", "Rate"]
    with open(path, 'w+') as file:
        dict_writer = csv.DictWriter(f = file, fieldnames = fieldname)
        dict_writer.writeheader()
        dict_writer.writerows(final_data)
    return

if __name__ == "__main__":
    combined_data = list()
    SJ_data = load_SJ()
    PHX_data = load_PHX()
    SF_data = load_SF()
    SD_data = load_SD()
    NYC_data = load_nyc()
    Charlotte_data = load_Charlotte()
    Indianapolis_data = load_Indianapolis()
    LA_data = load_LA()
    combined_data = SJ_data + SF_data + PHX_data + SD_data + Charlotte_data + NYC_data + Indianapolis_data + LA_data
    final_data = sort_data(combined_data)
    write_data_to_CSV(final_data, CSV_PATH)
=======
import pandas as pd
import os
import matplotlib.pyplot as plt


parking_data = pd.DataFrame()
data_dir = os.path.join("../artifacts")
OUTPUT_PATH = os.path.join(data_dir, "combined_results.csv")
PHX_file = os.path.join(data_dir, "Phoenix_results.csv")
SJ_file = os.path.join(data_dir, "SJ_results.csv")
SD_file = os.path.join(data_dir, "SD_results.csv")
SF_file = os.path.join(data_dir, "SF_results.csv")
Charlotte_file = os.path.join(data_dir, "Charlotte.csv")
NYC_file = os.path.join(data_dir, "SF_results.csv")
LA_file = os.path.join(data_dir, "Los Angeles.csv")
Indianapolis_file = os.path.join(data_dir, "Indianapolis.csv")

data_files = [PHX_file, SJ_file, SD_file, SF_file]
for file in data_files:
    df = pd.read_csv(file)
    parking_data = pd.concat([parking_data, df], ignore_index=True)

parking_data.to_csv(OUTPUT_PATH, index=False)

city_counts = parking_data["City"].value_counts()
city_counts.plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Number of parking meters/kiosks')
plt.title('Number of parking meters/kiosks by city')
save_path = os.path.join


# import CSV
# import os
# from SJ import load_SJ_Parking and cut_data and tranform_data and rename_data
# from SD import load_SD_Parking and cut_data and tranform_data and rename_data
# from SF import load_SF_Parking and cut_data and tranform_data and rename_data
# from PHX import load_PHX_Parking and cut_data and tranform_data and rename_data
# from nyc import load_NYC_parking and remove_data and calculate_average
# from charlotte import load_charlotte_parking and remove_data
# from indianapolis import indy_parking_data and narrow_down_data and transform_data and proper_names
# from la import LA_parking_data and narrow_down_data and transform_data and convert_average_rate_to_float and proper_names

# BASE_DIR = "artifacts"
# CSV_PATH = os.path.join(BASE_DIR, "results.csv")




# def load_SJ()
#     """Loads in SJ data"""
#     SJ_data = load_SJ_parking()
#     cut_data = remove_data(SJ_data)
#     transform_data = transform_data(cut_data)
#     SJ_data = rename_data(transform_data)

# def load_PHX()
#     """Loads in PHX data"""
#     PHX_data = load_SD_parking()
#     cut_data = remove_data(SD_data)
#     transform_data = transform_data(cut_data)
#     PHX_data = rename_data(transform_data)

# def load_SF()
#     """Loads in SF data"""
#     SF_data = load_SD_parking()
#     cut_data = remove_data(SD_data)
#     transform_data = transform_data(cut_data)
#     SF_data = rename_data(transform_data)

# def load_SD()
#     """Loads in SD data"""
#     SD_data = load_SD_parking()
#     cut_data = remove_data(SD_data)
#     transform_data = transform_data(cut_data)
#     SD_data = rename_data(transform_data)
# def load_nyc()
#     """Loads NYC data"""
#     NYC_data = load_NYC_parking()
#     cut_data = remove_data(NYC_data)
#     NYC_data = calculate_average(cut_data)
# def load_Charlotte()
#     """Loads Charlotte data"""
#     Charlotte_data = load_charlotte_parking()
#     Charlotee_data = remove_data(Charlotte_data)
# def load_Indianapolis()
#     """Loads Indianapolis data"""
#     parking_data = indy_parking_data()
#     narrowed_data = narrow_down_data(parking_data)
#     transformed_data = transform_data(narrowed_data)
#     Indianapolis_data = proper_names(transformed_data)
# def load_LA()
#     """Loads in LA data"""
#     parking_data = LA_parking_data()
#     narrowed_data = narrow_down_data(parking_data)
#     transformed_data = transform_data(narrowed_data)
#     converted_data = convert_average_rate_to_float(transformed_data)
#     LA_data = proper_names(converted_data)


# def sort_data(combined_data)
#     """Sorts data by cities"""
#     city_sort = sorted(data, key=lambda x: x["City"])
#     final_data = city_sort
#     return final data

# def write_data_to_CSV(final_data, path)
#     """Writes data to a CSV"""
#     fieldname = ["City", "Street Address", "Rate"]
#     with open(path, 'w+') as file:
#         dict_writer = csv.DictWriter(f = file, fieldnames = fieldname)
#         dict_writer.writeheader()
#         dict_writer.writerows(data)
#     return

# if __name__ == "__main__":
#     SJ_data = load_SJ()
#     PHX_data = load_PHX()
#     SF_data = load_SF()
#     SD_data = load_SD()
#     NYC_data = load_nyc()
#     Charlotte_data = load_Charlotte()
#     Indianapolis_data = load_Indianapolis()
#     LA_data = load_LA()
#     combined_data = SJ_data + SF_data + PHX_data + SD_data + Charlotte_data + NYC_data + Indianapolis_data + LA_data
#     final_data = sort_data(combined_data)
#     write_data_to_CSV(final_data, CSV_PATH)
>>>>>>> dae47433ce36bcfba1fa2fa792264961a69dd9eb
