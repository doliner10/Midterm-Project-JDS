import csv 
import os

INPUT_DIR = os.path.join("../file")
SD_PATH = os.path.join(INPUT_DIR, "SD Parking Info.csv")

def load_SD_parking():
    """"Loads the CSV of SD parking data as a list of dictionaries"""
    parking_dicts = list()
    with open(SD_PATH, "r") as file:
     reader = csv.DictReader(file)
     for row in reader:
        parking_dicts.append(row)
    return parking_dicts

def SD_remove_data(parking_dicts):
    """Removes unnecessary data from parking data"""
    cleaned_dict = list()
    needed_data = ["OBJECTID", "STREET_NAME", "STREET_NUM", "OLD_RATE_AREA" ]
    for park_dict in parking_dicts:
        new_dict = {"Street Address": park_dict["sub_area"], "Rate Config": park_dict["config_name"], "City": "San Diego"}
        cleaned_dict.append(new_dict)
    cut_data = cleaned_dict
    return cut_data

def SD_transform_data(cut_data):
    """Transforms RateTime values to average rate in $ per hour"""
    for cut_dict in cut_data:
        rate = "Average Rate"
        if "$" not in cut_dict["Rate Config"]:
            cut_dict[rate] =  float(0)
        if "$1.25" in cut_dict["Rate Config"]:
            cut_dict[rate] = float(1.25)
        if "$1.00" in cut_dict["Rate Config"]:
            cut_dict[rate] = float(1.00)
        if "$0.50" in cut_dict["Rate Config"]:
            cut_dict[rate] = float(0.50)
        if "$0.75" in cut_dict["Rate Config"]:
            cut_dict[rate] = float(0.75)
        if "$125" in cut_dict["Rate Config"]:
            cut_dict[rate] = float(125)
    for cut_dict in cut_data:
        del cut_dict["Rate Config"]
    transform_data = cut_data
    return transform_data
def SD_rename_data(transform_data):
     """Renames data to city data"""
     SD_data = transform_data
     return SD_data


if __name__ == "__main__":

    SD_data = load_SD_parking()
    cut_data = SD_remove_data(SD_data)
    transform_data = SD_transform_data(cut_data)
    SD_data = SD_rename_data(transform_data)