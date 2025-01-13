import json
import os
import sys

def generate_navigation_pages(json_file):
    try:
        # Load the JSON data from the provided file
        with open(json_file, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

    # Check if the outer structure is a dictionary with levels as keys
    if isinstance(data, dict):
        level_courses = data
    else:
        print("Error: The JSON structure should be a dictionary with levels as keys.")
        sys.exit(1)

    # Create the 'navigation_files' directory if it doesn't exist
    output_dir = 'navigation_files'
    os.makedirs(output_dir, exist_ok=True)

    # Generate a YAML file for each level
    for level, courses in level_courses.items():
        # Start with the YAML front matter layout
        yaml_content = f"---\nlayout: home\n\nhero:\n  name: \"{level.capitalize()} level\"\n\n\nfeatures:\n"

        # Add each course to the features list
        for course in courses:
            course_title = course['title']
            instructors = course['instructors']
            wiki_link = course['wiki_link']

            # Format instructor names, adding 'Prof.' if not already present
            instructors = ", ".join([f"Prof. {i.strip()}" if "Prof." not in i else i.strip() for i in instructors.split(",")])

            # Adding course information in YAML format with double quotes
            yaml_content += f'  - title: "{course_title}"\n'
            yaml_content += f'    details: "{instructors}"\n'
            yaml_content += f'    link: "{wiki_link}"\n'

        yaml_content += "---"

        # Write the YAML content to a file for the current level
        output_file = os.path.join(output_dir, f"{level.lower()}_courses.md")
        with open(output_file, 'w') as f:
            f.write(yaml_content)
        print(f"Generated {output_file}")

# Check if the file is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python generate_navigation.py <courses.json>")
    sys.exit(1)

# Get the input JSON file from the command-line argument
json_file = sys.argv[1]

# Generate navigation pages from the provided JSON file
generate_navigation_pages(json_file)
