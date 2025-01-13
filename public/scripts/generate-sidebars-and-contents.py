import os
import json
import yaml

# Define project root and paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
courses_structure_path = os.path.join(project_root, 'public', 'data', 'all-course-locations.json')
output_dir = os.path.join(project_root, 'public', 'database')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load courses structure
with open(courses_structure_path, 'r') as file:
    courses_structure = json.load(file)

# Initialize sidebars object
sidebars = {}

def process_course_tree(course_tree, base_path=""):
    for key, value in course_tree.items():
        if isinstance(value, dict):
            # Recursively process sub-trees
            process_course_tree(value, base_path)
        elif isinstance(value, str):
            # Handle course leaf nodes
            course_path = value.lstrip("/")  # Remove leading slash if present
            yaml_file_path = os.path.join(project_root, course_path, 'course-info.yaml')

            if os.path.exists(yaml_file_path):
                # Read and parse the YAML file
                with open(yaml_file_path, 'r') as yaml_file:
                    try:
                        course_data = yaml.safe_load(yaml_file)

                        # Extract sidebar property
                        if 'sidebar' in course_data:
                            # Adjust the path to be relative to `/courses`
                            relative_path = '/' + course_path.split('/', 1)[-1]
                            sidebars[relative_path] = course_data['sidebar']

                        # Extract contents property
                        if 'contents' in course_data:
                            content_output_path = os.path.join(project_root, course_path, 'contents.json')
                            os.makedirs(os.path.dirname(content_output_path), exist_ok=True)
                            with open(content_output_path, 'w') as content_file:
                                contents = course_data['contents']
                                contents['course-path'] = course_data['basic-info']['course-path']
                                json.dump(contents, content_file, indent=2)

                        # Append JSON representation of YAML to the course node
                        course_tree[key] = {
                            "location": value,
                            "data": course_data
                        }
                    except Exception as e:
                        print(f"Error processing YAML file at {yaml_file_path}: {e}")

# Process the courses structure
process_course_tree(courses_structure)

# Write updated courses structure to a new file
courses_output_path = os.path.join(output_dir, 'courses.json')
with open(courses_output_path, 'w') as file:
    json.dump(courses_structure, file, indent=2)

# Write sidebars JSON
sidebars_output_path = os.path.join(output_dir, 'sidebars.json')
with open(sidebars_output_path, 'w') as file:
    json.dump(sidebars, file, indent=2)

print(f"Updated courses data written to {courses_output_path}")
print(f"Sidebars data written to {sidebars_output_path}")
