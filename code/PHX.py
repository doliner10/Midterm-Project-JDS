import csv 
import os
import re

INPUT_DIR = os.path.join("../file")
PHX_PATH = os.path.join(INPUT_DIR, "Phoenix Parking Data.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Phoenix")

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
    #unneeded_data = ['\ufeffX', 'Y', 'OBJECTID', 'METER_NUMBER', 'METER_TYPE', 'STATUS', 'HC_METER', 'BIKERACK', 'DUAL_HEAD', 'COMMENTS', 'strSegmentID', 'GlobalID']
    for park_dict in parking_dicts:
        del park_dict["\ufeffX"]
        del park_dict["Y"]
        del park_dict["OBJECTID"]
        # for data in unneeded_data:
        #     if data in parking_dicts:
        #         del parking_dicts[data]
    cut_data = parking_dicts
    return cut_data

def transform_data(cut_data):
    """Transforms RateTime values to average rate in $ per hour"""
    for cut_dict in cut_data:
        rate = "Average Rate"
        if cut_dict["RateTimeLimits"] == "$1.00/hr 1hr 8A-10P Mon-Fri" or "$1.00/hr 2hr 8A-10P Mon-Fri" or "$1.00/hr 2hr 8A-10P Mon-Fri" or "$1.00/hr 30min 8A-10P Mon-Fri" or "$1.00/hr 4hr 8A-10P Mon-Fri" or "$1.00/hr 8hr 8A-10P Mon-Fri":
            cut_dict[rate] =  "$1.00"
        if cut_dict["RateTimeLimits"] == "$1.50/hr 15min max 8A-10P Mon-Sun" or "$1.50/hr 15min max 8A-5P M-F" or "$1.50/hr 1hr 8A-5P, 4HR 5P-10P" or "$1.50/hr 1hr max 8A-10P Mon-Sun" or "$1.50/hr 1hr max 8A-5P M-F" or "$1.50/hr 1hr Max 8A-5P Mon-Friday, 2hr Max 5P-10P Mon-Friday 2hr Max Sat & Sun" or "$1.50/hr 1hr Max 8A-5P Mon-Friday, 2hr Max 5P-10P Mon-Friday 2hr Max Sat & Sun-ADA" or "$1.50/hr 2hr 8A-5P, 4HR 5P-10P" or "$1.50/hr 2hr max 8A-10P Mon-Sun" or "$1.50/hr 30min 8A-5P, 4HR 5P-10P" or "$1.50/hr 30min max 8A-10P Mon-Su" or "$1.50/hr 30min max 8A-5P M-F" or "$1.50/hr 4hr max 8A-10P Mon-Sun" or "$1.50/hr 4hr max 8A-10P Mon-Sun PBP" or "$1.50/hr 4hr max 8A-10P Mon-Sun-ADA" or "$1.50/hr 4hr max 8A-5P M-F" or "$1.50/hr 4hr max 8A-5P M-F-ADA" or "$1.50/hr 5hr max 8A-10P Mon-Sun" or "$1.50/hr 5hr max 8A-10P Mon-Sun-ADA" or "$1.50/hr 8hr max 8A-5P M-F" or "ASU $1.50/hr 1hr 8A-4P Mon-Thur, 8a-10p Fri-Sun & 6hr 4P-10P Mon-Thur" or "ASU $1.50/hr 2hr Max 8A-4P Mon-Thur, 8A-10P Fri-Sun & 6hr Max 4P-10P Mon-Thur":
            cut_dict[rate] = "$1.50"
        if cut_dict["RateTimeLimits"] ==  "2hr" or "Copy of 8859 - M5+" or "Loading Zone 2hr Max" or "Loading Zone 4hr Max":
            cut_dict[rate] = "$0.00"
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
    return print(transform_data)

if __name__ == "__main__":

    PHX_data = load_PHX_parking()
    cut_data = remove_data(PHX_data)
    transform_data = transform_data(cut_data)
    proper_names(transform_data)

