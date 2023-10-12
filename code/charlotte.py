import csv
import os
import re

INPUT_DIR = os.path.join("../file")
Charlotte_PATH = os.path.join(INPUT_DIR, "Parking_Meters_Charlotte.csv")
OUTPUT_DIR = "../artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "Charlotte.csv")

def load_Charlotte_parking():
    """"Loads the CSV of Charlotte parking data as a list of dictionaries"""
    parking_dicts = list()
    with open(Charlotte_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            parking_dicts.append(row)
    return parking_dicts


def remove_data(parking_dicts):
    """""create a new dictionary"""
    cleaned_dict = list()
    for park_dict in parking_dicts:
        new_dict = {"Street Address": park_dict["WHOLESTNAME"], "Rate": float(1.25), "City": "Charlotte"}
        cleaned_dict.append(new_dict)
    return cleaned_dict

def charlotte_write_data_to_CSV(charlotte_remove_data, OUTPUT_PATH):
     """Writes data to a CSV"""
     fieldname = ["City", "Street Address", "Rate"]
     with open(OUTPUT_PATH, 'w+', newline='') as file:
         dict_writer = csv.DictWriter(f = file, fieldnames = fieldname)
         dict_writer.writeheader()
         dict_writer.writerows(charlotte_remove_data)

if __name__ == "__main__":

    Charlotte_data = load_Charlotte_parking()
    cut_data = remove_data(Charlotte_data)
    charlotte_write_data_to_CSV(cut_data, OUTPUT_PATH)