import pandas as pd
import os
import matplotlib.pyplot as plt


data_dir = os.path.join("../artifacts")
pop_dir = os.path.join("../file")
pop_file = os.path.join(pop_dir, "Census Bureau 2022 Pop Estimates.csv")
OUTPUT_PATH = os.path.join(data_dir, "combined_results.csv")
PHX_file = os.path.join(data_dir, "Phoenix_results.csv")
SJ_file = os.path.join(data_dir, "SJ_results.csv")
SF_file = os.path.join(data_dir, "SF_results.csv")
Charlotte_file = os.path.join(data_dir, "Charlotte.csv")
NYC_file = os.path.join(data_dir, "NYC.csv")
LA_file = os.path.join(data_dir, "Los Angeles.csv")
Indianapolis_file = os.path.join(data_dir, "Indianapolis.csv")
figure_path = os.path.join("../analysis")

parking_data = pd.DataFrame()
def combine_data():
    """Combines all CSVs into a single file"""
    parking_data = pd.DataFrame()
    data_files = [PHX_file, SJ_file, SF_file, Charlotte_file, NYC_file, LA_file, Indianapolis_file]
    for file in data_files:
        df = pd.read_csv(file)
        parking_data = pd.concat([parking_data, df], ignore_index=True)
    parking_data.to_csv(OUTPUT_PATH, index=False)
    return parking_data

def results_analysis(df):
    """Analyses results and returns the count of kiosks/meters in each city and average parking rate"""
    city = df.groupby('City')
    count_city = city["City"].count()
    rate_city = city["Rate"].mean()
    analysisdf = pd.DataFrame({"City": count_city.index, "City Count":count_city.values, "Avg Rate": rate_city.values})
    analysisdf.to_csv(os.path.join(figure_path, "analysis.csv"))
    return analysisdf

def make_city_bar(df):
    """Makes bar graph of count of kiosks/meters by city and average rate by city"""
    df.plot.bar(x = "City", y = "City Count", title = "Parking meter/kiosk count by city")
    plt.xlabel("City")
    plt.ylabel("Meter Count")
    plt.savefig(os.path.join(figure_path, "count_graph.png"))
    plt.xticks(rotation=45)
def make_avg_bar(df):
    df.plot.bar(x = "City", y = "Avg Rate", title = "Average parking meter rate by city")
    plt.xlabel("City")
    plt.ylabel("Avg Rate (in $/hr)")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(figure_path, "rate_graph.png"))
def mak_pop_df(path):
    """"Makes pop data into a dataframe"""
    popdf = pd.read_csv(path)
    return popdf
def merge_
if __name__ == "__main__":
    parking_data = combine_data()
    analysisdf = results_analysis(parking_data)
    make_city_bar(analysisdf)
    make_avg_bar(analysisdf)
