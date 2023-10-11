import csv 
import os

INPUT_DIR = os.path.join("../file")
SJ_PATH = os.path.join(INPUT_DIR, "San Jose Parking.csv")
OUTPUT_DIR = os.path.join("../artifacts")
SJ_OUT = os.path.join(OUTPUT_DIR, "SJ_results.csv")

def load_SJ_parking():
    """"Loads the CSV of SJ parking data as a list of dictionaries"""
    parking_dicts = list()
    with open(SJ_PATH, "r") as file:
     reader = csv.DictReader(file)
     for row in reader:
        parking_dicts.append(row)
    return parking_dicts

def SJ_remove_data(parking_dicts):
    """Removes unnecessary data from parking data"""
    cleaned_dict = list()
    for park_dict in parking_dicts:
        new_dict = {"Street Address": park_dict["METERADDRESS"], "Average_Rate": park_dict["PARKINGRATE"], "City": "San Jose"}
        cleaned_dict.append(new_dict)
    cut_data = cleaned_dict
    return cut_data

def SJ_transform_data(cut_data):
    """Transforms RateTime values to average rate in $ per hour"""
    for cut_dict in cut_data:
        rate = "Rate"
        if cut_dict["Average_Rate"] == "0":
            cut_dict[rate] =  float(0)
        if cut_dict["Average_Rate"] == "2":
            cut_dict[rate] = float(2)
    for cut_dict in cut_data:
        del cut_dict["Average_Rate"]
    transform_data = cut_data
    return transform_data

def write_data_to_CSV(final_data, path):
    """Writes data to a CSV"""
    fieldname = ["City", "Street Address", "Rate"]
    with open(path, 'w+') as file:
        dict_writer = csv.DictWriter(f = file, fieldnames = fieldname)
        dict_writer.writeheader()
        dict_writer.writerows(final_data)


if __name__ == "__main__":

    SJ_data = load_SJ_parking()
    cut_data = remove_data(SJ_data)
    transform_data = transform_data(cut_data)
    write_data_to_CSV(transform_data, SJ_OUT)
