import csv
import os
import re

INPUT_DIR = os.path.join("file")
LA_PATH = os.path.join(INPUT_DIR, "LA Parking Info.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Los Angeles")

def LA_parking_data():
    parking_dicts = list()
    with open(LA_PATH, "r") as file:
     reader = csv.DictReader(file)
     for row in reader:
        parking_dicts.append(row)
    return parking_dicts

def narrow_down_data(parking_dicts):
    # Define the columns to keep (relevant columns)
    relevant_columns = ["BlockFace", "RateType", "RateRange"]  
    
    relevant_data = []
    for park_dict in parking_dicts:
        relevant_entry = {col: park_dict[col] for col in relevant_columns if col in park_dict}
        relevant_data.append(relevant_entry)
    
    return relevant_data

def transform_data(relevant_data):
    "Transforming Rate Time data into average rates"
    for cut_dict in relevant_data:
        rate = "Average Rate"
        if cut_dict["RateType"] == "Flat":
            cut_dict[rate] =  cut_dict["RateRange"]
        if cut_dict["RateType"] == "TOD" and '-' in cut_dict["RateRange"]:
            parts = cut_dict["RateRange"].split('-')
            if len(parts) == 2:
                start_rate = parts[0].strip('$').strip()
                end_rate = parts[1].strip('$').strip()
                average_rate = f"${(float(start_rate.strip('$')) + float(end_rate.strip('$'))) / 2.0:.2f}"
                cut_dict[rate] = average_rate
        if cut_dict["RateType"] == "TOD" and '-' not in cut_dict["RateRange"]:
            cut_dict[rate] = cut_dict["RateRange"]
        if cut_dict["RateType"] == "JUMP":
            continue
        del cut_dict["RateType"]
        del cut_dict["RateRange"]
    transform_data = relevant_data
    return transform_data

def proper_names(transform_data):
    """Creates new keys with proper names for remaining data and adds city key-value"""
    for data in transform_data:
        data["City"] = "Los Angeles"
        if "BlockFace" in data:
            data["Street Address"] = data["BlockFace"]
            del data["BlockFace"]
    return transform_data

if __name__ == "__main__":
    parking_data = LA_parking_data()
    narrowed_data = narrow_down_data(parking_data)
    transformed_data = transform_data(narrowed_data)
    modified_data = proper_names(transformed_data)

    print(modified_data)