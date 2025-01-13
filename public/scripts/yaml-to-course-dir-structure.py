import os
import subprocess
import yaml
import re

def fetch_playlist_videos(playlist_url):
    command = ["yt-dlp", "--flat-playlist", "-J", playlist_url]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        video_data = yaml.safe_load(result.stdout)
        return [
            {"id": entry["id"], "title": entry["title"]}
            for entry in video_data["entries"]
        ]
    except subprocess.CalledProcessError as e:
        print(f"Error fetching playlist: {e.stderr}")
        print("Please check the playlist URL or yt-dlp installation.")
        return []

def process_yaml(course_file):
    with open(course_file, "r") as f:
        data = yaml.safe_load(f)

    basic_info = data.get("basic-info", {})
    base_url = basic_info.get("base-url", "/")
    playlist_url = basic_info.get("playlist-url")
    strategy = basic_info.get("strategy", "")
    basic_files = [{'link': 'index', 'text': 'Home'}, {'link': 'notes', 'text': 'Notes'}] + basic_info.get("basic-files", [])
    print(basic_files)
    # Parse strategy
    strategy_parts = strategy.split()
    method = strategy_parts[0]
    count = int(strategy_parts[1]) if len(strategy_parts) > 1 else 1
    prefix = strategy_parts[2] if len(strategy_parts) > 2 else "part"

    # Create basic files
    for file in basic_files:
        file_name = file.get("link") + ".md"
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "w") as f:
            f.write(f"# {file.get('text', 'Untitled')}")

    # Fetch playlist videos
    videos = fetch_playlist_videos(playlist_url)

    if not videos:
        print("No videos found. Exiting...")
        return

    # Divide videos based on strategy
    total_videos = len(videos)
    videos_per_part = (total_videos + count - 1) // count  # Ceiling division

    contents = {}
    for i in range(count):
        part_name = f"{prefix}{i + 1}"
        part_title = f"{prefix.capitalize()} {i + 1}"
        part_videos = videos[i * videos_per_part : (i + 1) * videos_per_part]

        # Create folder and markdown file
        folder_path = os.path.join(os.getcwd(), part_name)
        os.makedirs(folder_path, exist_ok=True)

        index_file = os.path.join(folder_path, "index.md")
        with open(index_file, "w") as f:
            # Write the script setup with dynamic part reference
            f.write(f"""<script setup>
import contents from '../contents.json';

const topic = {part_name};
</script>

<CoursePage :contents="contents" :topic="topic" />""")
        # Add to contents
        contents[part_name] = {
            "title": part_title,
            "videos": part_videos,
        }

    # Sort contents numerically
    sorted_contents = {k: contents[k] for k in sorted(contents, key=lambda x: int(re.search(r'\d+', x).group()))}

    # Update Sidebar
    sidebar = [
        {
            "text": "Course",
            "base": base_url,
            "items": [
                {"text": file.get("text"), "link": file.get("link")}
                for file in basic_files
            ],
        },
        {
            "text": "Contents",
            "base": base_url,
            "items": [
                {"text": value["title"], "link": key}
                for key, value in sorted_contents.items()
            ],
        },
    ]

    data["sidebar"] = sidebar

    # Move sidebar before contents in YAML
    final_data = {"sidebar": data["sidebar"], **data}
    final_data["contents"] = sorted_contents

    with open(course_file, "w") as f:
        yaml.dump(final_data, f, default_flow_style=False)

# Usage example
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <course-file.yaml>")
    else:
        process_yaml(sys.argv[1])
