import os
import pandas as pd
import time
from config import chunk_size, cur_path

# Set the current path where the files are located
file_path = cur_path + '/Data/'

# Specify the name of the newly created CSV file
csv_file_name = 'airline.csv'

# Define the path to the new CSV file
csv_file_path = os.path.join(file_path, csv_file_name)

# Specify the name of the filtered CSV file
filtered_csv_file_name = 'cleaned_data.csv'

# Define the path to the filtered CSV file
target_file = os.path.join(file_path, filtered_csv_file_name)

# Delete the target file if it already exists
if os.path.exists(target_file):
    os.remove(target_file)

# Read the CSV file in chunks using pandas
reader = pd.read_csv(csv_file_path, chunksize=chunk_size)

# Load airport codes
all_airport_codes = pd.read_csv('Projects/Tableau/Data/airport_codes.csv')

all_airport_codes['Longitude'] = all_airport_codes['location'].str.extract(r'POINT \((-?\d+\.\d+) \-?\d+\.\d+\)')
all_airport_codes['Latitude'] = all_airport_codes['location'].str.extract(r'POINT \(-?\d+\.\d+ (-?\d+\.\d+)\)')
# US rows only
us_codes = all_airport_codes.loc[all_airport_codes['country_id'] == 'US', ['code']]

# Load carrier codes
carrier_codes = pd.read_csv('Projects/Tableau/Data/carrier_codes.csv')

# Columns that to be removed
columns_to_remove = ['CRSArrTime', 'CRSElapsedTime', 'CRSDepTime', 'Month', 'DayofMonth', 'Year', 'ArrDelay', 'CancellationCode', 'CarrierDelay', 'DayOfWeek', 'DepDelay', 'Diverted', 'FlightNum', 'LateAircraftDelay', 'NASDelay', 'SecurityDelay', 'TailNum', 'TaxiIn', 'TaxiOut', 'WeatherDelay']

# New header for the csv file
new_header = ['Date', 'DepartureTime', 'ArrivalTime', 'AirTime', 'ActualElapsedTime', 'Distance', 'Origin', 'OriginState', 'OriginLongitude', 'OriginLatitude', 'Destination', 'DestinationState', 'DestinationLongitude', 'DestinationLatitude', 'UniqueCarrier', 'Cancelled']

# Specify the column name changes
column_name_changes = {
    'Dest': 'Destination',
    'DepTime': 'DepartureTime',
    'ArrTime': 'ArrivalTime',
}

# Runtime
start = time.time()

# Total Rows added
tot_rows = 0

# Iterate over each chunk and filter
for chunk in reader:
    
    # Filter years 1999-2003
    chunk = chunk[chunk['Year'] == 2001]

    # Rename columns
    chunk = chunk.rename(columns=column_name_changes)
    
    # Filter out any non us flight
    chunk = chunk[chunk['Origin'].isin(us_codes['code']) | chunk['Destination'].isin(us_codes['code'])]

    # Combine columns into a single date column
    chunk['Date'] = pd.to_datetime(chunk['Year'].astype(str) + '-' + chunk['Month'].astype(str).str.zfill(2) + '-' + chunk['DayofMonth'].astype(str).str.zfill(2))
    
    # Merge with us_codes to add origin information
    chunk = chunk.merge(all_airport_codes, left_on='Origin', right_on='code', how='left')
    chunk.rename(columns={'state': 'OriginState', 'Longitude': 'OriginLongitude', 'Latitude': 'OriginLatitude'}, inplace=True)
    
    # Merge with us_codes to add destination information
    chunk = chunk.merge(all_airport_codes, left_on='Destination', right_on='code', how='left')
    chunk.rename(columns={'state': 'DestinationState', 'Longitude': 'DestinationLongitude', 'Latitude': 'DestinationLatitude'}, inplace=True)
    
    # Merge with carrier codes to replace UniqueCarrier column
    chunk = chunk.merge(carrier_codes, left_on='UniqueCarrier', right_on='Code', how='left')
    chunk['UniqueCarrier'] = chunk['Description']
    chunk.drop(columns=['Code', 'Description'], inplace=True)
    
    # Convert time columns from HHMM format to datetime format
    time_columns = ['DepartureTime', 'ArrivalTime']
    for column in time_columns:
        chunk[column] = pd.to_datetime(chunk[column], format='%H%M', errors='coerce').dt.strftime('%H:%M')
    
    # Remove unwanted columns
    chunk = chunk.drop(columns=columns_to_remove)
    
    # Reorder columns
    chunk = chunk[new_header]
    
    tot_rows += len(chunk)
    
    # Write the filtered chunk to the filtered CSV file
    chunk.to_csv(target_file, mode='a', index=False, header=not os.path.exists(target_file))

print(f"Filtered CSV file saved as: {target_file} with {format(tot_rows, ',')} rows.")

# Runtime
print(f"Runtime:\nTotal Hours: {((time.time() - start) / 60 / 60):.2f}\nTotal Minutes: {((time.time() - start) / 60):.2f}\nTotal Seconds: {(time.time() - start):.2f}")

# Runtime:
# Total Hours: 0.11
# Total Minutes: 6.70
# Total Seconds: 402.26