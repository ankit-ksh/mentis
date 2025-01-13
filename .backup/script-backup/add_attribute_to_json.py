import json
import sys

def add_number_of_weeks(json_file):
    try:
        # Load the existing JSON data
        with open(json_file, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file: {e}")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Iterate through each level and each course to add the 'number_of_weeks' attribute
    for level, courses in data.items():
        for course in courses:
            # Add 'number_of_weeks' attribute. You can set the value manually or compute it.
            # Here, I'll set it to a default value of 12 for all courses as an example.
            course['number_of_weeks'] = 12  # Adjust this number as needed

    # Save the updated data back to the JSON file
    try:
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Updated JSON file with 'number_of_weeks' attribute.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# Check if a filename argument is passed
if len(sys.argv) != 2:
    print("Usage: python script_name.py <json_file>")
else:
    json_file = sys.argv[1]  # Get the JSON file path from command line argument
    add_number_of_weeks(json_file)
