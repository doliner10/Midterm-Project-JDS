import csv
import os
import re

INPUT_DIR = os.path.join("file")
INDY_PATH = os.path.join(INPUT_DIR, "Indianapolis Parking Info.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Indianapolis")

def indy_parking_data():
    parking_dicts = list()
    with open(INDY_PATH, "r") as file:
     reader = csv.DictReader(file)
     for row in reader:
        parking_dicts.append(row)
    return parking_dicts

#def remove_data(parking_dicts):
#   "Cutting down data leaving only relevant columns"
#    # omit_columns = ["X", "Y", "OBJECTID", "PRE_DIR", "STREET_NAME", "ADDRESS_BLOCK", "SUFFIX", "SUF_DIR", "METER_NUMBER", "SPACE_NUMBER", "SPACE_TYPE", "INSTALL_DATE", "RATE_INCREASE_DATE",  "ZONE_NAME", "OP_HOURS", "OP_DAYS", "PAY_TYPE"]
#    for park_dict in parking_dicts:
#        del park_dict["X"]
#        del park_dict["Y"]
#       del park_dict["OBJECTID"]
#        del park_dict["PRE_DIR"]
#        del park_dict["STREET_NAME"]
#        del park_dict["ADDRESS_BLOCK"]
#        del park_dict["SUFFIX"]
#        del park_dict["SUF_DIR"]
#        del park_dict["METER_NUMBER"]
#        del park_dict["SPACE_NUMBER"]
#        del park_dict["SPACE_TYPE"]
#        del park_dict["INSTALL_DATE"]
#        del park_dict["RATE_INCREASE_DATE"]
#        del park_dict["ZONE_NAME"]
#        del park_dict["OP_HOURS"]
#        del park_dict["OP_DAYS"]
#        del park_dict["PAY_TYPE"]
 #   relevant_data = parking_dicts
 #   return relevant_data

### another possible approoach

def narrow_down_data(parking_dicts):
    # Define the columns to keep (relevant columns)
    relevant_columns = ["FULL_ADDRESS", "HOURLY_RATE"]  
    
    relevant_data = []
    for park_dict in parking_dicts:
        relevant_entry = {col: park_dict[col] for col in relevant_columns if col in park_dict}
        relevant_data.append(relevant_entry)
    
    return relevant_data

def transform_data(relevant_data):
    "Transforming Rate Time data into average rates"
    for cut_dict in relevant_data:
        rate = "Average Rate"
        if cut_dict["HOURLY_RATE"] == "1.5" or "1.50":
            cut_dict[rate] =  "$1.50"
        if cut_dict["HOURLY_RATE"] == "1" or "1.0":
            cut_dict[rate] = "$1.00"
    for cut_dict in relevant_data:
        del cut_dict["HOURLY_RATE"]
    transform_data = relevant_data
    return transform_data

def proper_names(transform_data):
    """Creates new keys with proper names for remaining data and adds city key-value"""
    for data in transform_data:
        data["City"] = "Indianapolis"
        if "FULL_ADDRESS" in data:
            data["FULL_ADDRESS"] = data["FULL_ADDRESS"]
            del data["FULL_ADDRESS"]
    return transform_data

if __name__ == "__main__":
    parking_data = indy_parking_data()
    narrowed_data = narrow_down_data(parking_data)
    transformed_data = transform_data(narrowed_data)
    modified_data = proper_names(transformed_data)

    print(modified_data)
