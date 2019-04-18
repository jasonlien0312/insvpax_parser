import csv
import pprint as pp
# CONSTANTS
FILENAME = "0416/still" # change file name here
HEADER = ['id', 'msg_type', 'port_addr', 'length', 'sequence', 'idle_time', 'time_status', 'gps_week', 'gps_week_seconds', 'receiver_status', 'reserved', 'software_version', 'ins_status', 'position_type', 'latitude', 'longitude', 'altitude', 'undulation', 'north_velocity', 'east_velocity', 'up_velocity' ,'roll', 'pitch', 'azimuth', 'latitude_std', 'longitude_std', 'altitude_std','north_velocity_std', 'east_velocity_std', 'up_velocity_std' ,'roll_std' ,'pitch_std' ,'azimuth_std' ,'extended_status' ,'seconds_since_update']

with open(FILENAME+'.txt','r') as f:
    lines = f.readlines() # read file
csv_list = [] # create an empty list
csv_list.append(HEADER) # append header
i = 0 # iterator
for i in range(0,len(lines)):
    row = [] # create an empty row
    if(lines[i][0:6]=='header'):
        for j in range(0,35): # process everything below "header:"
            first,second = lines[i+j+1].split(':') # split by ':'
            row.append(float(second[1:-1])) # getting only the value and put it into the row
        csv_list.append(row)
# write a csv file
with open(FILENAME+".csv", "w") as csv_flie:
    writer = csv.writer(csv_flie)
    writer.writerows(csv_list)