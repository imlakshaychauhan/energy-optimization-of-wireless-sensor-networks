import numpy as np
import csv

def read_positions_from_file():
    # Read the data from the file
    file_name = "positions_data.csv"  # Replace with your file name
    data = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip headers
        for row in reader:
            data.append(list(map(float, row)))  # Convert strings to floats

    # Convert the read data into a NumPy array
    Positions = np.array(data)
    return Positions


Positions = read_positions_from_file()
print(Positions)
