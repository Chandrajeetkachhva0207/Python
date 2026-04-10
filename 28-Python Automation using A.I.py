#28-Python Automation using A.I
import pandas as pd
import os

# Ask user for folder path
folder_path = input("Enter folder path containing CSV files: ").strip()

# Check if folder exists
if not os.path.exists(folder_path):
    print("❌ Invalid folder path")
else:
    # Get all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

    if not csv_files:
        print("❌ No CSV files found in the folder")
    else:
        # Output Excel file path
        output_file = os.path.join(folder_path, "All_CSV_Converted_Into_Sheets.xlsx")

        # Create Excel writer
        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
            
            for file in csv_files:
                file_path = os.path.join(folder_path, file)
                
                # Read CSV
                df = pd.read_csv(file_path)
                
                # Sheet name = file name without extension
                sheet_name = os.path.splitext(file)[0]
                
                # Excel sheet name limit = 31 chars
                sheet_name = sheet_name[:31]
                
                # Write to Excel sheet
                df.to_excel(writer, sheet_name=sheet_name, index=False)

        print("✅ All CSV files converted successfully!")
        print(f"📁 Saved at: {output_file}")
