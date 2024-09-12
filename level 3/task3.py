# task 3

import os
import pandas as pd
from datetime import datetime

# Path to directory containing CSV files
input_folder = r"C:\Users\kuldip\OneDrive\Desktop\internship\python\level 3\csv"
output_folder = r"C:\Users\kuldip\OneDrive\Desktop\internship\python\level 3\csv"

def process_csv_files(input_folder):
    consolidated_data = pd.DataFrame()

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(input_folder, file_name)
            df = pd.read_csv(file_path)
            consolidated_data = pd.concat([consolidated_data, df])

    consolidated_data = consolidated_data.groupby(['date', 'region'], as_index=False)['sales'].sum()

    return consolidated_data


def save_report(consolidated_data, output_folder):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = os.path.join(output_folder, f"daily_report_{timestamp}.csv")

    consolidated_data.to_csv(output_file, index=False)
    print(f"Report saved as: {output_file}")


consolidated_data = process_csv_files(input_folder)
save_report(consolidated_data, output_folder)
