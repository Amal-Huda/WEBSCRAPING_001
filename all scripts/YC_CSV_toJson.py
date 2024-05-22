import csv
import json

def csv_to_json(csv_file, json_file):
    # Open the CSV file for reading
    with open(csv_file, 'r',encoding='utf-8') as csvfile:
        # Read the CSV file into a dictionary
        reader = csv.DictReader(csvfile)
        # Create a list to hold the rows
        data = []
        founder_object=[]
        # Iterate over each row in the CSV file
        for row in reader:
            # Append the row to the list
            data.append(row)
    # Open the JSON file for writing
    with open(json_file, 'w',encoding='utf-8') as jsonfile:
        # Write the data to the JSON file
        json.dump(data, jsonfile, indent=4)
csv_to_json('combined_data_Remaining_final_New.csv','YCCompanyDetails_Output_New.json')
# csv_to_json('cmp_details_19.csv','Com.json')

