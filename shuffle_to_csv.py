import os
import pandas as pd
import time
from config import chunk_size, cur_path

# Set the current path where the files are located
file_path = cur_path + '/Data/'

# Get a list of all files in the current path
file_list = os.listdir(file_path)

# Runtime
start = time.time()

# Iterate over the files in the directory
for file_name in file_list:
    if file_name.endswith('.shuffle'):
        shuffle_file_path = os.path.join(file_path, file_name)
        csv_file_path = os.path.join(file_path, file_name.replace('.shuffle', ''))

        # Remove the existing CSV file if it exists
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)

        # Read the .shuffle file in chunks using pandas
        reader = pd.read_csv(shuffle_file_path, chunksize=chunk_size, encoding='iso8859-1')
        
        # Iterate over each chunk and append it to the new .csv file
        for chunk in reader:
            chunk.to_csv(csv_file_path, mode='a', index=False, header=not os.path.exists(csv_file_path), encoding='utf-8')

        # Remove the .shuffle file
        os.remove(shuffle_file_path)

        print(f"File converted and saved as: {csv_file_path}")

# Runtime
print(f"Runtime:\nTotal Hours: {((time.time() - start) / 60 / 60):.2f}\nTotal Minutes: {((time.time() - start) / 60):.2f}\nTotal Seconds: {(time.time() - start):.2f}")

# Runtime:
# Total Hours: 0.37
# Total Minutes: 22.10
# Total Seconds: 1326.20