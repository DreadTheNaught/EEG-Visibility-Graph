import json
from tqdm import tqdm
import pandas as pd
import utility
import os

# Define the path to the folder
path = 'eeg_data_test/'

eeg_data_control = []
eeg_data_alcoholic = []

# Loop through the folder
for folder in os.listdir(path):
    if os.path.isdir(path + folder):
        for file in os.listdir(path + folder + '/'):
            with open(path + folder + '/' + file, 'r') as f:
                eeg_data_point = []
                for line in f:
                    # Split each line by whitespace
                    values = line.strip().split()
                    # Check if the line contains data
                    if line[0] != '#':
                        # Append the values to the data list
                        eeg_data_point.append([values[0], values[1], int(
                            values[2]), float(values[3])])
            if folder[3] == 'c':
                eeg_data_control.append(eeg_data_point)
            elif folder[3] == 'a':
                eeg_data_alcoholic.append(eeg_data_point)



sensor_list = [
    "FP1", "FP2", "F7", "F8", "AF1", "AF2", "FZ", "F4", "F3", "FC6", "FC5", "FC2", "FC1", "T8", "T7", "CZ", "C3", "C4", "CP5", "CP6", "CP1", "CP2", "P3", "P4", "PZ", "P8", "P7", "PO2", "PO1", "O2", "O1", "X", "AF7", "AF8", "F5", "F6", "FT7", "FT8", "FPZ", "FC4", "FC3", "C6", "C5", "F2", "F1", "TP8", "TP7", "AFZ", "CP3", "CP4", "P5", "P6", "C1", "C2", "PO7", "PO8", "FCZ", "POZ", "OZ", "P2", "P1", "CPZ", "Y"
]

sensor_dict = {}    

for sensor in sensor_list:
    sensor_dict[sensor] = {
        "control": [],
        "alcoholic": []
    }

for control_data, alcoholic_data in tqdm(zip(eeg_data_control, eeg_data_alcoholic), total=len(eeg_data_control), desc="Processing data", unit="data"):
    for sensor in tqdm(sensor_list, desc="Processing sensors", unit="sensor", leave=False):

        control_sensor_data = utility.get_sensor_values(control_data, sensor)
        alcoholic_sensor_data = utility.get_sensor_values(
            alcoholic_data, sensor)

        G_control = utility.visibility_graph(control_sensor_data)
        G_alcoholic = utility.visibility_graph(alcoholic_sensor_data)

        sensor_dict[sensor]["control"].append(utility.features(G_control))
        sensor_dict[sensor]["alcoholic"].append(utility.features(G_alcoholic))
        
# Define the file path
file_path = "sensor_data_test.json"

# Write sensor_dict to a JSON file
with open(file_path, "w") as file:
    json.dump(sensor_dict, file)
