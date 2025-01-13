import json
import os
import sys

def create_course_structure(course, level_dir):
    """Creates the folder structure and files for a given course in the specified level directory."""
    # Get the course title and number of weeks from the course data
    course_title = course['title']
    num_weeks = course.get('number_of_weeks', 0)

    # Create a directory for the course
    course_dir = os.path.join(level_dir, course['acronym'])
    os.makedirs(course_dir, exist_ok=True)

    # Create basic files for the course: about.md, reference.md, info.md
    for filename in ['about.md', 'reference.md', 'info.md']:
        file_path = os.path.join(course_dir, filename)
        with open(file_path, 'w') as f:
            f.write(f"# {course_title}\n\nContent for {filename}.")

    # Create week directories and files
    for week in range(1, num_weeks + 1):
        week_dir = os.path.join(course_dir, f"week{week}")
        os.makedirs(week_dir, exist_ok=True)

        # Create contents.md and questions.md for each week
        for week_file, content in [('contents.md', f"Week {week}"), ('questions.md', f"Week {week} - Questions")]:
            file_path = os.path.join(week_dir, week_file)
            with open(file_path, 'w') as f:
                f.write(f"# {content}\n\nContent for {content}.")

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
    output_dir = 'docs'
    os.makedirs(output_dir, exist_ok=True)

    # Generate a YAML file for each level and course structure
    for level, courses in level_courses.items():
        # Create the directory for the current level
        level_dir = os.path.join(output_dir, level.lower())
        os.makedirs(level_dir, exist_ok=True)

        # Create index.md for the current level with navigation details
        index_content = f"---\nlayout: home\n\nhero:\n  name: \"{level.capitalize()} level\"\n\n\nfeatures:\n"
        
        # Add each course to the features list and create course structure
        for course in courses:
            course_title = course['title']
            instructors = course['instructors']
            wiki_link = course['wiki_link']

            # Format instructor names, adding 'Prof.' if not already present
            instructors = ", ".join([f"Prof. {i.strip()}" if "Prof." not in i else i.strip() for i in instructors.split(",")])

            # Adding course information in YAML format
            index_content += f'  - title: "{course_title}"\n'
            index_content += f'    details: "{instructors}"\n'
            index_content += f'    link: "{wiki_link}"\n'

            # Call to create the folder structure for each course
            create_course_structure(course, level_dir)

        index_content += "---"

        # Write the YAML content to index.md for the current level
        index_file = os.path.join(level_dir, "index.md")
        with open(index_file, 'w') as f:
            f.write(index_content)
        # print(f"Generated {index_file}")

# Check if the file is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python generate_navigation.py <courses.json>")
    sys.exit(1)

# Get the input JSON file from the command-line argument
json_file = sys.argv[1]

# Generate navigation pages and course structure from the provided JSON file
generate_navigation_pages(json_file)
