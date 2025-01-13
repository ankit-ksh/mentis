# Goals

## Completed
### To make the process of addition of courses easy
  - Automatic sidebar management - A script which will take YAML files from the corresponding course directories, named course-info.yaml and use the sidebar object from there to construct a comprehensive sidebars.json object in the /public/database/sidebars.js file, which can be directly used by Vitepress to construct the sidebar for all courses in the site. The only requirement for this is that the course path should be listed in a json file, which is located at /public/data/all-course-locations.json. The script searches in only those locations for the YAML files.


## Working on
- 



## Features planned in the Future
- Add the support of practicing questions in the site for all the courses, using a database of questions and a human friendly question authoring tool.