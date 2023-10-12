import csv
import os
import re

INPUT_DIR = os.path.join("../file")
INDY_PATH = os.path.join(INPUT_DIR, "Indianapolis Parking Info.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_FILENAME = "Indianapolis.csv"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)

def indy_parking_data():
    parking_dicts = list()
    with open(INDY_PATH, "r") as file:
     reader = csv.DictReader(file)
     for row in reader:
        parking_dicts.append(row)
    return parking_dicts

def indy_narrow_down_data(parking_dicts):
    # Define the columns to keep (relevant columns)
    relevant_columns = ["FULL_ADDRESS", "HOURLY_RATE"]  
    
    relevant_data = []
    for park_dict in parking_dicts:
        relevant_entry = {col: park_dict[col] for col in relevant_columns if col in park_dict}
        relevant_data.append(relevant_entry)
    
    return relevant_data

def indy_transform_data(relevant_data):
    "Transforming Rate Time data into average rates"
    for cut_dict in relevant_data:
        rate = "Rate"
        if cut_dict["HOURLY_RATE"] == "1.5" or "1.50":
            cut_dict[rate] =  "1.50"
        if cut_dict["HOURLY_RATE"] == "1" or "1.0":
            cut_dict[rate] = "1.00"
    for cut_dict in relevant_data:
        del cut_dict["HOURLY_RATE"]
    transform_data = relevant_data
    return transform_data

def indy_proper_names(transform_data):
    """Creates new keys with proper names for remaining data and adds city key-value"""
    for data in transform_data:
        data["City"] = "Indianapolis"
        if "FULL_ADDRESS" in data:
            data["Street Address"] = data["FULL_ADDRESS"]
            del data["FULL_ADDRESS"]
    return transform_data

if __name__ == "__main__":
    parking_data = indy_parking_data()
    narrowed_data = indy_narrow_down_data(parking_data)
    transformed_data = indy_transform_data(narrowed_data)
    modified_data = indy_proper_names(transformed_data)


    new_csv_path = OUTPUT_PATH

    fieldnames = ["City", "Street Address", "Rate"]
# Write the modified_data to a new CSV file
    with open(new_csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(modified_data) 
