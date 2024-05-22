import pandas as pd

# csv_files = ['cmp_details.csv','cmp_details_2.csv','cmp_details_3.csv','cmp_details_4.csv','cmp_details_5.csv','cmp_details_6.csv','cmp_details_7.csv','cmp_details_8.csv','cmp_details_9.csv','cmp_details_10.csv','cmp_details_11.csv','cmp_details_12.csv','cmp_details_13.csv','cmp_details_14.csv','cmp_details_15.csv','cmp_details_16.csv','cmp_details_17.csv']  # Replace with your file paths
csv_files=['cmp_details_21.csv','cmp_details_22.csv']
all_dataframes = []
for filename in csv_files:
    df = pd.read_csv(filename)
    print(len(df))
    all_dataframes.append(df)
combined_df = pd.concat(all_dataframes, ignore_index=True, verify_integrity=True)
print('hi    ',len(combined_df))
combined_df.to_csv('combined_data_Remaining_final_New.csv', index=False)  # Adjust output filename and index option
