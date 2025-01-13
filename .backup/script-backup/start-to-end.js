import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import yaml from 'yaml';

// Determine the directory of the current file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Set the correct project root path
const projectRoot = path.resolve(__dirname, '../../'); // This should point to your project root
console.log(`Project root is: ${projectRoot}`);

// Import coursesStructure from JSON
const coursesStructurePath = path.join(projectRoot, 'public', 'data', 'all-courses-data.json');
console.log(`Looking for courses data at: ${coursesStructurePath}`);  // Debugging path

const coursesStructure = JSON.parse(fs.readFileSync(coursesStructurePath, 'utf8'));

// Function to recursively extract course paths
function getCoursePaths(courseTree) {
    let result = [];
    for (const key in courseTree) {
        if (typeof courseTree[key] === 'object') {
            result = result.concat(getCoursePaths(courseTree[key]));
        } else {
            result.push(courseTree[key]);
        }
    }
    return result;
}

// Extract course paths
const coursePaths = getCoursePaths(coursesStructure);

// Function to load and parse YAML for a course
function loadYaml(coursePath) {
    const yamlFilePath = path.join(projectRoot, coursePath, 'course-info.yaml');
    console.log(`Looking for YAML at: ${yamlFilePath}`);
    if (fs.existsSync(yamlFilePath)) {
        try {
            const fileContent = fs.readFileSync(yamlFilePath, 'utf8');
            return yaml.parse(fileContent);
        } catch (err) {
            console.error(`Error reading or parsing YAML file at ${yamlFilePath}: ${err.message}`);
        }
    } else {
        console.warn(`YAML file does not exist at ${yamlFilePath}`);
    }
    return null;
}

// Build the final courses object
const courses = {};
coursePaths.forEach(coursePath => {
    const courseName = coursePath.split('/').filter(Boolean).pop(); // Get the course name from path
    const courseData = loadYaml(coursePath);
    if (courseData) {
        courses[courseName] = courseData;
    }
});

// Set the output file path to ../data/
const outputFilePath = path.join(projectRoot, 'public', 'data', 'courses.js');

// Ensure the data directory exists
const outputDir = path.dirname(outputFilePath);
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

// Write the final JavaScript export to a file
const fileContent = `export const courses = ${JSON.stringify(courses, null, 2)};`;
fs.writeFileSync(outputFilePath, fileContent);

console.log(`Courses data has been written to ${outputFilePath}`);
