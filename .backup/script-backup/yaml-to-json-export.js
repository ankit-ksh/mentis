import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import yaml from 'yaml';

// Determine the directory of the current file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Specify the relative path to the project root
const projectRoot = path.resolve(__dirname, '../');

// List of course paths
import courseList from '../courseList.js'; // Assuming courseList is exported as an array

console.log('Loaded course list:', courseList);

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
courseList.forEach(coursePath => {
    const courseName = coursePath.split('/').filter(Boolean).pop(); // Get the course name from path
    const courseData = loadYaml(coursePath);
    if (courseData) {
        courses[courseName] = courseData;
    }
});

// Write the final JavaScript export to a file
const outputFilePath = path.join(__dirname, 'courses.js');
const fileContent = `export const courses = ${JSON.stringify(courses, null, 2)};`;

fs.writeFileSync(outputFilePath, fileContent);
console.log(`Courses data has been written to ${outputFilePath}`);
