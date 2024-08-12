# DOCX to PDF Converter

This script converts all `.docx` files in a specified input folder to PDF format and saves them in a specified output folder. It uses the `docx2pdf` library to perform the conversion.

## Requirements

- Python 3.x
- `docx2pdf` library

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies using pip:
   pip install -r requirements.txt

## Usage

1. Prepare an input folder containing the `.docx` files you want to convert.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:
   python main.py -i path/to/input/folder -o path/to/output/folder

   Replace `path/to/input/folder` with the path to your input folder containing the `.docx` files, and `path/to/output/folder` with the path to the desired output folder where the converted PDF files will be saved.

   If you don't provide the `-i` and `-o` arguments, the script will use the default folders `input` and `output` respectively, relative to the current directory.

4. The script will convert all `.docx` files found in the input folder to PDF format and save them in the output folder.

## Error Handling

The script includes error handling for the following scenarios:

- If the input or output folder doesn't exist, it will be created automatically.
- If an error occurs during the conversion process, an error message will be displayed.
- If an error occurs while removing the temporary folder, an error message will be displayed.

## Notes

- The script uses a temporary folder named `temp` in the current directory to group the `.docx` files before conversion. This folder is automatically created and removed by the script.
- The converted PDF files will have the same name as the original `.docx` files, with the `.docx` extension replaced by `.pdf`.
