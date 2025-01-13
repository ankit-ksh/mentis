import json
import os
import sys

def get_file_size(file_path):
    """Returns the size of the file in bytes."""
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        print(f"Error getting file size: {e}")
        return -1

def minify_json(input_file, output_file):
    """Minifies the input JSON file and saves it to the output file."""
    try:
        # Load the JSON data
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # Minify by dumping the JSON with no indentation
        with open(output_file, 'w') as f:
            json.dump(data, f, separators=(',', ':'))
    except Exception as e:
        print(f"Error during JSON minification: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python minify_json.py <input_json_file>")
        sys.exit(1)

    input_json_file = sys.argv[1]
    
    if not os.path.isfile(input_json_file):
        print(f"The file {input_json_file} does not exist.")
        sys.exit(1)
    
    # Output file path for the minified JSON
    output_json_file = input_json_file.replace('.json', '.min.json')

    # Get the original size of the JSON file
    original_size = get_file_size(input_json_file)
    if original_size == -1:
        sys.exit(1)
    print(f"Original file size: {original_size / 1024:.2f} KB")

    # Minify the JSON file
    minify_json(input_json_file, output_json_file)
    
    # Get the size of the minified JSON file
    minified_size = get_file_size(output_json_file)
    if minified_size == -1:
        sys.exit(1)
    print(f"Minified file size: {minified_size / 1024:.2f} KB")
    
    # Optionally, send the file (if needed, e.g., upload or process further)
    print(f"Minified file saved as: {output_json_file}")

if __name__ == "__main__":
    main()
