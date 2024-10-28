import pandas as pd
import openpyxl

def save_data_to_excel(data):
    # Example dict
    table_result = []
    table_row = data

    table_result.append(table_row)
    print("table in python dict:")
    print(table_result)
    print("-------------------------------------------------------------------------------")
    col_names = ['Page_URL', 'Image_URL', 'Image_Name', 'Name', 'Desccription', 'Box_01', 'Urban', 'Meet_Team', 'Amenities','Amenities_html_tags', 'Development', 'New_Apartment_Sale', 'New_Villa_Sale', 'New_TownHouse_Sale', 'Project_Overview', 'Image_URL_bulk', 'Image_Name_bulk']
    new_df = pd.DataFrame(table_result, columns=col_names)
    print("table in pandas dataframe:")
    print(new_df)

    try:
        # Try to read the existing Excel file
        existing_df = pd.read_excel('place.xlsx')
        print("Existing data in Excel:")
        print(existing_df)
        
        # Append the new data
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        print("Combined data:")
        print(combined_df)
    except FileNotFoundError:
        # If the file does not exist, just use the new data
        combined_df = new_df
        print("Excel file not found. Creating a new one.")

    print("==================================================")
    print("Saving data to Excel:")
    combined_df.to_excel('place.xlsx', index=False, engine='openpyxl')
    print("Data saved to excel: place.xlsx")
