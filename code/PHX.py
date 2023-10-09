import csv 
import os
import re

INPUT_DIR = os.path.join("file")
PHX_PATH = os.path.join(INPUT_DIR, "'Phoenix Parking Data.csv'")
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
    unneeded_data = ["X", "Y", "OBJECTID", "METER_NUMBER", "METER_TYPE", "STATUS", "HC_METER", "BIKERACK", "DUAL_HEAD", "COMMENTS" "strSegmentID", "GlobalID"]
    for park_dict in parking_dicts:
        for data in unneeded_data:
            if data in park_dict:
                del parking_dict[data]
    cut_data = parking_dicts
    return cut_data

def transform_data(cut_data)
"""Transforms RateTime values to cash value"""
for data in cut_data:
    