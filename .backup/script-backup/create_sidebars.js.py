import json
import os
import sys

def generate_sidebar_file(json_file):
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

    # Create the 'sidebars' directory if it doesn't exist
    output_dir = 'sidebars'
    os.makedirs(output_dir, exist_ok=True)

    sidebar_content = {}

    # Iterate over each level and its courses
    for level, courses in level_courses.items():
        for course in courses:
            course_acronym = course['acronym']
            base_path = f'/{level}/{course_acronym}'

            course_sidebar = {
                'base': base_path,  # Add the base property
                'items': [
                    { 'text': 'About the course', 'link': f'{base_path}/about' },
                    { 'text': 'Important information and links', 'link': f'{base_path}/info' },
                    { 'text': 'Reference', 'link': f'{base_path}/reference' }
                ]
            }

            # Add weekly information as items inside the same 'items' list
            num_weeks = course.get('number_of_weeks', 0)
            weeks_content = []

            for week in range(1, num_weeks + 1):
                weeks_content.append({
                    'text': f'Week {week}',
                    'collapsed': True,
                    'items': [
                        { 'text': 'Content', 'link': f'{base_path}/week{week}/content' },
                        { 'text': 'Questions', 'link': f'{base_path}/week{week}/questions' }
                    ]
                })

            # Add the weeks to the sidebar content
            course_sidebar['items'].append({
                'items': weeks_content
            })

            # Add the course sidebar to the overall dictionary with the course path as the key
            sidebar_content[base_path] = course_sidebar

    # Write the complete sidebar content to a single file
    sidebar_file = os.path.join(output_dir, 'sidebars.mts')
    with open(sidebar_file, 'w') as f:
        f.write(f"export default {json.dumps(sidebar_content, indent=2)};\n")
    print(f"Generated sidebar file: {sidebar_file}")

# Check if the file is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python generate_sidebar_file.py <courses.json>")
    sys.exit(1)

# Get the input JSON file from the command-line argument
json_file = sys.argv[1]

# Generate the sidebar file from the provided JSON file
generate_sidebar_file(json_file)
