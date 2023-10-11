import csv
csv.field_size_limit(100000000000000)
import os
import re

INPUT_DIR = os.path.join("../file")
NYC_PATH = os.path.join(INPUT_DIR, "New York Parking Rate.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "NYC")

def load_NYC_parking():
    """"Loads the CSV of NYC parking data as a list of dictionaries"""
    parking_dicts = list()
    with open(NYC_PATH, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            parking_dicts.append(row)
    return parking_dicts

def nyc_remove_data(parking_dicts):
    """""create a new dictionary"""
    cleaned_dict = list()
    for park_dict in parking_dicts:
        new_dict = {"Street Address": park_dict["On_Street"], "Rate": park_dict["All_Vehi_2"], "City": "New York City"}
        cleaned_dict.append(new_dict)
    cut_data = cleaned_dict
    return cut_data

def nyc_calculate_average(cut_data):
    """"calculate average parking rate"""
    for cut_dict in cut_data:
        rate = "Average Rate"
        if cut_dict["Rate"] == "$1.25 1st Hour / $2.00 2nd Hour":
            cut_dict[rate] = float(1.625)
        if cut_dict["Rate"] == "$1.25 1st Hour / $2.00 2nd Hour (Monday - Thursday) / $1.25 Per Hour (Friday)":
            cut_dict[rate] = float(1.4375)
        if cut_dict["Rate"] == "$1.25 Per Hour":
            cut_dict[rate] = float(1.25)
        if cut_dict["Rate"] == "$1.50 1st Hour / $2.50 2nd Hour":
            cut_dict[rate] = float(2.00)
        if cut_dict["Rate"] == "$1.50 1st Hour / $2.50 2nd Hour (Monday - Thursday) / $1.50 Per Hour (Friday)":
            cut_dict[rate] = float(1.75)
        if cut_dict["Rate"] == "$1.50 1st Hour / $2.50 2nd Hour / $3.00 3rd Hour":
            cut_dict[rate] = float(2.33)
        if cut_dict["Rate"] == "$1.50 Per Hour":
            cut_dict[rate] = float(1.50)
        if cut_dict["Rate"] == "$2.00 1st Hour / $4.00 2nd Hour":
            cut_dict[rate] = float(3.00)
        if cut_dict["Rate"] == "$2.00 Per Hour":
            cut_dict[rate] = float(2.00)
        if cut_dict["Rate"] == "$2.50 1st Hour / $4.00 2nd Hour":
            cut_dict[rate] = float(3.25)
        if cut_dict["Rate"] == "$2.50 Per Hour":
            cut_dict[rate] = float(3.25)
        if cut_dict["Rate"] == "$3.00 1st Hour / $3.00 2nd Hour / $2.00 Per Additional Hour":
            cut_dict[rate] = float(2.33)
        if cut_dict["Rate"] == "$4.00 1st Hour / $6.75 2nd Hour":
            cut_dict[rate] = float(5.375)
        if cut_dict["Rate"] == "$4.00 Per Hour":
            cut_dict[rate] = float(4.00)
        if cut_dict["Rate"] == "$4.50 1st Hour / $7.50 2nd Hour":
            cut_dict[rate] = float(6.00)
        if cut_dict["Rate"] == "$4.50 1st Hour / $7.50 2nd Hour (Before 6pm) / $4.50 Per Hour (After 6pm)":
            cut_dict[rate] = float(5.25)
        if cut_dict["Rate"] == "$4.50 Per Hour":
            cut_dict[rate] = float(4.50)
        if cut_dict["Rate"] == "N/A":
            cut_dict[rate] = float(0)
    for cut_dict in cut_data:
        del cut_dict["Rate"]
    calculate_average = cut_data
    return calculate_average

if __name__ == "__main__":

    NYC_data = load_NYC_parking()
    cut_data = nyc_remove_data(NYC_data)
    transform_data = nyc_calculate_average(cut_data)
    print(transform_data)