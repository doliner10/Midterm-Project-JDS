import csv 
import os
import re

INPUT_DIR = os.path.join("../file")
SF_PATH = os.path.join(INPUT_DIR, "SF Data.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "SF")

def load_SF_parking():
    """"Loads the CSV of SF parking data as a list of dictionaries"""
    parking_dicts = list()
    with open(SF_PATH, "r") as file:
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
        new_dict = {"Street Address": park_dict["STREET_NUM"] +" " + park_dict["STREET_NAME"], "RATE AREA": park_dict["OLD_RATE_AREA"], "City": "San Francisco"}
        cleaned_dict.append(new_dict)
        # del park_dict["OBJECTID"]
        # del park_dict["PARKING_SPACE_ID"]
        # del park_dict["MS_PAY_STATION_ID"]
        # del park_dict["ON_OFFSTREET_TYPE"]
        # del park_dict["SENSOR_FLAG"]
        # del park_dict["OSP_ID"]
        # del park_dict["PM_DISTRICT_ID"]
        # del park_dict["BLOCKFACE_ID"]
        # del park_dict["ACTIVE_METER_FLAG"]
        # del park_dict["REASON_CODE"]
        # del park_dict["SMART_METER_FLAG"]
        # del park_dict["METER_TYPE"]
        # del park_dict["strSegmentID"]
        # del park_dict["MOTORCYCLE_METER"]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # del park_dict[""]
        # for data in unneeded_data:
        #     if data in parking_dicts:
        #         del parking_dicts[data]
    cut_data = cleaned_dict
    return cut_data

def transform_data(cut_data):
    """Transforms RateTime values to average rate in $ per hour"""
    for cut_dict in cut_data:
        rate = "Average Rate"
        if cut_dict["RATE AREA"] == "-":
            cut_dict[rate] =  "$0"
        if cut_dict["RATE AREA"] == "Area 1":
            cut_dict[rate] = "$3.50"
        if cut_dict["RATE AREA"] ==  "Area 2":
            cut_dict[rate] = "$3.00"
        if cut_dict["RATE AREA"] ==  "Area 3":
            cut_dict[rate] = "$2.00"
        if cut_dict["RATE AREA"] ==  "Area 4":
            cut_dict[rate] = "$3.12"
            #For this one, the data listed an Area 4, but the key provided at the website only listed an area 5. Since an area 5 is not included in the spreadsheet, I'm going to assume that is a typo and it should be area 4. Also, this region has variable pricing, so I took the middle of the high and low prices, 0.25 and 6.00 as the average rate for this zone
        if cut_dict["RATE AREA"] ==  "MC1":
            cut_dict[rate] = "$0.70"
        if cut_dict["RATE AREA"] ==  "MC2":
            cut_dict[rate] = "$0.60"
        if cut_dict["RATE AREA"] ==  "MC3":
            cut_dict[rate] = "$0.40"
        if cut_dict["RATE AREA"] ==  "MC4":
            cut_dict[rate] = "$3.12"
            #Similar to Area 4, the key provided by at data.sfgov listed an area 5 that does not show up in the CSV, so I'm assuming they're referring to area 4 in the CSV. Also, pricing was variable between 0.25 and 6.00, so I'm going to take the middle of the 2, $3.12
        if cut_dict["RATE AREA"] ==  "Port 1":
            cut_dict[rate] = "$2.50"
        if cut_dict["RATE AREA"] ==  "Port 2":
            cut_dict[rate] = "$2.50"
        if cut_dict["RATE AREA"] ==  "Port 3":
            cut_dict[rate] = "$2.00"
        if cut_dict["RATE AREA"] ==  "Port 4":
            cut_dict[rate] = "$2.00"
        if cut_dict["RATE AREA"] ==  "Port 5":
            cut_dict[rate] = "$3.00"
        if cut_dict["RATE AREA"] ==  "Port 6":
            cut_dict[rate] = "$3.00"
        if cut_dict["RATE AREA"] ==  "Port 7":
            cut_dict[rate] = "$3.00"
        if cut_dict["RATE AREA"] ==  "Port 8":
            cut_dict[rate] = "$3.00"
        if cut_dict["RATE AREA"] ==  "Port 9":
            cut_dict[rate] = "$1.00"
        if cut_dict["RATE AREA"] ==  "Port 10":
            cut_dict[rate] = "$1.00"
        if cut_dict["RATE AREA"] ==  "Port 11":
            cut_dict[rate] = "$1.00"
        if cut_dict["RATE AREA"] ==  "Port 12":
            cut_dict[rate] = "$1.00"
        if cut_dict["RATE AREA"] ==  "PortMC1":
            cut_dict[rate] = "$0.25"
        if cut_dict["RATE AREA"] ==  "PortMC2":
            cut_dict[rate] = "$0.50"
        #Excluded tour bus rates since we're focusing on noncommercial parking rates for now
    for cut_dict in cut_data:
        del cut_dict["RATE AREA"]
    transform_data = cut_data
    return print(transform_data)

# def proper_names(transform_data):
#     """Creates new keys with proper names for remaining data and adds city key-value"""
#     for data in transform_data:
#         data["City"] = "Phoenix"
#         if "StreetAddress" in data:
#             data["Street Address"] = data["StreetAddress"]
#             del data["StreetAddress"]
#     proper_data = transform_data
#     return print(transform_data)

if __name__ == "__main__":

    SF_data = load_SF_parking()
    cut_data = remove_data(SF_data)
    transform_data = transform_data(cut_data)
    #proper_names(transform_data)