#!/usr/bin/node
const fs = require('fs');

// Get file paths from command line arguments
const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

// Read content of the first file
const content1 = fs.readFileSync(file1, 'utf-8');

// Read content of the second file
const content2 = fs.readFileSync(file2, 'utf-8');

// Write concatenated content to the destination file
fs.writeFileSync(destination, content1 + content2);
