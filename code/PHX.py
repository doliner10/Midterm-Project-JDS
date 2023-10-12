import csv 
import os

INPUT_DIR = os.path.join("../file")
PHX_PATH = os.path.join(INPUT_DIR, "Phoenix Parking Data.csv")
OUTPUT_DIR = os.path.join("../artifacts")
PHX_OUT = os.path.join(OUTPUT_DIR, "Phoenix_results.csv")


def load_PHX_parking():
    """"Loads the CSV of Phoenix parking data as a list of dictionaries"""
    parking_dicts = list()
    with open(PHX_PATH, "r") as file:
     reader = csv.DictReader(file)
     for row in reader:
        parking_dicts.append(row)
    return parking_dicts

def PHX_remove_data(parking_dicts):
    """Removes unnecessary data from parking data"""
    for park_dict in parking_dicts:
        del park_dict["\ufeffX"]
        del park_dict["Y"]
        del park_dict["OBJECTID"]
        del park_dict["METER_NUMBER"]
        del park_dict["METER_TYPE"]
        del park_dict["Status"]
        del park_dict["HC_METER"]
        del park_dict["BIKERACK"]
        del park_dict["DUAL_HEAD"]
        del park_dict["COMMENTS"]
        del park_dict["GlobalID"]
        del park_dict["AssetID"]
        del park_dict["strSegmentID"]
        del park_dict["MOTORCYCLE_METER"]
    cut_data = parking_dicts
    return cut_data

def PHX_transform_data(cut_data):
    """Transforms RateTime values to average rate in $ per hour and returns the most common max time limit for each spot"""
    for cut_dict in cut_data:
        rate = "Rate"
        if "$" not in cut_dict["RateTimeLimits"]: 
            cut_dict[rate] = float(0.00)
        if "$1.00/hr" in cut_dict["RateTimeLimits"]: 

            cut_dict[rate] =  float(1.00)
        if "$1.50/hr" in cut_dict["RateTimeLimits"]: 
            cut_dict[rate] = float(1.50)
    for cut_dict in cut_data:
        del cut_dict["RateTimeLimits"]
    transform_data = cut_data
    return transform_data

def PHX_proper_names(transform_data):
    """Creates new keys with proper names for remaining data and adds city key-value"""
    for data in transform_data:
        data["City"] = "PHX"
        if "StreetAddress" in data:
            data["Street Address"] = data["StreetAddress"]
            del data["StreetAddress"]
    proper_data = transform_data
    return proper_data


# def rename_data(proper_data):
#     """Renames data to city data"""
#     PHX_data = proper_data
#     return PHX_data
def write_data_to_CSV(final_data, path):
    """Writes data to a CSV"""
    fieldname = ["City", "Street Address", "Rate"]
    with open(path, 'w+') as file:
        dict_writer = csv.DictWriter(f = file, fieldnames = fieldname)
        dict_writer.writeheader()
        dict_writer.writerows(final_data)
    return

if __name__ == "__main__":

    PHX_data = load_PHX_parking()
    cut_data = PHX_remove_data(PHX_data)
    transform_data = PHX_transform_data(cut_data)
    proper_names = PHX_proper_names(transform_data)
    #rename_data = rename_data(proper_names)
    write_data_to_CSV(proper_names, PHX_OUT)
    # PHX_data = rename_data
 

