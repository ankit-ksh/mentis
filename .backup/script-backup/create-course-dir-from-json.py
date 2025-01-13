import os
import json
import sys

def create_course_structure(course_data, root_dir):
    """
    Create the folder and files for a given course inside its respective directory.
    """
    course_title = course_data['title']
    course_acronym = course_data['acronym']
    num_weeks = course_data.get('number_of_weeks', 12)  # Default to 12 weeks if not provided
    
    # Create the main folder for the course
    course_dir = os.path.join(root_dir, course_acronym)
    os.makedirs(course_dir, exist_ok=True)

    # Create 'about.md', 'reference.md', 'info.md' files
    for file_name in ['about.md', 'reference.md', 'info.md']:
        file_path = os.path.join(course_dir, file_name)
        with open(file_path, 'w') as file:
            file.write(f"# {course_title}\n")  # Top heading as the course title

    # Create weeks folders and files inside them
    for week_num in range(1, num_weeks + 1):
        week_dir = os.path.join(course_dir, f"week{week_num}")
        os.makedirs(week_dir, exist_ok=True)

        # Create contents.md and questions.md files for each week
        contents_md_path = os.path.join(week_dir, 'contents.md')
        questions_md_path = os.path.join(week_dir, 'questions.md')

        with open(contents_md_path, 'w') as file:
            file.write(f"# Week {week_num}\n")  # Top heading
        with open(questions_md_path, 'w') as file:
            file.write(f"# Week {week_num} - Questions\n")  # Top heading

        # Create directories for contents and questions
        os.makedirs(os.path.join(week_dir, 'contents'), exist_ok=True)
        os.makedirs(os.path.join(week_dir, 'questions'), exist_ok=True)

def process_courses_from_json(json_file):
    """
    Process the courses from the provided JSON file and create directories and files.
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file: {e}")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Iterate through all the levels and their courses
    for level, courses in data.items():
        level_dir = os.path.join("docs", level)
        os.makedirs(level_dir, exist_ok=True)

        # Create directories for each course
        for course in courses:
            create_course_structure(course, level_dir)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <json_file>")
        return

    json_file = sys.argv[1]  # Get the JSON file path from command line argument
    process_courses_from_json(json_file)

if __name__ == "__main__":
    main()
