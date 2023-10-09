import csv 
import os
import re

INPUT_DIR = os.path.join("../file")
SJ_PATH = os.path.join(INPUT_DIR, "San Jose Parking.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "SJ")

def load_SJ_parking():
    """"Loads the CSV of SJ parking data as a list of dictionaries"""
    parking_dicts = list()
    with open(SJ_PATH, "r") as file:
     reader = csv.DictReader(file)
     for row in reader:
        parking_dicts.append(row)
    return parking_dicts

def remove_data(parking_dicts):
    """Removes unnecessary data from parking data"""
    cleaned_dict = list()
    needed_data = ["OBJECTID", "STREET_NAME", "STREET_NUM", "OLD_RATE_AREA" ]
    #unneeded_data = ['\ufeffX', 'Y', 'OBJECTID', 'METER_NUMBER', 'METER_TYPE', 'STATUS', 'HC_METER', 'BIKERACK', 'DUAL_HEAD', 'COMMENTS', 'strSegmentID', 'GlobalID']
    for park_dict in parking_dicts:
        new_dict = {"Street Address": park_dict["METERADDRESS"], "Rate": park_dict["PARKINGRATE"], "City": "San Jose"}
        cleaned_dict.append(new_dict)
    cut_data = cleaned_dict
    return cut_data

def transform_data(cut_data):
    """Transforms RateTime values to average rate in $ per hour"""
    for cut_dict in cut_data:
        rate = "Average Rate"
        if cut_dict["Rate"] == "0":
            cut_dict[rate] =  "$0"
        if cut_dict["Rate"] == "2":
            cut_dict[rate] = "$2"
        #Excluded tour bus rates since we're focusing on noncommercial parking rates for now
    for cut_dict in cut_data:
        del cut_dict["Rate"]
    transform_data = cut_data
    return transform_data


if __name__ == "__main__":

    SJ_data = load_SJ_parking()
    cut_data = remove_data(SJ_data)
    transform_data = transform_data(cut_data)
    print(transform_data)