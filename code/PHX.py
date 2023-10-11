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

def remove_data(parking_dicts):
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

def transform_data(cut_data):
    """Transforms RateTime values to average rate in $ per hour and returns the most common max time limit for each spot"""
    for cut_dict in cut_data:
        rate = "Rate"
        if "$1.00" in cut_dict["RateTimeLimits"]: #== "$1.00/hr 1hr 8A-10P Mon-Fri" or "$1.00/hr 2hr 8A-10P Mon-Fri" or "$1.00/hr 2hr 8A-10P Mon-Fri" or "$1.00/hr 30min 8A-10P Mon-Fri" or "$1.00/hr 4hr 8A-10P Mon-Fri" or "$1.00/hr 8hr 8A-10P Mon-Fri":
            cut_dict[rate] =  float(1.00)
        if cut_dict["RateTimeLimits"] == "$1.50/hr 15min max 8A-10P Mon-Sun" or "$1.50/hr 15min max 8A-5P M-F" or "$1.50/hr 1hr 8A-5P, 4HR 5P-10P" or "$1.50/hr 1hr max 8A-10P Mon-Sun" or "$1.50/hr 1hr max 8A-5P M-F" or "$1.50/hr 1hr Max 8A-5P Mon-Friday, 2hr Max 5P-10P Mon-Friday 2hr Max Sat & Sun" or "$1.50/hr 1hr Max 8A-5P Mon-Friday, 2hr Max 5P-10P Mon-Friday 2hr Max Sat & Sun-ADA" or "$1.50/hr 2hr 8A-5P, 4HR 5P-10P" or "$1.50/hr 2hr max 8A-10P Mon-Sun" or "$1.50/hr 30min 8A-5P, 4HR 5P-10P" or "$1.50/hr 30min max 8A-10P Mon-Su" or "$1.50/hr 30min max 8A-5P M-F" or "$1.50/hr 4hr max 8A-10P Mon-Sun" or "$1.50/hr 4hr max 8A-10P Mon-Sun PBP" or "$1.50/hr 4hr max 8A-10P Mon-Sun-ADA" or "$1.50/hr 4hr max 8A-5P M-F" or "$1.50/hr 4hr max 8A-5P M-F-ADA" or "$1.50/hr 5hr max 8A-10P Mon-Sun" or "$1.50/hr 5hr max 8A-10P Mon-Sun-ADA" or "$1.50/hr 8hr max 8A-5P M-F" or "ASU $1.50/hr 1hr 8A-4P Mon-Thur, 8a-10p Fri-Sun & 6hr 4P-10P Mon-Thur" or "ASU $1.50/hr 2hr Max 8A-4P Mon-Thur, 8A-10P Fri-Sun & 6hr Max 4P-10P Mon-Thur":
            cut_dict[rate] = float(1.50)
        if cut_dict["RateTimeLimits"] ==  "2hr" or "Copy of 8859 - M5+" or "Loading Zone 2hr Max" or "Loading Zone 4hr Max":
            cut_dict[rate] = float(0.00)
        # if cut_dict["RateTimeLimits"] ==  "":
        #     cut_dict[rate] = float(0.00)

    for cut_dict in cut_data:
        del cut_dict["RateTimeLimits"]
    transform_data = cut_data
    return transform_data

def proper_names(transform_data):
    """Creates new keys with proper names for remaining data and adds city key-value"""
    for data in transform_data:
        data["City"] = "Phoenix"
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
    cut_data = remove_data(PHX_data)
    transform_data = transform_data(cut_data)
    proper_names = proper_names(transform_data)
    #rename_data = rename_data(proper_names)
    write_data_to_CSV(proper_names, PHX_OUT)
    # PHX_data = rename_data
    

