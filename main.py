import os
import argparse
import shutil
from docx2pdf import convert

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

def copy_files(input_folder_path, temp_folder_path):
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".docx"):
            input_file_path = os.path.join(input_folder_path, filename)
            shutil.copy(input_file_path, temp_folder_path)

def convert_files(temp_folder_path, output_folder_path):
    try:
        convert(temp_folder_path, output_folder_path)
        print("Conversion completed successfully.")
    except Exception as e:
        print(f"Error during conversion: {e}")

def remove_temp_folder(temp_folder_path):
    try:
        shutil.rmtree(temp_folder_path)
        print(f"Removed temporary folder: {temp_folder_path}")
    except Exception as e:
        print(f"Error removing temporary folder: {e}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert .docx files to PDF')
    parser.add_argument('-i', '--input_folder', default='input', help='Path to the folder containing .docx files (default: input)')
    parser.add_argument('-o', '--output_folder', default='output', help='Path to the folder where PDFs will be saved (default: output)')
    args = parser.parse_args()
    
    # Create input and output folders if they don't exist
    create_folder(args.input_folder)
    create_folder(args.output_folder)

    # Create a temporary folder for grouping .docx files
    temp_folder_path = os.path.join(os.getcwd(), 'temp')
    
    try:
        # Create the temporary folder
        create_folder(temp_folder_path)
        
        # Copy all .docx files to the temporary folder
        copy_files(args.input_folder, temp_folder_path)
        
        # Convert all .docx files in the temporary folder to PDF
        convert_files(temp_folder_path, args.output_folder)
        
    except Exception as e:
        print(f"Error during processing: {e}")
        
    finally:
        # Remove the temporary folder after conversion is complete
        remove_temp_folder(temp_folder_path)

if __name__ == "__main__":
    main()